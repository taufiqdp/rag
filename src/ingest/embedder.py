from models.embedding import AzureOpenAIEmbeddings

embedding_model = AzureOpenAIEmbeddings()


def get_embeddings(texts):
    """Gets embeddings for a list of texts."""
    embeddings = embedding_model.get_embeddings(texts)
    return embeddings
