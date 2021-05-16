from scrapingfiles.dependencies import json


def write_info_to_json(info_lst,file_name):
    with open(file_name, 'w') as cp:
        json.dump(info_lst, cp)
