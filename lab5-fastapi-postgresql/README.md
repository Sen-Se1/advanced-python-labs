# 🔥 Lab 5: FastAPI with PostgreSQL - Quiz Application

## 📋 Overview
Learn how to build a **FastAPI application with PostgreSQL** database integration for a complete Quiz Game application.

## 🎯 What You'll Learn
- Connect FastAPI with PostgreSQL using SQLAlchemy
- Create database models and relationships
- Implement CRUD operations with SQLAlchemy ORM
- Build a complete Quiz API with questions and choices
- Use Pydantic models for data validation

## 🚀 Quick Start

### 1. Create Virtual Environment
```bash
python -m venv .venv
```

### 2. Activate Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies & Run
```bash
cd lab5-fastapi-postgresql
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Then open:
- **API Documentation**: http://127.0.0.1:8000/docs

## 📁 Files
- `main.py` - FastAPI application with endpoints
- `database.py` - Database connection configuration
- `models.py` - SQLAlchemy database models
- `requirements.txt` - Dependencies

## 💡 Key Features
- **PostgreSQL Integration** - Robust database connectivity
- **SQLAlchemy ORM** - Object-relational mapping
- **CRUD Operations** - Create, read questions and choices
- **Data Validation** - Pydantic models for request/response
- **Relationship Mapping** - Questions and choices relationship

## 🗄️ Database Setup

### 1. Install PostgreSQL
```bash
# Ubuntu
sudo apt-get install postgresql postgresql-contrib

# macOS with Homebrew
brew install postgresql

# Windows: Download from postgresql.org
```

### 2. Create Database
```sql
-- Connect to PostgreSQL
psql -U postgres

-- Create database
CREATE DATABASE "quizApp";

-- Verify database was created
\l
```

### 3. Update Database Credentials
Make sure your PostgreSQL credentials in `database.py` match your setup:
```python
URL_DATABASE = 'postgresql://postgres:root@localhost:5432/quizApp'
```

## 🐛 Troubleshooting

### Common Issues:

1. **Database Connection Error**:
   - Ensure PostgreSQL is running
   - Check database credentials in `database.py`
   - Verify database `quizApp` exists

2. **Port Already in Use**:
   ```bash
   uvicorn main:app --reload --port 8001
   ```

3. **Virtual Environment Issues**:
   - Create: `python -m venv .venv`
   - Activate: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)

4. **Module Not Found Errors**:
   - Ensure virtual environment is activated
   - Run: `pip install -r requirements.txt`

5. **PostgreSQL Authentication Error**:
   - Check username/password in `database.py`
   - Verify PostgreSQL service is running

6. **Table Creation Issues**:
   - Check database permissions
   - Verify SQLAlchemy models are correct

---

**Previous:** [Lab 4 - Streamlit ←](../lab4-streamlit)

**Next:** [Lab 6 - Web Scraping →](../lab6-web-scraping)

---