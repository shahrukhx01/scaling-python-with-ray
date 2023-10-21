import time, pickle
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

URL = "/"

class ModelUser(FastHttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def get_prediction(self):
        self.client.get(URL, json="Hello world")

