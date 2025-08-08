from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

import os

PERSIST_DIR = 'chroma_db'
collection_name = 'secure_coding_guide'
load_dotenv()

pdf_filename = 'DATA/secure_coding_guide_for_python.pdf'
loader = PyPDFLoader(pdf_filename)
pages = loader.load()

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n\n", #문서 분할 기준
    chunk_size=1000, #청크 크기
    chunk_overlap=500 #청크 오버랩 크기
)

texts = text_splitter.split_documents(pages)

embeddings = OpenAIEmbeddings()

if os.path.exists(PERSIST_DIR):
    store = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR
    )
else:
    store = Chroma.from_documents(texts, embeddings, collection_name=collection_name, persist_directory=PERSIST_DIR)

llm = ChatOpenAI(temperature=0.1)
template = """
주어진 문서 내용을 바탕으로 질문에 답변해주세요.

문서 내용: {context}
질문: {q}

답변을 작성하고, 마지막에 참고한 페이지의 메타데이터를 이용해서 "출처: [source, page]"를 명시해주세요.

출처 표기 예시)
출처: python_guide_for_secure_coding.pdf, 3페이지
출처: secure_coding_guide_for_python.pdf, 12페이지
"""

prompt = ChatPromptTemplate.from_template(template)
retriever = store.as_retriever(search_kwargs={'k':5})
chain = {"context":retriever, "q":RunnablePassthrough()} | prompt | llm | StrOutputParser()


q = "시큐어 코딩의 주요 기법들에 대해서 리스트 형태로 요약해서 설명해줘."
res = chain.invoke(q)

print(f'Q: {q}')
print(f'A: {res}')

#1. DB 중복 생성하지 않게 분기처리
#2. 답변에 출처와 페이지를 함께 표시하기