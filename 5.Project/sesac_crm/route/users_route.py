from flask import render_template, request, Blueprint
import database.user_database as userdb

user_bp = Blueprint('users', __name__)

@user_bp.route('/')
def user_list():
    name = request.args.get('name', default='')
    gender = request.args.get('gender', default='')
    page = int(request.args.get('page', default=1))
    pagesize = 20
    pagination_size = 10
    pages = 0
    totalpage = 0
    total_count = 0

    if name and gender:
        users = [u for u in userdb.search_users_by_name_and_gender(name, gender, page, pagesize) if u['Gender'] == gender]
    elif name:
        users = userdb.search_users_by_name(name, page, pagesize)
    elif gender:
        users = userdb.search_users_by_gender(gender, page, pagesize)
    else:
        users = userdb.get_all_list(page, pagesize)

    if users:
        total_count = users[0]['Totalcount']
        totalpage = (total_count - 1) // pagesize + 1
        page_start = ((page - 1) // pagination_size) * pagination_size + 1
        page_end = min(page_start + pagination_size, totalpage + 1)
        print(total_count, totalpage, page_start, page_end)
        pages = [i for i in range(page_start, page_end)]

    return render_template('users.html', users=users, name=name, gender=gender, currentPage=page, pages=pages, totalPage=totalpage)

@user_bp.route('/detail/<userid>')
def user_detail(userid):
    userinfo = userdb.get_user_summary(userid)
    orderlist = userdb.get_user_history(userid)

    return render_template('user_detail.html', user=userinfo, orderlist=orderlist)