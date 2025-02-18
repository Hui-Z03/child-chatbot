from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Azure configuration settings
AZURE_CONFIG = {
    "speech_key": os.getenv("AZURE_SPEECH_KEY"),
    "speech_region": os.getenv("AZURE_SPEECH_REGION"),
    "openai_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "openai_key": os.getenv("AZURE_OPENAI_KEY"),
    "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
}

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=AZURE_CONFIG["openai_endpoint"],
    api_key=AZURE_CONFIG["openai_key"],
    api_version="2024-05-01-preview",
)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to get Azure configuration
@app.route("/get-azure-config")
def get_azure_config():
    return jsonify(
        {"key": AZURE_CONFIG["speech_key"], "region": AZURE_CONFIG["speech_region"]}
    )

# Route for speech-to-text conversion
@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    audio_data = request.files["audio"].read()
    # Call Azure Speech service for speech recognition
    # Implement according to Azure Speech API documentation
    return jsonify({"text": "recognized text from speech"})

# Route for chat interaction
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("text")
        chat_prompt = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "你是6岁孩子的中文老师。",
                    }
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": user_input}]},
        ]

        # Generate chat completion using Azure OpenAI
        completion = client.chat.completions.create(
            model=AZURE_CONFIG["deployment_name"],
            messages=chat_prompt,
            max_tokens=500,
            temperature=0.5,
            top_p=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.1,
        )

        response_text = completion.choices[0].message.content
        return jsonify({"reply": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
