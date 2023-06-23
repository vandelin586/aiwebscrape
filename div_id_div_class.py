import requests
from bs4 import BeautifulSoup

url = 'Your URL here'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

divs = soup.find_all('div', class_='className')
for div in divs:
    id = div.get('id')
    content = div.text
    print(f'id: {id}, content: {content}')
