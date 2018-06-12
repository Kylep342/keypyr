#TODO: Clean this up, a lot
import os

import sqlalchemy

import keypyr_helpers.check_csv as ccsv
import keypyr_helpers.inspect_sql_db as isql


PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))


def results_to_JSON(func, bool):
    pass


def main(csv_file_dir,
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
    if dups_to_JSON:
        import datetime
        import json
        import sys
        ts = datetime.datetime.now().isoformat()
        # out = open('./data/{}_dups.json', 'w')
        # sys.stdout = out


    eng = slqalchemy.create_engine(url)
    insp = slqalchemy.engine.reflection.Inspector(eng)

    csvs = sorted([f for f in os.listdir(csv_file_dir) if f.endswith('.csv') and f not in exclude_csvs])

    for _csv in csvs:
        tbl = _csv.split('.')[0]
        constraints = isql.conform_pk_and_uc(insp, tbl, db_schema)
        path = os.path.join(csv_file_dir, _csv)
        validate = ccsv.check_csv(path, constraints)
        for key in validate.keys():
            print(key, validate[key])


if __name__ == '__main__':
    import argparse

    parser = arparse.ArgumentParser()
    parser.add_argument(name='csvdir', help='Full path to directory of csv files to test')
    parser.add_argument(name='db_url', help='A DB connection URL')
    parser.add_argument(name='schema', default=None, help='Name of DB schema')
    parser.add_argument(name='exclude_tbls', default=None, help='List of names of tables to exclude')
    parser.add_argument(name='exclude_csvs', default=None, help='List of csv files to exclude')
    parser.add_argument(name='-j', action='store_true', help='Flag inclusion dumps results to JSON')

    args = parser.parse_args()

    main(args.csvdir,
         args.db_url,
         args.schema,
         args.exclude_tbls,
         args.exclude_csvs,
         False)
