from dotenv import load_dotenv
from flask import request, jsonify, Blueprint
from services import todo_service as svc

load_dotenv()

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('', methods=['GET'])
def get_list():
    return jsonify({'result':'success', 'data':svc.get_all()}), 200

@todo_bp.route('', methods=['POST'])
def add_todo():
    new_todo = request.get_json().get('task')

    if new_todo:
        new_index = svc.add(new_todo)
        return jsonify({'result':'success', 'idx':new_index}), 201
    return jsonify({'result':'error', 'msg':'할 일을 입력해주세요.'}), 400


@todo_bp.route('/<int:idx>', methods=['PUT'])
def update_todo(idx):
    try:
        res = svc.toggle(idx)
        return jsonify(res), 200
    except IndexError as e:
        print(e)
    return jsonify(res), 404


@todo_bp.route('/<int:idx>', methods=['DELETE'])
def delete_todo(idx):
    try:
        res = svc.delete(idx)
        return jsonify(res), 200
    except IndexError as e:
        print(e)
    return jsonify(res), 404