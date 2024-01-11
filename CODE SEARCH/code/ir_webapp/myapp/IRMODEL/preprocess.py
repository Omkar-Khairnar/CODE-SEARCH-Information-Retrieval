import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import pandas as pd

# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_document(document):
    document = document.lower()
    document = document.translate(str.maketrans("", "", string.punctuation.replace("+", "")))
    tokens = word_tokenize(document)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Join the preprocessed tokens into a space-separated string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

def preprocess_and_write_row(row, output_file):
    question_title = row[0]
    question_description = row[1]

    # Check if 'Question Description' is not NaN or an empty string
    if pd.notna(question_description) and question_description.strip() != '':
        preprocessed_document = preprocess_document(question_title + ' ' + question_description)
    else:
        preprocessed_document = preprocess_document(question_title)

    preprocessed_row = pd.DataFrame([[preprocessed_document, row[2]]], columns=['document', 'code'])
    preprocessed_row.to_csv(output_file, mode='a', index=False, header=False)

# Read CSV file
input_file = 'dataset/data/combined.csv'
output_file = 'dataset/preprocessed/combined.csv'

# Assuming the CSV file has at least three columns
input_dataset = pd.read_csv(input_file, header=None, encoding="latin1")

# Write preprocessed data to a new CSV file row by row
for index, row in input_dataset.iterrows():
    preprocess_and_write_row(row, output_file)
    print("Row", index)

print("Preprocessing completed. Results written to", output_file)
