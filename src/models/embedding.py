import warnings

from huggingface_hub import login
from openai import AzureOpenAI
from sentence_transformers import SentenceTransformer

from utils.utils import load_config

warnings.filterwarnings("ignore")
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


class HFEmbeddings:
    def __init__(self):
        hf_config = config["hf"]
        hf_token = hf_config["hf_token"]
        hf_embedding_model = hf_config["hf_embedding_model"]
        login(hf_token)

        self.model = SentenceTransformer(hf_embedding_model, trust_remote_code=True)

    def get_embedding(self, text):
        """Gets an embedding for the given text."""
        return self.model.encode(text)

    def get_embeddings(self, texts):
        """Gets embeddings for the given texts."""
        return self.model.encode(texts)
