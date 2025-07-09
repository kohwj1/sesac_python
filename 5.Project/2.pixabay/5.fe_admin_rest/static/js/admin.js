document.addEventListener('DOMContentLoaded', (e) => {
    e.preventDefault(); //양식 전송 시 페이지 이동되는 것 막기
    fetch('/api/list')
    .then((response) => response.json())
    .then((data) => {
        const statusArea = document.getElementById('status')
        const imageList = document.getElementById('imageList');
        statusArea.textContent = `총 ${data.length}개의 이미지가 등록되어 있습니다.`
        imageList.innerHTML = '';
        for (item of data) {
            imageList.innerHTML += `
            <tr>
                <td><img src="/static/img/${item.filename}"></td>
                <td>${item.filename}</td>
                <td>
                    <form>
                        <input class="newKeyword" name="${item.filename}" id="${item.filename}"  value="${item.keyword}">
                        <button type="button" onclick="update_keyword('${item.filename}')">수정</button>
                    </form>
                </td>
                <td>
                    <a href="#" onclick="delete_img('${item.filename}')">삭제</button>
                </td>
            </tr>
            `
        }
    })
    .catch((error) => {
        console.log(error);
    })
})

function upload() {
    const file = document.getElementById('uploadFileInput').files[0];
    const filedata = new FormData();
    filedata.append('file', file);
    fetch(`/api/upload`, {
        method: "POST",
        body: filedata
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.msg == 'success') {
            alert('파일이 업로드되었습니다.')
            location.replace('/admin');
        } else {
            alert('파일 업로드에 실패하였습니다.');
        }
    })
    .catch((error) => {
        console.log(error)
    });
}

function update_keyword(target) {
    if (confirm('정말로 수정하시겠습니까?')) {
        const new_keyword = document.getElementById(target).value;
        // console.log(new_keyword);
        fetch(`/api/update-keyword/${target}`, {
            method: "POST",
            headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            body: new URLSearchParams({'newKeyword':new_keyword})
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.msg == 'success') {
                alert('키워드가 수정되었습니다.');
                location.replace('/admin');
            } else {
                alert('키워드 변경에 실패하였습니다.');
            }
        })
        .catch((error) => {
            console.log(error)
        });
    }
}

function delete_img(target) {
    if (confirm('정말로 삭제하시겠습니까?')) {
        fetch(`/api/delete/${target}`, {
            method: "POST"
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.msg == 'success') {
                alert('삭제되었습니다.');
                location.replace('/admin');
            } else {
                alert('파일이 존재하지 않거나 이미 삭제되었습니다.');
            }
        })
        .catch((error) => {
            console.log(error)
        });
    }
}