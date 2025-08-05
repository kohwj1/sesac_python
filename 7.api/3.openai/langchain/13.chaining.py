from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser

load_dotenv()
api_key = os.getenv('API_KEY')

#템플릿으로 프롬프트 생성
my_template = "You are a naming consultant. Suggest 5 names for a {company} that makes {product}"

prompt = PromptTemplate(
    input_variables=['company', 'product'],
    template=my_template
)

#모델/파서 객체 생성
llm = OpenAI(api_key=api_key)
parser = StrOutputParser()
csv_parser = CommaSeparatedListOutputParser()
chain = prompt | llm | parser #각 단계를 한줄로 묶을 수 있는 연결(체인) Langchain Expression Language

inputs = {'company':'high-tech startup', 'product':'mobile game'}
res = chain.invoke(inputs)

print(res)