print("=" * 50)
print("REQUESTS TUTORIAL")
print("=" * 50)

# =============================================================================
# 1. GET REQUEST
# =============================================================================
print("\n" + "="*50)
print("1. GET REQUEST")
print("="*50)

import requests

print("\n--- Making GET Request ---")
url = "https://httpbin.org/json"
response = requests.get(url)

print(f"Response object: {response}")
print(f"Status code: {response.status_code}")

# =============================================================================
# 2. HTTP STATUS CODES
# =============================================================================
print("\n" + "="*50)
print("2. HTTP STATUS CODES")
print("="*50)

print("\n--- Status Codes Examples ---")
test_urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404", 
    "https://httpbin.org/status/500"
]

for test_url in test_urls:
    try:
        resp = requests.get(test_url)
        print(f"URL: {test_url} -> Status: {resp.status_code}")
        
        if resp.status_code == 200:
            print("  ✅ Success")
        elif 400 <= resp.status_code < 500:
            print("  ❌ Client Error")
        elif 500 <= resp.status_code < 600:
            print("  🔧 Server Error")
            
    except Exception as e:
        print(f"Error: {e}")

# =============================================================================
# 3. REQUEST CONTENT
# =============================================================================
print("\n" + "="*50)
print("3. REQUEST CONTENT")
print("="*50)

print("\n--- Response Content ---")
response = requests.get("https://httpbin.org/json")
print(f"Content (first 200 chars): {response.content[:200]}...")
print(f"Text (first 200 chars): {response.text[:200]}...")

# =============================================================================
# 4. POST REQUEST
# =============================================================================
print("\n" + "="*50)
print("4. POST REQUEST")
print("="*50)

print("\n--- Making POST Request ---")
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data)

response_data = response.json()
print("JSON Response:")
print(response_data)

# =============================================================================
# 5. HANDLING ERRORS
# =============================================================================
print("\n" + "="*50)
print("5. HANDLING ERRORS")
print("="*50)

print("\n--- Error Handling ---")
response = requests.get("https://httpbin.org/status/404")

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Request failed with status: {response.status_code}")
    print(f"Error message: {response.text}")

# =============================================================================
# 6. SETTING A TIMEOUT
# =============================================================================
print("\n" + "="*50)
print("6. SETTING A TIMEOUT")
print("="*50)

print("\n--- Timeout Example ---")
url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=5)
    print("✅ Request completed within timeout!")
    print(f"Status: {response.status_code}")
except requests.exceptions.Timeout as err:
    print(f"❌ Timeout error: {err}")
except Exception as e:
    print(f"Other error: {e}")

# =============================================================================
# 7. HTTP REQUEST HEADERS
# =============================================================================
print("\n" + "="*50)
print("7. HTTP REQUEST HEADERS")
print("="*50)

print("\n--- Setting Headers ---")
auth_token = "my-secret-token-12345"

headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)

print("Response showing our headers:")
print(response.json())

# =============================================================================
# 8. WEB SCRAPING WITH BEAUTIFULSOUP
# =============================================================================
print("\n" + "="*50)
print("8. WEB SCRAPING WITH BEAUTIFULSOUP")
print("="*50)

print("\n--- Web Scraping Example ---")
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
first_paragraph = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(f"Title: {title}")
print(f"First paragraph: {first_paragraph}")
print(f"All links: {links}")

# =============================================================================
# 9. REQUESTS VS URLLIB
# =============================================================================
print("\n" + "="*50)
print("9. REQUESTS VS URLLIB")
print("="*50)

print("\n--- Requests Example (Simple) ---")

data = {"name": "Salah", "message": "Hello!"}
response = requests.post("https://httpbin.org/post", json=data)
print(f"Requests - Status: {response.status_code}")
print(f"Requests - Response: {response.json()['json']}")

print("\n--- urllib Example (Complex) ---")
import urllib.request
import urllib.parse
import json

try:
    data = urllib.parse.urlencode({"name": "Salah", "message": "Hello!"}).encode("utf-8")
    req = urllib.request.Request("https://httpbin.org/post", data=data, method="POST")
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
        result = json.loads(html)
        print(f"urllib - Status: {response.status}")
        print(f"urllib - Response: {result['form']}")
except Exception as e:
    print(f"urllib error: {e}")
