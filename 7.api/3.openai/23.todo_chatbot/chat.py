from dotenv import load_dotenv
from flask import request, jsonify, Blueprint
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


load_dotenv()
chat_bp = Blueprint('chat', __name__)


system_template = "당신은 To-Do 관리 효율을 높여주는 AI 어시스턴트입니다."
prompt_history = [
            ("system", system_template),
            ("human", "{user_input}"),
        ]

prompt = ChatPromptTemplate(prompt_history)
llm = ChatOpenAI(temperature=0.0)
parser = StrOutputParser()


@chat_bp.route('/api/chat', methods=['POST'])
def chat_to_bot():
    data = request.get_json()
    chain = prompt | llm | parser
    res = chain.invoke(data)

    return jsonify({'chatbot': res}), 200
