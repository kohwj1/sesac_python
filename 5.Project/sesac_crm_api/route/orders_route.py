from flask import request, Blueprint, jsonify, send_file
import database.order as orderdb
from common.pagination import pagination, PAGE_SIZE

order_bp = Blueprint('orders', __name__)

@order_bp.route('/')
def order_list():
    return send_file('static/orders/orders.html')


@order_bp.route('/detail')
def order_detail():
    return send_file('static/orders/order_detail.html')


@order_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    store_name = request.args.get('name', default='')
    month = request.args.get('month', default='')

    if store_name and month:
        orders = orderdb.get_list_by_storename_month(store_name, month, page, PAGE_SIZE)
    elif store_name:
        orders = orderdb.get_list_by_storename(store_name, page, PAGE_SIZE)
    elif month:
        orders = orderdb.get_list_by_month(month, page, PAGE_SIZE)
    else:
        orders = orderdb.get_all_list(page, PAGE_SIZE)

    if orders:
        last_page = pagination(orders)

    return jsonify({'data':orders['data'], 'lastPage':last_page})

@order_bp.route('/api/summary/<id>')
def summary(id):
    orderinfo = orderdb.get_order_summary(id)
    return jsonify(orderinfo)

@order_bp.route('/api/orderitems/<id>')
def order_items(id):
    order_items = orderdb.get_orderitems(id)
    return jsonify({'data':order_items})