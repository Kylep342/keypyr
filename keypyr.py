#!/usr/bin/env python
import keypyr.validate_csvs as keypyr


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('csvdir', help='Full path to directory of csv files to test')
    parser.add_argument('db_url', help='A DB connection URL')
    parser.add_argument('-s', '--schema', default=None, help='Name of DB schema')
    parser.add_argument('-ec', '--exclude_csvs', nargs='*', help='List of csv file names to exclude')
    parser.add_argument('-j', '--json', default=False, action='store_true', help='Flag inclusion dumps results to JSON')

    args = parser.parse_args()

    keypyr.keypyr(
        args.csvdir,
        args.db_url,
        args.schema,
        args.exclude_csvs,
        args.json
    )
