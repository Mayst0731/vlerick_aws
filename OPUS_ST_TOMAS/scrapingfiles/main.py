from scrapingfiles.scraping_category_list import *
from scrapingfiles.read_write import *

def main():
    pass


if __name__ == '__main__':
    CATEGORY_PARENT_URLS = ['https://business.stthomas.edu/executive-education/individuals/index.html']
    category_list_info = categories_info(CATEGORY_PARENT_URLS)
    write_info_to_json(category_list_info, '../outputfiles/CATEGORY_LIST_XW_6110_CBUS_1003.json')


