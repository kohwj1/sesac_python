from dotenv import load_dotenv

from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')

llm = OpenAI(temperature=0.1)
# parser = StrOutputParser()
parser = RunnableLambda(lambda x: x.content)
summary_prompt = PromptTemplate(
    template="""
    아래 상품 리뷰 의견들을 종합해서 한줄로 요약할 것.
    \n\n {reviews_text}""",
    input_variables=['reviews_text']
)
translate_prompt = PromptTemplate(
    template="""
    아래 한국어 문장을 {target_lang}로 번역해서 보여줘.
    \n\n {summary_ko}""",
    input_variables=['target_lang', 'summary_ko']
)
summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm
summary_then_translate_chain = (
    {'summary_ko': summary_prompt | llm | parser,
     'target_lang': RunnablePassthrough()
     }
    | translate_prompt | llm | parser)

reviews = []
lang_dict = {'ko':'한국어','en':'영어','ja':'일본어','zh':'간체 중국어','it':'이탈리아어'}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/review', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = int(data.get('rating'))
    opinion = data.get('opinion')
    reviews.append({'rating':rating, 'opinion':opinion})

    # print(rating, opinion)
    return jsonify({'msg':'제출 성공'})

@app.route('/api/reviewes')
def get_reviews():
    return jsonify({"data": reviews})

@app.route('/api/ai-summary')
def get_aisummary():
    lang = request.args.get('lang')
    target_lang = lang_dict.get(lang, '영어')
    summary = '등록된 리뷰가 없습니다.'
    average_rating = 0.0
    
    if not reviews:
        # print(reviews)
        return jsonify({"summary": summary, 'averageRating': average_rating})
    
    average_rating = sum([r['rating'] for r in reviews]) / len(reviews)
    reviews_text = '\n'.join([f"rating:{r['rating']}, opinion: {r['opinion']}" for r in reviews])
    
    try:
        res = summary_then_translate_chain.invoke(
            {'reviews_text':reviews_text, 'target_lang':target_lang}
        )

        # summarized_text = summary_chain.invoke({'reviews_text':reviews_text})
        # res = translate_chain.invoke({'target_lang':target_lang, 'summarized_text':summarized_text})
        summary = res.strip()

    except:
        summary = '현재 요약 서비스 점검중입니다.'
    
    finally:
        return jsonify({"summary": summary, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(debug=True)