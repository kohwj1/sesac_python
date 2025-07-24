const env = apiPath()
const args = new URLSearchParams(window.location.search)
const storeid = args.get('id')
let month = args.get('month')
// console.log(storeid)

function displaySummary() {
    fetch(`${env}/stores/api/summary/${storeid}`)
        .then((response) => response.json())
        .then((data) => {
            document.title += data.Name;

            const storeId = document.getElementById('storeId')
            storeId.textContent = data.Id

            const storeSummary = document.getElementById('summary');
            storeSummary.innerHTML = `                    
                                    <tr>
                                        <td>${data.Name}</td>
                                        <td>${data.Type}</td>
                                        <td>${data.Address}</td>
                                    </tr>`;
        })
    };

function displaySales() {    
    fetch(`${env}/stores/api/sales_monthly/${storeid}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const monthlySales = document.getElementById('monthlySales')
            console.log(table_data)
            if (table_data.length == 0) {
                monthlySales.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                monthlySales.innerHTML = ''
                for (row of table_data) {
                    monthlySales.innerHTML += `                    
                            <tr>
                                <td><a href="?id=${storeid}&month=${row.OrderDate}">${row.OrderDate}</a></td>
                                <td>${row.Sales}</td>
                                <td>${row.SaleCount}</td>
                            </tr>
                            `
                }
            };
        })
    };

function displayRegulars() {    
    fetch(`${env}/stores/api/regulars/${storeid}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const monthlyregulars = document.getElementById('regulars')
            console.log(table_data)
            if (table_data.length == 0) {
                monthlyregulars.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                monthlyregulars.innerHTML = ''
                for (row of table_data) {
                    monthlyregulars.innerHTML += `                    
                            <tr>
                                <td><a href="/user/deatil?id=${row.UserId}">${row.UserId}</td>
                                <td>${row.UserName}</td>
                                <td>${row.OrderCount}</td>
                            </tr>
                            `
                }
            };
        })
    };

//여기는 월 필터 붙여서 API request 보내는 부분
function filteredSales(month) {    
    fetch(`${env}/stores/api/sales_monthly/${storeid}?month=${month}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const monthlySales = document.getElementById('monthlySales')
            console.log(table_data)
            if (table_data.length == 0) {
                monthlySales.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                monthlySales.innerHTML = ''
                for (row of table_data) {
                    monthlySales.innerHTML += `                    
                            <tr>
                                <td>${row.OrderDate}</td>
                                <td>${row.Sales}</td>
                                <td>${row.SaleCount}</td>
                            </tr>
                            `
                }
            };
        })
    };

function filteredRegulars(month) {    
    fetch(`${env}/stores/api/regulars/${storeid}?month=${month}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const monthlyregulars = document.getElementById('regulars')
            console.log(table_data)
            if (table_data.length == 0) {
                monthlyregulars.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                monthlyregulars.innerHTML = ''
                for (row of table_data) {
                    monthlyregulars.innerHTML += `                    
                            <tr>
                                <td><a href="/user/deatil?id=${row.UserId}">${row.UserId}</td>
                                <td>${row.UserName}</td>
                                <td>${row.OrderCount}</td>
                            </tr>
                            `
                }
            };
        })
    };

document.addEventListener('DOMContentLoaded', displaySummary)

if (month == null) {
    month = '';
    document.addEventListener('DOMContentLoaded', displaySales)
    document.addEventListener('DOMContentLoaded', displayRegulars)
} else {
    document.addEventListener('DOMContentLoaded', filteredSales(month))
    document.addEventListener('DOMContentLoaded', filteredRegulars(month))
}

