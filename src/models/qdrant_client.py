from qdrant_client import QdrantClient, models
from qdrant_client.models import Distance, VectorParams

from utils.utils import load_config

config = load_config()


class QdrantDB:
    def __init__(self):
        qdrant_config = config["qdrant"]
        self.host = qdrant_config["host"]
        self.port = qdrant_config["port"]
        self.collection_name = qdrant_config["collection_name"]
        self.client = QdrantClient(host=self.host, port=self.port, timeout=60)

    def create_collection(self, vector_size):
        """Creates a Qdrant collection if it doesn't exist."""
        try:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )
            print(f"Collection '{self.collection_name}' created.")
        except Exception as e:
            print(f"Collection '{self.collection_name}' may already exist: {e}")

    def upsert(self, points):
        """Upserts points into the Qdrant collection."""
        self.client.upsert(self.collection_name, points)

    def query(self, query_vector, limit=5):
        """Queries the Qdrant collection."""
        contexts = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
        )
        return contexts
