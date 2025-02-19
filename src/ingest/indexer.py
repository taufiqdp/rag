from qdrant_client.models import PointStruct

from ingest.embedder import get_embeddings
from models.qdrant_client import QdrantDB

qdrant_db = QdrantDB()


def create_points(texts):
    """Creates Qdrant PointStruct objects from texts and their embeddings."""
    embeddings = get_embeddings(texts)
    points = [
        PointStruct(
            id=idx,
            vector=data.embedding,
            payload={"text": text},
        )
        for idx, (data, text) in enumerate(zip(embeddings, texts))
    ]
    return points


def index_data(points):
    """Indexes the points into the Qdrant database."""
    qdrant_db.upsert(points)


def setup_index(points):
    """Creates the qdrant database if it does not exist and loads data"""
    qdrant_db.create_collection(len(points[0].vector))
    index_data(points)
