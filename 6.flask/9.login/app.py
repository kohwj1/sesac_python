from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
import sqlite3
import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-my-my-my'
app.config['PERMANANT_SESSION_LIFETIME'] = timedelta(minutes=15)
DB_FILENAME = 'users.db'

def hash_password(pw):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw.encode(), salt)

def get_user(userid, userpw):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(r"SELECT * FROM users WHERE username = ?", (userid, ))
    user = cur.fetchone()
    conn.close()

    if user and bcrypt.checkpw(userpw.encode(), user['password']):
        return user

def get_user_by_username(userid):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(r"SELECT * FROM users WHERE username = ?", (userid, ))
    
    user = cur.fetchone()

    conn.close()
    return user

def create(userid, userpw, name):
    hashed_pw = hash_password(userpw)
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (username, password, name) VALUES (?, ?, ?)", (userid, hashed_pw, name))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form.get('id')
        userpw = request.form.get('pw')

        user = get_user(userid, userpw)

        if user:
            session['user'] = {'id':user['id'], 'name':user['name']}
            flash('로그인에 성공했습니다.', 'success')
            return redirect(url_for('user'))
        else:
            flash('아이디 또는 비밀번호가 일치하지 않습니다.', 'danger')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form.get('id')
        userpw = request.form.get('pw')
        userpw2= request.form.get('pw2')
        name = request.form.get('name')

        if not userid or not userpw or not userpw2 or not name:
            flash('필수값을 모두 입력해주세요.', 'danger')
            return redirect(url_for('register'))

        if userpw != userpw2:
            flash('입력한 비밀번호가 일치하지 않습니다.', 'danger')
            return redirect(url_for('register'))

        if get_user_by_username(userid):
            flash('이미 존재하는 사용자 아이디입니다.', 'danger')
            return redirect(url_for('register'))

        create(userid, userpw, name)
        flash('회원 가입이 완료되었습니다.', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session.get('user', None)
        return render_template('user.html', user=user)
    flash('비정상 접근입니다.', 'warning')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('정상적으로 로그아웃되었습니다.', 'success')
    else:
        flash('비정상 접근입니다.', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)