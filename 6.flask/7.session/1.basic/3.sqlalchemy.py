from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'my-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

@app.route('/')
def get_session():
    if 'username' in session:
        return f"<p>session info: {session['username']}</p><a href='/clear'>logout</a>"
    return f'no session'

@app.route('/set/<username>')
def set_session(username):
    session['username'] = username
    return 'session has been saved'

@app.route('/clear')
def del_session():
    session.pop('username', None)
    return "<p>session deleted</p><a href='/'>main</a>"

if __name__ == '__main__':
    app.run(debug=True)