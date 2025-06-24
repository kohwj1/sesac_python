const display = document.getElementById('display');
const plus = document.getElementById('plus');
const minus = document.getElementById('minus');
const multiply = document.getElementById('multiply');
const divide = document.getElementById('divide');
const equal = document.getElementById('equal');

const num_btn = document.getElementsByClassName('num_btn');

// const num_0 = document.getElementById('0')
// const num_1 = document.getElementById('1')
// const num_2 = document.getElementById('2')
// const num_3 = document.getElementById('3')
// const num_4 = document.getElementById('4')
// const num_5 = document.getElementById('5')
// const num_6 = document.getElementById('6')
// const num_7 = document.getElementById('7')
// const num_8 = document.getElementById('8')
// const num_9 = document.getElementById('9')
let is_result = document.getElementById('is_result').value;


// num_0.onclick = () => {
//     cal_input(num_0.textContent)
// };
// num_1.onclick = () => {
//     cal_input(num_1.textContent)
// };
// num_2.onclick = () => {
//     cal_input(num_2.textContent)
// };
// num_3.onclick = () => {
//     cal_input(num_3.textContent)
// };
// num_4.onclick = () => {
//     cal_input(num_4.textContent)
// };
// num_5.onclick = () => {
//     cal_input(num_5.textContent)
// };
// num_6.onclick = () => {
//     cal_input(num_6.textContent)
// };
// num_7.onclick = () => {
//     cal_input(num_7.textContent)
// };
// num_8.onclick = () => {
//     cal_input(num_8.textContent)
// };
// num_9.onclick = () => {
//     cal_input(num_9.textContent)
// };

plus.onclick = () => {
    cal_input(plus.textContent)
};
minus.onclick = () => {
    cal_input(minus.textContent)
};
multiply.onclick = () => {
    cal_input(multiply.textContent)
};
divide.onclick = () => {
    cal_input(divide.textContent)
};

reset.onclick = () => {
    display.textContent = '0'
};

equal.onclick = () => {
    if (display.textContent != '') {
        calculate(display.textContent)
        console.log(calculate(display.textContent))
    };
};

function cal_input(myBtn) {
    if (display.textContent == '0' || is_result == 'true') {
        display.textContent = myBtn
        is_result = 'false'
    } else {
        display.textContent += myBtn
    }
}

function calculate(formular) {
    // if ('/0' in formular) {
    //     display.textContent = 'ZeroDivisionError'
    // } else {
    //   display.textContent = eval(formular)  
    // };
    display.textContent = eval(formular)
    is_result = 'true'
};