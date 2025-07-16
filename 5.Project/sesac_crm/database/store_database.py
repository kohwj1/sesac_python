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

    cur.execute("""SELECT Id, Type, Name AS StoreName, Address, COUNT(*) OVER () AS TotalCount
                FROM stores
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def get_store_summary(storeid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT Id AS StoreId, Name, Type, Address
                FROM stores
                WHERE Id = ?""", (storeid, ))
    
    storeinfo = cur.fetchone()
    return storeinfo

def get_sales(month_filter):
    pass

def get_store_info(orderid, month_filter) -> list | None:
    storeinfo = get_store_summary(orderid)
    sales = get_sales(month_filter)
    return {'info':storeinfo, 'sales':sales}