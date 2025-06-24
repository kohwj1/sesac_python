document.addEventListener('DOMContentLoaded', function() {
    let fruitSelector = document.getElementById('fruitSelector');
    fruitSelector.addEventListener('change', function() {
        console.log('변경 감지됨');
    }) ;
    fruitSelector.addEventListener('change',fruitsDisplay);
});        
function fruitsDisplay() {
    let fruit = document.getElementById('fruitSelector').value;
    let result = document.getElementById('fruitResult');
    
    switch(fruit) {
        case 'apple':
        case 'APPLE': //여러 케이스에서 같은 결과를 얻는 경우를 위해 아래로 쭉 실행함. 중간 탈출하려면 break 필요
            result.innerText = '이것은 사과입니다.';
            break;
        case 'banana':
            result.innerText = '<b>이것은 바나나입니다.</b>'; //innerText, textContent는 html태그가 렌더링되지 않음 (글자로 취급)
            break;
        case 'orange':
            result.innerHTML = '<b>이것은 오렌지입니다.</b>'; //innerHTML는 html태그가 렌더링됨
            break;
        case 'pineapple':
            result.innerText = '이것은 파인애플입니다.';
            break;
        default:
            result.textContent = '<b>오류!</b>'
    };
};