from flask import Flask, session, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'mymy-secret-key'

users = [
    {'name':'Alice', 'id':'alice', 'pw':'alice!'},
    {'name':'Bob', 'id':'bob', 'pw':'bob1234'},
    {'name':'Chalie', 'id':'chalie', 'pw':'hello'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userid = request.form.get('id')
        userpw = request.form.get('pw')

        user = next((u for u in users if u['id'] == userid and u['pw'] == userpw), None)

        if user:
            session['user'] = user #로그인한 사용자의 세션 생성
            return redirect(url_for('dashboard'))
        else:
            return '로그인에 실패하였습니다'
    else:
        current_user = session.get('user')
        if current_user:
            return redirect(url_for('dashboard'))
        return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    current_user = session.get('user')

    if current_user:
        return render_template('dashboard.html', user=current_user)
    return '<p>로그인 후 이용 가능합니다.</p><a href="/">로그인하기</a>'

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    user = session.get('user')
    if request.method == 'POST':
        pass
    else:
        if user:
            return render_template('profile', user=user)
        return '<p>로그인 후 이용 가능합니다.</p><a href="/">로그인하기</a>'

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# 과제1. 로그인된 사용자 대시보드
# 안녕하세요, {이름}님
# 과제2. 로그인 상태로 루트 페이지 접근 시 대시보드로 보내기
# 과제3. 로그아웃 구현하기 (대시보드 인사말 아래에 a로 구현)
# 과제4. 프로필 페이지에서 이름, 비번 수정 기능 만들기

if __name__ == '__main__':
    app.run(debug=True)
