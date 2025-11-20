const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const conversationList = document.getElementById('conversation-list');
const newChatButton = document.getElementById('new-chat-button');

const API_URL = 'http://127.0.0.1:5000'; // The address of the Flask server

// 会话管理
let currentConversationId = null;
const STORAGE_KEY = 'book_agent_conversations';

// 初始化
window.addEventListener('DOMContentLoaded', function() {
    loadConversations();
    createNewConversation();
});

// 从localStorage加载会话列表
function loadConversations() {
    const conversations = getConversations();
    renderConversationList(conversations);
}

// 获取所有会话
function getConversations() {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data) : {};
}

// 保存会话
function saveConversations(conversations) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(conversations));
}

// 获取会话消息
function getConversationMessages(conversationId) {
    const conversations = getConversations();
    return conversations[conversationId]?.messages || [];
}

// 保存消息到会话
function saveMessageToConversation(conversationId, className, message) {
    const conversations = getConversations();
    if (!conversations[conversationId]) {
        conversations[conversationId] = {
            id: conversationId,
            title: '新对话',
            messages: [],
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
    }
    
    conversations[conversationId].messages.push({
        className: className,
        message: message,
        timestamp: new Date().toISOString()
    });
    
    // 更新会话标题（如果是第一条用户消息）
    if (className === 'user-message') {
        const userMessages = conversations[conversationId].messages.filter(m => m.className === 'user-message');
        if (userMessages.length === 1) {
            // 第一条用户消息作为标题
            conversations[conversationId].title = getConversationTitle(message);
        }
    }
    
    conversations[conversationId].updatedAt = new Date().toISOString();
    saveConversations(conversations);
    renderConversationList(conversations);
}

// 从消息生成会话标题
function getConversationTitle(message) {
    if (message.length <= 20) {
        return message;
    }
    return message.substring(0, 20) + '...';
}

// 渲染会话列表
function renderConversationList(conversations) {
    conversationList.innerHTML = '';
    
    const sortedConversations = Object.values(conversations)
        .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt));
    
    if (sortedConversations.length === 0) {
        const emptyState = document.createElement('div');
        emptyState.className = 'empty-state';
        emptyState.innerHTML = '<p>暂无对话记录</p><p class="empty-hint">点击上方 + 按钮创建新会话</p>';
        conversationList.appendChild(emptyState);
        return;
    }
    
    sortedConversations.forEach(conv => {
        const item = document.createElement('div');
        item.className = 'conversation-item';
        if (conv.id === currentConversationId) {
            item.classList.add('active');
        }
        
        item.innerHTML = `
            <span class="conversation-title" title="${conv.title}">${conv.title}</span>
            <div class="conversation-actions">
                <button class="rename-conversation" data-id="${conv.id}" title="重命名会话">
                    <i class="fas fa-pen"></i>
                </button>
                <button class="delete-conversation" data-id="${conv.id}" title="删除会话">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;
        
        // 点击切换会话
        item.addEventListener('click', (e) => {
            if (!e.target.closest('.delete-conversation') && !e.target.closest('.rename-conversation')) {
                switchConversation(conv.id);
            }
        });
        
        // 重命名会话
        item.querySelector('.rename-conversation').addEventListener('click', (e) => {
            e.stopPropagation();
            renameConversation(conv.id);
        });
        
        // 删除会话
        item.querySelector('.delete-conversation').addEventListener('click', (e) => {
            e.stopPropagation();
            deleteConversation(conv.id);
        });
        
        conversationList.appendChild(item);
    });
}

// 创建新会话
function createNewConversation() {
    const conversationId = 'conv_' + Date.now();
    currentConversationId = conversationId;
    
    // 清空聊天框
    chatBox.innerHTML = '';
    
    // 显示欢迎消息
    showWelcomeMessage();
    
    // 更新会话列表
    loadConversations();
}

// 切换会话
function switchConversation(conversationId) {
    currentConversationId = conversationId;
    
    // 清空聊天框
    chatBox.innerHTML = '';
    
    // 加载会话消息
    const messages = getConversationMessages(conversationId);
    messages.forEach(msg => {
        appendMessage(msg.className, msg.message, false); // false表示不保存到localStorage
    });
    
    // 更新会话列表高亮
    loadConversations();
    
    // 滚动到底部
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 删除会话
function deleteConversation(conversationId) {
    if (confirm('确定要删除这个对话记录吗？')) {
        const conversations = getConversations();
        delete conversations[conversationId];
        saveConversations(conversations);
        
        // 如果删除的是当前会话，创建新会话
        if (conversationId === currentConversationId) {
            createNewConversation();
        } else {
            loadConversations();
        }
    }
}

// 新建会话按钮
newChatButton.addEventListener('click', createNewConversation);

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
                appendMessage('agent-message', data.message, true);
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
            appendMessage('agent-message', defaultWelcome, true);
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

    appendMessage('user-message', message, true);
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
            appendMessage('agent-message', data.response, true);
        } else if (data.error) {
            appendMessage('agent-message', `Error: ${data.error}`, true);
        }
    })
    .catch(error => {
        // 移除"正在生成中"提示
        removeTypingIndicator(typingIndicator);
        
        console.error('Error:', error);
        appendMessage('agent-message', `Sorry, a connection error occurred: ${error.message}`, true);
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

function appendMessage(className, message, saveToStorage = true) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;
    
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    
    // 使用格式化后的HTML内容
    bubble.innerHTML = formatMessage(message);
    
    messageElement.appendChild(bubble);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
    
    // 保存到localStorage
    if (saveToStorage && currentConversationId) {
        saveMessageToConversation(currentConversationId, className, message);
    }
}

// 重命名会话
function renameConversation(conversationId) {
    const conversations = getConversations();
    const conversation = conversations[conversationId];
    if (!conversation) return;
    
    const currentTitle = conversation.title || '新对话';
    const newTitle = prompt('请输入新的会话名称', currentTitle);
    if (newTitle === null) return; // 用户取消
    
    const trimmed = newTitle.trim();
    if (!trimmed) {
        alert('会话名称不能为空');
        return;
    }
    
    conversation.title = trimmed.substring(0, 50);
    conversation.updatedAt = new Date().toISOString();
    saveConversations(conversations);
    renderConversationList(conversations);
}
