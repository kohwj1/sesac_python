const env = apiPath()
const args = new URLSearchParams(window.location.search)
let page = args.get('page')
let q = args.get('q')

if (q == null) {
    q = ''
}

if (page == null) {
    page = 1;
}

function displayList() {
    document.getElementById('q').value = q
    fetch(`${env}/stores/api/list?q=${q}&page=${page}`)
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
            createPagination('store', parseInt(page), data.lastPage, [q])   
        })
    };

document.addEventListener('DOMContentLoaded', displayList)