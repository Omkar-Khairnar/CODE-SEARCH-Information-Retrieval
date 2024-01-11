import json
import math
import pandas as pd

def cosine_similarity(query_tfidf, documents_tfidf):
    similarity_scores = []
    for doc_tfidf in documents_tfidf.values():
        dot_product = sum(query_tfidf[word] * doc_tfidf.get(word, 0) for word in query_tfidf)
        query_norm = math.sqrt(sum(query_tfidf[word]**2 for word in query_tfidf))
        doc_norm = math.sqrt(sum(doc_tfidf[word]**2 for word in doc_tfidf))
        cosine_sim = dot_product / (query_norm * doc_norm) if (query_norm * doc_norm) != 0 else 0
        similarity_scores.append(cosine_sim)
    return similarity_scores


def cosine_similarity_queryTodocs():
    with open('myapp/IRMODEL/query/tf_idf.json', 'r') as file:
        query_json = json.load(file)

    # Load the second JSON
    with open('myapp/IRMODEL/tfidf/tf_idf.json', 'r') as file:
        docs_json = json.load(file)

    # Calculate similarity scores
    sc = cosine_similarity(query_json, docs_json)   

    # Get indices after sorting
    sorted_indices = sorted(range(len(sc)), key=lambda k: sc[k], reverse=True)

    # Create a list of dictionaries with document index and corresponding similarity score
    sorted_results = [{'document_index': index, 'similarity_score': sc[index]} for index in sorted_indices]

    # Save the results to a new JSON file
    # with open('myapp/IRMODEL/ranking.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(sorted_results, json_file, ensure_ascii=False, indent=4)

    csv_data = pd.read_csv('myapp/IRMODEL/dataset/preprocessed/combined.csv')

    # Create a dictionary to store document_index and corresponding values from CSV
    result_dict = {}
    desc_dict = {}

    # Specify the number of relevant documents to consider
    k = 20

    # Iterate through each entry in the JSON file
    for entry in sorted_results[:k]:
        document_index = entry['document_index']

        # Retrieve the value from the CSV file based on the document_index
        value_from_csv = csv_data.iloc[document_index - 1, 1]  # Assuming the index in JSON is 1-based
        desc_from_csv =  csv_data.iloc[document_index - 1, 0]

        # Store the result in the dictionary
        result_dict[document_index] = value_from_csv
        desc_dict[document_index] = desc_from_csv

    with open('myapp/IRMODEL/retrieve.json', 'w') as result_file:
        json.dump(result_dict, result_file, indent=2)

    with open('myapp/IRMODEL/retrieve_desc.json', 'w') as result_file:
        json.dump(desc_dict, result_file, indent=2)

    return result_dict, desc_dict