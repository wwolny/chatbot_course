import logging
from typing import List, Dict, Any, Optional, Text
from random import sample
from grakn.client import GraknClient
import re

logger = logging.getLogger(__name__)


class KnowledgeBase(object):

    def get_entities(
        self,
        entity_type: Text,
        attributes: Optional[List[Dict[Text, Text]]] = None,
        limit: int = 5,
    ) -> List[Dict[Text, Any]]:

        raise NotImplementedError("Method is not implemented.")

    def get_attribute_of(
        self, entity_type: Text, key_attribute: Text, entity: Text, attribute: Text
    ) -> List[Any]:

        raise NotImplementedError("Method is not implemented.")

    def validate_entity(
        self, entity_type, entity, key_attribute, attributes
    ) -> Optional[Dict[Text, Any]]:

        raise NotImplementedError("Method is not implemented.")

    def map(self, mapping_type: Text, mapping_key: Text) -> Text:

        raise NotImplementedError("Method is not implemented.")


class GraphDatabase(KnowledgeBase):
    """
    GraphDatabase uses a grakn graph database to encode your domain knowledege. Make
    sure to have the graph database set up and the grakn server running.
    """

    def __init__(self, uri: Text = "localhost:48555", keyspace: Text = "course"):
        self.uri = uri
        self.keyspace = keyspace

    def _thing_to_dict(self, thing):
        """
        Converts a thing (a grakn object) to a dict for easy retrieval of the thing's
        attributes.
        """
        entity = {"id": thing.id, "type": thing.type().label()}
        for each in thing.attributes():
            entity[each.type().label()] = each.value()
        return entity

    def _execute_entity_query(self, query: Text) -> List[Dict[Text, Any]]:
        """
        Executes a query that returns a list of entities with all their attributes.
        """
        with GraknClient(uri=self.uri) as client:
            with client.session(keyspace=self.keyspace) as session:
                with session.transaction().read() as tx:
                    print(query)
                    logger.debug("Executing Graql Query: " + query)
                    result_iter = tx.query(query)
                    concepts = result_iter.collect_concepts()
                    entities = []
                    for c in concepts:
                        entities.append(self._thing_to_dict(c))
                    return entities

    def _execute_attribute_query(self, query: Text) -> List[Any]:
        """
        Executes a query that returns the value(s) an entity has for a specific
        attribute.
        """
        query = query.replace('\\', '')
        with GraknClient(uri=self.uri) as client:
            with client.session(keyspace=self.keyspace) as session:
                with session.transaction().read() as tx:
                    print("Executing Graql Query: " + query)
                    result_iter = tx.query(query)
                    concepts = result_iter.collect_concepts()
                    return [c.value() for c in concepts]

    def _execute_relation_query(
        self, query: Text, relation_name: Text
    ) -> List[Dict[Text, Any]]:
        """
        Execute a query that queries for a relation. All attributes of the relation and
        all entities participating in the relation are part of the result.
        """
        with GraknClient(uri=self.uri) as client:
            with client.session(keyspace=self.keyspace) as session:
                with session.transaction().read() as tx:
                    print("Executing Graql Query: " + query)
                    result_iter = tx.query(query)

                    relations = []

                    for concept in result_iter:
                        relation_entity = concept.map().get(relation_name)
                        relation = self._thing_to_dict(relation_entity)

                        for (
                            role_entity,
                            entity_set,
                        ) in relation_entity.role_players_map().items():
                            role_label = role_entity.label()
                            thing = entity_set.pop()
                            relation[role_label] = self._thing_to_dict(thing)

                        relations.append(relation)

                    return relations

    def _get_attribute_clause(
        self, attributes: Optional[List[Dict[Text, Text]]] = None
    ) -> Text:
        """
        Construct the attribute clause.

        :param attributes: attributes

        :return: attribute clause as string
        """

        clause = ""

        if attributes:
            clause = ",".join([f"has {a['key']} '{a['value']}'" for a in attributes])
            clause = ", " + clause

        return clause

    def _get_contains_clause(self, contains: Optional[List[Dict[Text, Text]]] = None) -> Text:
        """
        Construct the contains technology clause.

        :param contains: list of technology

        :return: attribute clause as string
        """
        columns = ["title", "addressedTo", "prerequisites"]
        clause = ""
        for val in columns:
            clause += ", has {0} ${0}".format(val)
        clause += "; "
        for condition in contains:
            for val in columns:
                clause += f" {'{'}${val} contains ' {condition} ';{'}'} or"
        clause = clause[:-2]    # delete last "or"
        return clause

    def _get_price_clause(self, price_range: [] = None) -> Text:
        """
        Construct the price clause.

        :param price_range: list of length two, first argument is min price threshold and second is max price threshold

        :return: attribute clause as string
        """
        clause = ""
        if price_range is None:
            return clause

        if price_range[0]:
            clause += ", has price > {0}".format(price_range[0])

        if price_range[1]:
            clause += ", has price < {0}".format(price_range[1])

        return clause

    def get_attribute_of(
        self, key_attribute: Text, entity: Text, attribute: Text, entity_type: Text = 'course'
    ) -> List[Any]:
        """
        Get the value of the given attribute for the provided entity.

        :param key_attribute: key attribute of entity
        :param entity: name of the entity
        :param attribute: attribute of interest
        :param entity_type: entity type default value 'course'

        :return: the value of the attribute
        """

        return self._execute_attribute_query(
            f"""
              match
                ${entity_type} isa {entity_type},
                has {key_attribute} '{entity}',
                has {attribute} $a;
              get $a;
            """
        )

    def get_entities(
        self,
        attributes: Optional[List[Dict[Text, Text]]] = None,
        limit: int = 5,
        entity_type: Text = 'course'
    ) -> List[Dict[Text, Any]]:
        """
        Query the graph database for entities of the given type. Restrict the entities
        by the provided attributes, if any attributes are given.

        :param attributes: list of attributes
        :param limit: maximum number of entities to return
        :param entity_type: the entity type default 'course'

        :return: list of entities
        """

        attribute_clause = self._get_attribute_clause(attributes)
        courses = self._execute_entity_query(
            f"match "
            f"${entity_type} isa {entity_type}{attribute_clause}; "
            f"get ${entity_type};"
        )

        return sample(courses, min(limit,len(courses)))

    def map(self, mapping_type: Text, mapping_key: Text) -> Text:
        """
        Query the given mapping table for the provided key.

        :param mapping_type: the name of the mapping table
        :param mapping_key: the mapping key

        :return: the mapping value
        """
        value = self._execute_attribute_query(
            f"match $mapping isa {mapping_type}, has mapping-key '{mapping_key}', has mapping-value $v;get $v;"
        )

        if value and len(value) == 1:
            return value[0]

    def validate_entity(
        self, entity, key_attribute, attributes, entity_type: Text = 'course'
    ) -> Dict[Text, Any]:
        """
        Validates if the given entity has all provided attribute values.

        :param entity: name of the entity
        :param key_attribute: key attribute of entity
        :param attributes: attributes
        :param entity_type: entity type default 'course'

        :return: the found entity
        """
        attribute_clause = self._get_attribute_clause(attributes)

        value = self._execute_entity_query(
            f"match "
            f"${entity_type} isa {entity_type}{attribute_clause}, "
            f"has {key_attribute} '{entity}'; "
            f"get ${entity_type};"
        )

        if value and len(value) == 1:
            return value[0]

    def get_contains(
        self,
        contains: [] = None,
        limit: int = 5,
        price_range: [] = None,
        nlp: Optional = None,
        entity_type: Text = 'course'
    ) -> List[Dict[Text, Any]]:
        """
        Get the list of best matching courses for the current state.

        :param contains: list of technologies
        :param limit: number of courses to return
        :param price_range: price_range list with minimal or maximal value
        :param nlp: model of polish language
        :param entity_type: entity type default 'course'

        :return: the list of best matching courses
        """
        lemma_lst = []
        if nlp:
            for x in contains:
                doc = nlp(x)
                for tok in doc:
                    x_lemma = tok.lemma_
                    if x_lemma != x:
                        lemma_lst.append(x_lemma)

            contains_clause = self._get_contains_clause(contains + lemma_lst)
        else:
            contains_clause = self._get_contains_clause(contains)
        price_clause = self._get_price_clause(price_range)
        courses = self._execute_entity_query(
            f"match "
            f"${entity_type} isa {entity_type}{price_clause}{contains_clause};"
            f"get ${entity_type};"
        )

        if len(contains) > 0:
            re_clause = ""
            for el in contains + lemma_lst:
                re_clause += el + "|"
            re_clause = re_clause[:-1]
            re_clause = r"\b" + re_clause + r"\b"
            for c in courses:
                c["priority"] = len(re.findall(re_clause, c.get("title"), re.IGNORECASE)) * 2 \
                                + len(re.findall(re_clause, c.get("addressedTo"), re.IGNORECASE))
            courses = sorted(courses, key=lambda i: i["priority"], reverse=True)
            courses_out = courses[:min(limit, len(courses))]
        else:
            courses_out = sample(courses, min(limit, len(courses)))
        return courses_out
