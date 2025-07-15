from flask import render_template, request, Blueprint
import user_database as userdb

user_bp = Blueprint('users', __name__)

@user_bp.route('/')
def user_list():
    name = request.args.get('name', default='')
    gender = request.args.get('gender', default='')
    page = int(request.args.get('page', default=1))
    pagesize = 30

    if name and gender:
        users = [u for u in userdb.search_users_by_name(name, page, pagesize) if u['Gender'] == gender]
    elif name:
        users = userdb.search_users_by_name(name, page, pagesize)
    elif gender:
        users = userdb.filter_gender(gender, page, pagesize)
    else:
        users = userdb.get_all_list(page, pagesize)

    return render_template('users.html', users=users, name=name, gender=gender, currentpage=page)

@user_bp.route('/detail/<userid>')
def user_detail(userid):
    user = userdb.get_user_info(userid)
    userinfo = user['info']
    orderlist = user['history']

    return render_template('user_detail.html', user=userinfo, orderlist=orderlist)