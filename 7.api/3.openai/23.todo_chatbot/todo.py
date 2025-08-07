from dotenv import load_dotenv
from flask import request, jsonify, Blueprint

load_dotenv()

todo_bp = Blueprint('todo', __name__)

todos = []
idx = 0

@todo_bp.route('/api/todo', methods=['GET'])
def get_list():
    return jsonify({'result':'success', 'data':todos}), 200

@todo_bp.route('/api/todo', methods=['POST'])
def add_todo():
    new_todo = request.get_json().get('task')

    if new_todo:
        global idx
        idx += 1
        todos.append({'idx':idx, 'task':new_todo, 'status':False})
        return jsonify({'result':'success', 'idx':idx}), 201
    return jsonify({'result':'error', 'msg':'할 일을 입력해주세요.'}), 400


@todo_bp.route('/api/todo/<int:idx>', methods=['PUT'])
def update_todo(idx):
    try:
        for i, item in enumerate(todos):
            if item['idx'] == idx:
                todos[i]['status'] = not item['status']
                return jsonify({'result':'success', 'status':todos[i]['status']}), 200
    except IndexError as e:
        print(e)
    return jsonify({'status':'error','msg':'아이템이 존재하지 않습니다.'}), 404


@todo_bp.route('/api/todo/<int:idx>', methods=['DELETE'])
def delete_todo(idx):
    for i, item in enumerate(todos):
        if item['idx'] == idx:
            todos.pop(i)
            return jsonify({'result':'success'}), 200
    return jsonify({'result':'error','msg':'아이템이 존재하지 않습니다.'}), 404