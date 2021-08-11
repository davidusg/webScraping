import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

baseurl = 'https://www.amazon.com.mx'

switchList = []
for x in range(1, 4):
    r = requests.get(
        f'https://www.amazon.com.mx/s?k=nintendo+switch&page={x}&__mk_es_MX=ÅMÅŽÕÑ&crid=20TS7NKHVQXIB&qid=1628678824&sprefix=Nintendo+Switch%2Caps%2C286', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'data-component-type': 's-search-result'})

    for item in productList:
        name = item.find(
            'a', {'class': 'a-link-normal a-text-normal'}).text.strip()

        if 'Nintendo Consola Switch' in name:
            shortName = name[:50]
            link = item.find(
                'a', {'class': 'a-link-normal a-text-normal'})['href']

            try:
                price = item.find(
                    'span', {'class': 'a-offscreen'}).text.strip()
                stock = 'Hay Stock'
            except:
                price = 'Ver Sitio'
                stock = 'No Stock'

            switch = {
                'provider': 'Amazon',
                'name': shortName,
                'stock': stock,
                'price': price,
                'link': baseurl + link
            }

            switchList.append(switch)
            pd.DataFrame(switchList).to_csv(
                "amazon-nintendo-switch.csv", index=False)
