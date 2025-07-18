from flask import request, Blueprint, send_file, jsonify
import database.user as userdb
from common.pagination import PAGE_SIZE, pagination

user_bp = Blueprint('users', __name__)


@user_bp.route('/')
def user_list():
    return send_file('static/html/users.html')


@user_bp.route('/detail')
def user_detail():
    return send_file('static/html/user_detail.html')


@user_bp.route('/api/list')
def list():
    name = request.args.get('name', default='')
    gender = request.args.get('gender', default='')
    page = int(request.args.get('page', default=1))

    if name and gender:
        users = userdb.search_users_by_name_and_gender(name, gender, page, PAGE_SIZE)
    elif name:
        users = userdb.search_users_by_name(name, page, PAGE_SIZE)
    elif gender:
        users = userdb.search_users_by_gender(gender, page, PAGE_SIZE)
    else:
        users = userdb.get_all_list(page, PAGE_SIZE)
    
    if users:
        total_page = pagination(page, users)

    return jsonify({'data':users['data'], 'totalPage':total_page})

@user_bp.route('/api/summary/<id>')
def summary(id):
    userinfo = userdb.get_user_summary(id)
    return jsonify(userinfo)


@user_bp.route('/api/history/<id>')
def hisotry(id):
    hisotry = userdb.get_user_history(id)
    return jsonify({'data':hisotry})


@user_bp.route('/api/regulars/<id>')
def regulars(id):
    regulars = userdb.get_regular_store(id)
    return jsonify({'data':regulars})


@user_bp.route('/api/favorites/<id>')
def favorites(id):
    favorites = userdb.get_favorite_items(id)
    return jsonify({'data':favorites})