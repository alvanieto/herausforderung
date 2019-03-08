import os
from collections import OrderedDict

import pytest

from herausforderung.extractor import read_csv


def test_read_csv():
    expected = [
        OrderedDict([
            ('header1', 'data1'),
            ('header2', 'data2'),
        ]),
        OrderedDict([
            ('header1', 'field1'),
            ('header2', 'field2'),
        ]),
    ]
    assert list(read_csv(_abs_filename('example.csv'))) == expected


def test_read_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        list(read_csv('foo.csv'))


def _abs_filename(filename: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
