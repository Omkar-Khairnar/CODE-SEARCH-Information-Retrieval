import requests
from bs4 import BeautifulSoup
import csv

# Open the CSV file in write mode
with open('dataset/data/dataset2.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header row
    # csvwriter.writerow(['Line Number', 'Question Title', 'Question Description', 'Answer Code'])

    # Iterate through the URLs
    with open("dataset/urls/urls_cpp_1_to_186.txt", 'r', encoding='utf-16') as urls_file:
        for idx, url in enumerate(map(str.strip, urls_file), start=1):
            # Check if idx has reached 1000
            
            # if idx > 5:
            #     break
            
            if idx <= 76:
                continue
            
            print("Line Number:", idx)

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            # Extract question title
            question_title = questionHeader.find('h1').text if (questionHeader := soup.find('div', attrs={'id': 'question-header'})) else ''

            # Extract question description
            question_desc = ''
            if (questionDesc := soup.find('div', attrs={'class': 'postcell post-layout--right'})):
                p_tags = questionDesc.find_all('p')
                question_desc = ' '.join([p_tag.text for p_tag in p_tags])

            # Extract answer code
            answer_code = ''
            if (answer := soup.find('div', attrs={'class': 'answercell'})):
                if (pre := answer.find('pre')):
                    if (code := pre.find('code')):
                        answer_code = code.text

            # Skip writing the row if answer_code is empty
            if answer_code:
                # Write the data to the CSV file
                csvwriter.writerow([idx, question_title, question_desc, answer_code])

            # Print statements for verification
            # print("Question Title:", question_title)
            # print("Question Description:", question_desc)
            # print("Answer Code:", answer_code)
            # print("------------------------------------------------------------------------------")
