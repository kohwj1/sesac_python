from flask import Flask, render_template, request, redirect
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db.init_app(app)

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
#     db.init_app(app)
#     return app

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print(f'사용자 {user_id} 없음')
    return redirect('/')

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)