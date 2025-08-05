document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const userInputForm = document.getElementById('user-input-form');
    const userInputField = document.getElementById('user-input');
    const indicator = document.getElementById('load-indicator');

    userInputForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const userInput = userInputField.value;
        appendMessage('user', userInput)
        userInputField.value = ''

        loadingIndicator(true);
        const chatGPTResponse = await getChatGPTResponse(userInput);
        loadingIndicator(false);
        
        appendMessage('chatgpt', chatGPTResponse)
    })

    function appendMessage(role, content) {
        messageDiv = document.createElement('div');
        messageDiv.textContent = content;
        messageDiv.classList.add('message', role)
        chatContainer.appendChild(messageDiv);
        scrollToBottom();
    }
    async function getChatGPTResponse(userInput) {
        const res = await fetch('/api/chat', {
            method:'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({"userInput":userInput})
        })
        
        const data = await res.json()
        console.log(data)
        return data.response
    }
    function loadingIndicator(status) {
        if (status) {
            indicator.style.display = 'block';
        } else {
            indicator.style.display = 'none';
        }
    }
    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
})
