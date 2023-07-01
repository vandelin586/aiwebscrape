import requests
from bs4 import BeautifulSoup

url = 'https://www.michiganlottery.com/resources/number-tools?SELECTED_TOOL=PAST_RESULTS&SELECTED_GAME=B'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup)
divs = soup.find_all('div', class_='circle light')
print(divs)
for div in divs:
    id = div.get('id')
    content = id.text
    print(content)
    print(f'id: {id}, content: {content}')

    #<div id="mm-wn-1" class="circle light ">8</div><div id="mm-wn-2" class="circle light ">34</div><div id="mm-wn-3" class="circle light ">35</div><div id="mm-wn-4" class="circle light ">41</div><div id="mm-wn-5" class="circle light ">52</div><div id="mm-wn-megaball" class="circle megaball ">12</div><div id="mm-wn-megaplier" class="circle multiplier ">4x</div></div>