# Wojciech Wolny

import os
import re

from grakn.client import GraknClient

KEYSPACE = "course"
URI = "localhost:48555"


def execute_entity_query(query):
    with GraknClient(uri=URI) as client:
        with client.session(keyspace=KEYSPACE) as session:
            with session.transaction().read() as read_transaction:
                result = read_transaction.query(query)

                concepts = result.collect_concepts()

                entities = []

                for c in concepts:
                    attrs = c.attributes()
                    entity = {"id": c.id}
                    for each in attrs:
                        entity[each.type().label()] = each.value()
                    entities.append(entity)

                return entities


def get_entities(entity_type):
    return execute_entity_query(f"match $x isa {entity_type}; get;")


def write_to_file(file_name, entities):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w+", encoding="utf-8") as f:
        for e in entities:
            f.write(f"{e}\n")


def run():
    entities = get_entities("course")
    courses = list(map(lambda x: x["title"], entities))
    keywords = []
    for course in courses:
        tmp = re.findall(r"[A-Z]+\w*", course)
        for repetition in tmp:
            if repetition not in keywords:
                keywords.append(repetition)
    write_to_file("./data/lookup_tables/keywords.txt", set(keywords))
    write_to_file("./data/lookup_tables/course.txt", set(courses))


if __name__ == "__main__":
    run()
