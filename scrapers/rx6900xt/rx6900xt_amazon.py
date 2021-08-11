import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

baseurl = 'https://www.amazon.com.mx'

rxList = []
for x in range(1, 9):
    r = requests.get(
        f'https://www.amazon.com.mx/s?k=rx+6900+xt&page={x}&__mk_es_MX=ÅMÅŽÕÑ&crid=1TIRINI57MOX3&qid=1628681324&sprefix=rx%2Caps%2C223', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'data-component-type': 's-search-result'})

    for item in productList:
        name = item.find(
            'a', {'class': 'a-link-normal a-text-normal'}).text.strip()

        if 'RX 6900 XT' in name:
            if re.search('^((?!PC Gamer).)*$', name):
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

                rx3900 = {
                    'provider': 'Amazon',
                    'name': shortName,
                    'stock': stock,
                    'price': price,
                    'link': baseurl + link
                }

                rxList.append(rx3900)
                pd.DataFrame(rxList).to_csv(
                    "amazon-rx-6900-xt.csv", index=False)
