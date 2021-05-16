# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import grequests
import requests
import time


links = [
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=1",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=2",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=3",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=4",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=5",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=6",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=7",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=8",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=9",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=1",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=2",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=3",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=4",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=5",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=6",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=7",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=8",
"https://www.croma.com/phones-wearables/mobile-phones/c/10?q=%3Arelevance%3AskuStockFlag%3Atrue&amp;page=9"
]


def sync_scraping(links):
    start_time = time.time()
    for link in links:
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            lists = soup.find_all('a', attrs={'class': "product__list--name"})
            print(lists[0].text)
        except Exception as e:
            pass
        try:
            prices = soup.find_all('span', attrs={'class': "pdpPriceMrp"})
            print(prices[0].text)
        except:
            pass
        try:
            discount = soup.find_all("div", attrs={"class": "listingDiscnt"})
            print(discount[0].text)
        except:
            pass
    print("--- %s seconds ---" % (time.time() - start_time))


def async_scraping(links):
    start_time = time.time()
    reqs = (grequests.get(link) for link in links)
    resp = grequests.imap(reqs, grequests.Pool(10))

    for r in resp:
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            results = soup.find_all('a', attrs={"class": 'product__list-name'})
            print(results[0].text)
        except:
            pass
        try:
            prices = soup.find_all('span', attrs={'class': "pdpPriceMrp"})
            print(prices[0].text)
        except:
            pass
        try:
            discount = soup.find_all("div", attrs={"class": "listingDiscnt"})
            print(discount[0].text)
        except:
            pass
    print("--- %as seconds ---" % (time.time() - start_time))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sync_scraping(links)
    print('===============================================================')
    async_scraping(links)


