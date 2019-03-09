from copy import copy


def adapt_data(data_1, data_2):
    """Prepare the data to be processed.

    :param data_1: generator of data_1 dict
    :param data_2: generator of data_2 dict
    :return: generator of tuples of data_1 and data_2
    """
    for row_1, row_2 in zip(data_1, data_2):
        if row_1.get('variable1') and row_2.get('variable2'):
            new_row_1 = copy(row_1)
            new_row_2 = copy(row_2)
            new_row_1['variable1'] = int(row_1['variable1'])
            new_row_2['variable2'] = int(row_2['variable2'])
            yield new_row_1, new_row_2
