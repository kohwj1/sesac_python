from flask import render_template, request, Blueprint
import database.order as orderdb

order_bp = Blueprint('orders', __name__)

@order_bp.route('/')
def order_list():
    page = int(request.args.get('page', default=1))
    pagesize = 20
    pagination_size = 10
    total_count = 0

    orders = orderdb.get_all_list(page, pagesize)

    if orders:
        total_count = orders[0]['Totalcount']
        total_page = (total_count - 1) // pagesize + 1

        page_start = ((page - 1) // pagination_size) * pagination_size + 1
        page_end = min(page_start + pagination_size, total_page + 1)
        print(total_count, total_page, page_start, page_end)
        pages = [i for i in range(page_start, page_end)]

    return render_template('orders.html', orders=orders, currentPage=page, pages=pages, totalPage=total_page)

@order_bp.route('/detail/<orderid>')
def order_detail(orderid):
    orderinfo = orderdb.get_order_summary(orderid)
    orderitems = orderdb.get_orderitems(orderid)
    totalprice = orderdb.get_total_price(orderid)
    return render_template('order_detail.html', order=orderinfo, orderItems=orderitems, totalPrice=totalprice)