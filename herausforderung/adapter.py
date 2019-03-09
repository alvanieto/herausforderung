def adapt_data(data_1, data_2):
    """Prepare the data to be processed.

    :param data_1: generator of data_1 dict
    :param data_2: generator of data_2 dict
    :return: generator of tuples of data_1 and data_2
    """
    for row_1, row_2 in zip(data_1, data_2):
        yield row_1, row_2
