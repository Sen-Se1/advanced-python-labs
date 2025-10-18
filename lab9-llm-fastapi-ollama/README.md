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

## 🔐 API Implementation

### 1. Basic API Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Starts the FastAPI server with automatic documentation at `http://localhost:8000/docs`

### 2. API Key Authentication  
The API uses header-based authentication:
```python
def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key or No Credits")
    return x_api_key
```

### 3. Credit System Test
```bash
# Test with valid API key (5 credits initially)
curl -X POST "http://localhost:8000/generate?prompt=Hello" -H "x-api-key: your_secret_key"

# Test without API key (should fail)
curl -X POST "http://localhost:8000/generate?prompt=Hello"
```

## 🔧 Technical Implementation

### FastAPI Security Setup
```python
from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

# Track credits per API key
API_KEY_CREDITS = {os.getenv("API_KEY"): 5}
```

### Ollama Integration
```python
@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
    # Deduct credit and call LLM
    API_KEY_CREDITS[api_key] -= 1
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
```

## 📊 API Endpoints

### Generate Text
**POST** `/generate`

**Headers:**
- `x-api-key: your_secret_api_key`

**Parameters:**
- `prompt` (string): Text prompt for the LLM

**Example Request:**
```bash
curl -X POST "http://localhost:8000/generate?prompt=Explain%20AI" \
     -H "x-api-key: your_secret_key"
```

**Response:**
```json
{
  "response": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines..."
}
```

## 🐳 Docker Deployment

### Build and Run Locally
```bash
# Build the Docker image
docker build -t llm-api .

# Run the container with environment variables
docker run -p 8000:8000 --env-file .env llm-api
```

### Dockerfile Configuration
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🚀 Advanced Deployment

### Cloud Deployment Ready
The Dockerized application can be deployed to:
- **AWS ECS/EKS** - Elastic Container Service/Kubernetes Service
- **Google Cloud Run** - Serverless container platform
- **Azure Container Instances** - Quick container deployment
- **Heroku** - Platform as a Service with container support

### Environment Configuration
Create `.env` file:
```env
API_KEY=your_super_secret_api_key_123
```

## 🐛 Troubleshooting

### Common Issues:

1. **Ollama Not Running**:
   ```bash
   # Check if Ollama is installed and running
   ollama list
   
   # Pull the required model
   ollama pull gemma3:1b
   ```

2. **API Key Errors**:
   - Verify `.env` file exists in project root
   - Check `API_KEY` variable is set in `.env`
   - Ensure header name is exactly `x-api-key`

3. **Docker Issues**:
   ```bash
   # Check if Docker is running
   docker --version
   
   # View container logs for debugging
   docker logs <container_name>
   ```

4. **Port Conflicts**:
   ```bash
   # Check what's using port 8000
   lsof -i :8000
   
   # Or use different port
   docker run -p 8001:8000 --env-file .env llm-api
   ```

## ⚠️ Important Notes

- **Security** - Never commit `.env` files to version control
- **Credit System** - Credits reset on server restart (in-memory storage)
- **Resource Usage** - LLMs require significant RAM and CPU resources
- **Model Availability** - Ensure required Ollama models are downloaded
- **Rate Limiting** - Consider implementing request rate limits for production

## 🎯 Use Cases

- **Internal AI Tools** - Secure LLM access within organizations
- **API Services** - Offer LLM capabilities as a service
- **Development** - Prototype AI applications with proper security
- **Education** - Learn API security and AI integration patterns
- **Microservices** - AI components in larger distributed systems

## 🔍 Advanced Features

The current implementation provides foundation for:
- **Multiple API Keys** - Extend to support multiple users/teams
- **Persistent Storage** - Database integration for credit tracking
- **Rate Limiting** - Request throttling and usage quotas
- **Model Selection** - Dynamic model switching via API parameters
- **Batch Processing** - Handle multiple prompts efficiently
- **Monitoring** - Usage analytics and performance metrics
- **WebSocket Support** - Real-time streaming responses

---

**Previous:** [Lab 8 - Crawl4AI ←](../lab8-crawl4ai)

**Next:** [Lab 10 - Machine Learning →](../lab10-machine-learning)

---