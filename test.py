import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})