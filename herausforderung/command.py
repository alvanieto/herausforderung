from extractor import read_csv


def merger(input_1: str, input_2: str, alghoritm: str = None):
    """Orchestation function.

    :param input_1: csv filename of type 1
    :param input_2: csv filename of type 2
    """
    data_1 = read_csv(input_1)
    data_2 = read_csv(input_2)
