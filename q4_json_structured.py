import requests
import json

struct_prompts = [
# example 1: user profile

""" You are an expert JSON Formatter. Extract a user profile in JSON format with the following fields: name, age, email, and interests. Here's the user description:

"Sarah is a 28-year-old software engineer who enjoys hiking, painting, and reading tech blogs. You can contact her at sarah.mills@example.com"
""",

# example 2: product info
"""
You are an expert JSON Format. Generate a product listing in JSON format with fields: product_id, name, price, availability, tags (key words).

Here is the product description:

"The EcoBottle X200 (ID: EBX200) is available for $19.99. It’s a reusable bottle made for outdoor use and eco-conscious consumers."
""",

# example 3: book data
"""
You are an expert JSON Formatter. Extract book metadata from the description in JSON format with the fields: title, author, year, genre, and summary.

Description:
"'The Midnight Library' by Matt Haig, published in 2020, explores the choices that shape our lives. It blends science fiction with philosophical themes."
"""]

schemas = [
    {"name", "age", "email", "interests"},
    {"product_id", "name", "price", "availability", "tags"},
    {"title", "author", "year", "genre", "summary"}
]

def validate_schema(data, expected_fields):
    return expected_fields.issubset(data.keys())

for i, prompt in enumerate(struct_prompts):
    print(f"\n--- Running prompt {i + 1} ---\n")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False,
            "temperature": 0.2
        }
    )
    if response.status_code == 200:
        raw_output = response.json()["response"]
        print("Model Response:\n", raw_output)

        try:
            parsed = json.loads(raw_output)
            print("Parsed JSON:\n", json.dumps(parsed, indent=2))
            if validate_schema(parsed, schemas[i]):
                print("Schema is valid.")
            else:
                print("Schema is invalid. Missing fields.")
        except json.JSONDecodeError as e:
            print("Invalid JSON response:", e)
    else:
        print("Error:", response.status_code, response.text)
