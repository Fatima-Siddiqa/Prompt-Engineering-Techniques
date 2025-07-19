from jinja2 import Template
import requests

# templates
templates = {
    "summarization": """Summarize the following article in bullet points. 
Article: {{ article_text }}

Summary:""",
    
    "translation": """Translate the text from {{ original_language }} to {{ translated_language }}: {{ user_input }}""",
    
    "json_format": """Format the following text into JSON schema: 
{{ user_input }}""",
    
    "expert_qna": """Answer the following question as an expert in {{ context }} domain. Make the answer concise.
Question: {{ user_input }} 
Answer:""",
    
    "roleplay_director": """You are the creative director of a film studio. Answer the following question like a professional creative director: {{ user_input }}""",
    
    "general_qna": """Answer the following general knowledge question concisely.
Question: {{ user_input }} 
Answer:"""
}

# Menu
print("Select a prompt type:")
print("1. Summarization (bullet points)")
print("2. Translation")
print("3. JSON Schema Formatting")
print("4. Expert Q&A")
print("5. Roleplay as Creative Director")
print("6. General Knowledge Q&A")

choice_map = {
    "1": "summarization",
    "2": "translation",
    "3": "json_format",
    "4": "expert_qna",
    "5": "roleplay_director",
    "6": "general_qna"
}

choice = input("Enter your choice (1-6): ").strip()
selected = choice_map.get(choice)

if not selected:
    print("Invalid selection.")
    exit()

# inputs based on selected template
values = {}

if selected == "summarization":
    values["article_text"] = input("Enter the article text to summarize:\n")

elif selected == "translation":
    values["original_language"] = input("Enter original language: ")
    values["translated_language"] = input("Enter target language: ")
    values["user_input"] = input("Enter text to translate: ")

elif selected == "json_format":
    values["user_input"] = input("Enter text to format as JSON schema:\n")

elif selected == "expert_qna":
    values["context"] = input("Enter domain of expertise (e.g., biology, law): ")
    values["user_input"] = input("Enter your question: ")

elif selected == "roleplay_director":
    values["user_input"] = input("Enter the question for the creative director: ")

elif selected == "general_qna":
    values["user_input"] = input("Enter your general knowledge question: ")

# Render the selected template using Jinja2
template = Template(templates[selected])
rendered_prompt = "/no_think\n" + template.render(values)

print("\nPrompt Sent to Qwen3:\n")
print(rendered_prompt)

# Send to Ollama
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "qwen3:0.6b",
        "prompt": rendered_prompt,
        "stream": False
    }
)

# Handle response
if response.status_code == 200:
    print("\nModel Response:\n")
    print(response.json()["response"])
else:
    print(f"\nError: {response.status_code} - {response.text}")