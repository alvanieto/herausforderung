import re


def algorithm_pipeline(algorithm=''):
    """Factory that return a pipeline of algorthms.

    :param alghritom: Name of the algorithm pipeline
    :return: A list of algorithm to apply
    """
    return _ALGHORITM_PIPELINES.get(algorithm, [])


def _lowercase(value: str) -> str:
    return value.lower()


def _remove_special_chars(value: str) -> str:
    # NOTE: Order of special chars is important if the chars appears in various patterns
    return re.sub(r' – | - ', ' ', value)


def _normalize_street(value: str) -> str:
    return re.sub(r' st\.| st$', ' street', value)


def _normalize_road(value: str) -> str:
    return re.sub(r' rd\.| rd$', ' road', value)


_ALGHORITM_PIPELINES = {
    'simple': [
        _lowercase,
    ],
    'no_special_chars': [
        _lowercase,
        _remove_special_chars
    ],
    'normalize_street': [
        _lowercase,
        _remove_special_chars,
        _normalize_street
    ],
    'normalize_road': [
        _lowercase,
        _remove_special_chars,
        _normalize_street,
        _normalize_road
    ]
}
