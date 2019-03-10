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


@pytest.fixture
def data_2():
    return {
        'address': 'oben den linden'
    }


def test_match_data_no_algorithm_pipeline(data_1):
    assert next(match_data([(data_1, data_1)], [])) == (data_1, data_1)


def test_match_data(data_1, data_2):
    algorithm_pipeline = [lambda row: row, lambda row: 'unter den linden']
    assert next(match_data([(data_1, data_2)], algorithm_pipeline)) == (data_1, data_1)


def test_match_data_no_match_algorithm(data_1, data_2):
    with pytest.raises(StopIteration):
        algorithm_pipeline = [lambda row: row, lambda row: row]
        next(match_data([(data_1, data_2)], algorithm_pipeline))
