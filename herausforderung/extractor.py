from typing import List
import csv


def read_csv(filename: str) -> List[dict]:
    """Given a csv filename convert it to a generator of dicts where the keys are the columns
    name.

    :param filename: csv filename
    :return: generator of dict
    """
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            yield row
