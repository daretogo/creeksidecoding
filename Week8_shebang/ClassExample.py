#!/usr/bin/env python3
# Shebang line to allow direct execution from command line

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

"""
Segment 2: Understanding File Permissions
- Demonstrating how to make a Python script executable.
"""
# Instructions (not actual code):
# 1. Open your terminal
# 2. Navigate to the directory containing this script
# 3. Run `ls -l` to view current file permissions
# 4. Run `chmod +x ClassExample.py` to make the script executable
# 5. Run `ls -l` again to verify the permission changes

"""
Segment 3: Introduction to Shebang
- This script includes a shebang line at the very top.
- It allows the script to be run directly from the command line on Unix-like systems.
"""

"""
Segment 4: Running Python Scripts from the Command Line
- With the shebang line and executable permissions, this script can be run using ./ClassExample.py
- Note: For this part to work, you need to be in the same directory as the script.
"""

"""
Segment 5: Introduction to HTTP Requests and the `requests` Module
- Below is an example function that makes an HTTP GET request and prints the response status code.
"""
def make_http_request(url):
    response = requests.get(url)
    print("HTTP Status Code:", response.status_code)
    return response.text

"""
Segment 6: Creating a Web Scraper Command-Line Tool
- Below is an example function that scrapes the title of a webpage.
"""
def scrape_webpage_title(url):
    # Make an HTTP GET request to the given URL
    page_content = make_http_request(url)
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Find the title tag and print its content
    title_tag = soup.find('title')
    if title_tag:
        print("Webpage Title:", title_tag.get_text())
    else:
        print("Title tag not found.")

# This block ensures the code only runs when the script is executed directly (not when imported as a module)
if __name__ == "__main__":
    # Replace the URL below with the URL of the webpage you want to scrape
    url_to_scrape = "https://example.com"
    
    # Call the web scraper function
    scrape_webpage_title(url_to_scrape)
