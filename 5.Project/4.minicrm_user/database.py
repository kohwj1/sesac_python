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

def search_store(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM stores WHERE Name LIKE ?", (f'%{keyword}%', ))
    store_list = cur.fetchall()

    conn.close()
    return store_list