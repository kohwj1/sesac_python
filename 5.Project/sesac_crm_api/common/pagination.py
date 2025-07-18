PAGE_SIZE = 20
PAGINATION_SIZE = 5
TOTAL_COUNT = 0

def pagination(selectquery):
    total_count = selectquery['totalCount']
    total_page = (total_count - 1) // PAGE_SIZE + 1
    print(total_page)
    
    return total_page