import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.douban.com/')
soup = BeautifulSoup(result.text)
#html = soup.prettify()
#print(soup.prettify())
#print(soup.p.string)
#print(soup.select('title'))
#print(soup.select('#anony-time a[class="title"]'))
#print(soup.select('a[class="title"]'))
#print(soup.select('#anony-time li a[target="_blank"]'))
for trg in soup.select('#anony-time li a[target="_blank"]'):
#for trg in soup.select('a[target="_blank"]'):
    print(trg.get_text())