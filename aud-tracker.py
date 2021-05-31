from bs4 import BeautifulSoup
import requests

money = requests.get('https://wise.com/in/currency-converter/usd-to-aud-rate').text

inside = BeautifulSoup(money, 'lxml')
block = inside.find('h3', class_='cc__source-to-target')
change = block.find('span', class_='text-success').text

print(change)
