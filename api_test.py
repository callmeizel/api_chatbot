import requests
import json

url = "http://127.0.0.1:8000/Chatbot"

prompt = {'prompt':"explai why oxygen is important under 500 words only."}

response = requests.post(url,json=prompt)
print(response.json())