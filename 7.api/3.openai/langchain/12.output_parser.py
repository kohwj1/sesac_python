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

#결과 도출
inputs = {'company':'high-tech startup', 'product':'mobile game'}

filled_prompt = prompt.format(**inputs) #dict포맷으로 한번에 밀어넣을 수 있다
res = llm.invoke(filled_prompt)

parsed_str = parser.invoke(res)
csv_parsed_str = csv_parser.invoke(res)

print(parsed_str)
print(csv_parsed_str)
