# 🔥 Lab 8: Crawl4AI - Advanced Web Crawling

## 📋 Overview
Learn advanced web crawling techniques using **Crawl4AI** - a powerful Python library for parallel web crawling, data extraction, and content processing.

## 🎯 What You'll Learn
- Perform single-page web crawling
- Implement sequential crawling with session reuse
- Master parallel crawling with concurrency control
- Monitor memory usage during large-scale crawling
- Extract and process sitemap data
- Generate markdown from web content
- Use browser automation for complex web interactions

## 🚀 Quick Start

```bash
cd lab8-crawl4ai
pip install -r requirements.txt

# Run different crawling modes
python single_page_crawl.py
python sequential_crawling.py  
python parallel_crawling.py
```

## 📁 Files
- `single_page_crawl.py` - Basic single page crawling
- `sequential_crawling.py` - Sequential crawling with session reuse
- `parallel_crawling.py` - Parallel crawling with memory monitoring
- `requirements.txt` - Dependencies

## 💡 Key Features
- **Multiple Crawling Modes** - Single, sequential, and parallel crawling
- **Memory Monitoring** - Track resource usage during large crawls
- **Session Management** - Reuse browser sessions for efficiency
- **Markdown Generation** - Convert web content to clean markdown
- **Sitemap Processing** - Extract URLs from XML sitemaps automatically
- **Error Handling** - Robust error management for production crawls
- **Browser Automation** - Handle JavaScript-rendered content

## 🕷️ Crawling Examples

### 1. Single Page Crawl
```bash
python single_page_crawl.py
```
Crawls the Pydantic AI documentation homepage and extracts clean markdown content using the context manager pattern.

### 2. Sequential Crawling  
```bash
python sequential_crawling.py
```
Crawls all Pydantic AI documentation pages sequentially with session reuse and markdown generation.

### 3. Parallel Crawling
```bash
python parallel_crawling.py
```
Crawls multiple pages concurrently with memory usage monitoring and efficient resource management.

## 🔧 Technical Implementation

### Browser Configuration
```python
browser_config = BrowserConfig(
    headless=True,
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
)
```

### Crawler Run Configuration
```python
crawl_config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(),
    cache_mode=CacheMode.BYPASS
)
```

### Memory Monitoring
```python
process = psutil.Process(os.getpid())
current_mem = process.memory_info().rss  # Real-time memory tracking
```

## 📊 Performance Features

- **Concurrent Processing**: Up to 10 parallel crawls
- **Memory Optimization**: Track peak memory usage
- **Session Reuse**: Efficient browser instance management
- **Batch Processing**: Process URLs in controlled batches
- **Error Resilience**: Continue on individual URL failures

## 🐛 Troubleshooting

### Common Issues:

1. **Memory Errors**: 
   - Reduce `max_concurrent` in parallel crawling
   - Monitor memory usage with included tools
   - Use `--disable-dev-shm-usage` for Docker environments

2. **Connection Errors**:
   - Check internet connection
   - Verify target websites are accessible
   - Add retry logic for transient failures

3. **Dependency Issues**:
   - Ensure all requirements are installed
   - Use the provided `requirements.txt`
   - Install Playwright browsers: `playwright install`

4. **Rate Limiting**:
   - Add delays between requests for large crawls
   - Respect robots.txt and terms of service
   - Implement polite crawling practices

## ⚠️ Important Notes

- **Respect websites** - Don't overload servers with aggressive crawling
- **Check robots.txt** - Always respect website crawling policies
- **Monitor resources** - Large parallel crawls can use significant memory
- **Use responsibly** - Only crawl websites you have permission to access
- **Legal compliance** - Ensure compliance with local laws and website terms

## 🎯 Use Cases

- **Documentation scraping** - Extract and process technical documentation
- **Content aggregation** - Gather information from multiple sources
- **Data mining** - Extract structured data from websites
- **Research** - Academic and market research data collection
- **Monitoring** - Track changes across multiple web pages

## 🔍 Advanced Features

The Crawl4AI library supports:
- **Stealth mode** - Avoid detection by anti-bot systems
- **Custom markdown generation** - Tailor output format to your needs
- **Caching strategies** - Optimize performance with smart caching
- **Proxy support** - Route requests through proxies
- **Custom headers** - Modify request headers for specific sites

---

**Previous:** [Lab 7 - LangChain ←](../lab7-langchain)

---