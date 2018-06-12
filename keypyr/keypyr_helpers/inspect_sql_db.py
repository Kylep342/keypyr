#
"""
"""

def _get_primary_keys(insp, tbl, schema=None):
    const = []
    pk = insp.get_pk_constraint(tbl, schema)
    conformed_const = {'name' : pk['name'], 'cols' : pk['constrained_cols']}
    const.insert(conformed_const)
    return const


def _get_unique_cols(insp, tbl, schema=None):
    const = []
    ucs = insp.get_unique_constraints(tbl, schema):
    for uc in ucs:
        conformed_const = {'name' : uc['name'], 'cols' : uc['column_names']}
        const.insert(conformed_const)
    return const


def conform_pk_and_uc(insp, tbl, schema=None):
    return _get_primary_keys(insp, tbl, schema) + _get_unique_cols(insp, tbl, schema)
