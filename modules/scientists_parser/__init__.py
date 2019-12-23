from modules.scientists_parser.parser import *
import pandas as pd
import os
from modules.scientists_pages.scientists_link_parser import scientists_pages_path
from datetime import datetime as dt


def run():
    script_dir = os.path.dirname(__file__)
    data_path = os.path.relpath(scientists_pages_path(), script_dir) + '/data'
    scientists_pages = os.listdir(data_path)
    print('Started', dt.now())
    parsed_data = []
    for science in scientists_pages:
        file = open(data_path + '/' + science, 'r')
        scientist_type = next(file).strip('\n')
        print(scientist_type)
        links = []
        for line in file:
            links.append(line.strip('\n'))

        df = parse_all_scientists(links, scientist_type)
        df.to_csv('data/parsed_scientists_' + scientist_type.lower() + '.csv')
        file.close()
        parsed_data.append(df)

    df = pd.concat(parsed_data)
    print('Data was written', dt.now())
    df.reset_index(drop=True).to_csv('data/parsed_data.csv')


if __name__ == '__main__':
    run()
