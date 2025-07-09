from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

    #1. 사용자 최소 3명 이상(이름, 아이디, 암호)
    #2. 로그인에서 ID/PW 체크
    #3. 로그인 성공 시 user 페이지로 리다이렉트 -- 실패 시 로그인 실패라고 출력하기
USERS =[
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('name')
        print(f'입력된 이름은 {user}')
        return redirect(url_for('user'), user=user)
        # return render_template('user.html', user=user)
    return render_template('login.html')

@app.route('/user')
@app.route('/user/<user>')
def user(user=None):
    return render_template('user.hmtl', user=user)

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)