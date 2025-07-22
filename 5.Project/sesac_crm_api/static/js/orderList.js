const args = new URLSearchParams(window.location.search)
let page = args.get('page')
let month = args.get('month')
let storename = args.get('name')

if (month == null) {
    month = ''
}

if (storename == null) {
    storename = ''
}

if (page == null) {
    page = 1;
}

function displayList() {
    const nameInput = document.getElementById('name');
    const monthInput = document.getElementById('month');
    nameInput.value = storename;
    monthInput.value = month;
    fetch(`http://localhost:5500/orders/api/list?&month=${month}&name=${storename}&page=${page}`)
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
            createPagination('order', parseInt(page), data.lastPage, [storename, month])   
        })
    };

document.addEventListener('DOMContentLoaded', displayList)