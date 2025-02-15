from flask import Flask, render_template
from dotenv import load_dotenv

# import os

load_dotenv()  # load .env 文件，

# #test key and reg
# azure_key = os.getenv("AZURE_SPEECH_KEY")
# azure_region = os.getenv("AZURE_REGION")
# print(f"Azure Key: {azure_key}")
# print(f"Azure Region: {azure_region}")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
