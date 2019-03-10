import pytest

from herausforderung.alghoritm import alghoritm_pipeline, _lowercase, _remove_special_chars


@pytest.mark.parametrize('alghoritm, expected', [
    ('', []),
    ('simple', [_lowercase]),
])
def test_alghoritm_pipeline(alghoritm, expected):
    assert alghoritm_pipeline(alghoritm) == expected


def test_alghoritm_pipeline_default():
    assert alghoritm_pipeline() == []


@pytest.mark.parametrize('value, expected', [
    ('', ''),
    ('HallO WeLt', 'hallo welt'),
    ('HERAUS ', 'heraus '),
    (' forderung ', ' forderung '),
])
def test_lowercase(value, expected):
    assert _lowercase(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('', ''),
    ('street-value', 'street-value'),
    ('special - char', 'special char'),
])
def test_remove_special_chars(value, expected):
    assert _remove_special_chars(value) == expected
