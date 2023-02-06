import requests

reques = requests.get('http://127.0.0.1:8000/')
print(reques.json())
