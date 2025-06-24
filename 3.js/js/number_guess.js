const answer = Math.floor(Math.random() * 101);
const submit = document.getElementById('submit');
const history = document.getElementById('history');

console.log(answer)

submit.onclick = () => {
    checkAnswer();
}

function checkAnswer() {
    const input = document.getElementById('input').value;
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