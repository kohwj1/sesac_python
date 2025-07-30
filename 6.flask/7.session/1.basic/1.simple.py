from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'my-secret-key' #외부에 노출되면 안 되는 값

@app.route('/set/<username>')
def set_session(username):
    session['username'] = username
    #세션 쿠키가 프론트에 자동 생성 - 인코딩된 세션 정보 (암호화 아님!)
    return 'session has been saved'


@app.route('/get')
def get_session():
    if 'username' in session:
        return f"session info: {session['username']}"
    return f'no session'

@app.route('/clear')
def del_session():
    session.pop('username', None)
    return 'session deleted'


if __name__ == '__main__':
    app.run(debug=True)
    
#curl에서 쿠키 정보를 담아 주고받는 방법
#curl 127.0.0.1:5000/set/test1 -c cookie.txt
#curl 127.0.0.1:5000/get -b cookie.txt