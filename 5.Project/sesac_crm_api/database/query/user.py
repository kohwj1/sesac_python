from sqlalchemy import select, func, desc, insert
from database.util.commitchecker import commit_checker
from database.model.tables import User, Store, Order, OrderItem, Item, session
import uuid
from datetime import datetime

def get_list(page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(User.Id))).fetchone()[0]
        query = sess.execute(select(User)
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for u in query:
            row = u[0]
            all_list.append({'Id':row.Id, 'Name':row.Name, 'Gender':row.Gender,
                             'Age':row.Age, 'Birthdate':row.Birthdate, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def search_users_by_name(name, page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(User.Id))
                                 .where(User.Name.like(f'%{name}%'))).fetchone()[0]
        query = sess.execute(select(User)
                             .where(User.Name.like(f'%{name}%'))
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for u in query:
            row = u[0]
            all_list.append({'Id':row.Id, 'Name':row.Name, 'Gender':row.Gender,
                             'Age':row.Age, 'Birthdate':row.Birthdate, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def search_users_by_gender(gender, page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(User.Id)).where(User.Gender == gender)).fetchone()[0]
        query = sess.execute(select(User)
                             .where(User.Gender == gender)
                             .limit(pagesize)
                             .offset(off_start)).fetchall()
        all_list = []

        for u in query:
            row = u[0]
            all_list.append({'Id':row.Id, 'Name':row.Name, 'Gender':row.Gender, 
                             'Age':row.Age, 'Birthdate':row.Birthdate, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def search_users_by_name_and_gender(name, gender, page, pagesize):
    off_start = (page - 1) * pagesize
    with session() as sess:
        row_count = sess.execute(select(func.count(User.Id))
                                 .where(User.Gender == gender, User.Name.like(f'%{name}%'))).fetchone()[0]
        query = sess.execute(select(User)
                             .where(User.Gender == gender, User.Name.like(f'%{name}%'))
                             .limit(pagesize).offset(off_start)).fetchall()
        all_list = []

        for u in query:
            row = u[0]
            all_list.append({'Id':row.Id, 'Name':row.Name, 'Gender':row.Gender,
                             'Age':row.Age, 'Birthdate':row.Birthdate, 'Address':row.Address})
    
    return {'data':all_list, 'totalCount':row_count}

def get_user_summary(userid):
    with session() as sess:
        user_info = sess.execute(select(User).where(User.Id == userid)).fetchone()[0]
    
    return {'Id':user_info.Id, 'Name':user_info.Name, 'Gender':user_info.Gender,
            'Age':user_info.Age, 'Birthdate':user_info.Birthdate, 'Address':user_info.Address}

def get_user_history(userid):
    with session() as sess:
        query = sess.execute(select(Order.Id, Order.OrderAt, Order.StoreId, Store.Name)
                             .join(User, Order.UserId == User.Id)
                             .join(Store, Order.StoreId == Store.Id)
                             .where(User.Id == userid)
                             .order_by(desc(Order.OrderAt))).fetchall()
        all_list = []
        for row in query:
            all_list.append({'OrderId':row[0], 'OrderAt':row[1].strftime('%Y-%m-%d %H:%M:%S'),
                             'StoreId':row[2], 'StoreName':row[3]})
    
    return all_list

def get_regular_store(userid):
    with session() as sess:
        query = sess.execute(select(Store.Name, func.count(Order.Id).label('OrderCount'))
                             .join(User, Order.UserId == User.Id)
                             .join(Store, Order.StoreId == Store.Id)
                             .where(User.Id == userid)
                             .group_by(Store.Id)
                             .order_by(desc("OrderCount"))
                             .limit(5)).fetchall()
        all_list = []
        for row in query:
            all_list.append({'StoreName':row[0], 'OrderCount':row[1]})
    
    return all_list

def get_favorite_items(userid):
    with session() as sess:
        query = sess.execute(select(Item.Name, func.count(OrderItem.Id).label('ItemCount'))
                             .select_from(User)
                             .join(Order, User.Id == Order.UserId)
                             .join(OrderItem, Order.Id == OrderItem.OrderId)
                             .join(Item, OrderItem.ItemId == Item.Id)
                             .where(User.Id == userid)
                             .group_by(Item.Id)
                             .order_by(desc("ItemCount"))
                             .limit(5)).fetchall()
        all_list = []
        for row in query:
            all_list.append({'ItemName':row[0], 'OrderCount':row[1]})
    
    return all_list

def create_user(username, birthdate, age, gender, address):
    with session() as sess:
        new_user_key = str(uuid.uuid4())
        sess.execute(insert(User).values(Id=new_user_key,
                                         Name=username,
                                         Birthdate=birthdate,
                                         Age=age,
                                         Gender=gender,
                                         Address=address))
        sess.commit()

    return {'isCreated':commit_checker('create', User, new_user_key), 'newId': new_user_key}