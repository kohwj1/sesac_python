PAGE_SIZE = 20
PAGINATION_SIZE = 10

def pagination(selectquery):
    total_count = selectquery['totalCount']
    last_page = (total_count - 1) // PAGE_SIZE + 1
    print(last_page)
    
    return last_page