from ingestion.chunking import process_documents
from ingestion.embed import embed_texts
from ingestion.index import create_collection, index_chunks

chunks = process_documents()
texts = [c["text"] for c in chunks]

embeddings = embed_texts(texts)

create_collection(len(embeddings[0]))
index_chunks(chunks, embeddings)

print("Indexed successfully")