function renderGnb() {
    document.getElementById('nav').innerHTML = `
        <ul class="gnb">
            <li><a class="gnbItem" id="gnb_users" href="/users">User</a></li>
            <li><a class="gnbItem" id="gnb_orders" href="/orders">Order</a></li>
            <li><a class="gnbItem" id="gnb_orderitems" href="/orderitems">OrderItem</a></li>
            <li><a class="gnbItem" id="gnb_stores" href="/stores">Store</a></li>
            <li><a class="gnbItem" id="gnb_items" href="/items">Item</a></li>
        </ul>
    `
}

function gnbActivate(pos) {
    document.getElementById(`gnb_${String(pos)}`).classList.add('gnbActive')
}

document.addEventListener('DOMContentLoaded', () => {
    renderGnb()
    
    const pos = window.location.pathname.split('/')[1]
    gnbActivate(pos)
})