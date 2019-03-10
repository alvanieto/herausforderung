from unittest import mock

from herausforderung.command import merge_files


@mock.patch('herausforderung.command.generate_file')
@mock.patch('herausforderung.command.merge_data')
@mock.patch('herausforderung.command.algorithm_pipeline')
@mock.patch('herausforderung.command.match_data')
@mock.patch('herausforderung.command.adapt_data')
@mock.patch('herausforderung.command.read_csv')
def test_merge_data(read_csv, adapt_data, match_data, algorithm_pipeline, merge_data,
                    generate_file):
    read_csv.side_effect = ['data_1', 'data_2']
    adapt_data.return_value = 'adapted_data'
    algorithm_pipeline.return_value = None
    match_data.return_value = 'matched_data'
    merge_data.return_value = 'merged_data'

    merge_files('input_1', 'input_2', 'simple')

    read_csv.assert_has_calls([mock.call('input_1'), mock.call('input_2')])
    adapt_data.assert_called_once_with('data_1', 'data_2')
    algorithm_pipeline.assert_called_once_with('simple')
    match_data.assert_called_once_with('adapted_data', None)
    merge_data.assert_called_once_with('matched_data')
    generate_file.assert_called_once_with('merged_data')
