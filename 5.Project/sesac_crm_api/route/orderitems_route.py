from flask import request, Blueprint, jsonify, send_file
import database.query.orderitem as orderitemdb
from route.util.pagination import PAGE_SIZE, pagination

orderitem_bp = Blueprint('orderitems', __name__)


@orderitem_bp.route('/')
def page_order_list():
    return send_file('static/orderitems/orderitems.html')


@orderitem_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    orderitems = orderitemdb.get_list(page, PAGE_SIZE)

    if orderitems:
        last_page = pagination(orderitems)

    return jsonify({'data':orderitems['data'], 'lastPage':last_page})
