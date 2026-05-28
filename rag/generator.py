import os
import requests
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def generate_cloud(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_local(prompt):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
    )
    return res.json()["response"]


USE_LOCAL = os.getenv("USE_LOCAL", "true") == "true"


def generate(prompt):
    if USE_LOCAL:
        return generate_local(prompt)
    return generate_cloud(prompt)