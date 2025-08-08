from dotenv import load_dotenv

#채팅인터페이스에 필요한 모듈들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

#임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

#환경변수 메모리 로드
load_dotenv()

#문서 불러오기
loader = TextLoader('nvme.txt', encoding='utf-8')
document = loader.load()

#문서 청크 처리
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) #또는 사이즈 2000, 오버랩 500 정도가 무난
texts = text_splitter.split_documents(document)

#임베딩(청크 벡터화)
embeddings = OpenAIEmbeddings()

#벡터DB에 저장
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')

#벡터 DB 조회
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

#답변 출처(청크) 확인
# context_docs = retriever.invoke(question)

# for i, doc in enumerate(context_docs):
#     print(f'[---{i+1}---]\n{doc.page_content}')