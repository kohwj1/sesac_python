from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda

#환경 변수 메모리에 상주시키기
load_dotenv()

prompt = ChatPromptTemplate(messages=[
    ('system', '당신은 중고등학생을 대상으로 글쓰기와 논술을 지도하는 교사입니다.'),
    ('human', '아래 문장을 200자 이내로 요약해 주세요. \n\n {article}')
])

llm = ChatOpenAI(temperature=0.3)
parser = StrOutputParser()

#원문이 너무길어서 파일에서 가져오는 걸로 했습니다...
with open('test.txt', 'r', encoding='utf-8') as file:
    article = file.read()
    print(f'총 {len(article)}글자')

chain = prompt | llm | parser

inputs = {'article':article}
res = chain.invoke(inputs)

print(res)