from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # name = request.args.get('name') args = 쿼리 파라미터 파싱
    name = request.form.get('name') #body 파라미터 파싱
    age = request.form.get('age') #body 파라미터 파싱
    return f'안녕하세요, {age}세 {name}님'

if __name__ == '__main__':
    app.run(debug=True)