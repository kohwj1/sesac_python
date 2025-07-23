const args = new URLSearchParams(window.location.search)
const userid = args.get('id')

function displaySummary() {
    fetch(`http://localhost:5500/users/api/summary/${userid}`)
        .then((response) => response.json())
        .then((data) => {
            document.title += data.Name;
            const userSummary = document.getElementById('summary');
            userSummary.innerHTML = `                    
                                    <tr>
                                        <td>${data.Name}</td>
                                        <td>${data.Gender}</td>
                                        <td>${data.Age}</td>
                                        <td>${data.Birthdate}</td>
                                        <td>${data.Address}</td>
                                    </tr>`;
        })
    };

function displayHistory() {    
    fetch(`http://localhost:5500/users/api/history/${userid}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const userHistory = document.getElementById('history')
            // console.log(table_data)
            if (table_data.length == 0) {
                userHistory.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                for (row of table_data) {
                    userHistory.innerHTML += `                    
                            <tr>
                                <td><a href="/orders/detail?id=${row.OrderId}">${row.OrderId}</a></td>
                                <td>${row.OrderAt}</td>
                                <td><a href="/stores/detail?id=${row.StoreId}">${row.StoreName}</a></td>
                            </tr>
                            `
                }
            };
        })
    };

function displayRegulars() {    
    fetch(`http://localhost:5500/users/api/regulars/${userid}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const userRegulars = document.getElementById('regulars')
            // console.log(table_data)
            if (table_data.length == 0) {
                userRegulars.innerHTML = '<li>표시할 데이터가 없습니다</li>'
            } else {
                for (row of table_data) {
                    userRegulars.innerHTML += `<li class="additional">${row.StoreName} (${row.OrderCount}번 방문)</li>
                            `
                }
            };
        })
    };

function displayFavorites() {    
    fetch(`http://localhost:5500/users/api/favorites/${userid}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const userFavorites = document.getElementById('favorites')
            // console.log(table_data)
            if (table_data.length == 0) {
                userFavorites.innerHTML = '<li>표시할 데이터가 없습니다</li>'
            } else {
                for (row of table_data) {
                    userFavorites.innerHTML += `<li class="additional">${row.ItemName} (${row.OrderCount}번 구매)</li>
                            `
                }
            };
        })
    };

document.addEventListener('DOMContentLoaded', displaySummary)
document.addEventListener('DOMContentLoaded', displayHistory)
document.addEventListener('DOMContentLoaded', displayRegulars)
document.addEventListener('DOMContentLoaded', displayFavorites)
document.getElementById('createOrder').addEventListener('click', () => {
    location.href = `/orders/create?userid=${userid}`
})