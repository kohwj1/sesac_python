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

    cur.execute("""SELECT Id, Type, Name AS ItemName, UnitPrice, COUNT(*) OVER () AS TotalCount
                FROM items
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def get_item_summary(itemid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT Id AS ItemId, Name, Type, UnitPrice
                FROM items
                WHERE Id = ?""", (itemid, ))
    
    storeinfo = cur.fetchone()
    return storeinfo

def get_sales(itemid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT strftime('%Y-%m', o.OrderAt) AS OrderDate, SUM(i.UnitPrice) AS Sales, Count(*) AS SaleCount
                FROM items i
                JOIN orderitems oi ON i.Id = oi.ItemId
                JOIN orders o ON oi.OrderId = o.Id
                WHERE i.Id = ?
                GROUP BY OrderDate
                ORDER BY OrderDate DESC""", (itemid,))
    
    sales = cur.fetchall()
    return sales