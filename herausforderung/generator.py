import csv
from copy import copy
from decimal import Decimal, ROUND_UP


def generate_file(data):
    """Generate merged csv file. Ratio precision set to 3 decimals round up.

    :param data: data of type 1 and 2
    """
    with open('merged_data.csv', 'w') as csv_file:
        fieldnames = ('id_store', 'var1', 'var2', 'ratio')
        writer = csv.DictWriter(csv_file, delimiter=';', lineterminator='\n', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            new_row = copy(row)
            new_row['ratio'] = row['ratio'].quantize(Decimal('0.001'), rounding=ROUND_UP)
            writer.writerow(new_row)
