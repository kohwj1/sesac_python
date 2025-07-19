from flask import render_template, request, Blueprint
import database.item as itemdb
from common.pagination import pagination, PAGE_SIZE

item_bp = Blueprint('items', __name__)

@item_bp.route('/')
def list():
    page = int(request.args.get('page', default=1))
    pages = [1]
    last_page = 1

    items = itemdb.get_all_list(page, PAGE_SIZE)

    if items:
        pages = pagination(page, items)['pages']
        last_page = pagination(page, items)['totalPage']

    return render_template('items.html', items=items, currentPage=page, pages=pages, lastPage=last_page)

@item_bp.route('/detail/<id>')
def detail(id):
    item = itemdb.get_item_summary(id)
    sales = itemdb.get_sales(id)

    return render_template('item_detail.html', item=item, sales=sales)