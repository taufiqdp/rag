from openai import AzureOpenAI

from utils.utils import load_config

config = load_config()


class AzureOpenAIEmbeddings:
    def __init__(self):
        azure_config = config["azure_openai"]
        self.client = AzureOpenAI(
            api_key=azure_config["api_key"],
            azure_endpoint=azure_config["endpoint"],
            api_version=azure_config["api_version"],
        )
        self.model_name = azure_config["embedding_model"]

    def get_embedding(self, text):
        """Gets an embedding for the given text."""
        try:
            response = self.client.embeddings.create(
                input=[text],
                model=self.model_name,
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error getting embedding: {e}")
            return None

    def get_embeddings(self, texts):
        """Gets embeddings for the given texts."""
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=self.model_name,
            )
            return response.data
        except Exception as e:
            print(f"Error getting embeddings: {e}")
            return None
