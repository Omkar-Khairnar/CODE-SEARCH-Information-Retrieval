import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import json
from collections import Counter
import math

# nltk.download('punkt')
# nltk.download('stopwords')

# QUERY --------------------------------------------------------------------------------------------------------

# QUERY = "Red black tree in c++"

# PREPROCESSING ------------------------------------------------------------------------------------------------

def preprocess(document):
    document = document.lower()
    document = document.translate(str.maketrans("", "", string.punctuation.replace("", "")))
    tokens = word_tokenize(document)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Join the preprocessed tokens into a space-separated string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

# preprocessed_query = preprocess(QUERY)
# print("Preprocessing query : DONE")

# TF ----------------------------------------------------------------------------------------------------------

def calculate_term_frequency(document):
    # Tokenize the document (you may need more advanced tokenization based on your requirements)
    words = document.lower().split()

    # Calculate term frequency using 1 + log(count) for each term
    tf = {word: 1 + math.log(count) for word, count in Counter(words).items()}

    return tf

# term_freq = calculate_term_frequency(preprocessed_query)
# print("Calculating TF of query : DONE")

# TF-IDF ------------------------------------------------------------------------------------------------------

# json1 = term_freq

# Load the second JSON
# with open('tfidf/idf.json', 'r') as file:
#     json2 = json.load(file)

# result = {key: json1[key] * json2.get(key, 0) for key in json1}

# Save the modified result to a new JSON file
# with open('query/tf_idf.json', 'w') as file:
#     json.dump(result, file, indent=2)

def queryProcessing(Query):
    preprocessed_query = preprocess(Query)
    print("Preprocessing query : DONE")

    term_freq = calculate_term_frequency(preprocessed_query)
    json1 = term_freq
    print("Calculating TF of query : DONE")

    # Load the second JSON
    with open('myapp/IRMODEL/tfidf/idf.json', 'r') as file:
        json2 = json.load(file)

    result = {key: json1[key] * json2.get(key, 0) for key in json1}

    # Save the modified result to a new JSON file
    with open('myapp/IRMODEL/query/tf_idf.json', 'w') as file:
        json.dump(result, file, indent=2)
    print("Calculating weight : DONE")
    