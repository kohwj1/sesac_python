// mac에서 백틱 입력하는 방법: option + 

for (let i = 2; i <=9; i++) {
    for (let j = 1; j <=9; j++) {
        console.log(`${i} x ${j} = ${i*j}`);
    };
};

// 삼항연산자
var age = 26;
var beverage = age >= 21 ? "Beer" : "Juice";
console.log(beverage)

//함수
function greet(name) {
    console.log(`안녕하세요, ${name}님.`)
}

//배열 순회 반복문
fruits = ['apple', 'banana', 'cherry', 'orange']

//익명함수
fruits.forEach(function(f) {
    console.log(f);
});

//화살표 함수
fruits.forEach((f) => {
    console.log(f);
});



