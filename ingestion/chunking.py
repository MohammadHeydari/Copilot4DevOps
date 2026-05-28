from pathlib import Path

def load_documents(data_path="data"):
    docs = []

    for file in Path(data_path).rglob("*"):
        if file.suffix in [".md", ".txt", ".json"]:
            content = file.read_text(encoding="utf-8")
            docs.append({
                "text": content,
                "source": str(file),
                "type": file.parent.name
            })

    return docs


def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def process_documents():
    raw_docs = load_documents()
    all_chunks = []

    for doc in raw_docs:
        chunks = chunk_text(doc["text"])

        for c in chunks:
            all_chunks.append({
                "text": c,
                "source": doc["source"],
                "type": doc["type"]
            })

    return all_chunks