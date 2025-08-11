from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from vectorstore import get_store

PROMPT_JSON_FILE = "prompt.json"
PROMPT_YAML_FILE = "prompt.yaml"

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "당신은 문서 기반 질의 응답 시스템 입니다."
     "아래 '문서' 를 참고하여 질문에 답변하세요."
     "\n\n문서:\n{context}\n\n"
     "만약 문서에 정보가 없다면, 지어내지 말고, '모르겠습니다' 라고 답하세요."),
    ("human", "{question}")
])
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

def answer_question(question):
    store = get_store()
    # LLM 에 질의 응답한다
    if store is None:
        return "문서가 로드되지 않았습니다. 먼저 PDF를 업로드 해주세요."
    
    docs = store.similarity_search(question, k=5)
    context = "\n\n\n".join([doc.page_content for doc in docs])
    for i, d in enumerate(docs, 1):
        print(f"문서 #{i} - {d}")
        
    
    # 체인 호출, 질문과 함께...
    result = chain.invoke({"context": context, "question": question})
    
    return result

import json
def _load_prompts_from_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f) # 이거도 다 try except 해야함
        
    result = {}
    for name, p in data.items():
        template = p["template"]
        result[name] = ChatPromptTemplate.from_template(template)
    return result

import yaml
def _load_prompts_from_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) # yaml 문법에 escaping문자열로 나쁜짓 못하게...

    return {
        name: ChatPromptTemplate.from_template(p["template"])
        for name, p in data.items()
    }

def initialize_llm():
    global prompt, llm, output_parser, chain
    
    # prompt = _load_prompts_from_json(PROMPT_JSON_FILE)["default_prompt"]
    prompt = _load_prompts_from_yaml(PROMPT_YAML_FILE)["default_prompt"]
    print("프롬프트 로딩:", prompt)
    
    chain = prompt | llm | output_parser