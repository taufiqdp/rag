from qdrant_client.models import PointStruct

from ingest.embedder import get_embeddings


def create_points(texts, embedding_model):
    """Creates Qdrant PointStruct objects from texts and their embeddings."""
    embeddings = get_embeddings(texts, embedding_model)
    points = [
        PointStruct(
            id=idx,
            vector=data,
            payload={"text": text},
        )
        for idx, (data, text) in enumerate(zip(embeddings, texts))
    ]
    return points


def index_data(points, qdrant_db):
    """Indexes the points into the Qdrant database."""
    qdrant_db.upsert(points)


def setup_index(points, qdrant_db):
    """Creates the qdrant database if it does not exist and loads data"""
    qdrant_db.create_collection(len(points[0].vector))
    index_data(points, qdrant_db)
