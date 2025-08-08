from dotenv import load_dotenv

#채팅 인터페이스에 필요한 모듈들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_chroma import Chroma

#DB폴더 조회 및 제어
import os

load_dotenv()
PERSIST_DIR = 'chroma_db'

#chroma DB 없으면 새로 생성
def create_vectordb():
    doc1 = TextLoader('nvme.txt', encoding='utf-8')
    documents = doc1.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) #또는 사이즈 2000, 오버랩 500 정도가 무난
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    store = Chroma.from_documents(texts, embeddings, collection_name='nvme', persist_directory=PERSIST_DIR)
    return store

#이미 있는 chroma DB 조회
def load_vector_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name="nvme", embedding_function=embeddings, persist_directory=PERSIST_DIR)
    return store


if os.path.exists(PERSIST_DIR):
    print('저장된 DB를 사용합니다.')
    store = load_vector_db()
else:
    print('DB가 존재하지 않습니다. 신규로 생성합니다.')
    store = create_vectordb()

retriever = store.as_retriever()

#채팅 인터페이스 설정
llm = ChatOpenAI(temperature=0.1)
template = """
다음 내용을 바탕으로 질문에 답변해주세요.
{context}

질문: {question}
"""

prompt = ChatPromptTemplate.from_template(template=template)
chain = {"context":retriever, "question":RunnablePassthrough()} | prompt | llm

#사용자 입력과 응답
question = "NVME와 SATA의 차이점을 100자로 요약해주세요"
res = chain.invoke(question)
print(res.content)