# File name: serve_quickstart.py
from starlette.requests import Request

import ray
from ray import serve

from transformers import pipeline


@serve.deployment(
    ray_actor_options={"num_cpus": 1},
    max_concurrent_queries=8,
    autoscaling_config={
        "target_num_ongoing_requests_per_replica": 1,
        "min_replicas": 0,
        "initial_replicas": 0,
        "max_replicas": 8,
        "downscale_delay_s":10,
        "upscale_delay_s":1
    },
)
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_de", model="t5-small")
        print("model loaded...")

    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        return self.translate(english_text)


translator_app = Translator.bind()
