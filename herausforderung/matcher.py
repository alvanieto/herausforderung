import logging
from copy import copy


logging.basicConfig(level=logging.INFO, filename='herausforderung.log')


def match_data(data, alghoritm_pipeline):
    """This function try to match the two addresses applying the alghoritm defined in the pipeline.

    :param data: a row from file one and file two
    :return: generator with matched data
    """
    for data_1, data_2 in data:
        address_1 = data_1.get('address', '')
        address_2 = data_2.get('address', '')
        logging.info(f'Matching: #{address_1}# and #{address_2}#')
        if address_1 == address_2:
            logging.info('Matched, same name')
            yield data_1, data_2
        for alghoritm in alghoritm_pipeline:
            address_1 = alghoritm(address_1)
            address_2 = alghoritm(address_2)
            if address_1 == address_2:
                logging.info(f'Matched: {address_1} and {address_2}')
                new_data_1 = copy(data_1)
                new_data_1['address'] = address_1
                new_data_2 = copy(data_2)
                new_data_2['address'] = address_2
                yield new_data_1, new_data_2
        logging.info('Not matched')
