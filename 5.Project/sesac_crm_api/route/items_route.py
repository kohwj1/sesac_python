from flask import request, Blueprint, jsonify, send_file
import database.query.item as itemdb
from route.util.pagination import PAGE_SIZE, pagination

item_bp = Blueprint('items', __name__)

@item_bp.route('/')
def page_order_list():
    return send_file('static/items/items.html')

@item_bp.route('/detail')
def page_order_detail():
    return send_file('static/items/item_detail.html')

@item_bp.route('/create')
def page_item_create():
    return send_file('static/items/item_create.html')

@item_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    item_name = request.args.get('name', default='').title()

    if item_name:
        items = itemdb.get_list_by_itemname(item_name, page, PAGE_SIZE)
    else:
        items = itemdb.get_list(page, PAGE_SIZE)


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

@item_bp.route('/api/type')
def item_type():
    type_list = itemdb.get_item_type()
    return jsonify({'data':type_list})

@item_bp.route('/api/unique')
def list_unique():
    unique_list = itemdb.get_list_unique()
    return jsonify({'data':unique_list})

@item_bp.route('/api/create', methods=['POST'])
def item_create():
    ItemName = request.form.get('ItemName')
    Type = request.form.get('Type')
    UnitPrice = int(request.form.get('UnitPrice'))

    result = itemdb.create_item(ItemName, Type, UnitPrice)
    return jsonify({'isCreated':result['isCreated'], 'ItemId': result['newId']})