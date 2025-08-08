from dotenv import load_dotenv

#채팅 인터페이스에 필요한 모듈들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

#임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

#환경변수 메모리 로드
load_dotenv()

#문서 불러오기
doc1 = TextLoader('nvme.txt', encoding='utf-8').load()
doc2 = TextLoader('ssd.txt', encoding='utf-8').load()
documents = doc1 + doc2

#필요 시 추가적인 메타데이터를 추가 --> 출처 등의 명시에 사용
# documents = [Document(page_content=doc.page_content, metadata={"source":"nvme.txt"}) for doc in documents]
for i, doc in enumerate(doc1, start=1):
    doc.metadata.update({"chunk_id":i, "created":"2025-08-01"})
for i, doc in enumerate(doc2, start=1):
    doc.metadata.update({"chunk_id":i, "created":"2025-08-07"})

#문서 청크 처리
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) #또는 사이즈 2000, 오버랩 500 정도가 무난
texts = text_splitter.split_documents(documents)

# #임베딩(청크 벡터화)
embeddings = OpenAIEmbeddings()

#벡터DB에 저장
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')

#벡터 DB 조회
retriever = store.as_retriever(search_kwargs={'k':5})

#채팅 인터페이스 설정
llm = ChatOpenAI(temperature=0.1)
template = """
다음 내용을 바탕으로 질문에 답변해주세요. 참고문서에 내용이 없는 경우 모른다고 답변해주세요.
참고문서: {context}

질문: {question}

답변을 작성하고, 마지막에 참고한 문서의 "출처: [파일명:청크아이디]"를 명시해주세요.
출처 내에 답변이 없는 경우 출처를 "없음"이라고 명시해주세요.
예) 출처: nvme.txt:1, ssd.txt:3
"""

prompt = ChatPromptTemplate.from_template(template=template)

def answer_question(q):
    print('-' * 50)
    chain = {"context":retriever, "question":RunnablePassthrough()} | prompt | llm | StrOutputParser()

    #사용자 입력과 응답
    res = chain.invoke(q)
    print(res)
    print('-' * 50)
    return res

def debug_retrieval(q):
    retrieved_docs = retriever.invoke(q)

    for i, doc in enumerate(retrieved_docs, start=1):
        print('-' * 50)
        print(f'출처: {doc.metadata}')
        print(f'미리보기: {doc.page_content[:100]}...(중략)')
        if hasattr(doc, 'score'):
            print(f'유사도 점수: {doc.score}')
        print('-' * 50)

    return True

answer_question("NVME와 SATA의 차이점을 100글자로 요약해주세요.")
answer_question("PCIe란?")
answer_question("우주의 크기는 얼마나 되나요?")
# debug_retrieval("PCIe란?")