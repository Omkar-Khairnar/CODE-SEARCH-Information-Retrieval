import requests
from bs4 import BeautifulSoup
import csv

test = "https://www.programiz.com/dsa/stack"

# Open the CSV file in write mode
with open('programiz.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header row
    # csvwriter.writerow(['Question Title', 'Question Description', 'Answer Code'])

    # Iterate through the URLs
    with open("urls_programiz_dsa.txt", 'r', encoding='utf-16') as urls_file:
        for idx, url in enumerate(map(str.strip, urls_file), start=1):
            
            # if idx > 2:
            #     break
            
            if idx <= 2:
                continue
            
            print("Line Number:", idx)

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            # Extract question title
            question_title = soup.find('title').text 

            # Extract question description
            question_desc = ''
            if (questionDesc := soup.find('div', attrs={'class': 'content'})):
                ul_li_p_text = [item.text.strip() for item in questionDesc.find_all(['ul', 'li', 'p'])]
                question_desc = ' '.join(ul_li_p_text)

            # Extract codes
            answer_code = ''
            if (answer := soup.find('div', attrs={'class': 'code-editor code-editor--tabbed'})):
                if (allCodes := answer.findAll('div', attrs={'class': 'code-editor__area'})):
                    for code in allCodes:
                        answer_code = code.find('pre').find('code').text
                        csvwriter.writerow([question_title, question_desc, answer_code])




# with open("urls_programiz_dsa.txt", 'r', encoding='utf-16') as urls:
#   # for url in map(str.strip, urls):
#     # print(url)

#     r = requests.get(test)
#     soup = BeautifulSoup(r.content, 'html5lib')
#     # Extract question title
#     question_title = soup.find('title').text 
#     # print(question_title)

#     # Extract question description
#     question_desc = ''
#     if (questionDesc := soup.find('div', attrs={'class': 'content'})):
#       ul_li_p_text = [item.text.strip() for item in questionDesc.find_all(['ul', 'li', 'p'])]
#       question_desc = ' '.join(ul_li_p_text)
#       # print(question_desc)

#     # Extract codes
#     answer_code = ''
#     if (answer := soup.find('div', attrs={'class': 'code-editor code-editor--tabbed'})):
#         if (allCodes := answer.findAll('div', attrs={'class': 'code-editor__area'})):
#             for code in allCodes:
#                 print(code.find('pre').find('code').text)
#             # if (code := pre.find('code')):
#             #     answer_code = code.text