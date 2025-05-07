from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_msg}]
    )
    return jsonify({"reply": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run()
