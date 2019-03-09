'''POI-Adquisition feature tests.'''

import os
import filecmp

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from herausforderung.command import merge_files


@scenario('poi_adquisition.feature', 'Merging to csv files with different normalization alghoritm')
def test_merging_to_csv_files():
    '''Merging to csv files.'''


@given('two files <input_data_1> and <input_data_2>')
def two_files_input_data_1csv_and_input_data_2csv(input_data_1: str, input_data_2: str):
    pass


@when('I merge these files with normalize alghoritm <alghoritm>')
def i_merge_these_files(input_data_1: str, input_data_2: str, alghoritm: str):
    merge_files(_abs_filename(input_data_1), _abs_filename(input_data_2), alghoritm)


@then('I get the next merged file <merged_data>')
def i_get_the_next_merged_file(merged_data: str):
    assert filecmp.cmp(_abs_filename(merged_data), 'merged_data.csv')


def _abs_filename(filename: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
