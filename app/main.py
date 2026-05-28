from fastapi import FastAPI
from rag.retriever import retrieve
from rag.prompt import build_prompt
from rag.generator import generate, generate_local

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

USE_LOCAL = True


@app.get("/")
def root():
    return {"msg": "ok"}

@app.get("/ask")
def ask(q: str):
    try:
        contexts = retrieve(q)
        prompt = build_prompt(q, contexts)
        answer = generate(prompt)

        return {
            "question": q,
            "answer": answer,
            "contexts": contexts
        }

    except Exception as e:
        return {
            "error": str(e)
        }


Instrumentator().instrument(app).expose(app)
