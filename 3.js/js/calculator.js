const display = document.getElementById('display');
const equal = document.getElementById('equal');
let is_result = false;

clear.onclick = () => {
    display.textContent = '0'
};

equal.onclick = () => {
    if (display.textContent != '') {
        calculate(display.textContent)
        console.log(calculate(display.textContent))
    };
};

function cal_input(myBtn) {
    if (display.textContent == '0' || is_result == true) {
        display.textContent = `${myBtn}`
        is_result = false
    } else {
        display.textContent += `${myBtn}`
    }
}

function calculate(formular) {
    try {
        if (formular.includes('/0')) {
            display.textContent = '0';
            alert('0으로 나눌 수 없습니다.');
        } else {
            // eval을 직접 호출하면 보안상 위험...
            display.textContent = eval(formular)
        }
    } catch(e) {
        display.textContent = '0';
        alert('식을 올바르게 입력해주세요.');
    };
    is_result = true
};0