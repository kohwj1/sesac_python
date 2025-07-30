from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = 'my-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

@app.route('/')
def get_session():
    logout = ''
    stored_session_data = get_session_data(session.sid)
    stored_session_str = json.dumps(stored_session_data, indent=4)

    if stored_session_data:
        logout = '<a href="/clear">Logout</a>'

    return f'<p>stored info: {stored_session_str}</p>{logout}'

def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data and session_data.data:
        return json.loads(session_data.data)
    return {}

@app.route('/set/<username>')
def set_session(username):
    session['username'] = username
    session['count'] = 42
    session['my_list'] = ['red', 'green', 'blue']

    session_store(session.sid, dict(session))
    
    return 'session has been saved'

def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id=sid)

    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()

class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    data = db.Column(db.Text)

@app.route('/clear')
def del_session():
    # session.pop('username', None)
    # session_data = SessionData.query.get(sid)
    # session.pop(session_data, None)
    return "<p>session deleted</p><a href='/'>main</a>"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)