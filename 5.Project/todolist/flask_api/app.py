from flask import Flask, request, jsonify, send_file
from common import add_todo, delete_todo, get_all_list, switch_todo

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('static/todo.html')

@app.route('/api/list')
def get_list():
    mylist = get_all_list()
    return jsonify({'data':mylist})

@app.route('/api/add', methods=['POST'])
def item_add():
    todo = request.form.get('userInput')
    add_todo(todo)
    return jsonify({'result':0,'data':get_all_list()})


@app.route('/api/update/<idx>', methods=['PUT'])
def item_update(idx):
    switch_todo(idx)
    return jsonify({'result':0,'data':get_all_list()})


@app.route('/api/delete/<idx>', methods=['DELETE'])
def item_delete(idx):
    delete_todo(idx)
    return jsonify({'result':0,'data':get_all_list()})

if __name__ == '__main__':
    app.run(debug=True)