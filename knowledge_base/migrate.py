import csv

from grakn.client import GraknClient


def build_course_graph(inputs):
    with GraknClient(uri="localhost:48555") as client:
        with client.session(keyspace="course") as session:
            for input in inputs:
                print(
                    "Loading from [" + input["data_path"] + "] into Grakn ..."
                )
                load_data_into_grakn(input, session)


def load_data_into_grakn(input, session):
    items = parse_data_to_dictionaries(input)

    for item in items:
        with session.transaction().write() as transaction:
            graql_insert_query = input["template"](item)
            transaction.query(graql_insert_query)
            transaction.commit()

    print(
        f"Inserted {str(len(items))} items from [{input['data_path']}]"
        f"into Grakn."
    )


def course_template(course):
    graql_insert_query = "insert $course isa course"
    graql_insert_query += ', has title "' + course["title"] + '"'
    graql_insert_query += ", has price " + course["price"] + ""
    graql_insert_query += (
        ', has prerequisites "' + course["prerequisites"] + '"'
    )
    graql_insert_query += (
        ", has durationInDays " + course["durationInDays"] + ""
    )
    graql_insert_query += ', has addressedTo "' + course["addressedTo"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def attribute_mapping_template(mapping):
    graql_insert_query = "insert $mapping isa attribute-mapping"
    graql_insert_query += ", has mapping-key '" + mapping["mapping-key"] + "'"
    graql_insert_query += (
        ", has mapping-value '" + mapping["mapping-value"] + "'"
    )
    graql_insert_query += ";"
    return graql_insert_query


def mention_mapping_template(mapping):
    graql_insert_query = "insert $mapping isa mention-mapping"
    graql_insert_query += ", has mapping-key '" + mapping["mapping-key"] + "'"
    graql_insert_query += (
        ", has mapping-value '" + mapping["mapping-value"] + "'"
    )
    graql_insert_query += ";"
    return graql_insert_query


def entity_type_mapping_template(mapping):
    graql_insert_query = "insert $mapping isa entity-type-mapping"
    graql_insert_query += ", has mapping-key '" + mapping["mapping-key"] + "'"
    graql_insert_query += (
        ", has mapping-value '" + mapping["mapping-value"] + "'"
    )
    graql_insert_query += ";"
    return graql_insert_query


def parse_data_to_dictionaries(input):
    items = []
    with open(input["data_path"] + ".csv") as data:  # 1
        for row in csv.DictReader(data, skipinitialspace=True):
            item = {key: value for key, value in row.items()}
            items.append(item)  # 2
    return items


if __name__ == "__main__":
    inputs = [
        {
            "data_path": "./knowledge_base/data/courses",
            "template": course_template,
        },
        {
            "data_path": "./knowledge_base/data/attribute_mapping",
            "template": attribute_mapping_template,
        },
        {
            "data_path": "./knowledge_base/data/mention_mapping",
            "template": mention_mapping_template,
        },
        {
            "data_path": "./knowledge_base/data/entity_type_mapping",
            "template": entity_type_mapping_template,
        },
    ]

    build_course_graph(inputs)
