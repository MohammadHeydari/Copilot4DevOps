import os
from openai import OpenAI


def get_client():
    return OpenAI(
        api_key=os.getenv("your_api_key_here"),
        base_url=os.getenv("OPENAI_BASE_URL", "your_open_ai_url_here")
    )