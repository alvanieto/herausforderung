import argparse

from .command import merge_files


def main():
    parser = argparse.ArgumentParser(description='Merge POI-Adquisition data')
    parser.add_argument('input_data_1', type=str, help='part 1 csv file')
    parser.add_argument('input_data_2', type=str, help='part 2 csv file')
    parser.add_argument('--algorithm', dest='algorithm', default='simple',
                        choices=('simple', 'no_special_chars', 'normalize_street',
                                 'normalize_road'),
                        help='normalization algorithm for address field (default: simple)')
    args = parser.parse_args()

    merge_files(args.input_data_1, args.input_data_2, args.algorithm)
    print('File merged_data.csv generated !')
