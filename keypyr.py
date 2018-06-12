import os

import sqlalchemy

from keypyr.check_csv import check_csv


PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))


def results_to_JSON(func, bool):
    pass


def main(url,
         csv_file_dir,
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
        constraints = insp.get_unique_constraints(tbl, db_schema)
        path = os.path.join(csv_file_dir, _csv)
        validate = check_csv(path, constraints)
        for key in validate.keys():
            print(key, validate[key])


if __name__ == '__main__':
    import argparse

    parser = arparse.ArgumentParser()
    parser.add_argument(name='csvdir', help='Full path to directory of csv files to test')
    parser.add_argument(name='schema', default=None, help='Name of DB schema')
