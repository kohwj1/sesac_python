import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()
api_key = os.getenv('API_KEY')


llm = OpenAI(api_key=api_key, max_tokens=1000)

prompt = '인공지능이란'
result = llm.invoke(prompt)
print(result)