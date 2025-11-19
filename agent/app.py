from flask import Flask, request, jsonify
from flask_cors import CORS
from book_agent import BookRecommendationAgent

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create an instance of the agent
agent = BookRecommendationAgent()

@app.route('/')
def index():
    return "Book Recommendation Agent is running!"

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

if __name__ == '__main__':
    app.run(debug=True)
