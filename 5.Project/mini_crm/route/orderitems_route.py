from flask import render_template, request, Blueprint
import database.orderitem as orderitemdb
from common.pagination import pagination, PAGE_SIZE

orderitem_bp = Blueprint('orderitems', __name__)

@orderitem_bp.route('/')
def list():
    page = int(request.args.get('page', default=1))
    pages = [1]
    last_page = 1

    orderitems = orderitemdb.get_all_list(page, PAGE_SIZE)

    if orderitems:
        pages = pagination(page, orderitems)['pages']
        last_page = pagination(page, orderitems)['totalPage']

    return render_template('orderitems/orderitems.html', orderitems=orderitems, currentPage=page, pages=pages, lastPage=last_page)