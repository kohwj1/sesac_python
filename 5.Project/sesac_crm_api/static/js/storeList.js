const args = new URLSearchParams(window.location.search)
let page = args.get('page')

if (page == null) {
    page = 1;
}

function displayList() {
    fetch(`http://localhost:5500/stores/api/list?page=${page}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const tablecontent = document.getElementById('tableContent')
            // console.log(table_data)
            if (table_data.length == 0) {
                tablecontent.innerHTML = '<tr><td colspan="4" class="noResult">표시할 데이터가 없습니다<div><a href="#" onclick="history.back()">뒤로가기</a></div></td></tr>'
            } else {
                for (row of table_data) {
                    tablecontent.innerHTML += `                    
                            <tr>
                                <td><a href="/stores/detail?id=${row.Id}">${row.Id}</a></td>
                                <td>${row.Type}</td>
                                <td>${row.StoreName}</td>
                                <td>${row.Address}</td>
                            </tr>
                            `
                }
            };
            createPagination(parseInt(page), data.lastPage)   
        })
    };

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

document.addEventListener('DOMContentLoaded', displayList)