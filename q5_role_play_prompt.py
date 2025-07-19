import requests

# without roleplay
general_prompts = { 
    "Doctor":
"I've had a sore throat and mild fever for three days. Should I be concerned?",

"Lawyer": "Can I file for custody if I don’t have a stable income yet?",

"Customer Support Agent": "I received a damaged laptop in my order. What should I do?"
}

# with roleplay
role_play_prompts = { 
    "Doctor":
"""You are an experienced medical doctor specialized in general medicine. Answer the patient concisely.
The user asks: 'I've had a sore throat and mild fever for three days. Should I be concerned?'
Doctor:""",

"Lawyer": """You are a professional legal advisor with expertise in family law. Answer the user concisely.
    The user asks: 'Can I file for custody if I don’t have a stable income yet?'
    Lawyer:""",

"Customer Support Agent": """You are a polite and helpful customer support agent for an online electronics store. Answer the customer concisely is 2-3 sentences.
    The user asks: 'I received a damaged laptop in my order. What should I do?'
    Customer Support Agent:"""
}

# Send prompt to Ollama
print ("Model's Response Without Role Play:")
for key in general_prompts:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": general_prompts[key], #changing the index manually to check each prompt
            "stream": False,
            "temperature": 0.2
        }
    )
    # Handle response
    if response.status_code == 200:
        print(f"{key}:\n", response.json()["response"])
    else:
        print("Error:", response.status_code, response.text)

print ("Model's Response With Role Play:")
for key in role_play_prompts:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": role_play_prompts[key], #changing the index manually to check each prompt
            "stream": False,
            "temperature": 0.4
        }
    )
    # Handle response
    if response.status_code == 200:
        print(f"{key}:\n", response.json()["response"])
    else:
        print("Error:", response.status_code, response.text)