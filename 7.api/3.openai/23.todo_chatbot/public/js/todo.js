const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
const textInput = document.getElementById('text-input')

async function getTodoList() {
    const res = await fetch('/api/todo')
    const data = await res.json()
    todoList.innerHTML = ''

    for (item of data.data) {
        const todoItem = `<li>${item.item}<button class="btn-delete" onclick="deleteTodo(${item.idx})"><i class="bi bi-trash"></i></button></li>`
        todoList.innerHTML += todoItem
    }
}

async function addTodo() {
    const body_data = new FormData(todoForm);
    const res = await fetch('/api/todo', {
        method: 'POST',
        body: body_data
    })
    if (res.ok) {
        textInput.value = ''
        getTodoList()
    }
}   

async function deleteTodo(idx) {
    const res = await fetch(`api/todo/${idx}`, {
        method: 'DELETE'
    })
    if (res.ok) {
        getTodoList()
    }
}

document.addEventListener('DOMContentLoaded', getTodoList)
todoForm.addEventListener('submit', async(e) => {
    e.preventDefault();
    addTodo();
})