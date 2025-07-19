import requests

# Dataset: Sentiment classification
dataset = [
    {"text": "The service was terrible and slow.", "label": "Negative"},
    {"text": "It’s just another average day.", "label": "Neutral"},
    {"text": "Well, that was the best waste of two hours ever.", "label": "Negative"},
    {"text": "I expected more, but it was decent.", "label": "Neutral"},
    {"text": "Thanks a lot for ruining my day.", "label": "Negative"},
    {"text": "Absolutely stunning visuals, but a painfully slow plot.", "label": "Neutral"},
    {"text": "It's fine.", "label": "Neutral"}
]

# Prompt templates
def zero_shot_prompt(text):
    return f"""Classify the sentiment of this sentence as Positive, Negative, or Neutral:
Sentence: "{text}"
Sentiment:"""

def few_shot_prompt(text):
    return f"""Classify the sentiment of the following sentences:

Example 1:
Sentence: "The service was terrible and slow."
Sentiment: Negative

Example 2:
Sentence: "Everything was perfect and I enjoyed it."
Sentiment: Positive

Example 3:
Sentence: "It’s just another average day."
Sentiment: Neutral

Example 4:
Sentence: "Well, that was the best waste of two hours ever."
Sentiment: Negative

Example 5:
Sentence: "I expected more, but it was decent."
Sentiment: Neutral

Example 6:
Sentence: "Oh great, another masterpiece."
Sentiment: Negative 

Now classify:
Sentence: "{text}"
Sentiment:"""

# Call Ollama Phi model
def run_model(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        print("Error:", response.status_code, response.text)
        return ""

# Evaluation
correct_zero = 0
correct_few = 0

print("Evaluating on Phi...\n")

for i, item in enumerate(dataset):
    text = item["text"]
    true_label = item["label"]

    # Zero-shot
    z_prompt = zero_shot_prompt(text)
    z_output = run_model(z_prompt)

    # Few-shot
    f_prompt = few_shot_prompt(text)
    f_output = run_model(f_prompt)

    # Compare outputs
    z_correct = true_label.lower() in z_output.lower()
    f_correct = true_label.lower() in f_output.lower()

    if z_correct:
        correct_zero += 1
    if f_correct:
        correct_few += 1

    # Print result for each case
    print(f"Example {i+1}: {text}")
    print(f"Expected Sentiment : {true_label}")
    print(f"Zero-Shot Response : {z_output} {'✅' if z_correct else '❌'}")
    print(f"Few-Shot Response  : {f_output} {'✅' if f_correct else '❌'}")
    print("-" * 60)

# Accuracy calculation
accuracy_zero = correct_zero / len(dataset)
accuracy_few = correct_few / len(dataset)

# Summary
print(f"\n--- Accuracy Summary ---")
print(f"Zero-Shot Accuracy: {accuracy_zero * 100:.2f}%")
print(f"Few-Shot Accuracy : {accuracy_few * 100:.2f}%")