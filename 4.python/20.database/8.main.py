# from db_crud_sqlite import (
#     create_table, insert_user,
#     get_user, get_users,
#     delete_user_by_name, delete_user_by_id,
#     update_user_age)
# #import 구문이 길어질 경우 괄호로 묶어 여러 줄로 작성할 수 있다

import db_crud_sqlite as db

def main():
    db.create_table()
    db.insert_user('alice', 30)
    db.insert_user('bob', 25)
    db.insert_user('charlie', 35)

    user_list = db.get_users()
    for user in user_list:
        print (user)
    
    db.update_user_age('alice', 32)
    alice = db.get_user('alice')
    print (f'사용자 정보: {alice}')

    db.delete_user_by_name('bob')
    bob = db.get_user('bob')
    print(f'사용자 정보: {bob}')

    db.delete_user_by_id(3)
    charlie = db.get_user('charlie')
    print(f'사용자 정보: {charlie}')

if __name__ == '__main__':
    main()