import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

baseurl = 'https://www.amazon.com.mx'
url = 'https://www.amazon.com.mx/s?k=RTX+3080'

rtxList = []
for x in range(1, 9):
    r = requests.get(
        f'{url}&page={x}', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'data-component-type': 's-search-result'})

    for item in productList:
        name = item.find(
            'a', {'class': 'a-link-normal a-text-normal'}).text.strip()
        if 'GeForce RTX 3080' in name:
            if re.search('^((?!Ti).)*$', name):
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

                rtx3080 = {
                    'provider': 'Amazon',
                    'name': shortName,
                    'stock': stock,
                    'price': price,
                    'link': baseurl + link
                }

                rtxList.append(rtx3080)
                pd.DataFrame(rtxList).to_csv(
                    "amazon-rtx-3080.csv", index=False)
