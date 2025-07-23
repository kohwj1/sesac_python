function getTypeList() {
    fetch(`http://localhost:5500/items/api/typelist`)
        .then((response) => response.json())
        .then((data) => {
            const type_data = data.data;
            console.log(data.data)
            const typeList = document.getElementById('typeList')
            if (type_data.length == 0) {
                typeList.innerText = '상품 유형 정보를 가져오는 데 실패하였습니다.'
            } else {
                typeList.innerHTML = ''
                for (row of type_data) {
                    typeList.innerHTML += `
                                            <input type="radio" name="Type" id="${row}" value="${row}" required>
                                            <label for="${row}">${row}</label>`
                }
            }
        })
    };

function createItem() {
    const userForm = document.getElementById('createForm')
    let bodyData = new FormData(userForm);
    console.log(bodyData)

    fetch(`http://localhost:5500/items/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            ItemId = data.ItemId;

            if (data.isCreated) {
                alert(`상품 등록이 완료되었습니다.\n상품ID: ${ItemId}`)
                location.href = `/items/detail?id=${ItemId}`
            } else {
                throw new Error;
            }
        })
        .catch((error) => {
            console.log(error)
            alert(error)
        })
    };

document.addEventListener('DOMContentLoaded', getTypeList)
document.getElementById('createForm').addEventListener('submit', e => {
    e.preventDefault();
    createItem();
})