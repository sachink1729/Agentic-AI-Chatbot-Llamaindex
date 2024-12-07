# Agentic-AI-Chatbot-Llamaindex
Production ready Agentic AI ChatBot using Llamaindex and Groq-Llama 3.3

This repository demonstrates how to build a production-ready Agentic AI chatbot using LlamaIndex and Groq-Llama 3.3. It covers the essential steps to structure, implement, and deploy an AI chatbot capable of using tools and making function calls.

For clear explanation you can refer my article: https://sachinkhandewal.medium.com/a-simple-step-by-step-guide-to-build-production-ready-agentic-ai-chatbot-using-llamaindex-and-6f08e8006114

### What You'll Learn:
1. Demystifying Agentic AI and Agents: Breaking down the hype and understanding the fundamentals of Agentic AI.
2. ReActAgent & FunctionCallingAgent in LlamaIndex: Learn how to use these agents and integrate tools/functions into them.
3. Simple Agentic Function Calls: Implementing and testing a basic agentic function call.
4. Building a Production-Ready Agentic Chatbot: Project structuring and deploying your chatbot with Docker.

### Key Features:
1. Clear explanations of Agentic AI concepts.
2. Practical use of LlamaIndex's ReActAgent and FunctionCallingAgent.
3. Dockerized deployment for a scalable, production-ready solution.
4. Perfect for developers exploring the intersection of AI agents and practical applications.

### To install the requirements use:
```bash
pip install -r requirements.txt
```

### To start the Gradio UI
```bash
python ./simple_ui.py
```

### To start the app
```bash
python ./app.py
```

### Docker Build and Run App
```bash
docker build -t agentic_app .
docker run -p 5000:5000 agentic_app
```

⭐ Star this repo for more updates.

