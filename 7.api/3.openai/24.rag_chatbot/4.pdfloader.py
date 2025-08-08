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

pdf_filename = 'DATA/python_guide_for_secure_coding.pdf'
loader = PyPDFLoader(pdf_filename)
pages = loader.load()

# print(f"총 페이지수: {len(pages)}")
# print(f"미리보기: {pages[1].page_content[:100]}")
# print(f"메타데이터: {pages[1].metadata}")

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n\n", #문서 분할 기준
    chunk_size=1000, #청크 크기
    chunk_overlap=500 #청크 오버랩 크기
)

texts = text_splitter.split_documents(pages)

embeddings = OpenAIEmbeddings()







store = Chroma.from_documents(texts, embeddings, collection_name="secure_coding_guide", persist_directory='chroma_db')

llm = ChatOpenAI(temperature=0.1)
template = """
주어진 문서 내용을 바탕으로 질문에 답변해주세요.
문서 내용: {context}
질문: {q}
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