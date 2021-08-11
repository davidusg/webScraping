import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=radeon+rx+6900+xt&_sacat=175673&LH_TitleDesc=0'

rtxList = []
for x in range(1, 2):
    r = requests.get(
        f'{url}&_pgn={x}', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'class': 's-item__wrapper clearfix'})

    for item in productList:
        name = item.find(
            'a', {'class': 's-item__link'}).text.replace('Anuncio nuevo', '').strip()
        if 'Radeon RX 6900 XT' in name:
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

            rtx3080ti = {
                'provider': 'Ebay',
                'name': shortName,
                'stock': stock,
                'price': price,
                'link': link
            }

            rtxList.append(rtx3080ti)
            pd.DataFrame(rtxList).to_csv(
                "ebay-rx-6900-xt.csv", index=False)
