import requests
from bs4 import BeautifulSoup

url = 'https://z2.fm/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('title').text
paragraph = soup.find('p').text

print('Title:', title)
print('Paragraph:', paragraph)


# import requests
#import beautifulsoup4

#запрос на получення даних (музики)
#link = 'https://soundcloud.com/'

#отримаєш якійсь то там контент
#responce = requests.get(link).content
