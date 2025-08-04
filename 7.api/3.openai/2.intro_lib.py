import openai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv('SESAC_API_KEY')
openai.api_key = API_KEY


client = openai.OpenAI()
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {"role":"user", "content":"아무 말이나 입력할게요."}
    ]
)

print(response.choices[0].message.content)