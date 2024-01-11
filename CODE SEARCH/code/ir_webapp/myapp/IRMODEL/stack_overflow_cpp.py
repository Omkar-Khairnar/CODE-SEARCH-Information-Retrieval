import requests
from bs4 import BeautifulSoup

links = []

for i in range(400, 500):
    URL = f"https://stackoverflow.com/questions/tagged/c%2b%2b?tab=votes&page={i}&pagesize=50"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')

    # Find all 'div' elements with 'id' attribute equal to 'questions'
    tables = soup.findAll('div', attrs={'id': 'questions'})
    
    for table in tables:
        # Find all 'div' elements with 'class' attribute equal to 's-post-summary js-post-summary'
        divs = table.findAll('div', attrs={'class': 's-post-summary js-post-summary'})
        
        for div in divs:
            # Find the 'div' element with 'class' attribute equal to 's-post-summary--content'
            content = div.find('div', attrs={'class': 's-post-summary--content'})
            
            if content is not None:
                # Find the 'h3' element with 'class' attribute equal to 's-post-summary--content-title'
                currHead = content.find('h3', attrs={'class': 's-post-summary--content-title'})
                
                if currHead is not None:
                    # Extract and print the link
                    link = 'https://stackoverflow.com' + currHead.a['href']
                    print(link)
                    links.append(link)
