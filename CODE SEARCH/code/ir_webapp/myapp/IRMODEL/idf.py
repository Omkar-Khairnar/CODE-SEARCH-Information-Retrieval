import json
import math

TOTAL_DOCUMENTS = 50500

# Load original_data from a JSON file
with open('inverted index/inverted_index.json', 'r') as file:
    original_data = json.load(file)

# Create a new dictionary to store the number of key-value pairs
num_pairs_data = {}

# Calculate and store the inverted document frequency
for key, value in original_data.items():
    num_pairs_data[key] = math.log2(TOTAL_DOCUMENTS / len(value))

# Save the result to a new JSON file
with open('tfidf/idf.json', 'w') as file:
    json.dump(num_pairs_data, file, indent=2)

print("Number of key-value pairs saved to 'idf.json'")
