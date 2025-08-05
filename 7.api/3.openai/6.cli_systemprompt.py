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
    #페르소나: 가상의 인물을 만들어서 그 역할을 시킴
    gpt_system_prompt = {'role':'system', 'content':'당신은 동네 분식집의 주방장입니다.'}
    
    #시스템 프롬프트가 히스토리에 중복 추가되는 걸 방지
    if not history:
        history.append(gpt_system_prompt)
    
    #유저 입력 처리
    gpt_question = {"role":"user", "content": user_input}
    history.append(gpt_question)
    
    # print('실제 전송되는 대화:', history)

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