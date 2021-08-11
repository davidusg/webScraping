import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

switchList = []
productLinks = []

r = requests.get(
    'https://www.newegg.com/global/mx-en/p/pl?d=Nintendo+Switch', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productList = soup.find_all(
    'div', {'class': 'item-cell'})

for item in productList:
    name = item.find(
        'a', {'class': 'item-title'}).text.strip()
    if 'Nintendo Switch' in name:
        shortName = name[:50]
        link = item.find(
            'a', {'class': 'item-title'})['href']
        try:
            price = '$' + item.find(
                'li', {'class': 'price-current'}).find('strong').text.strip()
            stock = '1'
        except:
            price = 'Ver Sitio'
            stock = 'No Stock'

        switch = {
            'provider': 'Newegg',
            'name': shortName,
            'stock': stock,
            'price': price,
            'link': link
        }

        switchList.append(switch)
        pd.DataFrame(switchList).to_csv(
            "newegg-nintendo-switch.csv", index=False)
