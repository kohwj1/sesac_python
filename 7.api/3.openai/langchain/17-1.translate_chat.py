from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate(
    messages= [
        ('system', '당신은 IT관련 언론 매체의 전문 번역가입니다.'),
        ('human', '아래 기사를 영어로 번역해주세요.  \n\n{article}'),
    ],
    input_values=['article']
)

llm = ChatOpenAI(temperature=0.3)
parser = StrOutputParser()

chain = prompt | llm | parser

with open('test.txt', 'r', encoding='utf-8') as file:
    article = file.read()

inputs = {'article':article}

res = chain.invoke(inputs)
print(res)