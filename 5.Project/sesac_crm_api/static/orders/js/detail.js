const args = new URLSearchParams(window.location.search)
const orderId = args.get('id')

function displaySummary() {
    let totalPrice = 'N/A';
    fetch(`http://localhost:5500/orders/api/summary/${orderId}`)
        .then((response) => response.json())
        .then((data) => {
            const orderId = document.getElementById('orderId')
            orderId.textContent = data.OrderId

            if (data.totalPrice != null) {
                totalPrice = data.totalPrice
            }

            const orderSummary = document.getElementById('summary');
            orderSummary.innerHTML = `<tr>
                                        <td><a href="/users/detail?id=${data.UserId}">${data.UserName}</a></td>
                                        <td>${data.OrderAt}</td>
                                        <td><a href="/stores/detail?id=${data.StoreId}">${data.StoreName}</a></td>
                                        <td>${totalPrice}원</a></td>
                                    </tr>`;
    })
    };

function displayDetail() {    
    fetch(`http://localhost:5500/orders/api/orderitems/${orderId}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const orderDetail = document.getElementById('orderDetail')
            console.log(table_data)
            if (table_data.length == 0) {
                orderDetail.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                orderDetail.innerHTML = ''
                for (row of table_data) {
                    orderDetail.innerHTML += `                    
                            <tr>
                                <td><a href="/items/detail?id=${row.ItemId}">${row.ItemName}</a></td>
                                <td>${row.UnitPrice}</td>
                                <td>${row.UnitCount}</td>
                            </tr>`;
                }
            };
        })
    };

document.addEventListener('DOMContentLoaded', displaySummary)
document.addEventListener('DOMContentLoaded', displayDetail)