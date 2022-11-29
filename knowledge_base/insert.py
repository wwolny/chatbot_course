from grakn.client import GraknClient


def insert(graql_insert_query):
    with GraknClient(uri="localhost:48555") as client:
        with client.session(keyspace="course") as session:
            with session.transaction().write() as transaction:
                transaction.query(graql_insert_query)
                transaction.commit()


if __name__ == "__main__":
    graql_insert_query = """
    insert $c isa course, has title 'Administracja Apache Hadoop', \
    has price '1950', has durationInDays '2';
    """

    insert(graql_insert_query)
