function getItemList() {
    fetch(`http://localhost:5500/items/api/list`)
        .then((response) => response.json())
        .then((data) => {
            const item_data = data.data;
            const itemList = document.getElementById('itemList')
            if (item_data.length == 0) {
                itemList.innerText = '상품 정보를 가져오는 데 실패하였습니다.'
            } else {
                itemList.innerHTML = ''
                for (row of item_data) {
                    itemList.innerHTML += `
                                        <input class="itemUi" type="radio" id="${row.Id}" name="ItemId" value="${row.Id}" required>
                                        <label for="${row.Id}">${row.Name} (${row.UnitPrice}원)</label>`
                }
            }
        })
    };

function createOrder() {
    const now = new Date();
    const year = String(now.getFullYear())
    const month = String(now.getMonth() + 1).padStart(2, '0')
    const day = String(now.getDate()).padStart(2, '0')
    const hour = String(now.getHours()).padStart(2, '0')
    const minute = String(now.getMinutes()).padStart(2, '0')
    const second = String(parseInt(now.getSeconds())).padStart(2, '0')
    const orderat = `${year}-${month}-${day} ${hour}:${minute}:${second}`
    const orderForm = document.getElementById('createOrderForm')
    let bodyData = new FormData(orderForm);
    bodyData.append('OrderAt', orderat);
    // console.log(bodyData.get('OrderAt'))  
    // console.log(bodyData.get('UserId'))  
    // console.log(bodyData.get('ItemId'))  

    fetch(`http://localhost:5500/orders/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            OrderId = data.OrderId;
            console.log(OrderId)
            alert(`주문이 완료되었습니다.\n주문ID: ${OrderId}`)
            location.href = `/orders/detail?id=${OrderId}`
        })
        .catch((error) => {
            console.log(error)
            alert(error)
        })
    };

document.addEventListener('DOMContentLoaded', getItemList)
document.getElementById('createOrderForm').addEventListener('submit', e => {
    e.preventDefault();
    createOrder();
})