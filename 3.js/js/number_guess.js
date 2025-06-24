const answer = Math.floor(Math.random() * 101);
const submit = document.getElementById('submit');
const history = document.getElementById('history');

// console.log(answer)

submit.onclick = () => {
    checkAnswer();
}

function checkAnswer() {
    const input = document.getElementById('input').value;

    if (input <=0 || input > 100) {
        alert('1~100 사이의 자연수를 입력해 주세요!!')
        //자연수 체크 어떻게...? 소숫점 입력받고 싶지 않음..
        return;
    }

    const history_line = document.createElement('li');
    
    history_line.innerHTML = `예측 숫자: ${input}`;
    history.appendChild(history_line);
    
    const hint = document.getElementById('hint');
    if (answer == input) {
        hint.textContent = '정답!'
        document.body.style.backgroundColor = 'yellow'
    } else if (answer > input) {
        hint.textContent = 'High'
    } else {
        hint.textContent = 'Low'
    }
};