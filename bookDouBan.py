import requests
from bs4 import BeautifulSoup
result = requests.get('https://book.douban.com/')
soup = BeautifulSoup(result.text)
for targ in soup.select('#wrapper #content .info .title'):
    print(targ.getText())