# pip install requests
import requests


url = "https://github.com"
req = requests.get(url=url)
print(req)
print(req.text)
print(req.raw)
print(req.json())
