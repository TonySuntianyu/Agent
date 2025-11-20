from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from book_agent import BookRecommendationAgent
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Create an instance of the agent
agent = BookRecommendationAgent()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles chat messages from the user.
    """
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    # Get the user_id from the request, or use a default
    user_id = data.get('user_id', 'default_user')

    # Send the message to the agent and get the response
    response = agent.chat(message, user_id)

    return jsonify({'response': response})

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Provides book recommendations based on a given book.
    """
    data = request.get_json()
    book_title = data.get('book_title')
    user_id = data.get('user_id', 'default_user')

    if not book_title:
        return jsonify({'error': 'No book title provided'}), 400

    # Get recommendations from the agent
    recommendations = agent.recommend_books(book_title, user_id)

    return jsonify({'recommendations': recommendations})

@app.route('/welcome', methods=['GET'])
def welcome():
    """
    Returns a welcome message from the agent.
    """
    welcome_message = """👋 欢迎使用图书推荐Agent！

📚 我可以帮助您：
   • 搜索图书信息
   • 基于您浏览的图书推荐相似图书
   • 根据您的阅读偏好推荐图书
   • 分析您的阅读趋势
   • 提供个性化的图书推荐

💬 使用示例：
   • "搜索《三体》"
   • "我看了《活着》，推荐相似图书"
   • "推荐科幻小说"
   • "分析我的阅读偏好"

请告诉我您需要什么帮助吧！"""
    
    return jsonify({'message': welcome_message})

if __name__ == '__main__':
    app.run(debug=True)
