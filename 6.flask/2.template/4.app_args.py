from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name':'Alice', 'age':25, 'mobile':'0**-12**-5**8'},
    {'name':'Bob', 'age':30, 'mobile':'0**-11**-0**0'},
    {'name':'Charlie', 'age':35, 'mobile':'0**-12**-9**9'},
]

#미션1. 사용자 목록 테이블로 그리기
#미션2. 입력폼을 하나 만들어서 원하는 사용자만 골라내기
@app.route('/')
def search_by_name():
    name = request.args.get('username')
    print(name)

    result = users

    if name:
        result = [u for u in users if u['name'].lower() == name.lower()]
    
    return render_template('index4.html', users=result)

if __name__ == '__main__':
    app.run(debug=True)