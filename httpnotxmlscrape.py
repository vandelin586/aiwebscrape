import requests
from bs4 import BeautifulSoup

url = 'https://www.michiganlottery.com/games/mega-millions'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the winning numbers
winning_numbers_container = soup.find('div', class_='winning-numbers-card-bottom-numbers-container')
numbers = winning_numbers_container.find_all('div', class_='circle light')
numbers_list = [number.text for number in numbers]
print('Winning Numbers:', numbers_list)

# Find the Mega Ball and Megaplier
megaball = winning_numbers_container.find('div', id='mm-wn-megaball').text
megaplier = winning_numbers_container.find('div', id='mm-wn-megaplier').text
print('Mega Ball:', megaball)
print('Megaplier:', megaplier)
