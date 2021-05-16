from urllib import parse
import re
import bs4


from download_parse import download_site


async def get_overview_info(course,course_obj,session):
    video_info = get_video_info(course_obj)
    overview = get_course_desc(course_obj)
    who_should_attend = await get_who_should_attend_info(course,course_obj,session)
    takeaways = await get_takeaways(course,course_obj,session)
    return {"video_title":video_info['video_title'],
            "video_url":video_info['video_url'],
            "overview":overview,
            "who_should_attend":who_should_attend,
            "course_takeaways":takeaways}


def get_video_info(course_obj):
    video_url = ''
    video_title = ''
    try:
        video_session = course_obj.find('div',attrs={"class":"ytp-title-text"})
        video_title = video_session.find('a').text
        video_url = video_session.find('a').get('href')
    except:
        pass
    return {'video_title':video_title,
            'video_url':video_url}


def get_course_desc(course_obj):
    para = ''
    try:
        desc_session_div = course_obj.find('div',attrs={'class':'rte'})
        children_objs = desc_session_div.findChildren()
        for child in children_objs:
            if child.name == 'h1' or child.name == 'h2':
                continue
            elif child.name == 'hr':
                break
            elif child.name == 'p':
                para += child.text
            elif child.name == 'h3':
                para += child.text

        para = para.replace('\xa0',' ').strip()
    except:
        pass
    return para


def get_who_should_attend_url(course_url,course_obj):
    who_should_attend_url = ''
    a_link = course_obj.find('a', text='For whom?')
    if not a_link:
        a_link = course_obj.find('a', text='For Whom?')
    if a_link:
        who_should_attend_url_post = a_link.get('href')
        who_should_attend_url = parse.urljoin(course_url, who_should_attend_url_post)
    return who_should_attend_url


async def get_takeaways(course,course_obj,session):
    takeaways = ''
    try:
        takeaways_link = course_obj.find("a", text="Why this programme?").get('href')
        takeaways_url = parse.urljoin(course['url'], takeaways_link)
        page_obj = await download_site(takeaways_url,session)
        if page_obj.find('div',attrs={"class":"rte"}).find('p') and page_obj.find('div', attrs={"class": "rte"}).find('li'):
            takeaways_sessions = page_obj.find('div',attrs={"class":"rte"}).find_all('p')
            takeaways_sessions += page_obj.find('div',attrs={"class":"rte"}).find_all('li')
        elif page_obj.find('div',attrs={"class":"rte"}).find('p'):
            takeaways_sessions = page_obj.find('div', attrs={"class": "rte"}).find_all('p')
        elif page_obj.find('div', attrs={"class": "rte"}).find('li'):
            takeaways_sessions = page_obj.find('div', attrs={"class": "rte"}).find_all('li')
        for takeaways_session in takeaways_sessions:
            takeaways += takeaways_session.text
    except:
        pass
    return takeaways


async def get_who_should_attend_info(course,course_obj,session):
    who_should_attend = ''
    try:
        who_should_attend_url = get_who_should_attend_url(course['url'],course_obj)
        who_should_attend_obj = await download_site(who_should_attend_url,session)
        who_should_attend_div = who_should_attend_obj.find('div', attrs={'class': 'rte'})
        children_objs = who_should_attend_div.findChildren()
        who_should_attend = ''
        for child in children_objs:
            if child.name == 'p':
                who_should_attend += '\n' + child.text
            if child.name == 'ul':
                who_should_attend_lis = child.find_all('li')
                for who_should_attend_li in who_should_attend_lis:
                    who_should_attend += who_should_attend_li.text
        who_should_attend = who_should_attend.replace('\xa0',' ').strip()
    except:
        pass
    return who_should_attend


# **********************************************************************************
def get_overview_info_way2(course,course_obj,session):
    video_info = get_video_info(course_obj)
    who_should_attend = get_overview_info_way2(course_obj)
    takeaways = get_takeaways_way2(course_obj)
    overview = get_course_desc_way2(course_obj)
    return {"video_title":video_info['video_title'],
            "video_url":video_info['video_url'],
            "overview":overview,
            "who_should_attend":who_should_attend,
            "course_takeaways":takeaways}


def get_who_should_attend_way2(course_obj):
    who_should_attend = ''
    try:
        who_should_attend_related_session = course_obj.find("a",attrs={"id":"forwhom"})
        who_should_attend_sessions = who_should_attend_related_session.parent.parent.parent.find_all('p')
        for who_should_attend_session in who_should_attend_sessions:
            who_should_attend += who_should_attend_session.text
    except:
        pass
    if not who_should_attend_related_session:
        try:
            who_should_attend_relate_session = course_obj.find("strong",text="who would benefit?")
            who_should_attend_session = who_should_attend_relate_session.parent.parent.find('div',
                                                                                             attrs={
                                                                                                 "class":"text-wrap"})
            who_should_attend += who_should_attend_session.text
        except:
            pass
    if not who_should_attend_related_session:
        try:
            who_should_attend_relate_session = course_obj.find("strong",text="For whom")
            who_should_attend_sessions = who_should_attend_relate_session.parent.parent.find_all('p')
            for who_should_attend_session in who_should_attend_sessions:
                who_should_attend += who_should_attend_session.text
        except:
            pass

    return who_should_attend


def get_takeaways_way2(course_obj):
    takeaways = ''
    try:
        takeaways_related_session = course_obj.find('a',attrs={"id":"why"})
        takeaways_session = takeaways_related_session.parent.parent.parent.find('div',attrs={"class":"text-wrap"})
        if takeaways_session:
            if takeaways_session.find('p'):
                takeaways_session.p.extract()
            takeaways += takeaways_session.text.strip()
        if not takeaways_session:
            takeaways_sessions = takeaways_related_session.parent.parent.find_all('li')
            for takeaways_session in takeaways_sessions:
                takeaways += takeaways_session.text.strip()
        takeaways = takeaways.strip()
        return takeaways
    except:
        pass
    if not takeaways_related_session:
        try:
            takeaways_related_session = course_obj.find('strong',text="WHY THIS PROGRAMME?")
            takeaways_sessions =takeaways_related_session.parent.parent.find_all('li')
            for takeaways_session in takeaways_sessions:
                takeaways += takeaways_session.text.strip()
        except:
            pass
    takeaways = takeaways.strip()
    return takeaways


def get_course_desc_way2(course_obj):
    desc = ''
    try:
        desc_related_session = course_obj.find('a',attrs={"id":"design"})
        desc_session = desc_related_session.parent.parent.parent.find('div',attrs={"class":"text-wrap"})
        desc = desc_session.text
    except:
        pass
    if not desc_related_session:
        try:
            desc_session = course_obj.find('div',attrs={"class":"white-block"})
            desc = desc_session.text
        except:
            pass
    if not desc:
        try:
            desc_sessions = course_obj.find('div',attrs={"class":"grey-block sue-content-block"}).find_all('div',
                                                                                                           attrs={
                                                                                                               "class":"text-wrap"})
            for desc_session in desc_sessions:
                desc += desc_session.text
        except:
            pass
    desc = re.sub('[\s{2,3}]', ' ', desc)
    return desc

# special_version_url = ["https://www.vlerick.com/en/programmes/management-programmes/accounting-finance/essentials-in-finance",
#                         "https://www.vlerick.com/en/programmes/management-programmes/digital-transformation/digital-leadership",
#                         "https://www.vlerick.com/en/programmes/management-programmes/general-management/learn-to-speak-business",
#                         "https://www.vlerick.com/en/programmes/management-programmes/marketing-sales/essentials-in-marketing",
#                         "https://www.vlerick.com/en/programmes/management-programmes/operations-supply-chain-management/essentials-in-operations",
#                         "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/essentials-in-people-skills",
#                         "https://www.vlerick.com/en/programmes/management-programmes/strategy/essentials-in-strategy",
#                         "https://www.vlerick.com/en/programmes/management-programmes/people-management-leadership/negotiate-for-success"]
#
# for url in special_version_url:
#     source = requests.get(url).content
#     page = bs4.BeautifulSoup(source,'lxml')
#     print(url)
#     desc = get_course_desc_way2(page)
#     print(desc)


# url = "https://www.vlerick.com/en/programmes/management-programmes/special-industries-financial-services-management/asset-management/why-this-programme"
# source = requests.get(url).content
# page = bs4.BeautifulSoup(source,'lxml')
# takeaways = get_course_take_away_other_link(page)
# print(f'takeaways: {takeaways}')