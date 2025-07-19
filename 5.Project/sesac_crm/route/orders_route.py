from flask import render_template, request, Blueprint
import database.order as orderdb
from common.pagination import pagination, PAGE_SIZE

order_bp = Blueprint('orders', __name__)

@order_bp.route('/')
def list():
    page = int(request.args.get('page', default=1))
    pages = [1]
    last_page = 1

    orders = orderdb.get_all_list(page, PAGE_SIZE)

    if orders:
        pages = pagination(page, orders)['pages']
        last_page = pagination(page, orders)['totalPage']

    return render_template('orders.html', orders=orders, currentPage=page, pages=pages, lastPage=last_page)

@order_bp.route('/detail/<id>')
def detail(id):
    orderinfo = orderdb.get_order_summary(id)
    order_items = orderdb.get_orderitems(id)
    total_price = orderdb.get_total_price(id)
    return render_template('order_detail.html', order=orderinfo, orderItems=order_items, totalPrice=total_price)