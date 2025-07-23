from sqlalchemy import select, func
from database.db.tables import session


def commit_checker(tasktype, table, id):
    with session() as sess:
        commit_result = sess.execute(select(func.count(table.Id))
                                .where(table.Id == id)).fetchone()[0]
    
    if tasktype == 'delete':
        return bool(not commit_result)
    return bool(commit_result)