from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate(
    messages=[
        ('system','당신은 CEO의 비서로, CEO가 말하고자 하는 내용을 담은 메일 초안을 작성하는 역할을 맡고 있습니다.'),
        ('human','{receipient}에게 {topic}에 대해 이야기하는 업무 메일을 작성해 줘.')
    ]
)

llm = ChatOpenAI(temperature=1.1)
parser = StrOutputParser()


chain = prompt | llm | parser

user_input = {'receipient':'인사실장', 'topic':'내년도 사업계획에 따른 채용 계획 보고 요청'}

res = chain.invoke(user_input)
print(res)