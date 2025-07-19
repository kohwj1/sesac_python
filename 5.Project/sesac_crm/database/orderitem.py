from database.db_connect import get_connection

def get_all_list(page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT Id, OrderId, ItemId, COUNT(*) OVER() AS Totalcount
                FROM orderitems
                ORDER BY OrderId
                LIMIT ? OFFSET ?""", (pagesize, off_start))
    return cur.fetchall()