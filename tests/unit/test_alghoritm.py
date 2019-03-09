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
