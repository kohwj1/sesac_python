from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id
    if request.method == 'POST':
        username = request.form.get('username')
        age = int(request.form.get('age'))

        db.insert_user(username, age)

        return redirect('/')
    return render_template('index.html', users=db.get_users())

@app.route('/delete/<int:user_id>')
def delete_user(user_id):    
    db.delete_user_by_id(user_id)
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):   
    user = db.get_user(user_id)

    if user:
        if request.method == 'POST' :
            username = request.form.get('username') 
            age = int(request.form.get('age'))
            db.update_user(user_id, username, age)
            return redirect('/')
        else:
            return render_template('update_user.html', user=user)
    
    return '사용자를 찾을 수 없습니다.'

if __name__ == '__main__':
    db.create_table()
    app.run(debug=True) #디버그 모드가 켜져 있다면 두 번 호출될 수 있다! 주의