def alghoritm_pipeline(alghoritm=''):
    """Factory that return a pipeline of alghortms.

    :param alghoritm: Name of the alghoritm pipeline
    :return: A list of alghoritm to apply
    """
    return _ALGHORITM_PIPELINES.get(alghoritm, [])


def _lowercase(value: str) -> str:
    return value.lower()


def _remove_special_chars(value: str) -> str:
    special_chars = (' - ',)
    for char_ in special_chars:
        value = value.replace(char_, ' ')
    return value


_ALGHORITM_PIPELINES = {
    'simple': [
        _lowercase,
    ],
    'no_special_chars': [
        _lowercase,
        _remove_special_chars
    ]
}
