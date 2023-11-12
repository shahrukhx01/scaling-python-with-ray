import requests
import json

url = "http://127.0.0.1:8000"

payload = json.dumps({
  "prompt": "Wo ist Berlin?",
  "max_tokens": 1,
  "stream": True
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
