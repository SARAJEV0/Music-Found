import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://z2.fm/")
html = BS(r.content, 'html.parser')


for el in html.select(".songs-list > .songs-list-item"):
    title = el.select('.caption > a')
    print(title[0].text)


print(r) #пише чи підключився сайт до парсеру