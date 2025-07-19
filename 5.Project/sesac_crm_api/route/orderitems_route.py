from flask import request, Blueprint, jsonify, send_file
import database.orderitem as orderitemdb
from common.pagination import pagination, PAGE_SIZE

orderitem_bp = Blueprint('orderitems', __name__)


@orderitem_bp.route('/')
def order_list():
    return send_file('static/html/orderitems.html')


@orderitem_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    orderitems = orderitemdb.get_all_list(page, PAGE_SIZE)

    if orderitems:
        last_page = pagination(orderitems)

    return jsonify({'data':orderitems['data'], 'lastPage':last_page})
