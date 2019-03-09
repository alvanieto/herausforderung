from extractor import read_csv
from adapter import adapt_data
from alghoritm import alghoritm_pipeline
from matcher import match_data
from merger import merge_data
from generator import generate_file


def merge_files(input_1: str, input_2: str, alghoritm: str = None):
    """Orchestation function.

    :param input_1: csv filename of type 1
    :param input_2: csv filename of type 2
    """
    data_1 = read_csv(input_1)
    data_2 = read_csv(input_2)
    adapted_data = adapt_data(data_1, data_2)
    matched_data = match_data(adapted_data, alghoritm_pipeline(alghoritm))
    merged_data = merge_data(matched_data)
    generate_file(merged_data)
