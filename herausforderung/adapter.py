def adapt_data(data, type_):
    """Convert a list of dict to a dict with the field address as key.

    :param data: list of dict to adapt
    :param type_: namedtuple with the type specific info
    :return: dict
    """
    def _typed(row):
        return type_(**{field: row.get(field) for field in type_._fields})

    return {row['address']: _typed(row) for row in data if row.get('address')}
