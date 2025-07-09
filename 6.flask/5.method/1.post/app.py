from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

    #1. 사용자 최소 3명 이상(이름, 아이디, 암호)
    #2. 로그인에서 ID/PW 체크
    #3. 로그인 성공 시 user 페이지로 리다이렉트 -- 실패 시 로그인 실패라고 출력하기
USERS = {
    'id1': {'password':'test1','name':'김민지'},
    'id2': {'password':'test2','name':'김철수'},
}

def login_check(id, pw):
    try:
        return USERS.get(id)['password'] == pw
    except TypeError:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        # print(f'입력된 이름은 {user}')
        if login_check(id, password):
            return redirect(url_for('user', id=id))
        else:
            msg = '아이디가 존재하지 않거나 비밀번호가 일치하지 않습니다.'
        # return render_template('user.html', user=user)
    return render_template('login.html', msg=msg)

@app.route('/user')
@app.route('/user/<id>')
def user(id=None):
    username = USERS[id]['name']
    return render_template('user.html', id=id, username=username)

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)