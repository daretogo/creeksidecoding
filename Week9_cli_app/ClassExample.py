#!/usr/bin/env python3
import requests
import re
import random

# Function to fetch the content of the web page
def fetch_quotes_page():
    # The URL from which we'll fetch the quotes
    url = "https://blog.hubspot.com/sales/famous-quotes"
    
    # Make an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
        return None

# Function to parse the quotes from the page content
def parse_quotes(page_content):
    # List to hold all the quotes we find
    quotes_list = []
    
    # Use regular expression to find all instances of the pattern that match the quotes
    # This pattern looks for a number followed by a period and space, then captures
    # the quote text until it hits a closing tag ("<"). This is a simple approach
    # and may need adjustments if the page structure changes.
    quotes_pattern = re.compile(r'\d+\.\s(.*?)<')
    matches = quotes_pattern.findall(page_content)
    
    # Iterate over all the matches and add them to the quotes list
    for match in matches:
        # Clean the match by removing HTML tags if any; this is a simple approach
        # and may not remove all possible HTML tags, but is sufficient for this example.
        clean_quote = re.sub(r'<.*?>', '', match)
        quotes_list.append(clean_quote.strip())
    
    return quotes_list

# Function to pick a random quote from the list
def select_random_quote(quotes_list):
    # Use the random.choice method to pick a random item from the quotes list
    random_quote = random.choice(quotes_list)
    return random_quote

# The main function that will orchestrate our script
def main():
    # Fetch the content of the quotes page
    page_content = fetch_quotes_page()
    
    # If we successfully fetched the content, parse the quotes
    if page_content:
        quotes_list = parse_quotes(page_content)
        
        # If we found any quotes, select a random one and print it
        if quotes_list:
            print("Random quote of the day:")
            print(select_random_quote(quotes_list))
        else:
            print("No quotes found on the page.")
    else:
        print("The script was unable to fetch the webpage content.")

# This block ensures the code only runs when the script is executed directly
if __name__ == "__main__":
    main()
