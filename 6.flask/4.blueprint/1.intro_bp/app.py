from flask import Flask, render_template, request
from user_route import user_bp
from admin_route import admin_bp

app = Flask(__name__)

#app에 만들어둔 블루프린트를 등록

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)