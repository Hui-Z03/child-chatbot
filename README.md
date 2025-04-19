# child-chatbot
Mandarin (non-native) chatbot for children，儿童普通话（非母语）聊天机器人

# 普通话 AI 练习助手
# Mandarin AI Speaking Practice

## 介绍 | Introduction
这是一个基于 AI 的普通话口语练习工具，适合 6 岁儿童使用，（母语非中文普通话，但是能听懂简单中文）。   
This is an AI-powered Mandarin speaking practice tool designed for 6-year-old children (native language is not Mandarin, but who can understand simple Chinese).

## AI Language Models
This project supports **ChatGPT** as AI conversation engines.

- **ChatGPT**: Powered by OpenAI gpt-4o-mini (version:2024-07-18), with strong natural language understanding.
- **1k TPM**

- test link: [child-chatbot](child-chatbot-aneahubvf9bjgwh3.australiasoutheast-01.azurewebsites.net)


## 技术栈 | Tech Stack
- **后端 | Backend**: Flask (Python)
- **前端 | Frontend**: HTML + JavaScript
- **云服务 | Cloud Services**: Azure Speech API, OpenAI API
- **容器化 | Containerization**: Docker
- **CI/CD**: GitHub Actions

- **tools**: Agent builder for non-coders; Copilot Studio for coders; Copilt Studio + Visual Studio/GitHub for developers
- **Azure AI Agent Service** for single agent; **Semantic Kernel** for multi-agent
  
**Insights and Considerations from an Pilot Study Project:**

The deployment of Azure's OpenAI service has transitioned to "Azure AI Foundry."  Create resources in the Azure portal first and then deploy specific models through Azure AI Foundry.

Limited Quotas: Quotas are limited and vary by region. It's essential to identify suitable deployment regions in advance.

Prompt Token Consumption: Prompts are counted in each interaction, leading to rapid token consumption. Design prompts carefully. (Most S0-tier models have only 1k TPM.)

The Azure user interface updates rapidly, especially concerning AI deployments, which often change. There are also numerous restrictions on tokens and quotas. As a next step, consider exploring open-source models like DeepSeek, which offer more convenient deployment for development purposes and can help reduce costs.

- 14/04/2025
- 参加 MS AI Agent Hackathon 2025; LLM改用github marketplace
