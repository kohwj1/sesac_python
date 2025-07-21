const pagination = document.getElementById('pageList')
const pageDisplay = 10
let q_param = ''

function createPagination(type, currentPage, lastPage, param) {
    list_start = parseInt((currentPage - 1) / pageDisplay) * pageDisplay + 1
    list_end = Math.min(list_start + pageDisplay - 1, lastPage)
    console.log(lastPage)

    switch(type){
        case 'user':
            q_param = `&name=${param[0]}&gender=${param[1]}`;
            break;
        case 'store':
            q_param = `&q=${param[0]}`;
            break;
        case 'order':
            q_param = `&name=${param[0]}&month=${param[1]}`;
            break;
        case 'item':
            q_param = `&name=${param[0]}`
            break;
    }

    if (list_start -1 < 1) {
        pagination.innerHTML = `<li class="pageNum disabled">Prev</li>`
    } else {
        pagination.innerHTML = `<li class="pageNum"><a href="?page=${list_start - 1}${q_param}">Prev</a></li>`
    }
    
    for (i = list_start; i <= list_end; i++) {
        if (i == currentPage) {
            pagination.innerHTML += `<li class="pageNum currentPage">${currentPage}</li>`
        } else {
            pagination.innerHTML += `<li class="pageNum"><a href="?page=${i}${q_param}">${i}</a></li>`
        }
    }
    
    if (list_end + 1 > lastPage) {
        pagination.innerHTML += `<li class="pageNum disabled">Next</li>`
    } else {
        pagination.innerHTML += `<li class="pageNum"><a href="?page=${list_end + 1}${q_param}">Next</a></li>`
    }
}