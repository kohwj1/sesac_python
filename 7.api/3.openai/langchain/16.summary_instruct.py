from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import OpenAI

load_dotenv()

template = '다음 문장을 3줄로 요약하시오. \n\n\n {article}'
prompt = PromptTemplate(input_variables=['article'], template=template)

print_by_line_by_line = RunnableLambda(
    lambda x: {
        'summary': [line.strip() for line in x.split('\n') if line.strip()]
    }
)

llm = OpenAI(temperature=0.5)
# chain = prompt | llm | RunnableLambda(lambda x: {'summary':x.strip()})
chain = prompt | llm | print_by_line_by_line

input_text = {
    'article': r"""
애플이 올 가을 출시할 슬림형 ‘아이폰17 에어’의 배터리 두께를 보여주는 사진이 유출됐다고 IT매체 맥루머스가 4일(현지시간) 보도했다.
국내 IT 팁스터 란즈크는 블로그에 아이폰17 에어와 아이폰17 프로의 배터리 두께를 비교한 사진을 공개하며, 아이폰17 에어의 배터리 두께가 “메탈케이스 포함 2.49mm에 불과하다”고 주장했다.
사진에서 아이폰17 에어의 배터리 두께는 아이폰17 프로 배터리의 절반 정도로 보인다.
란즈크는 과거 아이폰17 에어의 배터리 용량이 2천800mAh라고 처음 주장했다. 이후 중국 소식통들은 아이폰17 에어의 배터리 용량이 3천mAh 미만일 것이라고 밝히며 이를 뒷받침했다. 고급형 모델인 아이폰17 프로의 배터리 용량에 대해서는 아직 알려지지 않은 상태고 최상위 모델 아이폰17 프로 맥스의 경우 5천mAh 이상일 것으로 전해지고 있다.
지난 5월 란즈크는 아이폰17 에어의 무게가 약 145g이라고 밝혔다. 이는 과거 아이폰SE 2(148g)와 아이폰13 미니(141g)와 비슷한 수준이다. 올 가을 출시되는 초박형 아이폰17 에어의 두께는 약 5.5mm로, 역대 가장 얇은 아이폰이 될 예정이다.
지난 3월 애플 전문 분석가 궈밍치는 아이폰17 에어에 대해 고밀도 배터리가 탑재될 것이라고 전망한 바 있다. 이후 블룸버그 통신은 일본 스마트폰 부품사 TDK가 6월 말까지 3세대 실리콘 음극 배터리 출하를 시작한다며, 아이폰17 에어에 해당 배터리가 탑재될 가능성을 거론했다.
이런 보도에도 불구하고 아이폰17 에어의 배터리 성능에 대한 전망은 엇갈리고 있는 상태다. IT매체 디인포메이션은 아이폰17 에어의 배터리 수명이 이전 아이폰 모델보다 더 나쁠 것으로 전망했다. 이 문제를 해결하기 위해 애플이 아이폰17 에어용 액세서리로 배터리 케이스를 출시할 계획이라고 전했다.
반면, 블룸버그 통신 마크 거먼은 하드웨어와 소프트웨어 최적화 덕분에 아이폰17 에어의 배터리 수명이 현재의 아이폰과 동일한 수준이 될 것이라며 좀 더 낙관적인 전망을 내놨다.
올 가을 출시되는 두께 5.5mm의 아이폰17 에어는 애플이 자체 개발한 전력 효율적인 C1 모뎀을 탑재하고 초광각 카메라를 탑재하지 않아 더 큰 배터리를 위한 내부 공간을 확보할 수 있을 것으로 보인다고 외신들은 전망하고 있다.
"""
}

res = chain.invoke(input_text)

# for line in res['summary'].split():
#     print(line)

print(res)