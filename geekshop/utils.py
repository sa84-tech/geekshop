import json
import os

from geekshop.settings import BASE_DIR


def get_data(data_name):
    try:

        file_path = os.path.join(BASE_DIR, 'geekshop', 'data', f'{data_name}.json')
        with open(file_path, 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            return data

    except IOError:
        print('I/O Error')
        return
