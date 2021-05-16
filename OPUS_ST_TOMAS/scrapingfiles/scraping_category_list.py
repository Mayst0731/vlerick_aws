from scrapingfiles.dependencies import *
from scrapingfiles.download_pages import *

def categories_info(parent_urls):
    '''
    :param parent_urls:
    :return: category list
    '''
    category_list = []
    page_objs = download_all_sites(parent_urls)
    executive_page = page_objs[0]
    cate_sessions = executive_page.find_all('li',attrs={'class':'link-grid__link-item'})
    for cate in cate_sessions:
        cate_name = cate.a.text.strip()
        cate_link = cate.find('a').get('href')
        cate_url = urllib.parse.urljoin(parent_urls[0], cate_link)
        info = {
            'category':cate_name,
            'url':cate_url,
        }
        category_list.append(info)
    for cate in category_list:
        cate.update({'parent_url':parent_urls[0]})
    return category_list

