from flask import Flask, session
from flask_session import Session
# import os

app = Flask(__name__)
app.secret_key = 'my-secret-key'

# 세션 저장 위치
# filesystem / redis / memcache / mongodb / sqlalchemy 등등 가능
app.config['SESSION_TYPE'] = 'filesystem'  
app.config['SESSION_FILE_DIR'] = 'mysession'

#세션 영구 유지 여부
app.config['SESSION_PERMANANT'] = False

#세션 쿠키 서명 여부
app.config['SESSION_USE_SIGNER'] = True

#flask 앱에 세션 옵션 적용
Session(app)

@app.route('/')
def get_session():
    if 'username' in session:
        return f"<p>session info: {session['username']}</p><a href='/clear'>logout</a>"
    return f'no session'

@app.route('/set/<username>')
def set_session(username):
    session['username'] = username
    return 'session has been saved'

@app.route('/clear')
def del_session():
    session.pop('username', None)
    return "<p>session deleted</p><a href='/'>main</a>"

if __name__ == '__main__':
    app.run(debug=True)