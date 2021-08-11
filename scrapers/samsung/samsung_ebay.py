import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=smartphone+samsung&_sacat=9355&LH_TitleDesc=0'

samsungList = []
for x in range(1, 2):
    r = requests.get(
        f'{url}&_pgn={x}', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'class': 's-item__wrapper clearfix'})

    for item in productList:
        name = item.find(
            'a', {'class': 's-item__link'}).text.replace('Anuncio nuevo', '').strip()
        if 'Samsung Galaxy' in name:
            shortName = name[:50]
            link = item.find(
                'a', {'class': 's-item__link'})['href']
            try:
                price = item.find(
                    'span', {'class': 's-item__price'}).text.replace('MXN ', '').replace('\u00A0', ',').strip()
                stock = '1'
            except:
                price = 'Ver Sitio'
                stock = 'No Stock'

            samsung = {
                'provider': 'Ebay',
                'name': shortName,
                'stock': stock,
                'price': price,
                'link': link
            }

            samsungList.append(samsung)
            pd.DataFrame(samsungList).to_csv(
                "ebay-samsung.csv", index=False)
