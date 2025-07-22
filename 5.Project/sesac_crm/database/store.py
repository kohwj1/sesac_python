from database.db_connect import cursor

def get_all_list(page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    cur = cursor()

    cur.execute("""SELECT Id, Type, Name AS StoreName, Address, COUNT(*) OVER () AS TotalCount
                FROM stores
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def search_stores(q, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    cur = cursor()

    cur.execute("""SELECT Id, Type, Name AS StoreName, Address, COUNT(*) OVER () AS TotalCount
                FROM stores
                WHERE Name LIKE ? OR Address LIKE ?
                LIMIT ? OFFSET ?""", (f'%{q}%', f'%{q}%', pagesize, off_start))
    return cur.fetchall()

def get_store_summary(storeid):
    cur = cursor()

    cur.execute("""SELECT Id AS StoreId, Name, Type, Address
                FROM stores
                WHERE Id = ?""", (storeid, ))
    
    storeinfo = cur.fetchone()
    return storeinfo

def get_sales(storeid):
    cur = cursor()

    cur.execute("""SELECT strftime('%Y-%m', o.OrderAt) AS OrderDate, SUM(i.UnitPrice) AS Sales, Count(*) AS SaleCount
                FROM items i
                JOIN orderitems oi ON i.Id = oi.ItemId
                JOIN orders o ON oi.OrderId = o.Id
                JOIN stores s ON o.StoreId = s.Id
                WHERE s.Id = ?
                GROUP BY OrderDate
                ORDER BY OrderDate DESC""", (storeid,))
    
    sales = cur.fetchall()
    return sales

def get_daily_sales(storeid, month_filter):
    cur = cursor()

    cur.execute("""SELECT strftime('%Y-%m-%d', o.OrderAt) AS OrderDate, SUM(i.UnitPrice) AS Sales, Count(*) AS SaleCount
                FROM items i
                JOIN orderitems oi ON i.Id = oi.ItemId
                JOIN orders o ON oi.OrderId = o.Id
                JOIN stores s ON o.StoreId = s.Id
                WHERE s.Id = ? AND strftime('%Y-%m', o.OrderAt) = ?
                GROUP BY OrderDate
                ORDER BY OrderDate DESC""", (storeid, month_filter))
    
    sales = cur.fetchall()
    return sales

def get_regulars(storeid, regular_limit):
    cur = cursor()

    cur.execute("""SELECT u.Id AS UserId, u.Name AS UserName, COUNT(*) AS OrderCount
                FROM users u
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE s.Id = ?
                GROUP BY UserId
                ORDER BY OrderCount DESC
                LIMIT ?""", (storeid, regular_limit))
    
    regulars = cur.fetchall()
    return regulars

def get_daily_regulars(storeid, month_filter, regular_limit):
    cur = cursor()

    cur.execute("""SELECT u.Id AS UserId, u.Name AS UserName, COUNT(*) AS OrderCount
                FROM users u
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE s.Id = ? AND strftime('%Y-%m', o.OrderAt) = ?
                GROUP BY UserId
                ORDER BY OrderCount DESC
                LIMIT ?""", (storeid, month_filter, regular_limit))
    
    regulars = cur.fetchall()
    return regulars