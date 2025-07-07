from flask import Flask, render_template, request

app = Flask(__name__)
users = [ {'id':i, 'name':f'user{i}', 'age':20 + (i % 10), 'phone':f'050-0000-{str(i).zfill(4)}'} for i in range(1, 101)]

#https://localhost:5000/?page=1
@app.route('/')
def index():
    page = request.args.get('page', default='')
    page_prev = '?page=1'
    page_next = '?page=2'
    filtered_users = users

    if page:
        page = int(page)
        page_prev = f'?page={page - 1}'
        page_next = f'?page={page + 1}'
        filtered_users = [user for user in users if users.index(user) // 10 == page - 1]

    return render_template('users.html', users=filtered_users, page=page, page_prev=page_prev, page_next=page_next)

if __name__ == '__main__':
    app.run(debug=True)