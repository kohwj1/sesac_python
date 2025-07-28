from sqlalchemy import select, func, desc, insert
from database.db.tables import User, Store, Order, OrderItem, Item, session
from database.util.commitchecker import commit_checker
import uuid


def get_list(page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(Store.Id))).fetchone()[0]
        query = sess.execute(select(Store).limit(pagesize).offset(off_start)).fetchall()
        all_list = []

        for s in query:
            row = s[0]
            all_list.append({'Id':row.Id, 'StoreName':row.Name, 'Type':row.Type, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def get_list_by_keyword(page, pagesize, q):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(Store.Id))
                                 .where(Store.Name.like(f'%{q}%') | Store.Address.like(f'%{q}%'))).fetchone()[0]
        query = sess.execute(select(Store)
                             .where(Store.Name.like(f'%{q}%') | Store.Address.like(f'%{q}%'))
                             .limit(pagesize).offset(off_start)).fetchall()
        all_list = []

        for s in query:
            row = s[0]
            all_list.append({'Id':row.Id, 'StoreName':row.Name, 'Type':row.Type, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def get_store_summary(storeid):
    with session() as sess:
        store_info = sess.execute(select(Store).where(Store.Id == storeid)).fetchone()[0]
    
    return {'Id':store_info.Id, 'Name':store_info.Name, 'Type':store_info.Type, 'Address':store_info.Address}

def get_sales(storeid):
    with session() as sess:
        query = sess.execute(select(func.strftime('%Y-%m', Order.OrderAt).label('OrderDate'),
                                    func.sum(Item.UnitPrice).label('Sales'), func.count('Order.*').label('SaleCount'))
                                 .select_from(Item)
                                 .join(OrderItem, Item.Id == OrderItem.ItemId)
                                 .join(Order, OrderItem.OrderId == Order.Id)
                                 .join(Store, Order.StoreId == Store.Id)
                                 .where(Store.Id == storeid)
                                 .group_by('OrderDate')
                                 .order_by(desc('OrderDate'))
                                 ).fetchall()
        sale_list = []
        for row in query:
            sale_list.append({'OrderDate':row.OrderDate, 'Sales':row.Sales, 'SaleCount':row.SaleCount})
    
    return sale_list

def get_filtered_sales(storeid, month_filter):
    with session() as sess:
        query = sess.execute(select(func.strftime('%Y-%m-%d', Order.OrderAt).label('OrderDate'),
                                    func.sum(Item.UnitPrice).label('Sales'), func.count('Order.*').label('SaleCount'))
                                 .select_from(Item)
                                 .join(OrderItem, Item.Id == OrderItem.ItemId)
                                 .join(Order, OrderItem.OrderId == Order.Id)
                                 .join(Store, Order.StoreId == Store.Id)
                                 .where(Store.Id == storeid, func.strftime('%Y-%m', Order.OrderAt) == month_filter)
                                 .group_by('OrderDate')
                                 .order_by(desc('OrderDate'))
                                 ).fetchall()
        sale_list = []
        for row in query:
            sale_list.append({'OrderDate':row.OrderDate, 'Sales':row.Sales, 'SaleCount':row.SaleCount})
    
    return sale_list

def get_regulars(storeid):
    with session() as sess:
        query = sess.execute(select(User.Id.label('UserId'), User.Name.label('UserName'), func.count('Order.*').label('OrderCount'))
                                 .select_from(User)
                                 .join(Order, Order.UserId == User.Id)
                                 .join(Store, Order.StoreId == Store.Id)
                                 .where(Store.Id == storeid)
                                 .group_by('UserId')
                                 .order_by(desc('OrderCount'))
                                 .limit(10)
                                 ).fetchall()
        regular_list = []
        for row in query:
            regular_list.append({'UserId':row.UserId, 'UserName':row.UserName, 'OrderCount':row.OrderCount})
    
    return regular_list

def get_filtered_regulars(storeid, month_filter):
    with session() as sess:
        query = sess.execute(select(User.Id.label('UserId'), User.Name.label('UserName'), func.count('Order.*').label('OrderCount'))
                                 .select_from(User)
                                 .join(Order, Order.UserId == User.Id)
                                 .join(Store, Order.StoreId == Store.Id)
                                 .where(Store.Id == storeid, func.strftime('%Y-%m', Order.OrderAt) == month_filter)
                                 .group_by('UserId')
                                 .order_by(desc('OrderCount'))
                                 .limit(10)
                                 ).fetchall()
        regular_list = []
        for row in query:
            regular_list.append({'UserId':row.UserId, 'UserName':row.UserName, 'OrderCount':row.OrderCount})
    
    return regular_list

def get_store_type():
    with session() as sess:
        query = sess.execute(select(func.distinct(Store.Type))).fetchall()
        all_list = []

        for s in query:
            row = s[0]
            all_list.append(row)
    
    # print(all_list)
    return all_list

def get_list_unique():
    with session() as sess:
        query = sess.execute(select(Store)
                             .group_by(Store.Type)).fetchall()
        unique_list = []

        for i in query:
            row = i[0]
            unique_list.append({'Id':row.Id, 'Type':row.Type, 'Name':row.Name})
    
    return unique_list

def create_store(storename, type, address):
    with session() as sess:
        new_store_key = str(uuid.uuid4())
        sess.execute(insert(Store).values(Id=new_store_key, Name=storename, Type=type, Address=address))
        sess.commit()

    return commit_checker('create', Store, new_store_key), new_store_key