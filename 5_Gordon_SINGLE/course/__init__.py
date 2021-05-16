from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import bs4
import requests

from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup



def collect_existing_courses_url(courses):
    urls = []
    for course in courses:
        url = course['url']
        urls.append(url)
    return urls


def extract_all_courses(urlpdf):
    page = requests.get(urlpdf).content
    with io.BytesIO(page) as f:
        pdf = PdfFileReader(f)
        pageObj = pdf.getPage(0)

        page_content = pageObj.extractText()
        print(page_content)
        # txt = f"""
        # Author: {information.author}
        # Creator: {information.creator}
        # Producer: {information.producer}
        # Subject: {information.subject}
        # Title: {information.title}
        # Number of pages: {number_of_pages}
        # """
        # # Here the metadata of your pdf
        # print(txt)
        # # numpage for the number page
        # numpage = 20
        # page = pdf.getPage(numpage)
        # page_content = page.extractText()
        # print the content in the page 20
        # print(page_content)
    return
url = 'https://www.gibs.co.za/Documents/Executive%20Education%20Short%20Courses.pdf'
extract_all_courses(url)