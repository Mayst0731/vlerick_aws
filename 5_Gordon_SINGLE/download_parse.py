import aiohttp
import requests
import time
import bs4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

async def download_site(url, session):
    content = await session.get(url)
    source = await content.text(errors="ignore")
    page = parse(source)
    return page


def parse(source):
    page = bs4.BeautifulSoup(source,'lxml')
    return page