from qdrant_client import QdrantClient
from ingestion.embed import embed_texts
from rag.qdrant_client import get_client

client = get_client()

# client = QdrantClient(host="localhost", port=6333)

# client = QdrantClient(path="./qdrant_storage")

COLLECTION = "rag_demo"


def retrieve(query, top_k=5):
    query_vec = embed_texts([query])[0]

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vec,
        limit=top_k
    ).points

    return [
        r.payload["text"] if isinstance(r.payload, dict)
        else str(r.payload)
        for r in results
    ]