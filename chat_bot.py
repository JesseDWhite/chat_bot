import sys
import openai
import os

key = os.environ['chat_key']
openai.api_key = key

input = sys.argv[1]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input}
    ]
)

print(response.choices[0].message.content)

sys.stdout.flush()
