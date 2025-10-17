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

---

## 📚 Labs Overview

| Lab | Topic | Description |
|-----|--------|-------------|
| **Lab 1** | Pydantic | Learn how to create and validate data models using Pydantic |
| **Lab 2** | Requests | Practice sending HTTP requests and interacting with APIs |
| **Lab 3** | FastAPI | Build a RESTful API using FastAPI and Pydantic models |
| **Lab 4** | Streamlit | Create interactive web apps for data science and ML |

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

---

## 🎯 Course Progression
1. **Data Validation** → Master Pydantic for robust data modeling
2. **API Communication** → Learn Requests for HTTP interactions  
3. **Web API Development** → Build FastAPI applications
4. **Web Applications** → Create interactive Streamlit apps

---

**Houssem Mbarki**  
*Advanced Python — [TeknoLabs](https://docs.teknolabs.net/courses/advanced-python)*