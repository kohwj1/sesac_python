function num_inc() {
    let number = document.getElementById('result');
    //innerText로 가져올 경우, 디자인 속성을 적용 받음 (숨겨져 있으면 가져오기 불가?)
    //innerHtml
    //textContent
    let number_string = number.textContent;
    // console.log(number_string);
    let number_string_to_number = Number(number_string);
    let result = number_string_to_number + 1
    number.textContent = result;
};

function num_dec() {
    document.getElementById('result').textContent -= 1;
};