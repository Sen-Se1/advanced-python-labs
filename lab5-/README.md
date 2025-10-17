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

### Prerequisites
- PostgreSQL installed and running
- Database named `quizApp` created

```bash
# Create and activate virtual environment
python -m venv myenv

# Activate virtual environment:
Windows: myenv\Scripts\activate
macOS/Linux: source myenv/bin/activate

# Install dependencies
cd lab5-fastapi-postgresql
pip install -r requirements.txt

# Run the application
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

---

**Previous:** [Lab 4 - Streamlit ←](../lab4-streamlit)

---

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

## 🎮 Testing the API

### Create a Question with Choices:
```bash
curl -X POST "http://127.0.0.1:8000/questions/" \
     -H "Content-Type: application/json" \
     -d '{
       "question_text": "What is the best Python Framework?",
       "choices": [
         {"choice_text": "FastAPI", "is_correct": true},
         {"choice_text": "Flask", "is_correct": false},
         {"choice_text": "Django", "is_correct": false}
       ]
     }'
```

### Get a Question:
```bash
curl -X GET "http://127.0.0.1:8000/questions/1"
```

### Get Choices for a Question:
```bash
curl -X GET "http://127.0.0.1:8000/choices/1"
```

## 📋 Features Implemented

✅ **FastAPI Setup** - Complete application structure  
✅ **PostgreSQL Connection** - SQLAlchemy database integration  
✅ **Database Models** - Questions and choices with relationships  
✅ **CRUD Endpoints** - Create questions and fetch data  
✅ **Data Validation** - Pydantic models for requests  
✅ **Error Handling** - Proper HTTP exceptions  
✅ **Interactive Documentation** - Auto-generated Swagger UI  

## 🛠 Requirements

```txt
fastapi>=0.104.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
uvicorn>=0.24.0
pydantic>=2.0.0
```

## 🔧 Application Structure

The app includes:
- **Database Models** - Questions and Choices with foreign key relationship
- **API Endpoints**:
  - `POST /questions/` - Create new questions with choices
  - `GET /questions/{id}` - Get specific question
  - `GET /choices/{question_id}` - Get choices for a question
- **Data Validation** - Pydantic models for request validation
- **Database Dependency** - SQLAlchemy session management

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

3. **Virtual Environment Not Activated**:
   - Make sure you see `(myenv)` in your terminal
   - Reactivate with: `source myenv/bin/activate` (macOS/Linux) or `myenv\Scripts\activate` (Windows)
