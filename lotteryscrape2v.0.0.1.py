import requests
from bs4 import BeautifulSoup

url = 'https://www.lotteryusa.com/michigan/mega-millions/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the winning numbers
winning_numbers = soup.find('ul', class_='draw-result list-unstyled list-inline')
print('Winning Numbers debug:', winning_numbers)
numbers = winning_numbers.find_all('li')
numbers_list = [number.text for number in numbers]
print('Winning Numbers:', numbers_list)
