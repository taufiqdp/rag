def retrieve_relevant_chunks(question, embedding_model, qdrant_db, limit=5):
    """Retrieves relevant chunks from the Qdrant database based on a question."""
    question_embedding = embedding_model.get_embedding(question)
    contexts = qdrant_db.query(query_vector=question_embedding, limit=limit)
    return contexts
