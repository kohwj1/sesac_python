from sqlalchemy import select, func, desc
from database.model.tables import User, Store, Order, OrderItem, Item, session
from datetime import datetime

def get_list(page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(OrderItem.Id))).fetchone()[0]
        query = sess.execute(select(OrderItem)
                             .order_by(OrderItem.OrderId)
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = [{'Id':row[0].Id, 'OrderId':row[0].OrderId, 'ItemId':row[0].ItemId} for row in query]

        # for s in query:
        #     row = s[0]
        #     all_list.append({'Id':row.Id, 'OrderId':row.OrderId, 'ItemId':row.ItemId})
    
    return {'data':all_list, 'totalCount':row_count}