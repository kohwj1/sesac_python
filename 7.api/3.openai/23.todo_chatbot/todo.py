from dotenv import load_dotenv
from flask import request, jsonify, Blueprint

load_dotenv()

todo_bp = Blueprint('todo', __name__)

todos = []
idx = 0

@todo_bp.route('/api/todo', methods=['GET'])
def get_list():
    return jsonify({'status':'success', 'data': todos}), 200

@todo_bp.route('/api/todo', methods=['POST'])
def add_todo():
    new_todo = request.form.get('todo')

    if new_todo:
        global idx
        idx += 1
        todos.append({'idx':idx, 'item':new_todo})
        return jsonify({'status':'success', 'idx': idx}), 201
    return jsonify({'status':'error', 'msg': '할일을 입력해주세요.'}), 400

@todo_bp.route('/api/todo', methods=['PUT'])
def update_todo():
    try: 
        data = request.get_json()
        todo_id = data.get('todo_id')
        new_todo = data.get('new_todo')
        todos[todo_id] = new_todo
    except IndexError:
        return jsonify({'status':'error','msg':'이미 삭제되었습니다.'}), 404
    return jsonify({'msg':'success'})

@todo_bp.route('/api/todo/<int:idx>', methods=['DELETE'])
def delete_todo(idx):
    for i, item in enumerate(todos):
        if item['idx'] == idx:
            todos.pop(i)
            break;
    return jsonify({'status':'success'}), 200