import requests
from bs4 import BeautifulSoup

links = []

# JS
# URL = "https://www.programiz.com/javascript/examples"

# DSA
URL = "https://www.programiz.com/dsa"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

# JS
# table = soup.find('ol')
# for row in table:
#   print("https://www.programiz.com" + row.a['href'])

# DSA
table = soup.findAll('div', attrs={"class" : "card-alt mb-9x"})

for row in table:
  section = row.findAll('li')
  for tag in section:
    currHead = tag.find('a')
    print("https://www.programiz.com" + currHead['href'])