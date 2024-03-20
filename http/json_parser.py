import requests

url = "https://jsonplaceholder.typicode.com/posts"

# get params - гет параметры
# url = "https://jsonplaceholder.typicode.com/posts?limit=25&order=desc&category=cooking"

params = {
    "limit": 25,
    "order": "desc",
    "category": "cooking",
}

req = requests.get(url=url, params=params)
# json_formatted = req.json()

print(req.url)
print(req.status_code)
