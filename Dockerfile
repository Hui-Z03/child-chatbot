# 使用官方 Python 3.9 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口（Azure Web App 默认使用 80 端口）
EXPOSE 80

# 设置环境变量（可选，也可以在 Azure 门户中配置）
ENV AZURE_SPEECH_KEY=""
ENV AZURE_SPEECH_REGION=""
ENV AZURE_OPENAI_ENDPOINT=""
ENV AZURE_OPENAI_KEY=""
ENV AZURE_OPENAI_DEPLOYMENT_NAME=""

# 使用 gunicorn 启动 Flask 应用
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "2", "app:app"]