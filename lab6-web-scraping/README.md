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

## 🐛 Troubleshooting

### Common Issues:

1. **Connection Errors**:
   - Check your internet connection
   - Verify the URL is accessible
   - The Hacker News page structure may have changed

2. **Module Not Found Errors**:
   - Ensure virtual environment is activated
   - Run: `pip install -r requirements.txt`

3. **No Data Found**:
   - The page structure may have changed
   - Check browser developer tools for updated CSS classes

4. **Matplotlib Display Issues**:
   - On servers, use: `plt.savefig('output.png')` instead of `plt.show()`

5. **Rate Limiting**:
   - Add delays between requests: `time.sleep(1)`
   - Respect robots.txt and terms of service

6. **HTML Parsing Errors**:
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

---