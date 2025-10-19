# 🐍 Advanced Python Labs  
**Author:** Houssem Mbarki  

---

## 🔥 Advanced Python Course Introduction

Welcome to the **Advanced Python** course — a hands-on, project-driven journey designed to elevate your Python skills and unlock the powerful tools used in modern software development, data science, and AI integration.

In this course, we go beyond the basics and explore the Python ecosystem that enables you to build APIs, web applications, automation tools, and intelligent systems with real-world impact.

---

## 🧠 What You'll Learn
Throughout the course, you'll dive deep into the following advanced topics:

- **Pydantic** – for robust data validation and settings management  
- **Requests** – for seamless communication with APIs and web services  
- **FastAPI** – a high-performance framework for building APIs with modern Python  
- **Streamlit** – for creating interactive web apps for data science and ML
- **PostgreSQL** – for database integration with FastAPI applications
- **Web Scraping** – for extracting and analyzing data from websites
- **LangChain** – for building AI applications with large language models
- **Crawl4AI** – for advanced web crawling and data extraction
- **LLM Access with FastAPI & Ollama** – for building secure AI APIs with authentication
- **Machine Learning with FastAPI & Render** – build, deploy, and monitor ML services in the cloud

---

## 📚 Labs Overview

| Lab | Topic | Description |
|-----|--------|-------------|
| **Lab 1** | Pydantic | Learn how to create and validate data models using Pydantic |
| **Lab 2** | Requests | Practice sending HTTP requests and interacting with APIs |
| **Lab 3** | FastAPI | Build a RESTful API using FastAPI and Pydantic models |
| **Lab 4** | Streamlit | Create interactive web apps for data science and ML |
| **Lab 5** | FastAPI + PostgreSQL | Build a complete Quiz API with database integration |
| **Lab 6** | Web Scraping | Extract and analyze data from websites |
| **Lab 7** | LangChain | Build AI applications with LLMs and agents |
| **Lab 8** | Crawl4AI | Advanced web crawling with parallel processing |
| **Lab 9** | LLM Access with FastAPI & Ollama | Build secure AI APIs with authentication and credit systems |
| **Lab 10** | Machine Learning – FastAPI Music Recommender | Train, containerize, automate, and deploy an ML prediction API on Render |

---

## 📂 Repository Structure
```
advanced-python-labs/
├── lab1-pydantic/
│   ├── pydantic_tutorial.py
│   ├── README.md
│   └── requirements.txt
├── lab2-requests/
│   ├── examples.py
│   ├── README.md
│   └── requirements.txt
├── lab3-fastapi/
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── lab4-streamlit/
│   ├── main.py
│   ├── movies.csv
│   ├── pages/
│   │   ├── 1_profile.py
│   │   └── 2_dashboard.py
│   ├── README.md
│   └── requirements.txt
├── lab5-fastapi-postgresql/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── README.md
│   └── requirements.txt
├── lab6-web-scraping/
│   ├── scraper.py
│   ├── README.md
│   └── requirements.txt
├── lab7-langchain/
│   ├── langchain_tutorial.py
│   ├── README.md
│   ├── requirements.txt
│   └── .env (create this file)
├── lab8-crawl4ai/
│   ├── parallel_crawling.py
│   ├── sequential_crawling.py
│   ├── single_page_crawl.py
│   ├── README.md
│   └── requirements.txt
├── lab9-llm-fastapi-ollama/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── README.md
│   └── .env (create this file)
├── lab10-machine-learning/
│   ├── MusicRecommender.ipynb
│   ├── music.csv
│   ├── music_recommender.joblib
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md
```

---

## 🧩 How to Run Each Lab

### ▶️ Lab 1 – Pydantic
```bash
cd lab1-pydantic
pip install -r requirements.txt
python pydantic_tutorial.py
```

### 🌐 Lab 2 – Requests
```bash
cd lab2-requests
pip install -r requirements.txt
python examples.py
```

### ⚡ Lab 3 – FastAPI
```bash
cd lab3-fastapi
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 📊 Lab 4 – Streamlit
```bash
cd lab4-streamlit
pip install -r requirements.txt
streamlit run main.py
```

### 🗄️ Lab 5 – FastAPI + PostgreSQL
```bash
cd lab5-fastapi-postgresql
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 🌐 Lab 6 – Web Scraping
```bash
cd lab6-web-scraping
pip install -r requirements.txt
python scraper.py
```

### 🤖 Lab 7 – LangChain
```bash
cd lab7-langchain
pip install -r requirements.txt

# Create .env file with your Groq API key
echo "GROQ_API_KEY=your_actual_api_key_here" > .env

python langchain_tutorial.py
```

### 🕷️ Lab 8 – Crawl4AI
```bash
cd lab8-crawl4ai
pip install -r requirements.txt

# Run single page crawl
python single_page_crawl.py

# Run sequential crawling
python sequential_crawling.py

# Run parallel crawling
python parallel_crawling.py
```

### 🔒 Lab 9 – LLM Access with FastAPI & Ollama
```bash
cd lab9-llm-fastapi-ollama
pip install -r requirements.txt

# Create .env file with your API key
echo "API_KEY=your_secret_key_here" > .env

# Run the API server
uvicorn main:app --reload --port 8000

# Test the API (in another terminal)
curl -X POST "http://localhost:8000/generate?prompt=Hello%20World" -H "x-api-key: your_secret_key_here"

# Or run with Docker
docker build -t llm-api .
docker run -p 8000:8000 --env-file .env llm-api
```

### 🎵 Lab 10 – Machine Learning – FastAPI Music Recommender

```bash
cd lab10-machine-learning
pip install -r requirements.txt
uvicorn app:app --reload --port 5000
```

Test locally:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 21, "gender": 1}'
```

🌐 **Deployed App:** [https://music-recommender-lab-s22y.onrender.com](https://music-recommender-lab-s22y.onrender.com)


---

## 🎯 Course Progression
1. **Data Validation** → Master Pydantic for robust data modeling
2. **API Communication** → Learn Requests for HTTP interactions  
3. **Web API Development** → Build FastAPI applications
4. **Web Applications** → Create interactive Streamlit apps
5. **Database Integration** → Connect FastAPI with PostgreSQL
6. **Data Extraction** → Master web scraping for data analysis
7. **AI Applications** → Build intelligent systems with LangChain
8. **Advanced Crawling** → Master parallel web crawling with Crawl4AI
9. **Secure AI APIs** → Build authenticated LLM access with FastAPI & Ollama
10. **Machine Learning Deployment** → Build, containerize, and deploy ML apps to Render

---

## 🛠 Prerequisites
- Python 3.8+ installed
- PostgreSQL (for Lab 5)
- Groq API account (for Lab 7) - free tier available
- Ollama installed (for Lab 9) - for local LLM access
- Render account (for Lab 10)
- Basic Git and virtual environment knowledge recommended

---

**Houssem Mbarki**  
*Advanced Python — [TeknoLabs](https://docs.teknolabs.net/courses/advanced-python)*