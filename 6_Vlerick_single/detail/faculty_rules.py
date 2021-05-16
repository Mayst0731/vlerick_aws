import re
from pprint import pprint
from urllib import parse

import bs4

from download_parse import download_site

'''
Mission 1: Get all faculty info for storing into a single file

{name:'',
title:'',
pic_url:'',
university_school:'',
intro_desc:'',
pdf_url:''
}


Mission 2: Get only name and title and store into each course info 
{
name : '',
title :''
}

'''


# get the link of faculties from course page
def get_faculty_url(course_url,course_obj):
    faculty_url = ''
    a_link = course_obj.find('a',text='Faculty')
    if a_link:
        faculty_url_post = a_link.get('href')
        faculty_url = parse.urljoin(course_url,faculty_url_post)
    return faculty_url


# Get all the information of faculties
async def get_faculty_info(course,course_obj,session):
    faculties = []
    try:
        fac_url = get_faculty_url(course['url'],course_obj)
        faculty_obj = await download_site(fac_url, session)
        tables = faculty_obj.find_all('table')
        for table in tables:
            person = {}
            tds = table.tbody.tr.find_all('td')

            img = ''
            try:
                img = tds[0].img.get('src')
            except Exception:
                pass

            name = ""
            try:
                name_obj = tds[1].a
                # check if name obj exists
                if not name_obj:
                    name_obj = tds[1].p

                name = name_obj.text
            except Exception:
                pass


            title = ''
                # check if title span exists
            try:
                title = tds[1].span.text
            except Exception:
                print(f'{name} has no title')

            intro = ''
            try:
                intro = str(tds[1].p.next_sibling)
            except Exception:
                print(f'{name} has no intro')

            if img.startswith('/~/') or len(img)!=0:
                img=complete_img_url(img)
            # cut off useless info in name
            name = delete_titles_in_name(name)
            name = cut_title_from_name(name)
            if len(name) != 0:
                person['name'] = name
                person['title'] = title.strip()
                person['pic_url'] = img
                person['intro_desc'] = intro.strip()
                person['university_school'] = '2222_EUR'
                person['pdf_url'] = ''
                faculties.append(person)
    except:
        pass
    return faculties


#Get partial info of each faculty for storing to the course detail
def get_partial_faculty_info(faculty_obj):
    '''
    :param faculty_url,faculty_obj
    :return: partial faculty info list
    '''
    tables = faculty_obj.find_all('table')
    faculties = []
    for table in tables:
        person = {}
        tds = table.tbody.tr.find_all('td')
        name = tds[1].a.text
        name = delete_titles_in_name(name)
        name = cut_title_from_name(name)
        title = tds[1].span.text.strip()
        person['name'] = name
        person['title'] = title
        faculties.append(person)
    return faculties


def delete_titles_in_name(name):
    '''
    The function is for clearing the useless information
    '''
    name_lst = name.split()
    if "Prof" in name_lst:
        name_lst.remove("Prof")
    if "Prof." in name_lst:
        name_lst.remove("Prof.")
    if "Professor" in name_lst:
        index_of_Professor = name_lst.index("Professor")
        name_lst = name_lst[:index_of_Professor]
    if "CEO" in name_lst:
        index_of_CEO = name_lst.index("CEO")
        name_lst = name_lst[:index_of_CEO]
    if "Founding" in name_lst:
        index_of_Founding = name_lst.index("Founding")
        name_lst = name_lst[:index_of_Founding]
    if "Managing" in name_lst:
        index_of_Managing = name_lst.index("Managing")
        name_lst = name_lst[:index_of_Managing]
    if "Director" in name_lst:
        index_of_Director = name_lst.index("Director")
        name_lst = name_lst[:index_of_Director]
    if "dr." in name_lst:
        name_lst.remove("dr.")
    if "Lecturer" in name_lst:
        index_of_Lecturer = name_lst.index("Lecturer")
        name_lst = name_lst[:index_of_Lecturer]
    if "Executive" in name_lst:
        index_of_Executive = name_lst.index("Executive")
        name_lst = name_lst[:index_of_Executive]
    if "Chief" in name_lst:
        index_of_Chief = name_lst.index("Chief")
        name_lst = name_lst[:index_of_Chief]
    if len(name_lst) > 10:
        name_lst = [""]
    new_name = " ".join(name_lst)
    return new_name


def cut_title_from_name(name):
    new_name = name
    if '\n' in name:
        name_lst = name.split('\n')
        new_name = name_lst[0]
    return new_name


def complete_img_url(src):
    url = parse.urljoin("https://www.vlerick.com", src)
    return url

# **********************************************************************************
async def get_faculty_info_way2(course,course_obj,session):
    faculties = []
    try:
        fac_urls = collect_fac_urls(course["url"],course_obj)
        for fac_url in fac_urls:
            if course['url'] == "https://www.vlerick.com/en/programmes/management-programmes/general-management/learn-to-speak-business":
                faculties = get_learn_to_speak_faculty(course['url'],course_obj)

            elif course['url'] == "https://www.vlerick.com/en/programmes/management-programmes/digital-transformation/digital-leadership":
                faculties = get_digital_leadership_faculty(course['url'],course_obj)
            else:
                fac_obj = await download_site(fac_url,session)
                one_fac_info = one_fac_info_way2(fac_obj)
                faculties.append(one_fac_info)
    except:
        pass
    return faculties


def get_digital_leadership_faculty(course_url,course_obj):
    faculties = []

    fac_sessions = course_obj.find('table',attrs={"class":"table-content"}).find_all('td')
    for fac_session in fac_sessions:
        name = ''
        title = ''
        pic_url = ''
        pdf_url = ''
        intro_desc = ''
        name = fac_session.strong.text
        if '-' in name:
            name,key,title = name.partition('-')
            if 'Professor' in name:
                name = name.replace("Professor", '').strip()
        elif 'Professor' in name:
            title = 'Professor'
            name = name.replace(title,'').strip()
        pic_link = fac_session.find('img').get('src')
        pic_url = parse.urljoin(course_url,pic_link)
        intro_desc = fac_session.find_all('p')[1].text
        fac = {"name": name,
               "title": title,
               "pic_url": pic_url,
               "intro_desc": intro_desc,
               "pdf_url": pdf_url}
        faculties.append(fac)

    return faculties


async def get_learn_to_speak_faculty(course_url,course_obj,session):
    faculties = []
    faculty_sessions = course_obj.find("table",attrs={"class":"table-content"}).find_all("td")
    for faculty_session in faculty_sessions:
        name = ''
        title = ''
        pic_url = ''
        intro_desc = ''
        pdf_url = ''
        name = faculty_session.find('strong').text
        if 'Prof' in name:
            name = name.replace('Prof','').strip()
        pic_url = faculty_session.find('img').get('src')
        one_link = faculty_session.find("a").get('href')
        one_url = parse.urljoin(course_url,one_link)
        other_info = await get_learn_to_speak_other_info(one_url,session)
        title = other_info['title']
        intro_desc = other_info['intro_desc']
        fac = {"name":name,
               "title":title,
               "pic_url":pic_url,
               "intro_desc":intro_desc,
               "pdf_url":pdf_url}
        faculties.append(fac)
    return faculties


async def get_learn_to_speak_other_info(url,session):
    page = await download_site(url,session)
    title,intro_desc = get_learn_to_speak_title_desc(page)
    return {"title":title,
            "intro_desc":intro_desc}


def get_learn_to_speak_title_desc(page):
    title = ''
    intro_desc = ''
    try:
        title_session = page.find("div",attrs={"class":"js-equal-height grid_13 alpha omega"})
        title_session.h1.extract()
        title_session_text = str(title_session)
        title,br,intro_desc = title_session_text.partition("<br/>")
        cutpart_idx = title.index('rte">')+5
        title = title[cutpart_idx:].strip()
        intro_desc= intro_desc.replace('</div>','').strip()
    except:
        pass
    return [title,intro_desc]




def collect_fac_urls(course_url,course_obj):
    urls = []
    links = course_obj.find_all("a",text="Learn more")
    for link in links:
        post_url = link.get('href')
        url = parse.urljoin(course_url, post_url)
        urls.append(url)
    return urls


def one_fac_info_way2(fac_page):
    name = ''
    title = ''
    pic_url = ''
    intro_desc = ''
    pdf_url = ''
    info_session = fac_page.find("div",attrs={"class":"c contact-box"})
    try:
        name = info_session.find("strong").text
    except:
        pass
    try:
        title= info_session.find("span").text
    except:
        pass
    try:
        pic_url = info_session.find('img').get('src')
    except:
        pass
    try:
        intro_desc_session= fac_page.find("div",attrs={"class":"faculty-detail"}).find('div',attrs={"class":"rte"})
        intro_desc = intro_desc_session.text
        intro_desc = re.sub('[\s{2,3}]', ' ', intro_desc)
    except:
        pass
    return {
                "name": name,
                "title": title,
                "pic_url": pic_url,
                "intro_desc": intro_desc,
                "pdf_url":pdf_url,
                "university_school": "2222_EUR"
            }

# special_version_url = ["https://www.vlerick.com/en/programmes/management-programmes/accounting-finance/essentials-in-finance",
#                         "https://www.vlerick.com/en/programmes/management-programmes/digital-transformation/digital-leadership",
#                         "https://www.vlerick.com/en/programmes/management-programmes/general-management/learn-to-speak-business",
#                         "https://www.vlerick.com/en/programmes/management-programmes/marketing-sales/essentials-in-marketing",
#                         "https://www.vlerick.com/en/programmes/management-programmes/operations-supply-chain-management/essentials-in-operations",
#                         "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/essentials-in-people-skills",
#                         "https://www.vlerick.com/en/programmes/management-programmes/strategy/essentials-in-strategy",
#                         "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/negotiate-for-success"]
#
#
# fac_urls = []
# for url in special_version_url:
#     source = requests.get(url).content
#     page = bs4.BeautifulSoup(source,'lxml')
#     facs = collect_fac_urls(url,page)
#     fac_urls += facs
#
# print(*fac_urls,sep="\n")
#
#
# for url in fac_urls:
#     print(url)
#     source = requests.get(url).content
#     page = bs4.BeautifulSoup(source, 'lxml')
#     info = one_fac_info_way2(page)
#     pprint(info)

# url = "https://www.vlerick.com/en/programmes/management-programmes/digital-transformation/digital-leadership"
# source = requests.get(url).content
# page = bs4.BeautifulSoup(source, 'lxml')
# info = get_digital_leadership_faculty(url,page)
# pprint(info)



