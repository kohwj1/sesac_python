from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()
llm = OpenAI()

my_template = "You are a naming consultant. Suggest a name for a company that makes {product}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=my_template
)

print('새 회사 이름을 생성하는 서비스입니다.\n종료하려면 quit 또는 exit를 입력해주세요.')

while True:
    product = input('제품/서비스 종류를 입력해주세요.')

    if product in {'quit', 'exit'}:
        print('이용해 주셔서 감사합니다.')
        break

    filled_template = prompt.format(product=product)
    res = llm.invoke(filled_template)
    print(f'생성된 이름: {res.strip()}')