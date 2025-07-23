from sqlalchemy import select, func, desc, insert
from database.db.tables import User, Store, Order, OrderItem, Item, session
from database.util.commitchecker import commit_checker
import uuid

def get_all_list(page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(Item.Id))).fetchone()[0]
        query = sess.execute(select(Item)
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for i in query:
            row = i[0]
            all_list.append({'Id':row.Id, 'Type':row.Type, 'Name':row.Name, 'UnitPrice':row.UnitPrice})
    
    return {'data':all_list, 'totalCount':row_count}

def get_list_by_itemname(item_name, page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(Item.Id))
                                 .where(Item.Name.like(f'%{item_name}%'))).fetchone()[0]
        query = sess.execute(select(Item)
                             .where(Item.Name.like(f'%{item_name}%'))
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for i in query:
            row = i[0]
            all_list.append({'Id':row.Id, 'Type':row.Type, 'Name':row.Name, 'UnitPrice':row.UnitPrice})
    
    return {'data':all_list, 'totalCount':row_count}

def get_item_summary(itemid):
    with session() as sess:
        item_info = sess.execute(select(Item)
                                   .where(Item.Id == itemid)).fetchone()[0]
            
    return {'ItemId':item_info.Id, 'Name':item_info.Name, 'Type':item_info.Type, 'UnitPrice':item_info.UnitPrice}

def get_monthly_sales(itemid):
    with session() as sess:
        query = sess.execute(select(func.strftime('%Y-%m',Order.OrderAt).label('Month'), func.sum(Item.UnitPrice).label('Sales'), func.count('*').label('SalesCount'))
                             .select_from(Order)
                             .join(OrderItem, Order.Id == OrderItem.OrderId)
                             .join(Item, OrderItem.ItemId == Item.Id)
                             .where(Item.Id == itemid)
                             .group_by('Month')
                             .order_by(desc('Month'))).fetchall()
        all_list = []

        for row in query:
            all_list.append({'Month':row.Month, 'Sales':row.Sales,'SalesCount':row.SalesCount})
        
        return all_list

def get_item_type():
    with session() as sess:
        query = sess.execute(select(func.distinct(Item.Type))).fetchall()
        all_list = []

        for s in query:
            row = s[0]
            all_list.append(row)
    
    return all_list

def create_item(itemname, type, unitprice):
    with session() as sess:
        new_item_key = str(uuid.uuid4())
        sess.execute(insert(Item).values(Id=new_item_key, Name=itemname, Type=type, UnitPrice=unitprice))
        sess.commit()

    return commit_checker('create', Item, new_item_key), new_item_key