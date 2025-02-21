def get_embeddings(texts, embedding_model):
    """Gets embeddings for a list of texts."""
    embeddings = embedding_model.get_embeddings(texts)
    return embeddings
