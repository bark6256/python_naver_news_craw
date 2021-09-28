import json
import requests

# response.json()  = dict
# json 모양의 문자열 -> json.loads() = dict
# dict -> json.dumps() = json


url = "http://localhost:8080/news"

response = requests.get(url)
newsDto = response.json()

print(type(newsDto))
print(newsDto)