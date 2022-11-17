# -*- coding: utf-8 -*-
from typing import Text, Dict, Any, List, Union
import spacy

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker

from schema import schema
from graph_database import GraphDatabase


def resolve_mention(tracker: Tracker) -> Text:
    """
    Resolves a mention of an entity, such as first, to the actual entity.
    If multiple entities are listed during the conversation, the entities
    are stored in the slot 'listed_items' as a list. We resolve the mention,
    such as first, to the list index and retrieve the actual entity.

    :param tracker: tracker
    :return: name of the actually entity
    """
    graph_database = GraphDatabase()

    mention = tracker.get_slot("mention")
    listed_items = tracker.get_slot("listed_items")

    if mention is not None and listed_items is not None:
        idx = int(graph_database.map("mention-mapping", mention))

        if type(idx) is int and idx < len(listed_items):
            return listed_items[idx]


def get_attribute(tracker: Tracker) -> Text:
    """
    Get the attribute mentioned by the user. As the user may use a synonym for
    an attribute, we need to map the mentioned attribute to the
    attribute name used in the knowledge base.

    :param tracker: tracker
    :return: attribute (same type as used in the knowledge base)
    """
    graph_database = GraphDatabase()
    attribute = tracker.get_slot("attribute")
    return graph_database.map("attribute-mapping", attribute)


def get_technology(tracker: Tracker) -> Text:
    """
    Get the name of the technology
    """
    technology = tracker.get_slot("technology")
    return technology


def get_price(tracker: Tracker) -> [int, int]:
    """
    Get the price range.
    """
    min_price = tracker.get_slot("min_price")
    max_price = tracker.get_slot("max_price")

    if max_price is None and min_price is None:
        return None

    return [min_price, max_price]


def get_entity_name(tracker: Tracker):
    """
    Get the name of the entity the user referred to. Either the NER detected the
    entity and stored its name in the corresponding slot or the user referred to
    the entity by an ordinal number, such as first or last, or the user refers to
    an entity by its attributes.

    :param tracker: Tracker

    :return: the name of the actual entity (value of key attribute in the knowledge base)
    """

    # user referred to an entity by an ordinal number
    mention = tracker.get_slot("mention")
    if mention is not None:
        return resolve_mention(tracker)

    # user referred to an entity by its attributes
    listed_items = tracker.get_slot("listed_items")
    attributes = get_attributes_of_entity(tracker)

    if listed_items and attributes:
        # filter the listed_items by the set attributes
        graph_database = GraphDatabase()
        for entity in listed_items:
            key_attr = schema['course']["key"]
            result = graph_database.validate_entity(
                entity, key_attr, attributes
            )
            if result is not None:
                return to_str(result, key_attr)

    return None


def get_attributes_of_entity(tracker):
    # check what attributes the NER found for entity type
    attributes = []
    for attr in schema['course']["attributes"]:
        attr_val = tracker.get_slot(attr.replace("-", "_"))
        if attr_val is not None:
            attributes.append({"key": attr, "value": attr_val})
    return attributes


def reset_attribute_slots(slots, tracker):
    # check what attributes the NER found for entity type
    for attr in schema['course']["attributes"]:
        attr = attr.replace("-", "_")
        attr_val = tracker.get_slot(attr)
        if attr_val is not None:
            slots.append(SlotSet(attr, None))
    return slots


def to_str(entity: Dict[Text, Any], entity_keys: Union[Text, List[Text]]) -> Text:
    """
    Converts an entity to a string by concatenating the values of the provided
    entity keys.

    :param entity: the entity with all its attributes
    :param entity_keys: the name of the key attributes
    :return: a string that represents the entity
    """
    if isinstance(entity_keys, str):
        entity_keys = [entity_keys]

    v_list = []
    for key in entity_keys:
        _e = entity
        for k in key.split("."):
            _e = _e[k]

        v_list.append(str(_e))
    return ", ".join(v_list)


class ActionQuerySearch(Action):
    """Action for listing entities with specific conditions.
    The entities might be filtered by specific attributes."""

    def name(self):
        return "action_query_search"

    def run(self, dispatcher, tracker, domain, NLP=None):
        graph_database = GraphDatabase()

        technology = get_technology(tracker)

        if not technology:
            dispatcher.utter_message("Jakie technologie Cię interesują?")
            return []

        price_range = get_price(tracker)
        entities = graph_database.get_contains(technology, price_range=price_range, nlp=NLP)
        if not entities:
            dispatcher.utter_message(
                "Nie znalazłem kursów dla podanych warunków."
            )
            # TODO: Nie znalazłem kursów, -> wypisz podobne, zaproponuj coś innego
            return []

        entity_representation = schema['course']["key"]

        # if len(entities) > 5:
        #     dispatcher.utter_message(
        #         "Znaleźliśmy dużo kursów, czy mógłbyś powiedzieć coś więcej o kursie, który Cię interesuje?"
        #     )
        #     return []
        if len(entities) == 1:
            for i, e in enumerate(entities):
                representation_string = to_str(e, entity_representation)
                dispatcher.utter_message(f"Proponuję kurs {representation_string}")
        else:
            dispatcher.utter_message(
                "Wyszukałem takie kursy:"
            )

            for i, e in enumerate(entities):
                representation_string = to_str(e, entity_representation)
                dispatcher.utter_message(f"{i + 1}: {representation_string}")
        entity_key = schema['course']["key"]
        slots = [
            SlotSet("listed_items", list(map(lambda x: to_str(x, entity_key), entities))),
        ]
        if len(entities) == 1:
            slots.append(SlotSet('mention', '1'))
            # slots.append(SlotSet('title', to_str(entities[0], entity_key)))
        reset_attribute_slots(slots, tracker)
        return slots


class ActionQueryEntities(Action):
    """Action for listing entities.
    The entities might be filtered by specific attributes."""

    def name(self):
        return "action_query_entities"

    def run(self, dispatcher, tracker, domain, NLP=None):
        graph_database = GraphDatabase()

        # check what attributes the NER found for entity type
        attributes = get_attributes_of_entity(tracker)

        # query knowledge base
        entities = graph_database.get_entities(attributes)

        if not entities:
            dispatcher.utter_template(
                "Nie znalazłem żadnych kursów.", tracker
            )
            return []

        # utter a response that contains all found entities
        # use the 'representation' attributes to print an entity
        entity_representation = schema['course']["key"]

        dispatcher.utter_message(
            "Znalazłem takie kursy:"
        )
        for i, e in enumerate(entities):
            representation_string = to_str(e, entity_representation)
            dispatcher.utter_message(f"{i + 1}: {representation_string}")

        # set slots
        # set the entities slot in order to resolve references to one of the found
        # entites later on
        entity_key = schema['course']["key"]

        slots = [
            SlotSet("listed_items", list(map(lambda x: to_str(x, entity_key), entities))),
        ]

        # if only one entity was found, that the slot of that entity type to the
        # found entity
        if len(entities) == 1:
            slots.append(SlotSet('course', to_str(entities[0], entity_key)))

        reset_attribute_slots(slots, tracker)

        return slots


class ActionQueryAttribute(Action):
    """Action for querying a specific attribute of an entity."""

    def name(self):
        return "action_query_attribute"

    def run(self, dispatcher, tracker, domain, NLP=None):
        graph_database = GraphDatabase()

        # get name of entity and attribute of interest
        name = get_entity_name(tracker)
        attribute = get_attribute(tracker)

        if name is None or attribute is None:
            dispatcher.utter_template("utter_rephrase", tracker)
            return None

        # query knowledge base
        key_attribute = schema['course']["key"]
        value = graph_database.get_attribute_of(
            key_attribute, name, attribute
        )

        # utter response
        if value is not None and len(value) == 1:
            if "price" in attribute:
                dispatcher.utter_message(
                    f"{name} kosztuje {value[0]} PLN."
                )
            elif "durationInDays" in attribute:
                dispatcher.utter_message(
                    f"{name} trwa {value[0]} dni."
                )
            elif "prerequisites" in attribute:
                dispatcher.utter_message(
                    f"{value[0]}"
                )
            elif "addressedTo" in attribute:
                dispatcher.utter_message(
                    f"{value[0]}"
                )
            else:
                dispatcher.utter_message(
                    f"{name} ma wartość atrybutu :'{value[0]}'."
                )
        else:
            dispatcher.utter_message(
                f"Nie znalazłem odpowiedniego atrybutu {attribute} dla kursu '{name}'."
            )
        return None


class ActionCompareEntities(Action):
    """Action for comparing multiple entities."""

    def name(self):
        return "action_compare_entities"

    def run(self, dispatcher, tracker, domain, NLP=None):
        graph = GraphDatabase()

        # get entities to compare and their entity type
        listed_items = tracker.get_slot("listed_items")

        # get attribute of interest
        attribute = get_attribute(tracker)

        if attribute is None:
            dispatcher.utter_template("utter_rephrase", tracker)
            return []

        # utter response for every entity that shows the value of the attribute
        for e in listed_items:
            key_attribute = schema['course']["key"]
            value = graph.get_attribute_of(key_attribute, e, attribute)

            if value is not None and len(value) == 1:
                dispatcher.utter_message(
                    f"'{e}': '{value[0]}'."
                )

        return []


class ActionResolveEntity(Action):
    """Action for resolving a mention."""

    def name(self):
        return "action_resolve_entity"

    def run(self, dispatcher, tracker, domain, NLP=None):
        graph = GraphDatabase()

        name = get_entity_name(tracker)
        key_attribute = schema['course']["key"]
        # Check if entity was mentioned as 'first', 'second', etc.
        mention = tracker.get_slot("mention")
        if mention is not None:
            for attr in ["price", "durationInDays", "addressedTo", "prerequisites"]:
                value = graph.get_attribute_of(
                    key_attribute, name, attr
                )
                if value is not None and len(value) == 1:
                    if "price" == attr:
                        dispatcher.utter_message(
                            f"{name} kosztuje {value[0]} PLN."
                        )
                    elif "durationInDays" == attr:
                        dispatcher.utter_message(
                            f"{name} trwa {value[0]} dni."
                        )
                    elif "prerequisites" == attr:
                        dispatcher.utter_message(
                            f"{value[0]}"
                        )
                    elif "addressedTo" == attr:
                        dispatcher.utter_message(
                            f"{value[0]}"
                        )
                    else:
                        dispatcher.utter_message(
                            f"{name} ma wartość atrybutu :'{value[0]}'."
                        )
                else:
                    dispatcher.utter_message(
                        f"Nie znalazłem odpowiedniego atrybutu {attr} dla kursu '{name}'."
                    )
            return []
        else:
            dispatcher.utter_template("utter_rephrase", tracker)
            return []
