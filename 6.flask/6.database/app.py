from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = []
next_id = 1


@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id
    if request.method == 'POST':
        username = request.form.get('username')
        age = int(request.form.get('age'))

        users.append({'id':next_id, 'name':username, 'age':age})
        next_id += 1

        return redirect('/')
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):    
    for u in users:
        if u['id'] == user_id:
            users.remove(u)
            break
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):   
    user = next((u for u in users if u['id'] == user_id), None) #파이썬 제너레이터
    
    if request.method == 'POST' :
        username = request.form.get('username') 
        age = int(request.form.get('age'))
        user['name'] = username
        user['age'] = age
        return redirect('/')

    else:
        return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)