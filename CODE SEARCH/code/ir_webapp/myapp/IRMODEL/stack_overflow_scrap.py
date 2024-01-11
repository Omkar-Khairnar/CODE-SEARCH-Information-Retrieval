import requests
from bs4 import BeautifulSoup
import csv

links = []

for i in range(2001, 3001):
    URL = f"https://stackoverflow.com/questions/tagged/javascript?tab=newest&page={i}&pagesize=50"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')

    table=soup.findAll('div', attrs={'class' : 's-post-summary js-post-summary'})

    for row in table:
        data=row.find('div', attrs={'class' : 's-post-summary--stats-item has-answers'})
        if data is not None:
            currHead=row.find('h3', attrs={'class': 's-post-summary--content-title'})
            print('https://stackoverflow.com'+currHead.a['href'])