import csv
import os


def check_csv(path_to_csv_file, uniq_constraints, headers=True):
    #TODO: Work
    """
    check_csv is the main utility in this package.

    Inputs:
        path_to_csv_file    [STRING]:       A file path to csv data for a SQL table


    """

    file_name = path_to_csv_file.split('/')[-1]
    table_name = file_name.replace('.csv', '')

    seen_keys = {constraint['name'] : {} for constraint in uniq_constraints}
    duplicate_keys = {'.'.join(table_name, constraint['name']) : [] for constraint in uniq_constraints}


    with open(path_to_csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        if headers:
            header_list = next(reader)
        constraint_locs = [[header_list.index(col)] for constraint['column_names'] in uniq_constraints for col in constraint]
        for row in reader:
            for constraint in constraint_locs:
                _key = (row[i] for i in constraint)
                if _key not in seen_keys.keys():
                    seen_keys[constraint['name']][_key] = True
                else:
                    duplicate_keys['.'.join(table_name, constraint['name'])].insert(_key)
    return duplicate_keys
