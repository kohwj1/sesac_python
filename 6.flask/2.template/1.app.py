from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') #템플릿이라는 폴더 안에 들어있어야 정상 동작!

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True, port=5000)