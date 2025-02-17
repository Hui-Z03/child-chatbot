from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import requests
import base64
from openai import AzureOpenAI

load_dotenv()  # load .env 文件，

app = Flask(__name__)

AZURE_CONFIG = {
    "speech_key": os.getenv("AZURE_SPEECH_KEY"),
    "speech_region": os.getenv("AZURE_SPEECH_REGION"),
    "openai_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "openai_key": os.getenv("AZURE_OPENAI_KEY"),
    "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
}

# Initialize Azure OpenAI Service client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=AZURE_CONFIG["openai_endpoint"],
    api_key=AZURE_CONFIG["openai_key"],
    api_version="2024-05-01-preview",
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-azure-config")
def get_azure_config():
    return jsonify(
        {"key": AZURE_CONFIG["speech_key"], "region": AZURE_CONFIG["speech_region"]}
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
    try:
        user_input = request.json.get("text")
        print(f"User input: {user_input}")  # 添加调试信息
        chat_prompt = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "你是一位耐心、热情的中文老师。你的任务是和孩子进行互动对话，帮助他练习中文。\n注意：\n1. 使用简单词汇和句子，不要用长句。\n2. 用温柔、鼓励的语气。\n3. 询问孩子的名字、兴趣爱好，让对话显得自然亲切。",
                    }
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": user_input}]},
        ]

        completion = client.chat.completions.create(
            model=AZURE_CONFIG["deployment_name"],
            messages=chat_prompt,
            max_tokens=500,
            temperature=0.5,
            top_p=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.1,
            stop=None,
            stream=False,
        )

        print(f"Completion: {completion}")  # 添加调试信息
        response_text = completion.choices[0].message.content
        print(f"Response text: {response_text}")  # 添加调试信息
        return jsonify({"reply": response_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
