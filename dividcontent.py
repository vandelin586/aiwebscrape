from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<div class="winning-numbers-card-bottom-numbers-container">
    <div id="mm-wn-1" class="circle light ">content 1</div>
    <div id="mm-wn-2" class="circle light ">content 2</div>
    <div id="mm-wn-3" class="circle light ">content 3</div>
    <div id="mm-wn-4" class="circle light ">content 4</div>
    <div id="mm-wn-5" class="circle light ">content 5</div>
    <div id="mm-wn-megaball" class="circle megaball ">content 6</div>
    <div id="mm-wn-megaplier" class="circle multiplier ">content 7</div>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class 'container'
containers = soup.find_all('div', class_='container')

# Iterate over each container
for container in containers:
    # Find all div elements within the container with id 'test'
    divs = container.find_all('div', id='test')
    