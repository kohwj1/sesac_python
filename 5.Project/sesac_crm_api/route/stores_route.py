from flask import request, Blueprint, send_file, jsonify
import database.query.store as storedb
from route.util.pagination import PAGE_SIZE, pagination

store_bp = Blueprint('stores', __name__)

@store_bp.route('/')
def page_store_list():
    return send_file('static/stores/stores.html')


@store_bp.route('/detail')
def page_store_detail():
    return send_file('static/stores/store_detail.html')


@store_bp.route('/create')
def page_store_create():
    return send_file('static/stores/store_create.html')


@store_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    q = request.args.get('q', default='')

    if q:
        stores = storedb.get_list_by_keyword(page, PAGE_SIZE, q)
    else:
        stores = storedb.get_list(page, PAGE_SIZE)

    if stores:
        last_page = pagination(stores)

    return jsonify({'data':stores['data'], 'lastPage':last_page})

@store_bp.route('/api/summary/<id>')
def summary(id):
    storeinfo = storedb.get_store_summary(id)
    return jsonify(storeinfo)

@store_bp.route('/api/sales_monthly/<id>')
def sales_monthly(id):
    month_filter = request.args.get('month', default='')
    if month_filter:
        sale_list = storedb.get_filtered_sales(id, month_filter)
    else:
        sale_list = storedb.get_sales(id)
    return jsonify({'data':sale_list})

@store_bp.route('/api/regulars/<id>')
def regulars(id):
    month_filter = request.args.get('month', default='')
    if month_filter:
        regulars = storedb.get_filtered_regulars(id, month_filter)
    else:
        regulars = storedb.get_regulars(id)
    return jsonify({'data':regulars})

@store_bp.route('/api/type')
def store_type():
    type_list = storedb.get_store_type()
    return jsonify({'data':type_list})

@store_bp.route('/api/unique')
def list_unique():
    unique_list = storedb.get_list_unique()
    return jsonify({'data':unique_list})

@store_bp.route('/api/create', methods=['POST'])
def store_create():
    StoreName = request.form.get('StoreName')
    Type = request.form.get('Type')
    Address = request.form.get('Address')

    result = storedb.create_store(StoreName, Type, Address)
    return jsonify({'isCreated':result['isCreated'], 'StoreId': result['newId']})