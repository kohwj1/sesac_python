document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('nav').innerHTML = `
        <ul class="gnb">
            <li><a class="gnbItem" href="/users">User</a></li>
            <li><a class="gnbItem" href="/orders">Order</a></li>
            <li><a class="gnbItem" href="/orderitems">OrderItem</a></li>
            <li><a class="gnbItem" href="/stores">Store</a></li>
            <li><a class="gnbItem" href="/items">Item</a></li>
        </ul>
        `
})