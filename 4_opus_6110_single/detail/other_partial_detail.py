import bs4
import requests
import re
from download_parse import download_site


async def course_page_detail(course,session):
    url = course["url"]
    exec_ed_inquiry_cc_emails = ''
    who_attend_desc = ''
    course_takeaways = ''
    try:
        page = await download_site(url,session)
        contact_email = contact_info(page)
    except:
        pass
    try:
        exec_ed_inquiry_cc_emails = contact_email(page)
    except:
        pass
    try:
        who_attend_desc = who_attend_info(page)
    except:
        pass
    try:
        course_takeaways = course_takeaways_desc(page)
    except:
        pass
    info = {"course_takeaways":course_takeaways,
            "exec_ed_inquiry_cc_emails":exec_ed_inquiry_cc_emails,
            "who_attend_desc":who_attend_desc}
    new_course = {**course,**info}
    return new_course


def contact_info(page):
    mail = ''
    try:
        mail = page.find('div',text="Email").find_next('a').get('href')
        mail = mail.replace('mailto:',"").strip()
    except:
        pass
    return mail


def who_attend_info(page):
    who_attend_desc = ''
    try:
        related_session = page.find('h2',text="Is This Program Right for You?")
        who_attend_desc = related_session.find_next('div').text
        who_attend_desc = re.sub(' +',' ',who_attend_desc)
        who_attend_desc = who_attend_desc.strip()
        who_attend_desc = who_attend_desc.replace('\n','*')
    except:
        pass
    return who_attend_desc


def course_takeaways_desc(page):
    takeaways = ''
    try:
        takeaways_related_session = page.find('h2',text="Benefits of This Program")
        takeaways = takeaways_related_session.parent.parent.find_next('div',attrs={"class":"block__inner"}).text
        takeaways = re.sub(' +',' ',takeaways)
        takeaways = takeaways.replace('\n', '*')
    except:
        pass
    return takeaways


