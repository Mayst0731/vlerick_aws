import asyncio
import aiohttp
import requests
import time
import bs4


async def download_site(url, session):
    async with session.get(url) as response:
        content = await response.text()
        return content


def parse(source):
    page = bs4.BeautifulSoup(source,'lxml')
    return page


async def get_title(url,session):
    source = await download_site(url,session)
    page = parse(source)
    title = page.p.text
    print(title)
    return title


def get_link(page):
    link = page.a
    print('link')
    return link




if __name__ == "__main__":
    cates = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    async def create_session():
        s = aiohttp.ClientSession()
        await get_cates(cates)
        await get_cates(cates)
        await get_cates(cates)
        await s.close()

    async def get_cates(cates):
        s = aiohttp.ClientSession()
        for url in cates:
            title = await get_title(url,s)
        await s.close()
    asyncio.run(create_session())
    duration = time.time() - start_time
    print(f"Downloaded {len(cates)} in {duration} seconds")