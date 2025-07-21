const pagination = document.getElementById('pageList')
const pageDisplay = 10

function createPagination(currentPage, lastPage) {
    list_start = parseInt((currentPage - 1) / pageDisplay) * pageDisplay + 1
    list_end = Math.min(list_start + pageDisplay - 1, lastPage)
    if (list_start -1 < 1) {
        pagination.innerHTML = `<li class="pageNum disabled">Prev</li>`
    } else {
        pagination.innerHTML = `<li class="pageNum"><a href="?page=${list_start - 1}">Prev</a></li>`
    }
    
    for (i = list_start; i < list_end; i++) {
        if (i == currentPage) {
            pagination.innerHTML += `<li class="pageNum currentPage">${currentPage}</li>`
        } else {
            pagination.innerHTML += `<li class="pageNum"><a href="?page=${i}">${i}</a></li>`
        }
    }
    
    if (list_end + 1 > lastPage) {
        pagination.innerHTML += `<li class="pageNum disabled">Next</li>`
    } else {
        pagination.innerHTML += `<li class="pageNum"><a href="?page=${list_end + 1}">Next</a></li>`
    }
}

function createPagination_user(currentPage, lastPage, name, gender) {
    list_start = parseInt((currentPage - 1) / pageDisplay) * pageDisplay + 1
    list_end = Math.min(list_start + pageDisplay - 1, lastPage)
    if (list_start -1 < 1) {
        pagination.innerHTML = `<li class="pageNum disabled">Prev</li>`
    } else {
        pagination.innerHTML = `<li class="pageNum"><a href="?page=${list_start - 1}&name=${name}&gender=${gender}">Prev</a></li>`
    }

    for (i = list_start; i <= list_end; i++) {
        if (i == currentPage) {
            pagination.innerHTML += `<li class="pageNum currentPage">${currentPage}</li>`
        } else {
            pagination.innerHTML += `<li class="pageNum"><a href="?page=${i}&name=${name}&gender=${gender}">${i}</a></li>`
        }
    }

    if (list_end + 1 > lastPage) {
        pagination.innerHTML += `<li class="pageNum disabled">Next</li>`
    } else {
        pagination.innerHTML += `<li class="pageNum"><a href="?page=${list_end + 1}&name=${name}&gender=${gender}">Next</a></li>`
    }
}