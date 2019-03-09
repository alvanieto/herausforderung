import pytest

from herausforderung.adapter import adapt_data


def test_adapt_data():
    expected = ({
        1: 'eins',
        2: 'zwei'
    }, {
        3: 'drei',
        4: 'vier'
    })
    data_1 = [{
        1: 'eins',
        2: 'zwei'
    }]
    data_2 = [{
        3: 'drei',
        4: 'vier'
    }]
    assert next(adapt_data(data_1, data_2)) == expected


def test_adapt_data_different_number_of_rows():
    with pytest.raises(StopIteration):
        data_1 = [{
            1: 'eins',
            2: 'zwei'
        }]
        next(adapt_data(data_1, []))
