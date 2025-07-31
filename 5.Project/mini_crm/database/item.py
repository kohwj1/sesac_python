from database.db_connect import cursor

def get_all_list(page, pagesize):
    off_start = (page - 1) * pagesize
    cur = cursor()

    cur.execute("""SELECT Id, Type, Name AS ItemName, UnitPrice, COUNT(*) OVER () AS TotalCount
                FROM items
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def get_list_by_itemname(page, pagesize, item_name):
    off_start = (page - 1) * pagesize
    keyword = item_name.title()
    print(keyword)
    cur = cursor()

    cur.execute("""SELECT Id, Type, Name AS ItemName, UnitPrice, COUNT(*) OVER () AS TotalCount
                FROM items
                WHERE Name LIKE ?
                LIMIT ? OFFSET ?""", (f'%{keyword}%', pagesize, off_start))
    return cur.fetchall()

def get_all_list(page, pagesize):
    off_start = (page - 1) * pagesize
    cur = cursor()

    cur.execute("""SELECT Id, Type, Name AS ItemName, UnitPrice, COUNT(*) OVER () AS TotalCount
                FROM items
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def get_item_summary(itemid):
    cur = cursor()

    cur.execute("""SELECT Id AS ItemId, Name, Type, UnitPrice
                FROM items
                WHERE ItemId = ?""", (itemid, ))
    
    storeinfo = cur.fetchone()
    return storeinfo

def get_sales(itemid):
    cur = cursor()

    cur.execute("""SELECT strftime('%Y-%m', o.OrderAt) AS OrderDate, SUM(i.UnitPrice) AS Sales, Count(*) AS SaleCount
                FROM items i
                JOIN orderitems oi ON i.Id = oi.ItemId
                JOIN orders o ON oi.OrderId = o.Id
                WHERE i.Id = ?
                GROUP BY OrderDate
                ORDER BY OrderDate DESC""", (itemid,))
    
    sales = cur.fetchall()
    return sales