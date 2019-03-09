import os
from decimal import Decimal

import pytest

from herausforderung.generator import generate_file


@pytest.fixture(scope='module')
def clean_previos_file():
    os.remove('merged_data.csv')


def test_generate_file():
    data = [{
        'id_store': 1,
        'var1': 74,
        'var2': 88,
        'ratio': Decimal(74 / 88)
    }, {
        'id_store': 2,
        'var1': 100,
        'var2': 50,
        'ratio': Decimal(2)
    }]
    expected = '\n'.join(['id_store;var1;var2;ratio',
                          '1;74;88;0.841',
                          '2;100;50;2.000', ''])
    generate_file(data)
    with open('merged_data.csv') as csv_file:
        assert csv_file.read() == expected
