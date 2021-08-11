import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

productLinks = []

r = requests.get(
    'https://www.cyberpuerta.mx/index.php?cl=search&searchparam=RTX+3070+Ti', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productList = soup.find_all(
    'li', {"class": ["cell", "productData", "small-12"]})

for item in productList:
    for link in item.find_all('a', href=True, class_="cp-picture-container"):
        productLinks.append(link['href'])

rtxList = []
for link in productLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_='detailsInfo_right_title').text.strip()
    try:
        stock = soup.find('span', class_='stockFlag').find('span').text.strip()
    except:
        stock = 'No Stock'
    price = soup.find('span', class_='priceText').text

    rtx3070ti = {
        'provider': 'CyberPuerta',
        'name': name,
        'stock': stock,
        'price': price,
        'link': link
    }

    rtxList.append(rtx3070ti)
    pd.DataFrame(rtxList).to_csv(
        "cyberpuerta-rtx-3070-ti.csv", index=False)
