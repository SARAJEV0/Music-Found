import requests
from beautifulsoup4 import *

#запрос на получення даних (музики)
link = 'https://soundcloud.com/'

#отримаєш якійсь то там контент
responce = requests.get(link).content