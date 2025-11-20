const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

const API_URL = 'http://127.0.0.1:5000'; // The address of the Flask server

// 页面加载时显示欢迎消息
window.addEventListener('DOMContentLoaded', function() {
    showWelcomeMessage();
});

// 显示欢迎消息
function showWelcomeMessage() {
    fetch(`${API_URL}/welcome`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.message) {
                appendMessage('agent-message', data.message);
            }
        })
        .catch(error => {
            console.error('Error fetching welcome message:', error);
            // 如果API调用失败，显示默认欢迎消息
            const defaultWelcome = `👋 欢迎使用图书推荐Agent！

📚 我可以帮助您：
   • 搜索图书信息
   • 基于您浏览的图书推荐相似图书
   • 根据您的阅读偏好推荐图书
   • 分析您的阅读趋势
   • 提供个性化的图书推荐

💬 请告诉我您需要什么帮助吧！`;
            appendMessage('agent-message', defaultWelcome);
        });
}

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
    
    // 禁用输入框和按钮
    userInput.disabled = true;
    sendButton.disabled = true;
    
    // 显示"正在生成中"提示
    const typingIndicator = showTypingIndicator();

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
        // 移除"正在生成中"提示
        removeTypingIndicator(typingIndicator);
        
        if (data.response) {
            appendMessage('agent-message', data.response);
        } else if (data.error) {
            appendMessage('agent-message', `Error: ${data.error}`);
        }
    })
    .catch(error => {
        // 移除"正在生成中"提示
        removeTypingIndicator(typingIndicator);
        
        console.error('Error:', error);
        appendMessage('agent-message', `Sorry, a connection error occurred: ${error.message}`);
    })
    .finally(() => {
        // 重新启用输入框和按钮
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    });
}

// 显示"正在生成中"提示
function showTypingIndicator() {
    const messageElement = document.createElement('div');
    messageElement.className = 'message agent-message typing-indicator';
    messageElement.id = 'typing-indicator';
    
    const bubble = document.createElement('div');
    bubble.className = 'bubble typing-bubble';
    bubble.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div><span class="typing-text">正在生成中...</span>';
    
    messageElement.appendChild(bubble);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    return messageElement;
}

// 移除"正在生成中"提示
function removeTypingIndicator(indicator) {
    if (indicator && indicator.parentNode) {
        indicator.parentNode.removeChild(indicator);
    }
}

// 格式化消息文本，优化排版
function formatMessage(text) {
    if (!text) return '';
    
    // 转义HTML特殊字符，防止XSS攻击
    const escapeHtml = (str) => {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    };
    
    // 按行分割文本
    const lines = text.split('\n');
    const formattedLines = [];
    let lastWasTitle = false;
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const trimmedLine = line.trim();
        
        // 忽略空行，直接跳过
        if (!trimmedLine) {
            continue;
        }
        
        // 转义HTML
        const escapedLine = escapeHtml(trimmedLine);
        
        // 检查是否是标题（以emoji开头）
        const isTitle = /^[📚💬👋📖🎯🔍🎉✅❌⚠️💡🔧📝🌐🧠👤🔄📊]+/.test(trimmedLine);
        
        // 如果不是第一行，添加换行
        if (formattedLines.length > 0) {
            formattedLines.push('<br>');
        }
        
        if (isTitle) {
            formattedLines.push(`<span class="message-title">${escapedLine}</span>`);
            lastWasTitle = true;
        }
        // 检查是否是列表项（以 •、-、· 等开头）
        else if (/^[•·▪▫-]\s+/.test(trimmedLine)) {
            formattedLines.push(`<span class="list-item">${escapedLine}</span>`);
            lastWasTitle = false;
        }
        // 普通文本
        else {
            formattedLines.push(escapedLine);
            lastWasTitle = false;
        }
    }
    
    // 用 <br> 连接所有行，直接换行，不添加额外空行
    return formattedLines.join('');
}

function appendMessage(className, message) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;
    
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    
    // 使用格式化后的HTML内容
    bubble.innerHTML = formatMessage(message);
    
    messageElement.appendChild(bubble);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}