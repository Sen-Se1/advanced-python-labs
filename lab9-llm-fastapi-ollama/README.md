# 🔥 Lab 9: LLM Access with FastAPI and Ollama

## 📋 Overview
Learn to build and secure APIs for Large Language Model access using **FastAPI** and **Ollama**. Implement API key authentication, credit systems, and containerized deployment for controlled AI model access.

## 🎯 What You'll Learn
- Build secure REST APIs with FastAPI
- Implement API key authentication and authorization  
- Create credit-based usage tracking systems
- Integrate with local LLMs via Ollama
- Containerize applications with Docker
- Deploy AI APIs to cloud platforms
- Set up environment-based configuration

## 🚀 Quick Start

```bash
cd lab9-llm-fastapi-ollama
pip install -r requirements.txt

# Create .env file with your API key
echo "API_KEY=your_secret_key_here" > .env
uvicorn main:app --reload

# Test the API (in another terminal)
curl -X POST "http://localhost:8000/generate?prompt=Hello%20World" \
     -H "x-api-key: your_secret_key_here"
```

## 📁 Project Files
- `main.py` - FastAPI application with authentication and credit system
- `requirements.txt` - Python dependencies (FastAPI, Ollama, Uvicorn, python-dotenv)
- `Dockerfile` - Container configuration for deployment
- `.env` - Environment variables for API keys (create this file)
- `README.md` - This documentation file

## 💡 Key Features
- **🔒 API Security** - Key-based authentication with dependency injection
- **💳 Credit System** - Usage tracking and limits with in-memory storage
- **🐳 Docker Ready** - Containerized deployment with environment variables
- **🤖 Ollama Integration** - Local LLM access with model support
- **⚡ Fast Performance** - Async FastAPI framework with automatic docs
- **🔧 DevOps Ready** - Environment-based configuration and containerization

## 🐳 Docker Deployment

### Build and Run Locally
```bash
# Build the Docker image
docker build -t llm-api .

# Run the container with environment variables
docker run -p 8000:8000 --env-file .env llm-api
```

---

**Previous:** [Lab 8 - Crawl4AI ←](../lab8-crawl4AI)

**Next:** [Lab 10 - Machine Learning →](../lab10-machine-learning)

---