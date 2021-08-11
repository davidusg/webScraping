import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

baseurl = 'https://www.amazon.com.mx'

rtxList = []
for x in range(1, 9):
    r = requests.get(
        f'https://www.amazon.com.mx/s?k=rtx+3070+ti&page={x}&__mk_es_MX=ÅMÅŽÕÑ&crid=2SGEHLY46ZDJ5&qid=1628675222&sprefix=rtx+3070+ti%2Caps%2C227', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'data-component-type': 's-search-result'})

    for item in productList:
        name = item.find(
            'a', {'class': 'a-link-normal a-text-normal'}).text.strip()

        if re.search(r'\bGeForce RTX 3070 Ti\b', name):
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

            rtx3070ti = {
                'provider': 'Amazon',
                'name': shortName,
                'stock': stock,
                'price': price,
                'link': baseurl + link
            }

            rtxList.append(rtx3070ti)
            pd.DataFrame(rtxList).to_csv(
                "amazon-rtx-3070-ti.csv", index=False)
