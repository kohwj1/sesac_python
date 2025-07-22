from flask import render_template, request, Blueprint
import database.user as userdb
from common.pagination import PAGE_SIZE, pagination

user_bp = Blueprint('users', __name__)

@user_bp.route('/')
def list():
    name = request.args.get('name', default='')
    gender = request.args.get('gender', default='')
    page = int(request.args.get('page', default=1))
    pages = [1]
    last_page = 1

    if name and gender:
        users = [u for u in userdb.search_users_by_name_and_gender(name, gender, page, PAGE_SIZE) if u['Gender'] == gender]
    elif name:
        users = userdb.search_users_by_name(name, page, PAGE_SIZE)
    elif gender:
        users = userdb.search_users_by_gender(gender, page, PAGE_SIZE)
    else:
        users = userdb.get_all_list(page, PAGE_SIZE)

    if users:
        pages = pagination(page, users)['pages']
        last_page = pagination(page, users)['totalPage']

    return render_template('users/users.html', users=users, name=name, gender=gender, currentPage=page, pages=pages, lastPage=last_page)

@user_bp.route('/detail/<id>')
def detail(id):
    userinfo = userdb.get_user_summary(id)
    orderlist = userdb.get_user_history(id)
    regulars = userdb.get_regular_store(id)
    favorites = userdb.get_favorite_items(id)

    return render_template('users/user_detail.html', user=userinfo, orderList=orderlist, regulars=regulars, favorites=favorites)