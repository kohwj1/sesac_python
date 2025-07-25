import sqlite3
MY_DATABASE = 'total.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE) #DB 연결
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
            )
        """)

    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""INSERT INTO users (name, age) VALUES(?, ?)""", (name, age))

    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()  #리스트가 리턴됨

    conn.commit()
    conn.close()
    return rows

def get_user(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE name = ?", (name, ))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    if row:
        return row
    return f'검색한 사용자 {name} 없음'

def update_user_age(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET age = ? WHERE name = ?", (age, name))

    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"DELETE FROM users WHERE id = ?", (id, ))

    conn.commit()
    conn.close()

def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"DELETE FROM users WHERE name = ?", (name, ))

    conn.commit()
    conn.close()

def main():
    create_table()
    insert_user('alice', 30)
    insert_user('bob', 25)
    insert_user('charlie', 35)

    user_list = get_users()
    for user in user_list:
        print (user)
    
    update_user_age('alice', 32)
    alice = get_user('alice')
    print (f'사용자 정보: {alice}')

    delete_user_by_name('bob')
    bob = get_user('bob')
    print(f'사용자 정보: {bob}')

    delete_user_by_id(3)
    charlie = get_user('charlie')
    print(f'사용자 정보: {charlie}')

if __name__ == '__main__':
    main()