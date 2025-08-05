from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI

load_dotenv()

template = '다음 수신자에게 주제의 내용에 해당하는 회사의 공식 이메일 형태로 작성해 주세요.\n\n수신자: {receipient}\n\n주제: {topic}'
prompt = PromptTemplate(input_variables=['receipient', 'topic'], template=template)

llm = OpenAI(temperature=1.0, max_tokens=1000) #토큰 기본값: 256
chain = prompt | llm | StrOutputParser()

input_text = {'receipient':'재경팀', 'topic':'월급명세서 발급 지연에 대한 항의'}
res = chain.invoke(input_text)
print(res)