import openai

openai.api_key = ""

def chatgpt_rasa(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=1,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0.2,
    )  
    return response.choices[0].text
def chatgpt_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0.8,
    )
    return response.choices[0].message['content']

print(chatgpt_rasa("Bạn là ai"))
print("=======================================================")
print(chatgpt_gpt("Bạn là ai"))