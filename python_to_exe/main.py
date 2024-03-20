import requests


url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 2
}
response = requests.get(url=url, params=params)
print(response.json())