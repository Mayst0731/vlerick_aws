import aiohttp
import requests
import time
import bs4


async def download_site(url, session):
    async with session.get(url) as response:
        content = await response.text()
        page = parse(content)
        return page


def parse(source):
    page = bs4.BeautifulSoup(source,'lxml')
    return page


async def download_json(url,session):
    async with session.get(url) as response:
        json_info = await response.json()
        return json_info