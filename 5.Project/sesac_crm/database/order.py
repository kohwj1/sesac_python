from database.db_connect import get_connection

def get_all_list(page, pagesize):
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT o.Id AS Id, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId, u.Id AS UserId, u.Name AS UserName, COUNT(*) OVER() AS Totalcount
                FROM users u 
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                ORDER BY OrderAt DESC
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()

def get_list_by_storename(page, pagesize, store_name):
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT o.Id AS Id, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId,
                u.Id AS UserId, u.Name AS UserName, COUNT(*) OVER() AS Totalcount
                FROM users u 
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE StoreName LIKE ?
                ORDER BY OrderAt DESC
                LIMIT ? OFFSET ?""", (f'%{store_name}%', pagesize, off_start))
    return cur.fetchall()

def get_list_by_month(page, pagesize, month):
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT o.Id AS Id, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId,
                u.Id AS UserId, u.Name AS UserName, COUNT(*) OVER() AS Totalcount
                FROM users u 
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE strftime('%Y-%m', OrderAt) = ?
                ORDER BY OrderAt DESC
                LIMIT ? OFFSET ?""", (month, pagesize, off_start))
    return cur.fetchall()

def get_list_by_storename_month(page, pagesize, store_name, month):
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT o.Id AS Id, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId, u.Id AS UserId, u.Name AS UserName, COUNT(*) OVER() AS Totalcount
                FROM users u 
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE StoreName LIKE ? AND strftime('%Y-%m', OrderAt) = ?
                ORDER BY OrderAt DESC
                LIMIT ? OFFSET ?""", (f'%{store_name}%', month, pagesize, off_start))
    return cur.fetchall()

def get_orderitems(orderid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT i.Id AS ItemId, i.Name AS ItemName, i.UnitPrice AS UnitPrice, COUNT(*) AS UnitCount
                FROM orders o
                JOIN orderitems oi ON o.Id = oi.OrderId
                JOIN items i ON oi.ItemId = i.Id
                WHERE o.Id = ?
                GROUP BY ItemName
                ORDER BY OrderAt DESC, UnitCount DESC""", (orderid,))
    orderitems = cur.fetchall()
    return orderitems

def get_total_price(orderid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT SUM(i.UnitPrice) AS TotalPrice
                FROM orders o
                JOIN orderitems oi ON o.Id = oi.OrderId
                JOIN items i ON oi.ItemId = i.Id
                WHERE o.Id = ?""", (orderid,))
    totalprice = cur.fetchone()[0]
    return totalprice

def get_order_summary(orderid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT o.Id AS OrderId, o.OrderAt AS OrderAt, s.Id AS StoreId, s.Name AS StoreName, u.Id AS UserId, u.Name AS UserName
                FROM users u 
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id
                WHERE o.Id = ?
                ORDER BY OrderAt DESC""", (orderid, ))
    
    orderinfo = cur.fetchone()
    return orderinfo