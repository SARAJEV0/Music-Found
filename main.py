import requests
from bs4 import BeautifulSoup

r = requests.get("https://stopgame.ru/news")
html = BS(r.content, 'html.parser')

for el in html.select(".")