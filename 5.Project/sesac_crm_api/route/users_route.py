from flask import request, Blueprint, send_file, jsonify
import database.query.user as userdb
from route.util.pagination import PAGE_SIZE, pagination
import html

user_bp = Blueprint('users', __name__)


@user_bp.route('/')
def page_user_list():
    return send_file('static/users/users.html')


@user_bp.route('/detail')
def page_user_detail():
    return send_file('static/users/user_detail.html')

@user_bp.route('/create')
def page_user_create():
    return send_file('static/users/user_create.html')


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
        users = userdb.get_list(page, PAGE_SIZE)
    
    if users:
        last_page = pagination(users)

    return jsonify({'data':users['data'], 'lastPage':last_page})

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

@user_bp.route('/api/create', methods=['POST'])
def user_create():
    #html.escape를 이용하여 text필드 XSS 1차 방어 처리
    UserName = html.escape(request.form.get('UserName', default=''))
    Birthdate = request.form.get('Birthdate', default='')
    Gender = request.form.get('Gender', default='')
    Address = html.escape(request.form.get('Address', default=''))

    try:
        #나이 숫자 캐스팅 가능 여부 체크
        Age = int(request.form.get('Age', default=0))
        #필수값 입력 여부 체크
        if UserName and Birthdate and Age and Gender and Address:
            result = userdb.create_user(UserName, Birthdate, Age, Gender, Address)
            is_created = result['isCreated']
            new_id = result['newId']
            msg = 'success'

    except ValueError:
            is_created = False
            new_id = None
            msg = '나이는 숫자만 입력할 수 있습니다.'
    
    finally:
        return jsonify({'isCreated':is_created, 'msg': msg, 'UserId':new_id})