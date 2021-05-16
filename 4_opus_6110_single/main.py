import time

import aiohttp
import asyncio

from course import extract_courses
from detail import extract_details, rename_keys
from detail.other_partial_detail import course_page_detail
from faculty import get_faculty_urls_with_name
from faculty.fac_info import get_one_fac_info
from test import final_run
from write_to_json import write_to_json

from category import extract_categories


async def start_crawl(base_url):
    session = aiohttp.ClientSession()
    category_list = await extract_categories(base_url, session)
    write_to_json(category_list, './category/outputfiles/categories.json')
    course_list = extract_courses()
    write_to_json(course_list, './course/outputfiles/courses.json')
    detail_list = await extract_details(course_list,session)
    write_to_json(detail_list, './detail/outputfiles/origin_details.json')
    partial_detail = rename_keys(detail_list)
    write_to_json(partial_detail, './detail/outputfiles/first_partial_detail.json')

    coroutines = []
    for detail in partial_detail:
        coroutines.append(course_page_detail(detail,session))
    final_details = await asyncio.gather(*coroutines)
    # print(final_details)
    write_to_json(final_details, './detail/outputfiles/detail_6110_CBUS_XW_0226.json')

    fac_urls_with_names = get_faculty_urls_with_name(final_details)
    coroutines = []
    for url_with_name in fac_urls_with_names:
        coroutines.append(get_one_fac_info(url_with_name[0],url_with_name[1],session))
    faculties = await asyncio.gather(*coroutines)
    write_to_json(faculties, 'faculty/outputfiles/faculty_6110_CBUS_XW_0316.json')
    await session.close()
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    BASE_URL = 'https://business.stthomas.edu/executive-education/individuals/index.html'
    asyncio.run(start_crawl(BASE_URL))
    final_run()
    duration = time.time() - start_time
    minutes = duration // 60
    print(f"Crawled {duration} seconds, {minutes} mins")

