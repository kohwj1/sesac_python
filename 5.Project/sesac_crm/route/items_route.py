from flask import render_template, request, Blueprint
import database.item as itemdb

item_bp = Blueprint('items', __name__)

@item_bp.route('/')
def item_list():
    page = int(request.args.get('page', default=1))
    pagesize = 20
    pagination_size = 10
    total_count = 0

    items = itemdb.get_all_list(page, pagesize)

    if items:
        total_count = items[0]['Totalcount']
        total_page = (total_count - 1) // pagesize + 1

        page_start = ((page - 1) // pagination_size) * pagination_size + 1
        page_end = min(page_start + pagination_size, total_page + 1)
        print(total_count, total_page, page_start, page_end)
        pages = [i for i in range(page_start, page_end)]

    return render_template('items.html', items=items, currentPage=page, pages=pages, totalPage=total_page)

@item_bp.route('/detail/<itemid>')
def item_detail(itemid):
    item = itemdb.get_item_summary(itemid)
    sales = itemdb.get_sales(itemid)

    return render_template('item_detail.html', item=item, sales=sales)