document.addEventListener('DOMContentLoaded', function() {
    let americano = document.getElementById('americano');
    let cappuccino = document.getElementById('cappuccino');
    let latte = document.getElementById('latte');
    let reset = document.getElementById('reset');
    
    americano.addEventListener('click',order_americano);
    cappuccino.addEventListener('click',order_cappuccino);
    latte.addEventListener('click',order_latte);
    reset.addEventListener('click',order_reset);
});  
      
function order_americano() {
    let count = document.getElementsByClassName('cnt')[0];
    let price = document.getElementsByClassName('price')[0];
    let total_price = document.getElementById('total_price');
    count.textContent = Number(count.textContent) + 1;
    total_price.textContent = Number(total_price.textContent) + Number(price.textContent);
};

function order_cappuccino() {
    let count = document.getElementsByClassName('cnt')[1];
    let price = document.getElementsByClassName('price')[1];
    let total_price = document.getElementById('total_price');
    count.textContent = Number(count.textContent) + 1;
    total_price.textContent = Number(total_price.textContent) + Number(price.textContent);
};

function order_latte() {
    let count = document.getElementsByClassName('cnt')[2];
    let price = document.getElementsByClassName('price')[2];
    let total_price = document.getElementById('total_price');
    count.textContent = Number(count.textContent) + 1;
    total_price.textContent = Number(total_price.textContent) + Number(price.textContent);
};

function order_reset() {
    let counts = document.getElementsByClassName('cnt');
    for (let count of counts) {
        count.textContent = 0
    };

    let total_price = document.getElementById('total_price');
    total_price.textContent = 0;
};