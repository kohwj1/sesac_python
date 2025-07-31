from flask import render_template, request, Blueprint
import database.store as storedb
from common.pagination import PAGE_SIZE, pagination

store_bp = Blueprint('stores', __name__)

@store_bp.route('/')
def list():
    page = int(request.args.get('page', default=1))
    q = request.args.get('q', default='')
    pages = [1]
    last_page = 1

    if q:
        stores = storedb.search_stores(q, page, PAGE_SIZE)
    else:
        stores = storedb.get_all_list(page, PAGE_SIZE)

    if stores:
        pages = pagination(page, stores)['pages']
        last_page = pagination(page, stores)['totalPage']

    return render_template('stores/stores.html', stores=stores, currentPage=page, pages=pages, lastPage=last_page, q=q)

@store_bp.route('/detail/<id>')
def detail(id):
    month_filter = request.args.get('month', default='')
    store_info = storedb.get_store_summary(id)
    regular_limit = 10

    if month_filter:
        sales = storedb.get_daily_sales(id, month_filter)
        regulars = storedb.get_daily_regulars(id, month_filter, regular_limit)
    else:
        sales = storedb.get_sales(id)
        regulars = storedb.get_regulars(id, regular_limit)

    return render_template('stores/store_detail.html', store=store_info, sales=sales, regulars=regulars, limit=regular_limit, isFiltered=bool(month_filter))