const args = new URLSearchParams(window.location.search)
const userid = args.get('userid')

function getItemList() {
    fetch(`/items/api/unique`)
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
                                        <input class="itemUi" type="checkbox" id="${row.Id}" name="ItemId" value="${row.Id}">
                                        <label for="${row.Id}">${row.Name} / ${row.UnitPrice}원</label>`
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
    const orderForm = document.getElementById('createForm')
    let bodyData = new FormData(orderForm);
    bodyData.append('OrderAt', orderat);
    // console.log(bodyData.get('OrderAt'))  
    // console.log(bodyData.get('UserId'))  
    // console.log(bodyData.getAll('ItemId'))
    
    if (bodyData.getAll('ItemId').length == 0) {
        alert('상품을 1개 이상 선택해주세요.');
        return;
    }

    fetch(`/orders/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            OrderId = data.OrderId;

            if (data.isCreated) {
                alert(`주문이 완료되었습니다.\n주문ID: ${OrderId}`)
                location.href = `/orders/detail?id=${OrderId}`
            } else {
                throw new Error;
            }
        })
        .catch((error) => {
            console.log(error)
            alert(error)
        })
    };

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('userid').value = userid
    getItemList()
})

document.getElementById('createForm').addEventListener('submit', e => {
    e.preventDefault();
    createOrder();
})