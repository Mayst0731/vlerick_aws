from pprint import pprint

import requests
import time
import bs4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from download_parse import download_site

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def extract_detail_from_cate_page(cate_url):
    course_list = []
    xpath = '/html/body/form/div[3]/div/div[10]/div[2]/section[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/button'
    class_name = 'col-xs-12 col-sm-6 col-md-4 col-lg-4 programmesItem'
    courses = click_and_get_courses(cate_url,xpath,class_name)
    for course in courses:
        name = ''
        url = ''
        category = ''
        img_url = ''
        type = ''
        desc = ''
        try:
            name = course.find('h5',attrs={"class":"cardHeadingForOverviews"}).text.strip()
        except:
            pass
        try:
            url = course.find('a').get('href')
        except:
            pass
        try:
            category = course.find('div',attrs={"class","category"}).text.strip()
        except:
            pass
        try:
            img_url = course.find('img').get('src')
        except:
            pass

        try:
            type = course.find_all('img')[1].parent.text
        except:
            pass

        try:
            desc = course.find('p',attrs={"class":"newsDescription"}).text.strip()
        except:
            pass
        info = {'name':name,
                'url':url,
                'category':category,
                'type':type,
                'img_url':img_url,
                'desc':desc,
                'category_url':cate_url,
                'parent_url':cate_url}
        course_list.append(info)
    return course_list


def click_and_get_courses(url,xpath,class_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    browser = webdriver.Chrome(executable_path=r'./chromedriver')
    # --| Parse
    browser.get(url)
    time.sleep(2)
    can_click = True
    while can_click:
        try:
            button = browser.find_element_by_xpath(xpath=xpath)
            button.click()
        except:
            can_click = False

    page = bs4.BeautifulSoup(browser.page_source, 'lxml')
    courses = page.find_all("div", attrs={"class": class_name})
    browser.quit()
    return courses


def filter_category(courses,cate_url):
    cate_list = []
    cate_set = set()
    for course in courses:
        if course['category'] not in cate_set:
            info = {'category':course['category'],
                    'url':cate_url,
                    'parent_url':cate_url}
            cate_list.append(info)
            cate_set.add(course['category'])
    return cate_list


def delete_repeating_courses(courses):
    course_dict = dict()
    for course in courses:
        if course['url'] not in course_dict:
            category_list = [course['category']]
            category_url_list = [course['category_url']]
            course_dict[course['url']] = {'name':course['name'],
                    'url':course['url'],
                    'category':category_list,
                    'category_url':category_url_list,
                    'parent_url':course['parent_url'],
                    'type': course['type'],
                    'img_url': course['img_url'],
                    'desc': course['desc']}
        else:
            course_dict[course['url']]['category'].append(course['category'])
            course_dict[course['url']]['category_url'].append(course['category_url'])
    cleanded_courses = []
    for course in course_dict.values():
        cleanded_courses.append(course)
    return cleanded_courses









