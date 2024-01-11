import json

# Load the first JSON file
with open('tfidf/log_tf.json', 'r', encoding='utf-8') as json_file:
    first_json = json.load(json_file)

# Load the second JSON file
with open('tfidf/idf.json', 'r', encoding='utf-8') as json_file:
    second_json = json.load(json_file)

# Multiply corresponding values for each key in the first JSON
result = {}
for outer_key, inner_dict in first_json.items():
    result[outer_key] = {}
    for key, value in inner_dict.items():
        if key in second_json:
            result[outer_key][key] = value * second_json[key]

# Save the results to a new JSON file
with open('tfidf/tf_idf.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)
