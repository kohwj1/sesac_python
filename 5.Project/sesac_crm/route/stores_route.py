from flask import render_template, request, Blueprint
import database.store_database as storedb
from common.pagination import PAGE_SIZE, pagination

store_bp = Blueprint('stores', __name__)

@store_bp.route('/')
def store_list():
    page = int(request.args.get('page', default=1))
    q = request.args.get('q', default='')
    pages = [0]
    lastpage = 1

    if q:
        stores = storedb.search_stores(q, page, PAGE_SIZE)
    else:
        stores = storedb.get_all_list(page, PAGE_SIZE)

    if stores:
        pages = pagination(page, stores)['pages']
        total_page = pagination(page, stores)['totalPage']

    return render_template('stores.html', stores=stores, currentPage=page, pages=pages, totalPage=total_page, q=q)

@store_bp.route('/detail/<storeid>')
def store_detail(storeid):
    month_filter = request.args.get('month', default='')
    store_info = storedb.get_store_summary(storeid)
    regular_limit = 10

    if month_filter:
        sales = storedb.get_daily_sales(storeid, month_filter)
        regulars = storedb.get_daily_regulars(storeid, month_filter, regular_limit)
    else:
        sales = storedb.get_sales(storeid)
        regulars = storedb.get_regulars(storeid, regular_limit)

    return render_template('store_detail.html', store=store_info, sales=sales, regulars=regulars, limit=regular_limit, isFiltered=bool(month_filter))