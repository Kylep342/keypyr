import csv


def check_csv(path_to_csv_file, uniq_constraints, headers=True):
    """
    """
    seen_keys, duplicate_keys = {}, {}
    file_name = path_to_csv_file.split('/')[-1]
    table_name = file_name.replace('.csv', '')

    with open(path_to_csv_file, 'r') as csv_file:
        if headers:
            header_list = next(csv_file)
            constraint_locs = [[header_list.index(col)] for constraint in uniq_constraints for col in constraint]
            for row in csv_file:
                for constraint in constraint_locs:
