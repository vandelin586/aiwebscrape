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


#xpath to what we want to start at /html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1] | element <td class="c-result-card__result c-result-card__result--has-extra"><div class="c-result-card__result-row"><ul class="c-result c-result-card__result-list    "><li class="c-ball c-result__item   c-ball--default"><span class="c-ball__label">6</span></li><li class="c-ball c-result__item   c-ball--default"><span class="c-ball__label">37</span></li><li class="c-ball c-result__item   c-ball--default"><span class="c-ball__label">39</span></li><li class="c-ball c-result__item   c-ball--default"><span class="c-ball__label">45</span></li><li class="c-ball c-result__item   c-ball--default"><span class="c-ball__label">46</span></li><li class="c-result__item c-result__bonus-ball"><span class="c-ball c-ball--yellow c-ball--  ">21</span><abbr class="c-result__abbr  " title="Mega Ball">MB</abbr></li><li class="c-result__multiplier  ">Megaplier: x4</li></ul></div></td>