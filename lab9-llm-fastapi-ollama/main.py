from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import requests
import json

# =============================================================================
# FASTAPI SETUP
# =============================================================================

app = FastAPI(
    title="Local LLM API with Ollama",
    description="A FastAPI server that integrates with local Ollama LLMs",
    version="1.0.0"
)

# Ollama API configuration
OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.1:8b"

# =============================================================================
# PYDANTIC MODELS
# =============================================================================

class ChatMessage(BaseModel):
    role: str  # 'user', 'assistant', 'system'
    content: str

class ChatRequest(BaseModel):
    model: str = DEFAULT_MODEL
    messages: List[ChatMessage]
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    stream: bool = False

class ChatResponse(BaseModel):
    model: str
    message: ChatMessage
    total_duration: Optional[int] = None
    load_duration: Optional[int] = None
    prompt_eval_count: Optional[int] = None
    eval_count: Optional[int] = None

class ModelInfo(BaseModel):
    name: str
    modified_at: str
    size: int
    digest: str

class HealthCheck(BaseModel):
    status: str
    ollama_available: bool
    available_models: List[str] = []

# =============================================================================
# OLLAMA CLIENT FUNCTIONS
# =============================================================================

def check_ollama_health() -> bool:
    """Check if Ollama is running and accessible"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        return response.status_code == 200
    except:
        return False

def get_available_models() -> List[str]:
    """Get list of available Ollama models"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        if response.status_code == 200:
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        return []
    except:
        return []

def generate_chat_completion(chat_request: ChatRequest) -> Dict[str, Any]:
    """Generate chat completion using Ollama"""
    try:
        # Prepare the request for Ollama
        ollama_payload = {
            "model": chat_request.model,
            "messages": [msg.dict() for msg in chat_request.messages],
            "stream": chat_request.stream,
            "options": {
                "temperature": chat_request.temperature,
            }
        }
        
        if chat_request.max_tokens:
            ollama_payload["options"]["num_predict"] = chat_request.max_tokens
        
        # Make request to Ollama
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json=ollama_payload,
            timeout=60
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Ollama API error: {response.text}"
            )
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama service unavailable: {str(e)}"
        )

def generate_completion(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Generate simple text completion"""
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            raise Exception(f"Ollama error: {response.text}")
            
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama service unavailable: {str(e)}"
        )

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    """Root endpoint with welcome message"""
    return {
        "message": "Local LLM API Server",
        "status": "running",
        "ollama_available": check_ollama_health()
    }

@app.get("/health", response_model=HealthCheck)
async def health_check():
    """Health check endpoint"""
    ollama_healthy = check_ollama_health()
    models = get_available_models() if ollama_healthy else []
    
    return HealthCheck(
        status="healthy" if ollama_healthy else "degraded",
        ollama_available=ollama_healthy,
        available_models=models
    )

@app.get("/models")
async def list_models():
    """List available Ollama models"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to fetch models from Ollama"
            )
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Ollama service unavailable"
        )

@app.post("/chat", response_model=ChatResponse)
async def chat_completion(chat_request: ChatRequest):
    """Chat completion endpoint"""
    result = generate_chat_completion(chat_request)
    
    return ChatResponse(
        model=result.get("model", chat_request.model),
        message=ChatMessage(
            role="assistant",
            content=result["message"]["content"]
        ),
        total_duration=result.get("total_duration"),
        load_duration=result.get("load_duration"),
        prompt_eval_count=result.get("prompt_eval_count"),
        eval_count=result.get("eval_count")
    )

@app.post("/generate")
async def text_completion(
    prompt: str,
    model: str = DEFAULT_MODEL,
    max_tokens: Optional[int] = None
):
    """Simple text completion endpoint"""
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        if max_tokens:
            payload["options"] = {"num_predict": max_tokens}
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Ollama error: {response.text}"
            )
            
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama service unavailable: {str(e)}"
        )

@app.post("/chat/stream")
async def chat_completion_stream(chat_request: ChatRequest):
    """Streaming chat completion endpoint"""
    try:
        # Prepare streaming request
        ollama_payload = {
            "model": chat_request.model,
            "messages": [msg.dict() for msg in chat_request.messages],
            "stream": True,
            "options": {
                "temperature": chat_request.temperature,
            }
        }
        
        if chat_request.max_tokens:
            ollama_payload["options"]["num_predict"] = chat_request.max_tokens
        
        # Make streaming request to Ollama
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json=ollama_payload,
            stream=True,
            timeout=60
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Ollama API error: {response.text}"
            )
        
        # Return streaming response
        def generate():
            for line in response.iter_lines():
                if line:
                    yield f"data: {line.decode()}\n\n"
        
        return generate()
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama service unavailable: {str(e)}"
        )

# =============================================================================
# EXAMPLE USAGE ENDPOINTS
# =============================================================================

@app.post("/examples/translate")
async def translate_text(
    text: str,
    target_language: str,
    model: str = DEFAULT_MODEL
):
    """Example: Translate text to target language"""
    prompt = f"Translate the following text to {target_language}. Only provide the translation, no additional text:\n\n{text}"
    
    translation = generate_completion(prompt, model)
    return {
        "original_text": text,
        "translated_text": translation.strip(),
        "target_language": target_language,
        "model": model
    }

@app.post("/examples/summarize")
async def summarize_text(
    text: str,
    model: str = DEFAULT_MODEL
):
    """Example: Summarize text"""
    prompt = f"Please provide a concise summary of the following text:\n\n{text}"
    
    summary = generate_completion(prompt, model)
    return {
        "original_text": text,
        "summary": summary.strip(),
        "model": model
    }

@app.post("/examples/code-explanation")
async def explain_code(
    code: str,
    model: str = DEFAULT_MODEL
):
    """Example: Explain code"""
    prompt = f"Explain what this code does in simple terms:\n\n```python\n{code}\n```"
    
    explanation = generate_completion(prompt, model)
    return {
        "code": code,
        "explanation": explanation.strip(),
        "model": model
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI with Ollama Server...")
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("🔍 Health Check: http://127.0.0.1:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000)