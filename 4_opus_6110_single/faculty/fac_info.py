import urllib

import bs4
import requests

from download_parse import download_site


async def get_one_fac_info(name,url,session):
    name = name
    page = await download_site(url, session)
    title = get_fac_title(page)
    pic_url = get_fac_pic_url(page)
    pdf_url = get_fac_pdf_url(page)
    intro_desc = get_fac_intro_desc(page)
    fac_info = {"name":name,
                "title":title,
                "pic_url":pic_url,
                "pdf_url":pdf_url,
                "intro_desc":intro_desc,
                "university_school":"6110_CBUS"}
    return fac_info



def get_fac_title(page):
    title = ''
    try:
        title = page.find("div",attrs={"id":"content"}).h2.find_next('p').text
        if len(title) > 70:
            title = page.find("div",attrs={"id":"content"}).h3.text
    except Exception as e:
        print(e)
    return title


def get_fac_pic_url(page):
    pic_url = ''
    try:
        pic_link = page.find('img').get('src')
        pic_url = urllib.parse.urljoin("https://business.stthomas.edu/",pic_link)
    except:
        pass
    return pic_url


def get_fac_pdf_url(page):
    pdf_url = ''
    try:
        pdf_link = page.find("a",attrs={"class":"block__cta"}).get('href')
        pdf_url = urllib.parse.urljoin("https://business.stthomas.edu/",pdf_link)
    except:
        pass
    return pdf_url


def get_fac_intro_desc(page):
    intro_desc = ''
    try:
        intro_desc_session = page.select("#block__item-copy-container-facbio-0 > div")
        intro_desc = intro_desc_session[0].text
    except:
        pass
    return intro_desc


url = "https://business.stthomas.edu/faculty-research/faculty-bios/giovannelli-gino/index.html"
source = requests.get(url).content
page = bs4.BeautifulSoup(source,'lxml')
title = get_fac_title(page)
pic_url = get_fac_pic_url(page)
pdf_url = get_fac_pdf_url(page)
desc = get_fac_intro_desc(page)
print(title)
print(pic_url)
print(pdf_url)
print(desc)

