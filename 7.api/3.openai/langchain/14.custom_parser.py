from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda #runnales: 실행 집합

load_dotenv()

#템플릿으로 프롬프트 생성
my_template = "You are a naming consultant. Suggest 5 names for a {company} that makes {product}"

prompt = PromptTemplate(
    input_variables=['company', 'product'],
    template=my_template
)

#모델/파서 객체 생성
llm = OpenAI()

#커스텀 체인용 함수 예시
def custom_parser_function(output):
    cleaned_output = output.strip().replace('"','')
    return {'response':cleaned_output}

#체인 기본주조: 프롬프트 --> 모델(llm) --> 파싱 (파싱 부분을 커스터마이징하는것)
#이 예시에서 커스터마이징한 파서: {'response':파싱내용(공백제거)} 형태로 담기 위한 커스텀 객체

# chain = prompt | llm | RunnableLambda(lambda x: {'response': x.strip()})
chain = prompt | llm | RunnableLambda(custom_parser_function)

inputs = {'company':'high-tech startup', 'product':'mobile game'}
res = chain.invoke(inputs)

print(res)