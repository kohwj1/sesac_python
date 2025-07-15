import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_stores():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM stores")
    store_list = cur.fetchall()

    conn.close()
    return store_list

def search_stores(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM stores WHERE Name LIKE ?", (f'%{keyword}%', ))
    store_list = cur.fetchall()

    conn.close()
    return store_list

def get_usercount():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    page_list = cur.fetchone()[0]
    print(page_list)

    conn.close()
    return page_list

def get_users_per_page(page, pagesize):
    offset_pos = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users LIMIT ? OFFSET ?", (pagesize, offset_pos))
    user_list = cur.fetchall()

    conn.close()
    return user_list

def search_users(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE Name LIKE ?", (f'%{keyword}%', ))
    user_list = cur.fetchall()

    conn.close()
    return user_list