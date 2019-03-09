import pytest

from herausforderung.alghoritm import alghoritm_pipeline, _lowercase


@pytest.mark.parametrize('alghoritm, expected', [
    ('', []),
    ('simple', [_lowercase]),
])
def test_alghoritm_pipeline(alghoritm, expected):
    assert alghoritm_pipeline(alghoritm) == expected


def test_alghoritm_pipeline_default():
    assert alghoritm_pipeline() == []


@pytest.mark.parametrize('field, expected', [
    ('', ''),
    ('HallO WeLt', 'hallo welt'),
    ('HERAUS ', 'heraus '),
    (' forderung ', ' forderung '),
])
def test_alghoritm_lowercase(field, expected):
    assert _lowercase(field) == expected
