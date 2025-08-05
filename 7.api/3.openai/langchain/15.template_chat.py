from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content='You are a naming consultant for new companies'),
        HumanMessage(content='What is a good name for a {company} that makes {product}?')
    ]
)

#현업버전 축약형 프롬프트 템플릿 13~18줄과 같은 내용
# https://python.langchain.com/docs/concepts/prompt_templates/ 참고
# prompt_short = ChatPromptTemplate.from_messages(
#     [
#         ('system','You are a naming consultant for new companies'),
#         ('human','What is a good name for a {company} that makes {product}?'),
#     ]
# )

llm = ChatOpenAI(model='gpt-3.5-turbo') #인스트럭터 모델이 들어가면 오류남?
parser = StrOutputParser()

chain = prompt | llm | parser
inputs = {'company':'high-tech startup', 'product':'electrical automobile'}

result = chain.invoke(inputs)
print(result)