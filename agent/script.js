const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

const API_URL = 'http://127.0.0.1:5000'; // The address of the Flask server

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return;

    appendMessage('user-message', message);
    userInput.value = '';

    fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message, user_id: 'frontend_user' })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.response) {
            appendMessage('agent-message', data.response);
        } else if (data.error) {
            appendMessage('agent-message', `Error: ${data.error}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('agent-message', `Sorry, a connection error occurred: ${error.message}`);
    });
}

function appendMessage(className, message) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;
    
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = message;
    
    messageElement.appendChild(bubble);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}