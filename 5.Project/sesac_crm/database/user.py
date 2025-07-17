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

    cur.execute("SELECT *, COUNT(*) OVER() AS Totalcount FROM users LIMIT ? OFFSET ?", (pagesize, off_start))
    return cur.fetchall()

def search_users_by_name(name, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT *, COUNT(*) OVER() AS Totalcount
                FROM users
                WHERE Name LIKE ? LIMIT ? OFFSET ?""", (f'%{name}%', pagesize, off_start))
    return cur.fetchall()

def search_users_by_gender(gender, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT *, COUNT(*) OVER() AS Totalcount
                FROM users
                WHERE Gender = ? LIMIT ? OFFSET ?""", (gender, pagesize, off_start))
    return cur.fetchall()

def search_users_by_name_and_gender(name, gender, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT *, COUNT(*) OVER() AS Totalcount
                FROM users
                WHERE Name LIKE ? AND Gender = ?
                LIMIT ? OFFSET ?""", (f'%{name}%', gender, pagesize, off_start))
    return cur.fetchall()

def get_user_history(userid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT o.Id AS OrderId, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId
                FROM users u
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id 
                WHERE u.Id = ?
                ORDER BY OrderAt DESC""", (userid, ))
    user_history = cur.fetchall()
    return user_history

def get_user_summary(userid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE Id = ?", (userid, ))
    summary = cur.fetchone()
    return summary

def get_regular_store(userid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT s.Name AS StoreName, COUNT(o.Id) AS OrderCount
                FROM users u
                JOIN orders o ON u.Id = o.UserId
                JOIN stores s ON o.StoreId = s.Id 
                WHERE u.Id = ?
                GROUP BY s.Id
                ORDER BY OrderCount DESC
                LIMIT 5""", (userid, ))
    regulars = cur.fetchall()
    return regulars

def get_favorite_items(userid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT i.Name AS ItemName, COUNT(oi.Id) AS ItemCount
                FROM users u
                JOIN orders o ON u.Id = o.UserId
                JOIN orderitems oi ON o.Id = oi.OrderId
                JOIN items i ON oi.ItemId = i.Id
                WHERE u.Id = ?
                GROUP BY i.Id
                ORDER BY ItemCount DESC
                LIMIT 5""", (userid, ))
    regulars = cur.fetchall()
    return regulars