from dotenv import load_dotenv

from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')
openai = OpenAI()
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
        print(reviews)
        return jsonify({"summary": summary, 'averageRating': average_rating})
    
    average_rating = sum([r['rating'] for r in reviews]) / len(reviews)
    reviews_text = '\n'.join([f"'별점': {r['rating']}, '리뷰': {r['opinion']}" for r in reviews])
    
    try:
        res = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role':'user', 'content':f'다음 상품 리뷰 의견들을 종합해서 최대 3문장으로 요약해주세요. 요약된 문장을 {target_lang}로만 보여주세요. \n\n {reviews_text}'}
            ]
        )
        summary = res.choices[0].message.content
    
    except:
        summary = '현재 요약 서비스 점검중입니다.'
    
    finally:
        return jsonify({"summary": summary, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(debug=True)