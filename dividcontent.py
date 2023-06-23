from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<div class="container">
    <div id="test">Div 1</div>
    <div id="other">Div 2</div>
</div>
<div class="container">
    <div id="test">Div 3</div>
    <div id="test">Div 4</div>
</div>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class 'container'
containers = soup.find_all('div', class_='container')

# Iterate over each container
for container in containers:
    # Find all div elements within the container with id 'test'
    divs = container.find_all('div', id='test')
    