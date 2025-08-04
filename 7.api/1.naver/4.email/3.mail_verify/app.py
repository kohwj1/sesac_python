from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import random, datetime

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('NAVER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('NAVER_PASSWORD')
app.config['MAIL_SERVER'] = os.getenv('SMTP_SERVER')
app.config['MAIL_PORT'] = os.getenv('SMTP_PORT')

mail = Mail(app)

def create_code():
    code = str(random.randint(1, 999999)).zfill(6)
    return code

def create_temp_pw():
    code = str(random.randint(1, 999999)).zfill(6)
    return code

def send_email(recipient, task, code):
    if task == 'join':
        form_text = '회원가입'
    elif task == 'reset':
        form_text = '비밀번호 초기화'
    
    try:
        msg = Message(
            subject = f'[TEST] {form_text} 인증 메일',
            body = f'{form_text} 진행을 위해 다음 인증코드를 입력해주세요: {code}',
            recipients = [recipient],
            sender = ('message from P', app.config['MAIL_USERNAME'])
        )
        mail.send(msg)
        return True
    
    except Exception as e:
        print(e)
        return False

@app.before_request
def expire_session():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=2)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.form.get('email')
    task = request.form.get('task')
    code = create_code()
    # print(email, code)

    send_result = send_email(email, task, code)

    if send_result:
        session['email'] = email
        session['code'] = code
        return jsonify({'msg':'인증 메일을 발송하였습니다.'}), 200
    return jsonify({'msg':'인증 메일 발송에 실패하였습니다.'}), 500


@app.route('/verify-code', methods=['POST'])
def vefiry_code():
    verified_email = session.get('email')
    session_code = session.get('code')
    input_email = request.form.get('email')
    input_code = request.form.get('code')

    if not input_email:
        return jsonify({'msg':'이메일을 입력해주세요'}), 400
    if not input_code:
        return jsonify({'msg':'인증번호를 입력해주세요'}), 401
    if not session_code:
        return jsonify({'msg':'인증코드가 만료되었습니다. 페이지 새로고침 후 다시 진행해 주세요.'}), 403
    if verified_email != input_email:
        return jsonify({'msg':'인증한 메일주소와 현재 메일주소가 일치하지 않습니다. 다시 입력해주세요.'}), 403
    if session_code != input_code:
        return jsonify({'msg':'인증번호가 일치하지 않습니다. 다시 입력해주세요.'}), 403
    session['is_verified'] = True
    return jsonify({'msg':'인증코드와 일치'}), 200

@app.route('/signup', methods=['POST'])
def signup():
    verified_email = session.get('email')
    session_code = session.get('code')
    input_id = request.form.get('userid')
    input_email = request.form.get('email')
    input_code = request.form.get('code')

    if not input_id:
        return jsonify({'msg':'아이디를 입력해주세요'}), 400
    if not input_email:
        return jsonify({'msg':'이메일을 입력해주세요'}), 400
    if not input_code:
        return jsonify({'msg':'인증번호를 입력해주세요'}), 401
    if not session_code:
        return jsonify({'msg':'인증코드가 만료되었습니다. 페이지 새로고침 후 다시 진행해 주세요.'}), 403
    if verified_email != input_email:
        return jsonify({'msg':'인증한 메일주소와 현재 메일주소가 일치하지 않습니다. 다시 입력해주세요.'}), 403
    if session_code != input_code:
        return jsonify({'msg':'인증번호가 일치하지 않습니다. 다시 입력해주세요.'}), 403
    if not session['is_verified']:
        return jsonify({'msg':'인증을 완료해주세요.'}), 403
    return jsonify({'msg':f'회원 가입 성공! {input_id} 회원님, 환영합니다.'}), 200

@app.route('/reset-pw', methods=['GET', 'POST'])
def reset_pw():
    if request.method == 'POST':
        verified_email = session.get('email')
        session_code = session.get('code')
        input_email = request.form.get('email')
        input_code = request.form.get('code')
        input_pw = request.form.get('password')
        if not input_email:
            return jsonify({'msg':'이메일을 입력해주세요'}), 400
        if not input_code:
            return jsonify({'msg':'인증번호를 입력해주세요'}), 401
        if not session_code:
            return jsonify({'msg':'인증코드가 만료되었습니다. 페이지 새로고침 후 다시 진행해 주세요.'}), 403
        if verified_email != input_email:
            return jsonify({'msg':'인증한 메일주소와 현재 메일주소가 일치하지 않습니다. 다시 입력해주세요.'}), 403
        if session_code != input_code:
            return jsonify({'msg':'인증번호가 일치하지 않습니다. 다시 입력해주세요.'}), 403
        if not session['is_verified']:
            return jsonify({'msg':'인증을 완료해주세요.'}), 403
        return jsonify({'msg':f'개인정보가 수정되었습니다. 변경된 비밀번호: {input_pw}'}), 200
    return render_template('resetpw.html')

if __name__ == '__main__':
    app.run(debug=True)