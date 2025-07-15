from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagesize = 20
    # first_page = 1
    last_page = db.get_usercount() // pagesize

    list_start = 1
    list_end = list_start + 10

    pagelist = [i for i in range(list_start, list_end)]
    users = db.get_users_per_page(page, pagesize)
    return render_template('index.html', users=users, pages=pagelist, liststart=list_start, lastpage=last_page)

if __name__ == '__main__':
    app.run(debug=True)