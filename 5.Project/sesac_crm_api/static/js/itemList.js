const args = new URLSearchParams(window.location.search)
let page = args.get('page')
let itemname = args.get('name')

if (itemname == null) {
    itemname = ''
}

if (page == null) {
    page = 1;
}

function displayList() {
    const nameInput = document.getElementById('name')
    nameInput.value = itemname
    fetch(`http://localhost:5500/items/api/list?page=${page}&name=${itemname}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            console.log(table_data)
            const tablecontent = document.getElementById('tableContent')
            if (table_data.length == 0) {
                tablecontent.innerHTML = '<tr><td colspan="4" class="noResult">표시할 데이터가 없습니다<div><a href="#" onclick="history.back()">뒤로가기</a></div></td></tr>'
            } else {
                for (row of table_data) {
                    tablecontent.innerHTML += `<tr>
                                                    <td><a href="/items/detail?id=${row.Id}">${row.Id}</a></td>
                                                    <td>${row.Type}</td>
                                                    <td>${row.Name}</td>
                                                    <td>${row.UnitPrice}</td>
                                                </tr>`;
                }
            };
            createPagination('item', parseInt(page), data.lastPage, [itemname])   
        })
    };

document.addEventListener('DOMContentLoaded', displayList)