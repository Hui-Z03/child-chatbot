from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Azure Speech configuration
AZURE_CONFIG = {
    "speech_key": os.getenv("AZURE_SPEECH_KEY"),
    "speech_region": os.getenv("AZURE_SPEECH_REGION"),
}

# GitHub GPT-4.1 Nano configuration
GITHUB_CONFIG = {
    "endpoint": "https://models.github.ai/inference",
    "model": "openai/gpt-4.1-nano",
    "token": os.getenv("GITHUB_TOKEN"),
}

# Initialize GitHub ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint=GITHUB_CONFIG["endpoint"],
    credential=AzureKeyCredential(GITHUB_CONFIG["token"]),
)

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Route to get Azure Speech configuration
@app.route("/get-azure-config")
def get_azure_config():
    return jsonify(
        {"key": AZURE_CONFIG["speech_key"], "region": AZURE_CONFIG["speech_region"]}
    )

# Route for speech-to-text conversion using Azure Speech
@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    audio_data = request.files["audio"].read()
    # TODO: Implement Azure Speech API call for speech recognition
    return jsonify({"text": "recognized text from speech"})

# Route for chat interaction using GitHub GPT-4.1 Nano
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("text")
        chat_prompt = [
            SystemMessage("你是幼儿园的中文老师，陪我练习中文口语。"),
            UserMessage(user_input),
        ]

        # Call GitHub GPT-4.1 Nano API for chat completion
        response = client.complete(
            messages=chat_prompt,
            temperature=0.5,
            top_p=0.9,
            model=GITHUB_CONFIG["model"],
        )

        # Extract the reply from the response
        response_text = response.choices[0].message.content
        return jsonify({"reply": response_text})
    except Exception as e:
        # Log the error to the console for debugging
        print(f"Error in /chat route: {e}")
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)