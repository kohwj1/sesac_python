from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render_template('index2.html', names = users) #템플릿이라는 폴더 안에 들어있어야 정상 동작!

if __name__ == '__main__':
    app.run(debug=True)