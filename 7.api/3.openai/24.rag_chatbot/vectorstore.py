from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

import os

load_dotenv()

VECTOR_DB = 'chroma.db'
collection_name = 'my_pdf_store'

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0.1)
template = """
주어진 문서 내용을 바탕으로 질문에 답변해주세요.

문서 내용: {context}
질문: {q}

답변을 작성하고, 마지막에 참고한 페이지의 메타데이터를 이용해서 "출처: [source, page1, page2, page3와 같이]"를 명시해주세요.
출처에서 적절한 답변을 찾지 못한 경우 출처 표기를 하지 말고 대답만 해주세요.

출처 표기 예시)
출처: python_guide_for_secure_coding.pdf: 3페이지, 6페이지, 52페이지
출처: secure_coding_guide_for_python.pdf: 12페이지
"""

prompt = ChatPromptTemplate.from_template(template)


# 프롬프트, 랭체인용 체인 등은 위에서 한 번만 선언하자! (함수 안에 넣어서 반복 호출할 필요 X)

def init_vector_db():
    store = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory=VECTOR_DB
    )
    return store

def create_vector_db(pdf_filename):
    # 1. 벡터 DB 생성
    # 2. 파일 가져오기
    # 3. 문서 청크
    # 4. 임베딩 (벡터화)
    loader = PyPDFLoader(pdf_filename)
    pages = loader.load()

    text_splitter = CharacterTextSplitter(
        separator="\n\n", #문서 분할 기준
        chunk_size=500, #청크 크기
        chunk_overlap=100 #청크 오버랩 크기
    )

    texts = text_splitter.split_documents(pages)
    store = Chroma.from_documents(texts, embeddings, collection_name=collection_name, persist_directory=VECTOR_DB)
    return store

def answer_question(q):
    store = init_vector_db()
    if store.get(limit=1).get('ids'):
        res = 'DB 생성이 정상적으로 진행되지 않았습니다. 파일을 다시 업로드해주세요'

    retriever = store.as_retriever(search_kwargs={'k':5})
    chain = {"context":retriever, "q":RunnablePassthrough()} | prompt | llm | StrOutputParser()
    res = chain.invoke(q)

    # 1. llm에 질의응답하기
    # 2. 체인 호출하여 질문에 대한 대답 받아내기
    return res