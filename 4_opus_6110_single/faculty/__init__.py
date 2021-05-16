import json
from pprint import pprint


def get_faculty_urls_with_name(courses):
    faculty_name_list = filter_out_all_fac_names(courses)
    fac_urls = []
    for fac_name in faculty_name_list:
        print(fac_name)
        first_name = fac_name.split()[0].lower()
        last_name = fac_name.split()[1].lower()
        fac_url = "https://business.stthomas.edu/faculty-research/faculty-bios/"+last_name+"-"+first_name+"/index.html"
        fac_urls.append((fac_name,fac_url))
    return fac_urls


def filter_out_all_fac_names(courses):
    names_set = set()
    for course in courses:
        faculties = course["course_faculties"]
        if len(faculties)>0:
            for fac in faculties:
                names_set.add(fac)
    return list(names_set)






# with open("../detail/outputfiles/detail_6110_CBUS_XW_0226.json",'r') as f:
#     info = json.load(f)
#
#
# urls = get_faculty_urls(info)
# pprint(urls)
