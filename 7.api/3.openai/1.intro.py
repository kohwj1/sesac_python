from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

json = {
    "model":"gpt-4o",
    "messages":[
        {"role":"user", "content":"오늘 저녁 메뉴는?"}
    ]
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

response= requests.post('https://api.openai.com/v1/chat/completions', json=json, headers=headers)
response_data = response.json()

# print(response_data['output'][0]['content'][0]['text'])
print(response_data['choices'][0]['message']['content'])