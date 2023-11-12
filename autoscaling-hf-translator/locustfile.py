import time, pickle
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

URL = "/generate"

class ModelUser(FastHttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def get_prediction(self):
        import requests
        import json

        url = "http://127.0.0.1:8000"

        payload = json.dumps({
          "prompt": "Wo ist Berlin?",
          "max_tokens": 50,
          "stream": True
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = self.client.get(URL, headers=headers, data=payload)

        # print(response.text)
