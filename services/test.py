import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.bestchange.ru/bitcoin-to-tether-trc20.html'
response = requests.get(url, timeout=10)
reply = response.text

data = BeautifulSoup(reply, features='html.parser')

# table = data.find(id='rates_block').tbody.findAll('tr')
table = data.find(id='rates_block').tbody.contents

for line in table:
    try:
        url = line.find(class_='bj').a.get('href')
        id = re.search(r'(?<=id=)\d+', url)
        print(id[0], '\t', url)
    except (TypeError, AttributeError):
        pass
