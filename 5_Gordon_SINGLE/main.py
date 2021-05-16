import time
from pprint import pprint

import aiohttp
import asyncio

import bs4
import requests

from category import extract_detail_from_cate_page, filter_category, delete_repeating_courses
from course import extract_recommend_courses
from download_parse import download_site
from write_to_json import write_to_json

def start_crawl(base_url):
    partial_details = extract_detail_from_cate_page(base_url)
    write_to_json(partial_details, './files/origianl_detail_partial.json')
    category = filter_category(partial_details, base_url)
    write_to_json(category, './files/category.json')
    cleaned_courses = delete_repeating_courses(partial_details)
    write_to_json(cleaned_courses, './files/cleaned_detail_partial.json')



if __name__ == '__main__':
    start_time = time.time()
    BASE_URL = 'https://www.gibs.co.za/academic-programmes/Pages/Academic-Programmes-and-Courses-Overview.aspx'
    start_crawl(BASE_URL)
    duration = time.time() - start_time
    minutes = duration // 60
    print(f"Crawled {duration} seconds, {minutes} mins")






