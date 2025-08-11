import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

# 필요한 글로벌 변수 선언
VECTOR_DB = './chroma_db'
COLLECTION_NAME = "my-data"
embeddings = OpenAIEmbeddings()
store = None

def get_store():
    return store

def initialize_vector_db():
    global store
    # 이전 DB가 있었으면? 로딩..
    if os.path.exists(VECTOR_DB) and os.listdir(VECTOR_DB):
        store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=VECTOR_DB)
    else:
        # 없으면? 디렉토리 생성
        os.makedirs(VECTOR_DB, exist_ok=True)
    return True
    
def create_vector_db(file_path):
    global store
    # 벡터 DB 생성...
    # 1. 파일을 가져온다
    documents = PyPDFLoader(file_path).load()
    
    for doc in documents:
        doc.metadata['source'] = os.path.basename(file_path) # 경로 제외하고 파일명만 남기기
        
    # 2. 문서 분할한다
    texts = CharacterTextSplitter(chunk_size=100, chunk_overlap=20).split_documents(documents)
    print(texts)
    
    # 3. 임베딩 한다
    if store:
        store.add_documents(texts)
    else:
        store = Chroma.from_documents(
            texts, embedding=embeddings, collection_name=COLLECTION_NAME, persist_directory=VECTOR_DB)
    
    print("벡터 DB가 정상적으로 생성되었습니다.")
    return store

def delete_file_from_vstore(filename):
    # NoSQL 기반의 DB에서 자료 삭제하는것과 동일함 (예, mongodb)
    store._collection.delete(where={"source": filename})
    
    # 백터DB가 persist 옵션이 켜져 있으면? 저장..
    if hasattr(store, "persist"):
        store.persist()