from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()
api_key = os.getenv('API_KEY')

my_template = "You are a naming consultant. Suggest a name for a company that makes {product}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=my_template
)

llm = ChatOpenAI(api_key=api_key)

# filled_prompt = prompt.format(product='icecream')
# print(filled_prompt)

# filled_prompt = prompt.format(product='cookie')
# print(filled_prompt)

# filled_prompt = prompt.format(product='smartphone')
# print(filled_prompt)

test_product = [
    'mobile games',
    'robot toys',
    'electric bike',
    'camping goods',
    'programming language education'
]

for item in test_product:
    result = prompt.format(product=item)

    send_message = [
        HumanMessage(content=result)
    ]
    res = llm.invoke(send_message)
    print(res.content.strip('"'))

    # print(f'[{item}]: {result}')