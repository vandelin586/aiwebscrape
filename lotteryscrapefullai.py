import requests
from bs4 import BeautifulSoup

url = 'https://www.michiganlottery.com/games/mega-millions'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the winning numbers
winning_numbers = soup.find('div', class_='winning-numbers')
print(winning_numbers)
numbers = winning_numbers.find_all('div', class_='mega-millions-game-card-container')
numbers_list = [number.text for number in numbers]
print('Winning Numbers:', numbers_list)

#//*[@id="mega-millions-game-card-container"]/div[2]/div[2]/div