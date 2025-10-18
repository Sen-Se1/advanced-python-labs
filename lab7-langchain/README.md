# 🔥 Lab 7: LangChain - AI Application Development

## 📋 Overview
Learn how to build sophisticated AI applications using **LangChain** - a powerful framework for developing applications with large language models (LLMs).

## 🎯 What You'll Learn
- Set up LangChain with Groq API
- Create prompt templates and chains  
- Generate structured outputs with Pydantic
- Build AI agents with reasoning capabilities
- Use environment variables for API keys

## 🚀 Quick Start

```bash
cd lab7-langchain
pip install -r requirements.txt

# Create .env file with your API key
echo "GROQ_API_KEY=your_actual_api_key_here" > .env

python langchain_tutorial.py
```

## 📁 Files
- `langchain_tutorial.py` - Complete LangChain tutorial
- `.env` - Environment variables (create this file)
- `requirements.txt` - Dependencies

## 💡 Key Features
- **Model I/O** - Interface with LLMs using Groq
- **Prompt Templates** - Create reusable prompts with variables
- **Structured Output** - Consistent response formats with Pydantic
- **AI Agents** - Build reasoning engines with search and calculator tools
- **Environment Variables** - Secure API key management

## 🔑 API Setup

### 1. Get Groq API Access
1. Create free account at [Groq](https://groq.com/)
2. Go to API Keys → Create API token
3. Save token securely

### 2. Create .env File
Create a `.env` file in the lab7-langchain directory:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

## 🐛 Troubleshooting

### Common Issues:
1. **API Key Errors**: 
   - Ensure `.env` file exists with correct API key
   - Verify your Groq account has API access

2. **Module Not Found**: 
   - Run `pip install -r requirements.txt`
   - Check all dependencies are installed

3. **Rate Limiting**: 
   - Groq has free tier limits
   - Add delays between requests if needed

4. **Agent Dependencies**:
   - Ensure `duckduckgo-search` and `langchain-community` are installed

## ⚠️ Important Notes

- **Keep API keys secure** - never commit `.env` files to version control
- **Add `.env` to .gitignore** to protect your API keys
- **Respect rate limits** - be mindful of API usage
- **Test with different models** - explore various LLM capabilities

---

**Previous:** [Lab 6 - Web Scraping ←](../lab6-web-scraping)

---