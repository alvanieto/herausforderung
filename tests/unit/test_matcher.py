import pytest

from herausforderung.matcher import match_data


def test_match_data_no_data():
    data = ({'address': ''}, {'address': ''})
    assert next(match_data([data], [])) == data


def test_match_data_no_address_field():
    assert next(match_data([({}, {})], [])) == ({}, {})


@pytest.fixture
def data_1():
    return {
        'address': 'unter den linden'
    }


def test_match_data_no_alghoritm_pipeline(data_1):
    assert next(match_data([(data_1, data_1)], [])) == (data_1, data_1)


def test_match_data(data_1):
    alghoritm_pipeline = [lambda row: row, lambda row: row]
    assert next(match_data([(data_1, data_1)], alghoritm_pipeline)) == (data_1, data_1)


def test_match_data_no_match_alghoritm(data_1):
    with pytest.raises(StopIteration):
        data_2 = {
            'address': 'oben den linden'
        }
        alghoritm_pipeline = [lambda row: row, lambda row: row]
        next(match_data([(data_1, data_2)], alghoritm_pipeline))
