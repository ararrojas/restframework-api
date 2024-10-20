import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title":'product2'})
print(response.json())