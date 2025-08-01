from flask import Flask, render_template, redirect, request, session, url_for
from dotenv import load_dotenv
import os, requests

load_dotenv()

#숙제
#1. 네아로 회원 sqlite3에 담기
#1-1. 시나리오1: 기존 회원인지 조회
#1-2. 시나리오2: 신규 회원으로 DB에 저장

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
NAVER_REDIRECT_URI = os.getenv('NAVER_REDIRECT_URI')
SESSION_SECRET_KEY = os.getenv('SESSION_SECRET_KEY')

app = Flask(__name__)
app.secret_key = SESSION_SECRET_KEY

@app.route('/')
def index():
    user = session.get('user', None)

    if user:
        return render_template('index.html', user=user)
    return redirect(url_for('login_naver'))

@app.route('/login/naver')
def login_naver():
    #네아로 주소
    auth_url = (f'https://nid.naver.com/oauth2.0/authorize?'
                f'response_type=code'
                f'&client_id={NAVER_CLIENT_ID}'
                f'&redirect_uri={NAVER_REDIRECT_URI}'
                f'&state=test'
            )
    
    return redirect(auth_url)

@app.route('/naver/callback') #네아로 성공 이후 돌아올 uri
def naver_callback():
    code = request.args.get('code') #서버가 인증 성공 시 보내는 값
    state = request.args.get('state') #내 사이트에서 출발 -> 도착했는지 확인하는 값 (내가 보낸 값 그대로 돌아옴?)

    token_url = (f'https://nid.naver.com/oauth2.0/token?'
                 f'grant_type=authorization_code'
                 f'&client_id={NAVER_CLIENT_ID}'
                 f'&client_secret={NAVER_CLIENT_SECRET}'
                 f'&code={code}'
                 f'&state={state}'
            )

    token_res = requests.get(token_url).json()
    print(token_res)

    #사용자가 제대로 인증하고 온거 확인 완료. 이 정보가 서버에서 정식으로 받아온 게 맞는지 검증 진행
    access_token = token_res.get('access_token')
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    profile = requests.get('https://openapi.naver.com/v1/nid/me', headers=headers).json()
    print(profile)

    session['user'] = profile['response']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)