from qdrant_client.models import VectorParams, Distance, PointStruct
from rag.qdrant_client import get_client

client = get_client()

COLLECTION = "rag_demo"


def create_collection(vector_size):
    client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )


def index_chunks(chunks, embeddings):
    points = []

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=emb,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION,
        points=points
    )