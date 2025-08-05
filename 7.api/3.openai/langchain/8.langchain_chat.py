import os
from dotenv import load_dotenv
from langchain_openai import OpenAI #문장을 완성해주는 (completion) 모델
from langchain_openai import ChatOpenAI #chat (QA) 모델 - question and answer?
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()
api_key = os.getenv('API_KEY')

llm = OpenAI(api_key=api_key, max_tokens=1000) #사용 모델: 3.5 터보 인스트럭터
prompt = '인공지능이란'
result = llm.invoke(prompt)
print(result)

llm2 = ChatOpenAI(api_key=api_key) #사용 모댈: 3.5 터보
new_prompt = [
    SystemMessage(content='당신은 요리 레시피 연구가입니다.'),
    HumanMessage(content='디저트 케이크를 맛있게 만들려면'),
    AIMessage(content='신선한 재료를 사용하고, 정확한 계량과 온도 조절로 부드럽고 촉촉한 식감을 살리는 것이 비결입니다.'),
    HumanMessage(content='식감을 살리는 비결은'),
]
result2 = llm2.invoke(new_prompt)
print(result2.content)