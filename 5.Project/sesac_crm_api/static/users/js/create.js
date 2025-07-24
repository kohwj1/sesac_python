const env = apiPath()

function getAge (birth) {
    const today = new Date();
    const birthday = new Date(Date.parse(birth))

    let age = today.getFullYear() - birthday.getFullYear()
    
    if ( today.getMonth() < birthday.getMonth() || (today.getMonth() == birthday.getMonth() & today.getDate() < birthday.getDate() )) {
        age += -1;
    }

    return age
}

function createUser() {
    const userForm = document.getElementById('createForm');
    const age = getAge(document.getElementById('Birthdate').value);
    let bodyData = new FormData(userForm);
    bodyData.append('Age', age);

    console.log(bodyData)

    fetch(`${env}/users/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            // console.log(data)
            UserId = data.UserId;

            if (data.isCreated) {
                alert(`고객 등록이 완료되었습니다.\n고객ID: ${UserId}`)
                location.href = `/users/detail?id=${UserId}`
            } else {
                throw new Error;
            }
        })
        .catch((error) => {
            // console.log(error)
            alert(error)
        })
    };

document.getElementById('createForm').addEventListener('submit', e => {
    e.preventDefault();
    createUser();
})