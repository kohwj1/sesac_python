from flask import request, Blueprint, send_file, jsonify
import database.store as storedb
from common.pagination import PAGE_SIZE, pagination

store_bp = Blueprint('stores', __name__)

@store_bp.route('/')
def store_list():
    return send_file('static/html/stores.html')


@store_bp.route('/detail')
def store_detail():
    return send_file('static/html/store_detail.html')


@store_bp.route('/api/list')
def list():
    page = int(request.args.get('page', default=1))
    q = request.args.get('q', default='')

    if q:
        stores = storedb.get_list_by_keyword(page, PAGE_SIZE, q)
    else:
        stores = storedb.get_all_list(page, PAGE_SIZE)

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