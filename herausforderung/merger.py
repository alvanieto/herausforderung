from decimal import Decimal


def merge_data(data):
    """Generate a dict with merged data.

    :param data: data_1 and data_2 matched
    :return: dict with merged fields
    """
    for data_1, data_2 in data:
        var1 = data_1.get('variable1', '')
        var2 = data_2.get('variable2', '')
        yield {
            'id': data_1.get('id', ''),
            'var1': var1,
            'var2': var2,
            'ratio': Decimal(var1 / var2)
        }
