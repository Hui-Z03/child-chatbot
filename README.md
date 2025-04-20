# **Little Mandarin Buddy: AI Chatbot for Young Learners**

# **童趣话伴：儿童AI中文聊天伙伴**



## Introduction

**Little Mandarin Buddy** is an AI-powered chatbot designed to help young learners from non-Chinese backgrounds—primarily aged 5 to 8—practice speaking Mandarin in a fun, interactive, and supportive way. Through age-appropriate topics, playful prompts, and gentle guidance, the chatbot encourages natural, confidence-building conversations that make language learning engaging and enjoyable.



## AI Language Models

This project uses **GitHub OpenAI GPT-4.1-nano** model to power natural and responsive Mandarin conversations. The lightweight yet capable model is optimized for interactive dialogue, making it ideal for engaging young learners in age-appropriate, AI-guided language practice.



## **Technologies**

- **Backend**: Python 3.12 with Flask
- **Frontend**: HTML + CSS + JavaScript
- **Cloud Services**:
  - Azure Speech API
  - OpenAI API 
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

- ##### **Development Tools**: 

  - Agent Builder 

  - Copilot Studio

  - Copilot Studio + Visual Studio / GitHub 

- ##### **AI Agent Infrastructure**: 

  - Azure AI Agent Service



## **Launch**

**Little Mandarin Buddy** is a web-based application designed to run in a **laptop browser** (not optimized for mobile devices). No installation is required.

To start using the chatbot, simply open the link below in a supported laptop browser:

🌐 [Let’s have fun chatting in Mandarin!](https://child-chatbot-aneahubvf9bjgwh3.australiasoutheast-01.azurewebsites.net/)

This will open the chatbot interface, where children can begin speaking Mandarin with their friendly AI companion right away.

> ✅ Recommended browsers: Chrome or Edge on a laptop.
> 
> 🎤 Make sure your microphone is enabled for voice interaction.



## **Illustrations** of Use Example

[![Screenshot-2025-04-20-213329.png](https://i.postimg.cc/W3ZFLqb2/Screenshot-2025-04-20-213329.png)](https://postimg.cc/r08F5mrb)



## **Project Status & Sources**

### 🚧 Project Status

**Little Mandarin Buddy** is currently **under active development** by a team of four collaborators, each contributing with unique skill sets across backend, frontend, AI integration, and UX design. Together, we’re building an engaging and educational Mandarin chatbot tailored for young non-native speakers.

### 💡 Inspiration

This project was inspired by the **Microsoft AI Agents Hackathon 2025** — a free, three-week virtual event focused on accelerating innovation in AI agent development. We’re leveraging knowledge and best practices from over **20 expert-led sessions** in this Hackathon, and these resources have played a major role in shaping how we think about agent design, natural language flow, and accessible AI-powered experiences for young learners.



## **Motivation**

Many young Chinese language learners, especially those from **non-Chinese linguistic backgrounds** or growing up in **non-Chinese-speaking environments**, face a common challenge:
 While they may learn vocabulary and grammar in the classroom, they often lack real-life opportunities to **practice speaking** Mandarin in a meaningful and engaging way. This project was created to help bridge that gap.

**Little Mandarin Buddy** aims to give children more chances to **actively use spoken Mandarin** outside the classroom, in a safe, fun, and supportive environment. By simulating natural conversations with a friendly AI chatbot, we hope to boost learners’ **confidence**, **fluency**, and **enjoyment** of speaking Mandarin—making the language come alive through everyday practice.



## **Current Challenges**

While **Little Mandarin Buddy** is functional and accessible via laptop browsers, there are still areas for improvement as development continues:

- 📱 **Not Optimized for Mobile**: The chatbot interface is currently designed for laptop use only. Mobile and tablet support is limited, which may restrict accessibility for some users.
- 🎤 **Voice Interaction Consistency**: Microphone permissions and voice input performance may vary slightly across browsers and devices.

We’re actively working on addressing these challenges to make the experience smoother, more accessible, and more inclusive across platforms.



## **Limitations**

While **Little Mandarin Buddy** is a promising prototype, several limitations currently affect its scalability, performance, and cost-efficiency:

### ⚠️ **Quota Constraints**

- **Limited Quotas**: Azure OpenAI service quotas are region-specific and can be quite restrictive. Identifying suitable deployment regions ahead of time is essential to avoid service interruptions.
- **Token Usage Limits**: Most S0-tier models support only **1,000 tokens per minute (TPM)**. Because each prompt and response consumes tokens, usage can add up quickly. Careful **prompt design** is necessary to stay within limits.

### 🔄 **Rapid Platform Changes**

- The **Azure UI and deployment workflows**—especially around AI agents—are updated frequently. This can lead to compatibility issues or unexpected limitations in service behavior, tokens, and quotas.

### 💸 **Development Costs**

- The reliance on proprietary cloud models like GPT-4-1 Nano can become expensive over time, especially during prototyping. As a potential next step, the team is exploring **open-source alternatives** like **DeepSeek**, which allow for **local or self-hosted deployments**—offering more flexibility and reduced costs for development.

### 🧠 **Agent Architecture**

- The chatbot currently runs on a **single-agent instance**, limiting its ability to handle more dynamic or role-based interactions.
- The team is actively exploring tools like **Semantic Kernel** to learn how to orchestrate **multi-agent systems**, enabling more complex and adaptive conversations in the future.



## **Future Enhancements**

As development continues, the team envisions several key improvements to make **Little Mandarin Buddy** more inclusive, engaging, and ethical for young learners:

### 🎯 **Multi-Level Learning Support**

- Introduce **different difficulty levels** to cater to a wider range of learners—from complete beginners to more advanced young speakers.
- Adapt vocabulary, sentence structure, and conversation themes based on the learner’s proficiency and progress.

### 🎨 **Improved Child-Friendly UI**

- Redesign the interface with **more engaging visuals**, animations, and intuitive interactions tailored to children aged 5–8.
- Enhance accessibility features, such as larger buttons, clearer audio prompts, and visual cues for non-readers.

### 🛡️ **Ethical Language Use & Safety**

- Continue refining the AI’s **language use** to ensure all conversations remain **age-appropriate**, **culturally respectful**, and **safe**.
- Incorporate **usage monitoring**, **parental controls**, and **ethical guidelines** in line with best practices for AI use with children.

These future enhancements aim to create a more personalized, supportive, and responsible learning experience—making Mandarin learning both fun and safe for young users.
