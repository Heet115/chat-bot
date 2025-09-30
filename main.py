from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Gemini client
client = genai.Client()

# Simple conversation memory (store in memory for demo)
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    text = data.get('data')
    user_input = text
    
    try:
        # Add user input to conversation history
        conversation_history.append(f"User: {user_input}")
        
        # Create context from conversation history (last 10 messages)
        context = "\n".join(conversation_history[-10:]) if conversation_history else ""
        prompt = f"{context}\nUser: {user_input}\nAssistant:"
        
        # Generate response using Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        output = response.text
        
        # Add assistant response to conversation history
        conversation_history.append(f"Assistant: {output}")
        
        return jsonify({"response": True, "message": output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message": error_message, "response": False})
    
if __name__ == '__main__':
    app.run()
