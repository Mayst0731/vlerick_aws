from pprint import pprint

from download_parse import download_site
import urllib
import bs4
import requests


# need to add async and session later on.
async def extract_categories(url,session):
    executive_page = await download_site(url, session)
    category_list = []
    cate_sessions = executive_page.find_all('li', attrs={'class': 'link-grid__link-item'})
    for cate in cate_sessions:
        cate_name = cate.a.text.strip()
        cate_link = cate.find('a').get('href')
        cate_url = urllib.parse.urljoin(url, cate_link)
        info = {
            'category': cate_name,
            'url': cate_url,
        }
        category_list.append(info)
    for cate in category_list:
        cate.update({'parent_url': url})

    new_cate_list = []
    for cate in category_list:
        new_cate = package_category(cate["url"],cate["parent_url"], cate["category"])
        new_cate_list.append(new_cate)
    return new_cate_list


def package_category(url,parent_url,category):
    if "Health Care" in category:
        url = 'https://business.stthomas.edu/executive-education/individuals/program-finder/health-care/index.html'
    if "Nonprofit Management" in category:
        url = "https://business.stthomas.edu/executive-education/individuals/program-finder/nonprofit-management/index.html"
    if "Project Management" in category:
        url = "https://business.stthomas.edu/executive-education/individuals/program-finder/project-management/index.html"
    cate_info = {
        'category': category,
        'url': url,
        'parent_url': parent_url
    }
    return cate_info


# def test(url,func):
#     res = func(url)
#     pprint(res)
#
# test('https://business.stthomas.edu/executive-education/individuals/index.html',extract_categories)