const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
const textInput = document.getElementById('text-input')

async function getTodoList() {
    const res = await fetch('/api/todo')
    const data = await res.json()
    todoList.innerHTML = ''

    for (item of data.data) {
        drawList(item)
    }
}

async function addTodo() {
    const newTodo = textInput.value;
    const res = await fetch('/api/todo', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({'task':newTodo})
    })
    if (res.ok) {
        textInput.value = ''
        getTodoList()
    }
}   

async function updateTodo(idx) {
    const res = await fetch(`/api/todo/${idx}`, {
        method:'PUT',
    })
    if (res.ok) {
        getTodoList()
    }
}   

async function deleteTodo(idx) {
    const res = await fetch(`api/todo/${idx}`, {
        method:'DELETE'
    })
    if (res.ok) {
        getTodoList()
    }
}

function drawList(item) {
    const todoItem = `
        <li class="${item.status ? 'done' : ''}" onclick="updateTodo(${item.idx})">${item.task} 
            <button class="btn-delete" onclick="deleteTodo(${item.idx})">
                <i class="bi bi-trash"></i>
            </button>
        </li>`
        todoList.innerHTML += todoItem
}

document.addEventListener('DOMContentLoaded', getTodoList)
todoForm.addEventListener('submit', async(e) => {
    e.preventDefault();
    addTodo();
})