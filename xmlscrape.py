from bs4 import BeautifulSoup

html = '''<div class="winning-numbers-card-bottom-numbers-container"><div id="mm-wn-1" class="circle light ">4</div><div id="mm-wn-2" class="circle light ">24</div><div id="mm-wn-3" class="circle light ">34</div><div id="mm-wn-4" class="circle light ">45</div><div id="mm-wn-5" class="circle light ">57</div><div id="mm-wn-megaball" class="circle megaball ">19</div><div id="mm-wn-megaplier" class="circle multiplier ">3x</div></div>'''
soup = BeautifulSoup(html, 'html.parser')

# Find the winning numbers
numbers = soup.find_all('div', class_='circle light')
numbers_list = [number.text for number in numbers]
print('Winning Numbers:', numbers_list)

# Find the Mega Ball and Megaplier
megaball = soup.find('div', id='mm-wn-megaball').text
megaplier = soup.find('div', id='mm-wn-megaplier').text
print('Mega Ball:', megaball)
print('Megaplier:', megaplier)
