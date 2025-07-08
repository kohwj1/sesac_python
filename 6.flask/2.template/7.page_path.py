from flask import Flask, render_template

app = Flask(__name__)
users = [ {'id':i, 'name':f'user{i}', 'age':20 + (i % 10), 'phone':f'050-0000-{str(i).zfill(4)}'} for i in range(1, 101)]

#https://localhost:5000/pages/1
@app.route('/')
def index():
    page = ''
    page_prev = '/pages/1'
    page_next = '/pages/2'
    filtered_users = users
    return render_template('users.html', users=filtered_users, page=page, page_prev=page_prev, page_next=page_next)

@app.route('/pages/<int:num>')
def pages(num):
    page = int(num)
    page_size = 10
    page_prev = f'/pages/{page - 1}'
    page_next = f'/pages/{page + 1}'
    start = page_size * (page - 1)
    end = start + page_size
    filtered_users = users[start:end]
    return render_template('users.html', users=filtered_users, page=page, page_prev=page_prev, page_next=page_next)

if __name__ == '__main__':
    app.run(debug=True)