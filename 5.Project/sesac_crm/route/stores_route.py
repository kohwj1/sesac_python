from flask import render_template, request, Blueprint
import database.store_database as storedb

store_bp = Blueprint('stores', __name__)

@store_bp.route('/')
def store_list():
    page = int(request.args.get('page', default=1))
    pagesize = 20
    pagination_size = 10
    total_count = 0

    stores = storedb.get_all_list(page, pagesize)

    if stores:
        total_count = stores[0]['Totalcount']
        total_page = (total_count - 1) // pagesize + 1

        page_start = ((page - 1) // pagination_size) * pagination_size + 1
        page_end = min(page_start + pagination_size, total_page + 1)
        print(total_count, total_page, page_start, page_end)
        pages = [i for i in range(page_start, page_end)]

    return render_template('stores.html', stores=stores, currentPage=page, pages=pages, totalPage=total_page)

@store_bp.route('/detail/<storeid>')
def store_detail(storeid):
    month_filter = request.args.get('month', default='')
    storeinfo = storedb.get_store_summary(storeid)
    regular_limit = 10

    if month_filter:
        sales = storedb.get_daily_sales(storeid, month_filter)
        regulars = storedb.get_daily_regulars(storeid, month_filter, regular_limit)
    else:
        sales = storedb.get_sales(storeid)
        regulars = storedb.get_regulars(storeid, regular_limit)

    return render_template('store_detail.html', store=storeinfo, sales=sales, regulars=regulars, limit=regular_limit, is_filtered=bool(month_filter))