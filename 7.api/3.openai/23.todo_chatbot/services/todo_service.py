_todos = []
_idx = -1

def get_all():
    return _todos

def add(new_todo):
    global _idx
    _idx += 1
    _todos.append({'idx':_idx, 'task':new_todo, 'is_done':False})
    return _idx


def toggle(idx):
    try:
        for i, item in enumerate(_todos):
            if item['idx'] == idx:
                _todos[i]['is_done'] = not _todos[i]['is_done']
                return {'result':'success', 'is_done':_todos[i]['is_done']}
    except IndexError as e:
        print(e)
    return {'is_done':'error','msg':'아이템이 존재하지 않습니다.'}


def delete(idx):
    for i, item in enumerate(_todos):
        if item['idx'] == idx:
            _todos.pop(i)
            return {'result':'success'}
    return {'result':'error','msg':'아이템이 존재하지 않습니다.'}