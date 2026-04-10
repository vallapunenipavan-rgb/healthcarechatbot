from flask import Flask, request, jsonify
from my_health_carechatbot.agent import root_agent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    try:
        response = root_agent.generate(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Healthcare Chatbot API', 'endpoints': ['/health', '/chat']})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
