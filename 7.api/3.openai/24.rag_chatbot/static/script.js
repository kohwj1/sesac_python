const answer = document.getElementById('answer')

async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const bodyData = new FormData();
    const file = fileInput.files[0];
    console.log(file)
    bodyData.append('file', file)
    const res = await fetch('/upload', {
        method: 'POST',
        body: bodyData
    })
    const result = await res.json()
    alert(result.msg)
}

async function askQuestion() {
    answer.innerText = '답변 대기중입니다...'
    const qInput = document.getElementById('qInput')
    let q = qInput.value
    const res = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({q})
    })
    const result = await res.json()
    answer.innerText = ''
    answer.innerText += result.msg
    qInput.value = ''
}