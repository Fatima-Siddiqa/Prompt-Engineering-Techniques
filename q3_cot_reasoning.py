import requests

# chain of thought hard coded examples
cot_prompts = ["""
Solve the following math problem step by step:
Q: 325 * 5 = ?
A: First, break down 325 into chunks : 300 + 20 + 5. Then, multiply each by 5: (300 x 5) + (20 x 5) + (5 x 5). 
Finally, add the results (1500 + 100 + 25 = 1625).

Q: 112 * 4 = ?
A:""", 

"""
Q: What is the next number in the sequence: 2, 4, 8, 16, ?
A: Observe the pattern: each number is multiplied by 2.
2 × 2 = 4, 4 × 2 = 8, 8 × 2 = 16.
So, 16 × 2 = 32.

Q: What is the next number in the sequence: 3, 6, 12, 24, ?
A:""", 

"""
Q: If 5 pencils cost $15, how much do 3 pencils cost?
A: Follow a step-by-step approach. First, find the cost of 1 pencil: $15 ÷ 5 = $3 per pencil.
Now multiply by 3: $3 × 3 = $9.

Q: 6 apples cost $24. How much will 10 apples cost?
A:""", 

"""
Q: 144 + 256 = ?
A: First, break down the numbers:
144 = 100 + 40 + 4
256 = 200 + 50 + 6

Now add corresponding parts:
100 + 200 = 300
40 + 50 = 90
4 + 6 = 10

Finally, add all results:
300 + 90 + 10 = 400

Q: 345 + 102 = ?
A: First, break down the numbers:
345 = 300 + 40 + 5
102 = 100 + 0 + 2

Now add corresponding parts:
300 + 100 = 400
40 + 0 = 40
5 + 2 = 7

Finally, add all results:
400 + 40 + 7 = 447

Q: 256 + 123 = ?
A:""",

"""
Respond with step-by-step logic and a short final answer only. Do not add extra commentary or characters.

Q: Tom is twice as old as Jerry. If Jerry is 5 years old, how old is Tom?
A: First, note that Tom is 2 times Jerry's age.
Now multiply: 5 × 2 = 10 years old.
Now answer the following using the same steps:

Q: A bookshelf has 4 shelves. If each shelf holds 7 books, how many books are there in total?
A:"""]


# Send prompt to Ollama
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi",
        "prompt": cot_prompts[4], #changing the index manually to check each prompt
        "stream": False,
        "temperature": 0.2
    }
)

# Handle response
if response.status_code == 200:
    print("Model Response:\n", response.json()["response"])
else:
    print("Error:", response.status_code, response.text)