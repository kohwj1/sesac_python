from flask import render_template, request, Blueprint
import database.order as orderdb
from common.pagination import pagination, PAGE_SIZE

order_bp = Blueprint('orders', __name__)

@order_bp.route('/')
def list():
    page = int(request.args.get('page', default=1))
    month = request.args.get('month', default='')
    name = request.args.get('name', default='')
    pages = [1]
    last_page = 1

    if month and name:
        orders = orderdb.get_list_by_storename_month(page, PAGE_SIZE, name, month)
    elif month:
        orders = orderdb.get_list_by_month(page, PAGE_SIZE, month)
    elif name:
        orders = orderdb.get_list_by_storename(page, PAGE_SIZE, name)
        print(orders)
    else:
        orders = orderdb.get_all_list(page, PAGE_SIZE)

    if orders:
        pages = pagination(page, orders)['pages']
        last_page = pagination(page, orders)['totalPage']

    return render_template('orders/orders.html', orders=orders, currentPage=page, pages=pages, lastPage=last_page, name=name, month=month)

@order_bp.route('/detail/<id>')
def detail(id):
    orderinfo = orderdb.get_order_summary(id)
    order_items = orderdb.get_orderitems(id)
    total_price = orderdb.get_total_price(id)
    return render_template('orders/order_detail.html', order=orderinfo, orderItems=order_items, totalPrice=total_price)