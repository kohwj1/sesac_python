const args = new URLSearchParams(window.location.search)
let username = args.get('name')
let gender = args.get('gender')
let page = args.get('page')

if (page == null) {
    page = 1;
}
if (gender == null) {
    gender = '';
}
if (username == null) {
    username = '';
}

function displayList() {
    const nameInput = document.getElementById('name')
    nameInput.value = username
    // console.log(username, gender)
    switch (gender) {
        case 'Male':
            const maleOption = document.getElementById('male');
            maleOption.selected = true;
            break;
        case 'Female':
            const femaleOption = document.getElementById('female');
            femaleOption.selected = true;
            break;
    }
    
    fetch(`http://localhost:5500/users/api/list?page=${page}&name=${username}&gender=${gender}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const tablecontent = document.getElementById('tableContent')
            // console.log(table_data)
            if (table_data.length == 0) {
                tablecontent.innerHTML = '<tr><td colspan="5" class="noResult">표시할 데이터가 없습니다<div><a href="#" onclick="history.back()">뒤로가기</a></div></td></tr>'
            } else {
                for (row of table_data) {
                    tablecontent.innerHTML += `                    
                            <tr>
                                <td><a href="/users/detail?id=${row.Id}">${row.Id}</a></td>
                                <td>${row.Name}</td>
                                <td>${row.Gender}</td>
                                <td>${row.Age}</td>
                                <td>${row.Birthdate}</td>
                            </tr>
                            `
                }
            };
            createPagination(parseInt(page), data.lastPage)   
        })
    };

document.addEventListener('DOMContentLoaded', displayList)