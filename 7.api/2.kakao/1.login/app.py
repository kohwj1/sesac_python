from flask import Flask, render_template, redirect, request, url_for, session
from dotenv import load_dotenv
import os, requests

load_dotenv()
KAKAO_CLIENT_SECRET = os.getenv('KAKAO_CLIENT_SECRET')
KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')
KAKAO_REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    kakao_auth_url = (
        f'https://kauth.kakao.com/oauth/authorize'
    )

    return render_template('index.html')

@app.route('/auth/login')
def kakao_login():
    pass

@app.route('/auth/kakao/callback')
def callback():
    code = request.args.get('code')
    print(f'코드값:{code}')

    token_url = (
        #카카오에 코드 검중 후 토큰 발급할 엔드포인트
    )

    #사용자 요청
    user_info_url = (
        #사용자 조회 엔드포인트?
    )

    user_info = requests.get(user_info_url)
    #세션에 현재 유저 담기
    print(f'현재 로그인 사용자: {user_info}')
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user = session.get('user', None)

    if user:
        return render_template('profile.html', user=user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)