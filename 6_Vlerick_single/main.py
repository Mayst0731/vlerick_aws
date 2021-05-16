from category import extract_categories
from course import *
import time
import aiohttp
import asyncio


from detail import extract_details
from final_arrangement import final_run

from write_to_json import write_to_json


async def start_crawl(base_url,special_version_url):
    session = aiohttp.ClientSession()
    category_list = await extract_categories(base_url, session)
    write_to_json(category_list,'./category/outputfiles/categories.json')
    course_list = await extract_courses(category_list,session)
    write_to_json(course_list,'./course/outputfiles/courses.json')
    detail_list = await extract_details(course_list,session,special_version_url)
    write_to_json(detail_list, './detail/outputfiles/comprehensive_details.json')

    await session.close()
    return

if __name__ == '__main__':
    start_time = time.time()
    BASE_URL = "https://www.vlerick.com/en/programmes/management-programmes"

    special_version_url = ["https://www.vlerick.com/en/programmes/management-programmes/accounting-finance/essentials-in-finance",
                           "https://www.vlerick.com/en/programmes/management-programmes/digital-transformation/digital-leadership",
                           "https://www.vlerick.com/en/programmes/management-programmes/general-management/learn-to-speak-business",
                           "https://www.vlerick.com/en/programmes/management-programmes/marketing-sales/essentials-in-marketing",
                           "https://www.vlerick.com/en/programmes/management-programmes/operations-supply-chain-management/essentials-in-operations",
                           "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/essentials-in-people-skills",
                           "https://www.vlerick.com/en/programmes/management-programmes/strategy/essentials-in-strategy",
                           "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/negotiate-for-success"]
    asyncio.run(start_crawl(BASE_URL,special_version_url))
    final_run()
    duration = time.time() - start_time
    minutes = duration//60
    print(f"Crawled {duration} seconds, {minutes} mins")

