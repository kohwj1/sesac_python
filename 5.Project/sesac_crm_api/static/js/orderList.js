const args = new URLSearchParams(window.location.search)
let page = args.get('page')

if (page == null) {
    page = 1;
}

function displayList() {
    fetch(`http://localhost:5500/orders/api/list?page=${page}`)
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
                                <td><a href="/orders/detail?id=${row.Id}">${row.Id}</a></td>
                                <td>${row.OrderAt}</td>
                                <td><a href="/stores/detail?id=${row.StoreId}">${row.StoreName}</a></td>
                                <td><a href="/users/detail?id=${row.UserId}">${row.UserName}</a></td>
                            </tr>
                            `
                }
            };
            createPagination(parseInt(page), data.lastPage)   
        })
    };

document.addEventListener('DOMContentLoaded', displayList)