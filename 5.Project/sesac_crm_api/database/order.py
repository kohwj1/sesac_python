from sqlalchemy import select, func, desc
from database.tables import User, Store, Order, OrderItem, Item, session
from datetime import datetime

def get_all_list(page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(Order.Id))).fetchone()[0]
        query = sess.execute(select(Order.Id, func.strftime('%Y-%m-%d %H:%M:%S',Order.OrderAt).label('OrderAt'),
                                    Store.Name.label('StoreName'), Store.Id.label('StoreId'), User.Id.label('UserId'), User.Name.label('UserName'))
                             .select_from(User)
                             .join(Order, User.Id == Order.UserId)
                             .join(Store, Order.StoreId == Store.Id)
                             .order_by(desc(Order.OrderAt))
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for row in query:
            all_list.append({'Id':row.Id, 'OrderAt':row.OrderAt, 'StoreName':row.StoreName, 'StoreId':row.StoreId, 'UserId':row.UserId, 'UserName':row.UserName})
    
    return {'data':all_list, 'totalCount':row_count}

def get_total_price(orderid):
    with session() as sess:
        total_price = sess.execute(select(func.sum(Item.UnitPrice))
                                   .select_from(Order)
                                   .join(OrderItem, Order.Id == OrderItem.OrderId)
                                   .join(Item, OrderItem.ItemId == Item.Id)
                                   .where(Order.Id == orderid)).fetchone()[0]
            
    return total_price

def get_order_summary(orderid):
    with session() as sess:
        order_info = sess.execute(select(Order.Id.label('OrderId'), func.strftime('%Y-%m-%d %H:%M:%S', Order.OrderAt).label('OrderAt'), Store.Id.label('StoreId'),
                                          Store.Name.label('StoreName'), User.Id.label('UserId'), User.Name.label('UserName'))
                                   .select_from(User)
                                   .join(Order, Order.UserId == User.Id)
                                   .join(Store, Store.Id == Order.StoreId)
                                   .where(Order.Id == orderid)).fetchone()
            
    return {'OrderId':order_info.OrderId, 'OrderAt':order_info.OrderAt, 'StoreId':order_info.StoreId, 'StoreName':order_info.StoreName,
            'UserId':order_info.UserId, 'UserName':order_info.UserName, 'totalPrice':get_total_price(orderid)}

def get_orderitems(orderid):
    with session() as sess:
        query = sess.execute(select(Item.Id, Item.Name, Item.UnitPrice, func.count('*').label('UnitCount'))
                             .select_from(Order)
                             .join(OrderItem, Order.Id == OrderItem.OrderId)
                             .join(Item, OrderItem.ItemId == Item.Id)
                             .where(Order.Id == orderid)
                             .group_by(Item.Name)
                             .order_by(desc('UnitCount'))).fetchall()
        all_list = []

        for row in query:
            all_list.append({'ItemId':row.Id, 'ItemName':row.Name, 'UnitPrice':row.UnitPrice, 'UnitCount':row.UnitCount})
    
    return all_list