document.addEventListener('DOMContentLoaded', () => {
    loadFileList();
})

async function loadFileList() {
    const fileListElem = document.getElementById('file-list');

    const response = await fetch('/files');
    const data = await response.json();

    console.log(data);
    fileListElem.innerHTML = data.files.map(fn => 
        `<li>
            ${fn} <button data-file="${fn}" class="delete-btn">삭제</button>
        </li>`
    ).join(''); // List 를 순회 하면서, 기본값 [oo,oo,oo] 를 '' 공백으로 연결

    fileListElem.addEventListener('click', async (e) => {
        if (!e.target.matches('.delete-btn')) return;

        const filename = e.target.dataset.file;
        console.log('삭제하려고 함: ', filename)

        // if (!confirm(`'${filename}'을 정말 삭제하시겠습니까?`)) return;

        const response = await fetch(`/files/${filename}`, {method: 'DELETE'})
        const result = await response.json()
        console.log('요청한 결과: ', result.message)

        loadFileList() // 삭제 후 파일목록 DOM 다시 그리기
    })
}

async function uploadFile() {
    console.log('업로드 실행');
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    // console.log(file);
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    alert(result.message);

    loadFileList();
}

async function askQuestion() {
    const questionInput = document.getElementById('questionInput');
    const question = questionInput.value;

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({question})
    })

    const data = await response.json();
    const result = document.getElementById('answer');
    result.innerHTML = data.message;
}