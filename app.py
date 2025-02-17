from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # load .env 文件，

app = Flask(__name__)

AZURE_CONFIG = {
    "speech_key": os.getenv("AZURE_SPEECH_KEY"),
    "speech_region": os.getenv("AZURE_SPEECH_REGION"),
    "openai_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "openai_key": os.getenv("AZURE_OPENAI_KEY"),
    "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-azure-config")
def get_azure_config():
    return jsonify(
        {
            "key": os.getenv("AZURE_SPEECH_KEY"),
            "region": os.getenv("AZURE_SPEECH_REGION"),
        }
    )


@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    audio_data = request.files["audio"].read()
    # 调用Azure Speech服务进行语音识别
    # 这里需要根据Azure Speech API文档进行实现
    # 返回识别结果
    return jsonify({"text": "recognized text from speech"})


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("text")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {AZURE_CONFIG["openai_key"]}',
    }
    data = {"prompt": user_input}
    response = requests.post(
        f'{AZURE_CONFIG["openai_endpoint"]}/openai/deployments/{AZURE_CONFIG["deployment_name"]}/completions',
        headers=headers,
        json=data,
    )
    response_json = response.json()
    return jsonify({"reply": response_json["choices"][0]["text"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
