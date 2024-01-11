import csv
from collections import Counter
import json
import math

def read_documents_from_csv(file_path):
    with open(file_path, 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        # Assuming the first column contains the text/documents
        documents = [row[0] for row in reader]
    return documents

def calculate_term_frequency(documents):
    term_frequency = []
    
    for document in documents:
        # Tokenize the document (you may need more advanced tokenization based on your requirements)
        words = document.lower().split()
        
        # Calculate term frequency using 1 + log(count) for each term
        tf = {word: 1 + math.log(count) for word, count in Counter(words).items()}
        
        term_frequency.append(tf)
    
    return term_frequency

file_path = 'dataset/preprocessed/combined.csv'  # Replace with the actual path to your CSV file
documents = read_documents_from_csv(file_path)

term_frequency = calculate_term_frequency(documents)

# Create a JSON object for the results
results = {}
for i, tf in enumerate(term_frequency):
    results[i] = tf

# Save the results to a JSON file
with open('tfidf/log_tf.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)
