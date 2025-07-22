from flask import request, Blueprint, jsonify, send_file
import database.item as itemdb
from common.pagination import pagination, PAGE_SIZE

item_bp = Blueprint('items', __name__)

@item_bp.route('/')
def order_list():
    return send_file('static/items/items.html')


@item_bp.route('/detail')
def order_detail():
    return send_file('static/items/item_detail.html')


@item_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    item_name = request.args.get('name', default='').title()

    if item_name:
        items = itemdb.get_list_by_itemname(item_name, page, PAGE_SIZE)
    else:
        items = itemdb.get_all_list(page, PAGE_SIZE)


    if items:
        last_page = pagination(items)

    return jsonify({'data':items['data'], 'lastPage':last_page})

@item_bp.route('/api/summary/<id>')
def summary(id):
    iteminfo = itemdb.get_item_summary(id)
    return jsonify(iteminfo)

@item_bp.route('/api/sales_monthly/<id>')
def monthly_sales(id):
    monthly_sales = itemdb.get_monthly_sales(id)
    return jsonify({'data':monthly_sales})