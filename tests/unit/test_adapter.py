import pytest

from herausforderung.adapter import adapt_data


def test_adapt_data():
    expected = ({
        1: 'eins',
        2: 'zwei',
        'variable1': 10
    }, {
        3: 'drei',
        4: 'vier',
        'variable2': 20
    })
    data_1 = [{
        1: 'eins',
        2: 'zwei',
        'variable1': '10'
    }]
    data_2 = [{
        3: 'drei',
        4: 'vier',
        'variable2': '20'
    }]
    assert next(adapt_data(data_1, data_2)) == expected


def test_adapt_no_variable():
    data_1 = [{
        1: 'eins',
        2: 'zwei'
    }]
    with pytest.raises(StopIteration):
        next(adapt_data(data_1, data_1))


def test_adapt_data_different_number_of_rows():
    with pytest.raises(StopIteration):
        data_1 = [{
            1: 'eins',
            2: 'zwei'
        }]
        next(adapt_data(data_1, []))
