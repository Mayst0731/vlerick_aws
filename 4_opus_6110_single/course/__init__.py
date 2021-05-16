from pprint import pprint
from urllib import response

import bs4
import requests

from write_to_json import write_to_json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
from download_parse import download_site
import urllib

# async and session need to be added later on


def extract_courses():
    url = 'https://cbecrm.stthomas.edu/web_service/services.asmx/GetPrograms'
    source = requests.get(url, headers=headers).json()
    course_list = source['Programs']
    return course_list





def get_instructors_info():
    return


def get_staff_info():
    return












