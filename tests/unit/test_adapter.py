import pytest

from herausforderung.adapter import adapt_data
from herausforderung.data_types import Type1, Type2


@pytest.mark.parametrize('type_', [
    (Type1,),
    (Type2,),
])
def test_adapt_data_no_data(type_):
    assert adapt_data([{}], type_) == {}


def test_adapt_data_type_1_not_all_fields():
    expected = {
        'avenida de trueba': Type1(1, 'A', None),
        'glorieta de quevedo': Type1(2, None, 99)
    }
    data = [{
        'id': 1,
        'address': 'avenida de trueba',
        'category': 'A',
    }, {
        'id': 2,
        'address': 'glorieta de quevedo',
        'variable1': 99
    }]
    assert adapt_data(data, Type1) == expected


def test_adapt_data_type_2_not_all_fields():
    expected = {
        'avenida de trueba': Type2(33),
        'glorieta de quevedo': Type2(None)
    }
    data = [{
        'address': 'avenida de trueba',
        'variable2': 33,
    }, {
        'address': 'glorieta de quevedo'
    }]
    assert adapt_data(data, Type2) == expected
