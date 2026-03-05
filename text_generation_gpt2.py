from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Prompt
prompt = "Artificial Intelligence will change the future because"

# Generate text
result = generator(prompt, max_length=80)

# Print result
print(result[0]['generated_text'])