import os
from openai import OpenAI


def get_client():
    return OpenAI(
        api_key=os.getenv("sk-3cUlsgtJ9n3Bds6KU9K3nCLyVL995mgWW3pHWK9C1JVwqcKq"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.gapgpt.app/v1")
    )