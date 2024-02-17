import openai

openai.api_key = 'sample_api'

def generate_response(prompt):
    # Call the OpenAI API to generate a completion based on the given prompt
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=150,  
        temperature=0.7 
    )

    return response['choices'][0]['text'].strip()

# Example prompt
prompt_text = "Translate the following English text to French:"

# Generate a response
generated_text = generate_response(prompt_text)

# Print the generated text
print(generated_text)
