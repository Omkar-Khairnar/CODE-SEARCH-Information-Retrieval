import json
import math

with open('query/tf_idf.json', 'r') as file:
    query_json = json.load(file)

# Load the second JSON
with open('tfidf/tf_idf.json', 'r') as file:
    docs_json = json.load(file)

def cosine_similarity(query_tfidf, documents_tfidf):
    similarity_scores = []
    for doc_tfidf in documents_tfidf.values():
        dot_product = sum(query_tfidf[word] * doc_tfidf.get(word, 0) for word in query_tfidf)
        query_norm = math.sqrt(sum(query_tfidf[word]**2 for word in query_tfidf))
        doc_norm = math.sqrt(sum(doc_tfidf[word]**2 for word in doc_tfidf))
        cosine_sim = dot_product / (query_norm * doc_norm) if (query_norm * doc_norm) != 0 else 0
        similarity_scores.append(cosine_sim)
    return similarity_scores

sc = cosine_similarity(query_json, docs_json)

print(sc)
