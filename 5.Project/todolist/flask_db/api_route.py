from flask import request, jsonify, Blueprint
from common import add_todo, delete_todo, get_all_list, switch_todo

api_bp = Blueprint('api', __name__)

@api_bp.route('/list')
def get_list():
    mylist = get_all_list()
    # print(mylist)
    return jsonify({'data':mylist})

@api_bp.route('/add', methods=['POST'])
def item_add():
    todo = request.form.get('userInput')
    duedate = request.form.get('dateInput')
    add_todo(todo, duedate)
    return jsonify({'result':0,'data':get_all_list()})


@api_bp.route('/update/<idx>', methods=['PUT'])
def item_update(idx):
    switch_todo(idx)
    return jsonify({'result':0,'data':get_all_list()})


@api_bp.route('/delete/<idx>', methods=['DELETE'])
def item_delete(idx):
    delete_todo(idx)
    return jsonify({'result':0,'data':get_all_list()})