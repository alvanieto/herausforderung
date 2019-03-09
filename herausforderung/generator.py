import csv
from copy import deepcopy
from decimal import Decimal, ROUND_UP


def generate_file(data):
    """Generate merged csv file. Ratio precision set to 3 decimals round up.

    :param data: data of type 1 and 2
    """
    with open('merged_data.csv', 'w') as csv_file:
        fieldnames = ('id', 'var1', 'var2', 'ratio')
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        data_copy = deepcopy(data)
        for row in data_copy:
            row['ratio'] = row['ratio'].quantize(Decimal('0.001'), rounding=ROUND_UP)
            writer.writerow(row)
