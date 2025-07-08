from flask import Flask, render_template

app = Flask(__name__)

# static 폴더를 다른 이름으로 지정할 수는 있지만 특별한 이유가 있지 않은 한 굳이 변경할 필요는 없음
# static이라고 폴더명을 지정해주며, 자동으로 외부에 노출됨 (img, html, )
# 템플릿 내에서 static 경로를 하드코딩해도 동작은 하지만, url_for('static', filename='') 으로 진자 템플릿을 통해 넘기는 구조가 더 좋다

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)