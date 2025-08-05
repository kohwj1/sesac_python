from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import OpenAI

load_dotenv()

template = '다음 문장을 {language}로 번역하시오. \n\n\n {article}'
prompt = PromptTemplate(input_variables=['language', 'article'], template=template)

print_by_line_by_line = RunnableLambda(
    lambda x: {
        'translated': [line.strip() for line in x.split('\n') if line.strip()]
    }
)

llm = OpenAI(temperature=0.5)
# chain = prompt | llm | RunnableLambda(lambda x: {'summary':x.strip()})
chain = prompt | llm | print_by_line_by_line

input_text = {
    'article': r"""
- 아이폰17 에어의 배터리 두께가 매우 얇다는 사진이 유출됐다.
- 아이폰17 에어의 배터리 용량은 2천800mAh로 추정되며, 애플은 배터리 케이스를 출시할 예정이다.
- 아이폰17 에어는 C1 모뎀을 탑재하고 초광각 카메라를 탑재하지 않아 더 큰 배터리를 위한 내부 공간을 확보할 수 있다.
""",
    'language':'일본어'
}

res = chain.invoke(input_text)

# for line in res['summary'].split():
#     print(line)

print(res)