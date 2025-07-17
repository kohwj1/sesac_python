import sqlite3

DATABASE = 'database/mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_list(page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT Id OrderId, ItemId, COUNT(*) OVER() AS Totalcount
                FROM orderitems
                ORDER BY OrderAt DESC
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()