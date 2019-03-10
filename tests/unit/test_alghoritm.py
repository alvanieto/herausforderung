import pytest

from herausforderung.alghoritm import (alghoritm_pipeline, _lowercase, _remove_special_chars,
                                       _normalize_street, _normalize_road)


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
    ('special – char', 'special char'),
    ('promenades shopping centre 31 the promenades shopping centre bridlington – yo15 2dx',
     'promenades shopping centre 31 the promenades shopping centre bridlington yo15 2dx'),
])
def test_remove_special_chars(value, expected):
    assert _remove_special_chars(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('', ''),
    ('100 high st.', '100 high street'),
    ('1 north st', '1 north street'),
    ('2 southest', '2 southest'),
    ('3 west street', '3 west street'),
])
def test_normalize_street(value, expected):
    assert _normalize_street(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('', ''),
    ('382-384 brixton rd', '382-384 brixton road'),
])
def test_normalize_road(value, expected):
    assert _normalize_road(value) == expected
