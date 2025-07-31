from flask import Flask, request, session, render_template, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = 'mymymy-test-test'

users = [
    {'id':'user', 'pw':'test', 'name': 'MyName'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userid = request.form.get('id')
        userpw = request.form.get('pw')

        user = next((u for u in users if u['id'] == userid and u['pw'] == userpw), None)

        if user: #로그인 성공했으면
            session['user'] = user
            flash('로그인에 성공했습니다', 'success')
            return redirect(url_for('user'))
        flash('아이디 또는 비밀번호가 일치하지 않습니다.', 'danger')
        return redirect(url_for('home')) #로그인 실패했으면
    else:
        if 'user' in session: #이미 로그인한 상태로 접근한 경우
            flash('이미 로그인 상태입니다.', 'warning')
            return redirect(url_for('user'))
        return redirect(url_for('home')) #로그인 안한 상태로 접근한 경우    

@app.route('/user')
def user():
    user = session.get('user')

    if not user:
        flash('로그인 후 이용 가능합니다.', 'warning')
        return redirect(url_for('home')) 

    return render_template('user.html', name=user['name'])

@app.route('/logout')
def logout():
    user = session.get('user')

    if not user:
        flash('이미 로그아웃되었습니다.', 'warning')
    else:
        session.pop('user', None)
        flash('정상적으로 로그아웃되었습니다.', 'success')
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)