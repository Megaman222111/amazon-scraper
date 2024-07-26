# trial with scraper and random website
import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.ca/amazon-fire-tv-55-inch-4-series-4k-smart-tv/dp/B08T6H1RQD/?_encoding=UTF8&pd_rd_w=JHXPX&content-id=amzn1.sym.6ab822bb-4b3a-4cfa-8197-4ab3cee1b8d9&pf_rd_p=6ab822bb-4b3a-4cfa-8197-4ab3cee1b8d9&pf_rd_r=KQ95DG5K7N3KVZGQQMP0&pd_rd_wg=qacoU&pd_rd_r=2988b518-6a39-4a5a-8c38-455638267dc5&ref_=pd_hp_d_atf_unk'
headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
proxies = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}
response = requests.get(url, , headers=headers)
soup = BeautifulSoup(response.content, 'html5lib')
print(soup.prettify())