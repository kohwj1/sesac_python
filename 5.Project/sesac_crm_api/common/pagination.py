PAGE_SIZE = 20
PAGINATION_SIZE = 5
TOTAL_COUNT = 0

def pagination(page, selectquery):
    total_count = selectquery['totalCount']
    # total_count = 1000
    total_page = (total_count - 1) // PAGE_SIZE + 1

    
    # page_start = ((page - 1) // PAGINATION_SIZE) * PAGINATION_SIZE + 1
    # page_end = min(page_start + PAGINATION_SIZE - 1, total_page + 1)
    
    # prev = max(0, page_start -1)
    # next = min(page_end + 1, total_page)

    # print(page_start, page_end, prev, next)
    
    return total_page