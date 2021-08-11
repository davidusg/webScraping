import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

baseurl = 'https://www.amazon.com.mx'

playstationList = []
for x in range(1, 4):
    r = requests.get(
        f'https://www.amazon.com.mx/s?k=sony+playstation+5&page={x}&__mk_es_MX=ÅMÅŽÕÑ&qid=1628686918&', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all(
        'div', {'data-component-type': 's-search-result'})

    for item in productList:
        name = item.find(
            'a', {'class': 'a-link-normal a-text-normal'}).text.strip()

        if 'Consola PlayStation 5' in name:
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

            playstation = {
                'provider': 'Amazon',
                'name': shortName,
                'stock': stock,
                'price': price,
                'link': baseurl + link
            }

            playstationList.append(playstation)
            pd.DataFrame(playstationList).to_csv(
                "amazon-playstation-5.csv", index=False)
