from flask import Flask, render_template, request, redirect, url_for
from common import add_todo, delete_todo, get_all_list, switch_todo

app = Flask(__name__)

@app.route('/')
def index():
    # print(get_all_list())
    return render_template('todo.html', todolist=get_all_list())

@app.route('/add', methods=['POST'])
def add_item():
    content = request.form.get('userInput')
    add_todo(content)
    return redirect(url_for('index'))

@app.route('/update/<idx>', methods=['POST'])
def update_item(idx):
    switch_todo(idx)
    return redirect(url_for('index'))

@app.route('/delete/<idx>', methods=['POST'])
def delete_item(idx):
    delete_todo(idx)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5500)