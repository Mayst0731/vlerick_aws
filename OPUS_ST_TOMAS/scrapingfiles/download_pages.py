from scrapingfiles.dependencies import *


def parse_page_to_obj(response):
    soup = ''
    try:
        html_content = response.content
        soup = BeautifulSoup(html_content, features='lxml')
    except Exception as e:
        print(e)
    return soup



def download_site(url, session):
    with session.get(url) as response:
        soup = parse_page_to_obj(response)
    return soup

def download_all_sites(urls):
    soups = []
    with requests.Session() as session:
        for url in urls:
            soup = download_site(url, session)
            soups.append(soup)
    return soups




