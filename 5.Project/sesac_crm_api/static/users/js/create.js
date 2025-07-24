const env = apiPath()

function createUser() {
    const userForm = document.getElementById('createForm')
    let bodyData = new FormData(userForm);
    console.log(bodyData)

    fetch(`${env}/users/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            UserId = data.UserId;

            if (data.isCreated) {
                alert(`고객 등록이 완료되었습니다.\n고객ID: ${UserId}`)
                location.href = `/users/detail?id=${UserId}`
            } else {
                throw new Error;
            }
        })
        .catch((error) => {
            console.log(error)
            alert(error)
        })
    };

document.getElementById('createForm').addEventListener('submit', e => {
    e.preventDefault();
    createUser();
})