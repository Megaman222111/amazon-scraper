import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.ca/Jafanda-Purifiers-Coverage-Filtration-activated/dp/B0B461L34Z/'
headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

# UNEEDED: Function to strip the url to the base url for the Amazon URL
'''
def url_strip():
    backslash_count = 0
    index_count = 0
    for i in url:
        if backslash_count >=6:
            break
        if i == '/':
            backslash_count += 1
        index_count += 1
    url = url[:index_count]
    return url
'''

def scrape(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    title = str(soup.find("span", attrs={"id":'productTitle'}).string).strip()
    price_dollars = (soup.find("span", attrs={"class":'a-price-whole'})).get_text().strip().strip('.').strip('$')
    price_cents = str(soup.find("span", attrs={"class":'a-price-fraction'}).string).strip()
    # Not Working Yet: before_sale_price = str(soup.find("div", attrs={"class":'a-section a-spacing-small aok-align-center'}).string).strip()
    print("Title: ", title)
    print("Current Price: ", price_dollars + '.' + price_cents)
    # Not Working Yet: print(before_sale_price)

scrape(url, headers)