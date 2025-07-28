from flask import request, Blueprint, jsonify, send_file
import database.query.order as orderdb
from route.util.pagination import PAGE_SIZE, pagination

order_bp = Blueprint('orders', __name__)

@order_bp.route('/')
def page_order_list():
    return send_file('static/orders/orders.html')

@order_bp.route('/detail')
def page_order_detail():
    return send_file('static/orders/order_detail.html')

@order_bp.route('/create')
def page_order_create():
    return send_file('static/orders/order_create.html')

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
        orders = orderdb.get_list(page, PAGE_SIZE)

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

@order_bp.route('/api/create', methods=['POST'])
def order_create():
    order_at = request.form.get('OrderAt')
    user_id = request.form.get('UserId')
    store_id = request.form.get('StoreId')
    item_id = request.form.getlist('ItemId')
    isCreated = orderdb.create_order(order_at, user_id, store_id, item_id)
    return jsonify({'isCreated':isCreated[0], 'OrderId': isCreated[1]})

@order_bp.route('/api/delete/<id>', methods=['DELETE'])
def order_delete(id):
    isDeleted = orderdb.delete_order(id)
    return jsonify({'isDeleted':isDeleted})