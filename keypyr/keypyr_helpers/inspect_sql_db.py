"""
This module holds functions for gathering information from a SQL DB
The public, exportable functions allow for:
    - Inspection of a table to get all unique constraints and the
    primary key for the table
    - Inspection of a table to get all column names in order

"""

def _get_primary_keys(insp, tbl, schema=None):
    """
    Private function to get the primary key, and conform the keys in
    the dictionary that is returned by SQLAlchemy's base
    get_pk_constraint() function
    """
    const = []
    pk = insp.get_pk_constraint(tbl, schema)
    conformed_const = {'name' : pk['name'], 'cols' : pk['constrained_cols']}
    const.insert(conformed_const)
    return const


def _get_unique_cols(insp, tbl, schema=None):
    """
    Private function to get the unique constraints, and conform the
    keys in the dictionary that is returned by SQLAlchemy's base
    get_unique_constraints() function
    """
    const = []
    ucs = insp.get_unique_constraints(tbl, schema):
    for uc in ucs:
        conformed_const = {'name' : uc['name'], 'cols' : uc['column_names']}
        const.insert(conformed_const)
    return const


def conform_pk_and_uc(insp, tbl, schema=None):
    """
    Public function that calls both _get_unique_cols() and
    _get_primary_keys(), and then concatenates and returns both of the
    return values.

    Conforming the key access allows for a single funciton call per
    table in the main utility of the app, and allows for cleaner
    iteration
    """
    return _get_primary_keys(insp, tbl, schema) + _get_unique_cols(insp, tbl, schema)


def get_table_column_names(insp, tbl, schema=None):
    """
    Public function that returns a list of the columns in a table in
    order. Useful for when the csv being loaded does not include
    headers
    """
    return [col['name'] for col in insp.get_columns(tbl, schema)]
