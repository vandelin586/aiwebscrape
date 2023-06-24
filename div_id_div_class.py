import requests
from bs4 import BeautifulSoup

url = 'https://www.michiganlottery.com/games/mega-millions'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

divs = soup.find_all('div id', class_='circle light')

for div in divs:
    id = div.get('id')
    content = id.text
    print(content)
    print(f'id: {id}, content: {content}')