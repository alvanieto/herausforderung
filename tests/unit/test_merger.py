from decimal import Decimal

import pytest

from herausforderung.merger import merge_data


def test_merge_data_no_data():
    with pytest.raises(StopIteration):
        next(merge_data([]))


def test_merge_data():
    data = [({
        'id_store': 1,
        'variable1': 90
    }, {
        'variable2': 45
    })]
    expected = {
        'id_store': 1,
        'var1': 90,
        'var2': 45,
        'ratio': 2
    }
    assert next(merge_data(data)) == expected


def test_merge_data_zero_variable2():
    with pytest.raises(ZeroDivisionError):
        data = [({
            'id_store': 1,
            'variable1': 0
        }, {
            'variable2': 0
        })]
        next(merge_data(data))


def test_merge_data_ratio_precision():
    data = [({
        'variable1': 74
    }, {
        'variable2': 88
    })]
    expected = {
        'id_store': '',
        'var1': 74,
        'var2': 88,
        'ratio': Decimal(74 / 88)
    }
    assert next(merge_data(data)) == expected
