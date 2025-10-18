# 🔥 Lab 9: LLM Access with FastAPI & Ollama

## 📋 Overview
Learn how to build a **FastAPI application with local LLM integration** using **Ollama**. Create your own local AI API server that can run completely offline without external API dependencies.

## 🎯 What You'll Learn
- Set up Ollama for local LLM execution
- Integrate local LLMs with FastAPI
- Create chat completion endpoints
- Build a streaming response API
- Manage multiple AI models locally
- Deploy a self-contained AI API server

## 🚀 Quick Start

### 1. Install Ollama
```bash
# Visit https://ollama.ai/ and download Ollama
# Or use these commands:

# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Pull a Model
```bash
# Pull a model (e.g., Llama 3.1 8B)
ollama pull llama3.1:8b

# Or try these models:
# ollama pull codellama:7b
# ollama pull mistral:7b
# ollama pull gemma2:2b
```

### 3. Run the Application
```bash
cd lab9-llm-fastapi-ollama
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Then open:
- **API Documentation**: http://127.0.0.1:8000/docs

## 📁 Files
- `main.py` - FastAPI application with Ollama integration
- `requirements.txt` - Dependencies
- `README.md` - This documentation

## 💡 Key Features
- **Local LLM Execution** - Run AI models completely offline
- **FastAPI Integration** - Professional API endpoints
- **Streaming Responses** - Real-time chat experience
- **Multiple Model Support** - Switch between different LLMs
- **No API Keys Required** - Completely self-hosted
- **Production Ready** - Proper error handling and validation

## 🔧 Ollama Setup

### 1. Installation
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download installer from https://ollama.ai/download
```

### 2. Model Management
```bash
# List available models
ollama list

# Pull a model
ollama pull llama3.1:8b

# Remove a model
ollama rm llama3.1:8b

# Start Ollama service
ollama serve
```

### 3. Available Models
- `llama3.1:8b` - Good balance of performance and resource usage
- `llama3.1:70b` - Higher quality (requires more RAM)
- `mistral:7b` - Fast and efficient
- `codellama:7b` - Specialized for coding
- `gemma2:2b` - Lightweight option

## 🐛 Troubleshooting

### Common Issues:

1. **Ollama Not Found**:
   - Ensure Ollama is installed and in PATH
   - Restart terminal after installation

2. **Model Download Errors**:
   - Check internet connection
   - Verify model name is correct
   - Use `ollama pull <model>` to download

3. **Memory Issues**:
   - Use smaller models (8B or less) for limited RAM
   - Close other memory-intensive applications

4. **Port Conflicts**:
   ```bash
   uvicorn main:app --reload --port 8001
   ```

5. **Ollama Service Not Running**:
   ```bash
   ollama serve
   # Keep this running in a separate terminal
   ```

## ⚠️ System Requirements

- **Minimum**: 8GB RAM, 4GB free disk space
- **Recommended**: 16GB+ RAM, 10GB+ free disk space
- **Storage**: Models are 4-40GB each
- **Internet**: Required only for initial model download

---

**Previous:** [Lab 8 - Crawl4AI ←](../lab8-crawl4ai)

---