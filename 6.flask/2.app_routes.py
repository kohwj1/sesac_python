from flask import Flask

app = Flask(__name__) #__name__: 현재 파일명을 이름으로 사용할 수 있음 (파일명 그대로 사용해야 할 때 관행적으로 사용)

@app.route('/user')
def user():
    return '<h1>hello User!</h1>'

#꺾쇠로 묶으면 flask의 데코레이터가 변수로 인식하여 함수에 인자로 전달함: 서버-사이드 렌더링 (필요한 HTML을 서버에서 만들어 전달함)
@app.route('/user/<username>')
def username(username):
    return f'<h1>hello {username}!</h1>'

#꺾쇠로 묶은 변수는 별도 지정하지 않을 시 string임. 타입 지정 가능
@app.route('/user/<int:age>')
def greet_with_age(age):
    return f'<h1>안녕하세요, {age}살 아무개님!</h1>'

#꺾쇠로 묶은 변수는 별도 지정하지 않을 시 string임. 타입 지정 가능
@app.route('/user/<float:weight>')
def greet_with_weight(weight):
    if weight > 60:
        msg = '뚱뚱한'
    elif weight < 40:
        msg = '날씬한'
    else:
        msg = ''
    return f'<h1>{weight}kg {msg} 아무개님!!</h1>'

@app.route('/user/<name>/<int:Age>/<float:weight>')
def greet_with_userdetail(name, age, weight):
    page_content = f"""
    <h1>안녕하세요</h1>
    <h2>사용자 정보</h2>
    <ul>
        <li>이름: {name}</li>
        <li>나이: {age}</li>
        <li>체중: {weight}</li>
    </ul>
"""
    return page_content

if __name__ == '__main__':
    print('메인함수')
    app.run(debug=True) #디버그 모드가 켜져 있으면 저장 시 서버가 자동으로 재시작 & 클라이언트(브라우저, curl)에 오류메시지가 그대로 다 노출됨 --> 보안 취약!!!! 배포 전 반드시 확인
