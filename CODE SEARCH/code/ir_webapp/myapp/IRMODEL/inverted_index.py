import re
import json
import csv
from collections import defaultdict

def create_inverted_index(documents, output_file):
    inverted_index = defaultdict(lambda: defaultdict(int))

    for doc_id, document in enumerate(documents):
        words = re.findall(r'\b\w+\b', document.lower())  # Tokenize the document
        for word in set(words):  # Use set to count unique occurrences
            inverted_index[word][doc_id] += words.count(word)

    # Convert defaultdict to a regular dictionary for JSON serialization
    inverted_index = {term: dict(postings) for term, postings in inverted_index.items()}

    # Write the combined inverted index to the output file in JSON format
    with open(output_file, 'w') as file:
        json.dump(inverted_index, file, indent=2)

    return inverted_index

def read_documents_from_csv(file_path):
    with open(file_path, 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        # Assuming the first column contains the text/documents
        documents = [row[0] for row in reader]
    return documents

def create_inverted_index_from_csv(input_csv, output_file):
    documents = read_documents_from_csv(input_csv)
    inverted_index = create_inverted_index(documents, output_file)
    return inverted_index

# Example usage:
input_csv_file = "dataset/preprocessed/combined.csv"
output_json_file = "inverted index/inverted_index.json"
inverted_index = create_inverted_index_from_csv(input_csv_file, output_json_file)