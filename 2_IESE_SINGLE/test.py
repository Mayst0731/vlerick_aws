import json
from pprint import pprint

from write_to_json import write_to_json

with open('detail/outputfiles/faculty_2222_EUR_XW_0316.json', 'r') as f:
    data = json.load(f)


for fac in data:
    if len(fac["name"]) > 20 and "Academic Director" in fac["name"]:
        print(f'---------{fac["name"]}')
        fac["name"] = fac["name"].replace("Academic Director",'').strip()
    if len(fac["name"]) > 20 and "Directora académica" in fac["name"]:
        print(f'---------{fac["name"]}')
        fac["name"] = fac["name"].replace("Directora académica",'').strip()

for fac in data:
    print(f'{fac["name"]}: {len(fac["name"])},{len(fac["title"])}, {len(fac["intro_desc"])}')
    if fac["name"] == "Nuria Chinchilla":
        title = fac["title"].split(';')
        title = title[0]
        fac["title"] = title
write_to_json(data, "detail/outputfiles/faculty_2222_EUR_XW_0316.json")

