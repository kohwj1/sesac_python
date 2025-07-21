function createPagination(currentPage, lastPage) {
    const pagination = document.getElementById('pageList')
    if (currentPage -1 < 1) {
        pagination.innerHTML = `<li class="pageNum disabled">Prev</li>`
    } else {
        pagination.innerHTML = `<li class="pageNum"><a href="?page=${currentPage - 1}">Prev</a></li>`
    }

    


    pagination.innerHTML += `<li class="pageNum currentPage">${currentPage}</li>`

    if (currentPage + 1 > lastPage) {
        pagination.innerHTML += `<li class="pageNum disabled">Next</li>`
    } else {
        pagination.innerHTML += `<li class="pageNum"><a href="?page=${currentPage + 1}">Next</a></li>`
    }
}