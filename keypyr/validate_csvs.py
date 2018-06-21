#TODO: Clean this up, a lot
import os

import sqlalchemy

import keypyr_helpers.check_csv as ccsv
import keypyr_helpers.inspect_sql_db as isql


PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))


def keypyr(csv_file_dir,
         url,
         db_schema=None,
         exclude_tbls=None,
         exclude_csvs=None,
         dups_to_JSON=False
    ):
    """
    Dynamic passing of a DB url allows for multiple DBs containing
    unique constraints to be tested.

    Table names are assumed to be equal to csv file names.
    Additionally, a 1 to 1 relationship between csv and table is assumed.
    """

    eng = sqlalchemy.create_engine(url)
    insp = sqlalchemy.engine.reflection.Inspector(eng)

    csvs = sorted([f for f in os.listdir(csv_file_dir) if f.endswith('.csv') and f not in exclude_csvs])

    for _csv in csvs:
        tbl = _csv.split('.')[0]
        constraints = isql.conform_pk_and_uc(insp, tbl, db_schema)
        path = os.path.join(csv_file_dir, _csv)
        validate = ccsv.check_csv(path, constraints)
        for key in validate.keys():
            if validate[key]:
                print(key, validate[key])
