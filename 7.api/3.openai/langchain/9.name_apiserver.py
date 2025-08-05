from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI, ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

load_dotenv()
api_key = os.getenv('API_KEY')

app = Flask(__name__)

llm1 = OpenAI(temperature=0.9, api_key=api_key)
llm2 = ChatOpenAI(temperature=0.9, api_key=api_key)

@app.route('/api/name', methods=['POST'])
def generate_name():
    data = request.get_json()
    product = data.get('product', None)

    # prompt = f'What is a good company name that makes {product}?'
    prompt = f'{product}를 생산하는 회사명을 지어줄래? 가장 괜찮은 것 하나만 보여줘.'

    result = llm1.invoke(prompt)
    names = result.strip()

    return jsonify({'product':product, 'name':names})

@app.route('/api/name2', methods=['POST'])
def generate_name2():
    data = request.get_json()
    product = data.get('product', None)

    prompt = [
        SystemMessage(content='당신은 신생 기업을 대상으로 창의적인 회사명 작명을 도와주는 컨설턴트입니다.'),
        HumanMessage(content=f'{product}를 생산하는 회사명을 지어줄래? 가장 괜찮은 것 하나만 보여줘.'),
    ]

    result = llm2.invoke(prompt)
    names = result.content.strip('"')

    return jsonify({'product':product, 'name':names})

if __name__ == '__main__':
    app.run(debug=True)