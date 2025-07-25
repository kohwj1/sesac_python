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

    if (age < 14) {
        alert('만 14세 미만은 회원으로 등록할 수 없습니다.');
        return;
    }

    bodyData.append('Age', age);
    // console.log(bodyData)

    fetch(`/users/api/create`, {
        method: 'POST',
        body: bodyData
    })
        .then((response) => response.json())
        .then((data) => {
            UserId = data.UserId;

            if (data.isCreated) {
                alert(`고객 등록이 완료되었습니다.\n고객ID: ${UserId}`)
                location.href = `/users/detail?id=${UserId}`
            } else {
                throw new Error;
            }
        })
        .catch((error) => {
            alert(error)
        })
    };

document.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const day_limit = `${String(today.getFullYear() - 14)}-${String(today.getMonth() + 1).padStart(2,'0')}-${String(today.getDate()).padStart(2,'0')}`;
    document.getElementById('Birthdate').setAttribute('max', day_limit);
})

document.getElementById('createForm').addEventListener('submit', e => {
    e.preventDefault();
    createUser();
})