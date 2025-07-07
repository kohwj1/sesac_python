from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int) #page 파라미터가 입력되지 않을 경우 기본값을 정수형 1로 요청
    print(query, page)
    
    return f'검색어: {query},\n페이지: {page}'

if __name__ == '__main__':
    app.run(debug=True)