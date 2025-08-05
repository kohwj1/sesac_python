import openai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

history = []

#클라이언트 초기화
client = openai.OpenAI()

#답변 파싱
def ask_chatgpt(user_input):
    gpt_question = {"role":"user", "content": user_input}
    history.append(gpt_question)
    
    print('실제 전송되는 대화:', history)


    response = client.chat.completions.create(
        model='gpt-4o',
        messages=history,
        temperature=0.7
    )

    gpt_response = {"role":"assistant", "content":response.choices[0].message.content}
    history.append(gpt_response)

    return f"ChatGPT: {gpt_response['content']}"


while True:
    user_input = input('사용자: ')

    if user_input in {'!종료', '!끝'}:
        break

    print(ask_chatgpt(user_input))