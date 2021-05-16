import json
from pprint import pprint

from write_to_json import write_to_json


def final_run():
    with open('faculty/outputfiles/faculty_6110_CBUS_XW_0316.json', 'r') as f:
        data = json.load(f)
    for fac in data:
        print(f'{fac["name"]}, {len(fac["name"])}, {len(fac["title"])}, {len(fac["intro_desc"])}')
        if 'Copyright' in fac["title"]:
            fac["title"] = ''
    write_to_json(data, './faculty/outputfiles/faculty_6110_CBUS_XW_0316.json')
