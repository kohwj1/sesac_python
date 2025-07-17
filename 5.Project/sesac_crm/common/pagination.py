PAGE_SIZE = 10
PAGINATION_SIZE = 10
TOTAL_COUNT = 0

def pagination(page, selectquery:list):
    total_count = selectquery[0]['Totalcount']
    total_page = (total_count - 1) // PAGE_SIZE + 1

    page_start = ((page - 1) // PAGINATION_SIZE) * PAGINATION_SIZE + 1
    page_end = min(page_start + PAGINATION_SIZE, total_page + 1)
    # print(total_count, total_page, page_start, page_end)
    return {'pages':[i for i in range(page_start, page_end)], 'totalPage':total_page}