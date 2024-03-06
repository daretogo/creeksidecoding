import requests

def make_http_request(url):
    response = requests.get(url)
    print("`HTTP Status Code:", response.status_code)
    return response.text

url = "https://futureofworking.com/23-best-teenage-mutant-ninja-turtles-sayings/"
website_text = make_http_request(url)
print(website_text)