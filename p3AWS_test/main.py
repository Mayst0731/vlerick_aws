
import urllib
from pprint import pprint
import requests
from bs4 import BeautifulSoup


def category_info_object(url,parent_url,category):
    cate_info = {
        'category': category,
        'url': url,
        'parent_url': parent_url
    }
    return cate_info


def get_categories():
    url = 'https://www.insead.edu/executive-education/open-programmes'
    html = requests.get(url)
    soup_category_page = BeautifulSoup(html.content, "html.parser")
    # Initialize the return category
    all_categories = []
    category_nav_bar= soup_category_page.find("ul", attrs={"class": "level1"})
    categories_level1 = category_nav_bar.find_all('li',attrs={"class": ""})
    # Got the three categories directly from the navbar
    three_cates = ["Live Virtual Programmes","Certificates", "Coaching"]
    for cate in categories_level1:
        cate_name = cate.a.text
        if cate_name in three_cates:
            cate_url_a = cate.a.get('href')
            cate_url = urllib.parse.urljoin('https://www.insead.edu/executive-education/', cate_url_a)
            cate_info = category_info_object(cate_url, url, cate_name)
            all_categories.append(cate_info)
    open_programme_nav = category_nav_bar.find('li',attrs={"class": "active"})
    open_programme_toggle = open_programme_nav.find('ul',attrs={"class": "level2"})
    open_programmes = open_programme_toggle.find_all('li', recursive=False)
    for cate in open_programmes:
        cate_name = cate.a.text
        cate_url_a = cate.a.get('href')
        cate_url = urllib.parse.urljoin('https://www.insead.edu/executive-education/', cate_url_a)
        cate_info = category_info_object(cate_url,url,cate_name)
        all_categories.append(cate_info)
    # Because the last category is programme finder, delete it
    all_categories.pop()
    return all_categories[0]


pprint(get_categories())


