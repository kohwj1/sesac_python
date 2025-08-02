from flask import Flask, render_template, redirect, request, url_for, session, flash
from dotenv import load_dotenv
import os, requests, json

load_dotenv()
KAKAO_CLIENT_ID = os.getenv('KAKAO_CLIENT_ID')
KAKAO_CLIENT_SECRET = os.getenv('KAKAO_CLIENT_SECRET')
KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/kakao/login')
def kakao_login():
    kakao_auth_url = (
        'https://kauth.kakao.com/oauth/authorize'
        '?response_type=code'
        '&scpoe=openid'
        f'&client_id={KAKAO_CLIENT_ID}'
        f'&redirect_uri={KAKAO_REDIRECT_URI}'
    )

    return redirect(kakao_auth_url)

@app.route('/auth/kakao/callback')
def callback():
    code = request.args.get('code', None)
    
    if not code:
        flash('로그인 중 문제가 발생하였습니다. 관리자에게 문의해주세요.', 'danger')
        return redirect(url_for('index'))

    token_url = 'https://kauth.kakao.com/oauth/token'
    token_headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
    token_payload = {"grant_type": "authorization_code",
                     "client_id": f"{KAKAO_CLIENT_ID}",
                     "client_secret": f"{KAKAO_CLIENT_SECRET}",
                     "redirect_uri": f"{KAKAO_REDIRECT_URI}",
                     "code": f"{code}"}

    token_res = requests.post(token_url, data=token_payload, headers=token_headers)
    token_data = json.loads(token_res.text)

    user_info_url = 'https://kapi.kakao.com/v2/user/me?secure_resource=true'
    user_info_header = {
        "Authorization": f"bearer {token_data.get('access_token')}",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    user_info = requests.get(user_info_url, headers=user_info_header)
    user_info_data = json.loads(user_info.text)
    user_info_data['access_token'] = token_data.get('access_token')
    
    session['user'] = user_info_data
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user = session.get('user', None)

    if user:
        properties = user.get('properties')
        if properties:
            return render_template('profile.html', user=user)
    flash('로그인이 필요합니다.', 'warning')
    return redirect(url_for('index'))

@app.route('/logout')
def kakao_logout():
    user = session.get('user', None)
    
    if not user:
        flash('이미 로그아웃되었습니다.', 'warning')
        return redirect(url_for('index'))

    access_token = user.get('access_token', None)
    logout_headers = {
        "Authorization": f"Bearer {access_token}"
    }

    result = requests.post('https://kapi.kakao.com/v1/user/logout', headers=logout_headers)
    
    return redirect(url_for('session_logout'))

@app.route('/auth/logout')
def session_logout():
    user = session.get('user', None)

    if not user:
        flash('이미 로그아웃되었습니다.', 'warning')
    else:
        session.pop('user')
        flash('정상적으로 로그아웃되었습니다.', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)