import sqlalchemy

def get_uniq_constraints(url, table, schema=None):
    """
    Dynamic passing of a DB url allows for multiple DBs containing
    unique constraints to be tested.
    """
    eng = slqalchemy.create_engine(url)
    insp = slqalchemy.engine.reflection.Inspector(eng)
    return insp.get_unique_constraints(table, schema)
