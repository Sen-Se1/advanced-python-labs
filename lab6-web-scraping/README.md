# 🔥 Lab 6: Web Scraping - Data Extraction

## 📋 Overview
Learn how to extract and analyze data from websites using **Web Scraping** with Python. Build a job market analyzer that scrapes Hacker News job postings and visualizes technology trends.

## 🎯 What You'll Learn
- Make HTTP requests to websites
- Parse HTML content with BeautifulSoup
- Clean and process scraped data
- Analyze technology trends in job postings
- Visualize data with Matplotlib
- Follow web scraping ethics

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
cd lab6-web-scraping
pip install -r requirements.txt
python scraper.py
```

## 📁 Files
- `scraper.py` - Main web scraping script
- `requirements.txt` - Dependencies

## 💡 Key Features
- **HTTP Requests** - Fetch web page content
- **HTML Parsing** - Extract specific data with BeautifulSoup
- **Data Cleaning** - Process and clean scraped text
- **Trend Analysis** - Count technology mentions in job posts
- **Data Visualization** - Create bar charts with Matplotlib

## 🗄️ Virtual Environment Setup

### 1. Create Virtual Environment
```bash
python -m venv .venv
```

### 2. Activate Virtual Environment
```bash
# Windows (Command Prompt)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

### 3. Verify Activation
You should see `(.venv)` at the beginning of your command line when activated.

## 🐛 Troubleshooting

### Common Issues:

1. **Virtual Environment Not Working**:
   - Ensure Python is installed: `python --version`
   - On Windows, try: `python -m venv .venv --prompt webscraping`

2. **Connection Errors**:
   - Check your internet connection
   - Verify the URL is accessible
   - The Hacker News page structure may have changed

3. **Module Not Found Errors**:
   - Ensure virtual environment is activated (you should see `(.venv)`)
   - Run: `pip install -r requirements.txt`

4. **No Data Found**:
   - The page structure may have changed
   - Check browser developer tools for updated CSS classes

5. **Matplotlib Display Issues**:
   - On servers, use: `plt.savefig('output.png')` instead of `plt.show()`

6. **Rate Limiting**:
   - Add delays between requests: `import time; time.sleep(1)`
   - Respect robots.txt and terms of service

7. **HTML Parsing Errors**:
   - Verify CSS selectors are correct
   - Use browser developer tools to inspect page structure

## ⚠️ Web Scraping Ethics
- Be mindful about how you scrape!
- Don't overdo it - request data at a reasonable rate
- Respect the owners of the data
- Check robots.txt and terms of service
- Consider using official APIs when available

---

**Previous:** [Lab 5 - FastAPI with PostgreSQL ←](../lab5-fastapi-postgresql)

**Next:** [Lab 7 - LangChain →](../lab7-langchain)

---