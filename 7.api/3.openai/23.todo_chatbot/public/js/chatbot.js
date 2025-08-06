const ECHO_MODE = true;

document.addEventListener('DOMContentLoaded', initChatbot);

function initChatbot() {
    createChatbotUI();
    registerEventHandlers();
}


function createChatbotUI() {
    const chatbotHTML = `
        <div class="chatbot-icon" id="chatbotIcon">
            <i class="bi bi-chat-dots-fill"></i>
        </div>
        <div class="chatbot-window" id="chatbotWindow">
            <div class="chatbot-header">
                <span>Chatbot</span>
                <button id="closeChatbot">X</button>
            </div>
            <div class="chatbot-body">
                <div class="chatbot-messages" id="chatbotMessage"></div>
                <div class="chatbot-input-container">
                    <input id="chatbotInput" placeholder="내용 입력">
                    <button id="sendMessage">Send</button>
                </div>
            </div>
        </div>
    `
    document.body.insertAdjacentHTML('beforeend', chatbotHTML) //끝나기 직전에 코드를 넣을 것
}

function registerEventHandlers() {
    const chatbotIcon = document.getElementById('chatbotIcon');
    const chatbotWindow = document.getElementById('chatbotWindow');
    const closeChatbot = document.getElementById('closeChatbot');
    const sendMessage = document.getElementById('sendMessage');
    const chatbotInput = document.getElementById('chatbotInput');

    chatbotIcon.addEventListener('click', () => {
        chatbotIcon.style.display = 'none';
        chatbotWindow.style.display = 'flex';
    })
    closeChatbot.addEventListener('click', () => {
        chatbotIcon.style.display = 'flex';
        chatbotWindow.style.display = 'none';
    })

    sendMessage.addEventListener('click', handlerUserMessage)
    chatbotInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handlerUserMessage()
        }
    })
}

async function handlerUserMessage() {
    const input = document.getElementById('chatbotInput');
    const message = input.value.trim()

    if (!message) return;

    addMessage(message, 'user');

    const botResponse = await sendMessageToServer(message)
    input.value= ''

    addMessage(botResponse, 'bot');
}

function addMessage(message, sender) {
    const container = document.getElementById('chatbotMessage');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = sender === 'user'
        ? `<i class="bi bi-person"></i> ${message}`
        : `<i class="bi bi-robot"></i> ${message}`
    messageElement.classList.add(sender)

    container.appendChild(messageElement);
    container.scrollTop = container.scrollHeight;
}

async function sendMessageToServer(userInput) {
    if (ECHO_MODE) {
        return `[BOT] ${userInput}`
    }

    const res = await fetch('/api/chat', {
        method:'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(userInput)
    })
    const data = await res.json()
    return data.chatbot
}