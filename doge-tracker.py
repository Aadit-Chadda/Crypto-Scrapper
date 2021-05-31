from bs4 import BeautifulSoup
import requests

link = requests.get('https://coinmarketcap.com/currencies/dogecoin/').text

soup = BeautifulSoup(link, 'lxml')
widget = soup.find('h1', class_='sc-16r8icm-0 kXPxnI priceTitle___1cXUG')
price = soup.find('div', class_='priceValue___11gHJ').text.replace(' ', '')
print('USD: ', price)
price = price.strip('$')

print(price)
