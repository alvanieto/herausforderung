def alghoritm_pipeline(alghoritm=''):
    """Factory that return a pipeline of alghortms.

    :param alghoritm: Name of the alghoritm pipeline
    :return: A list of alghoritm to apply
    """
    return _ALGHORITM_PIPELINES.get(alghoritm, [])


def _lowercase(value: str) -> str:
    return value.lower()


_ALGHORITM_PIPELINES = {
    'simple': [
        _lowercase,
    ]
}
