from models.embedding import AzureOpenAIEmbeddings, HFEmbeddings

# embedding_model = AzureOpenAIEmbeddings()
embedding_model = HFEmbeddings()


def get_embeddings(texts):
    """Gets embeddings for a list of texts."""
    embeddings = embedding_model.get_embeddings(texts)
    return embeddings
