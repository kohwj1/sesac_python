const args = new URLSearchParams(window.location.search)
let page = args.get('page')

if (page == null) {
    page = 1;
}

function displayList() {
    fetch(`/orderitems/api/list?page=${page}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            console.log(table_data)
            const tablecontent = document.getElementById('tableContent')
            if (table_data.length == 0) {
                tablecontent.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다<div><a href="#" onclick="history.back()">뒤로가기</a></div></td></tr>'
            } else {
                for (row of table_data) {
                    tablecontent.innerHTML += `<tr>
                                                    <td>${row.Id}</td>
                                                    <td><a href="/orders/detail?id=${row.OrderId}">${row.OrderId}</a></td>
                                                    <td><a href="/items/detail?id=${row.ItemId}">${row.ItemId}</a></td>
                                                </tr>`;
                }
            };
            createPagination('default', parseInt(page), data.lastPage, [])   
        })
    };
    
document.addEventListener('DOMContentLoaded', displayList)