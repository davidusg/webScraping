import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

productLinks = []

r = requests.get(
    'http://www.cyberpuerta.mx/Computadoras/PC-s-de-Escritorio/', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productList = soup.find_all(
    'li', {"class": ["cell", "productData", "small-12"]})

for item in productList:
    for link in item.find_all('a', href=True, class_="cp-picture-container"):
        productLinks.append(link['href'])

pcList = []
for link in productLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_='detailsInfo_right_title').text.strip()
    try:
        stock = soup.find('span', class_='stockFlag').find('span').text.strip()
    except:
        stock = 'No Stock'
    price = soup.find('span', class_='priceText').text

    pc = {
        'provider': 'CyberPuerta',
        'name': name,
        'stock': stock,
        'price': price,
        'link': link
    }

    pcList.append(pc)
    pd.DataFrame(pcList).to_csv(
        "cyberpuerta-pc.csv", index=False)
