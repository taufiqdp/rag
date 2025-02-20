from generation.generator import generate_answer
from generation.prompt_builder import build_prompt
from ingest.chunker import chunk_data
from ingest.data_loader import load_data
from ingest.indexer import create_points, setup_index
from models.qdrant_client import QdrantDB
from retrieval.retriever import retrieve_relevant_chunks
from utils.utils import load_config

qdrant_db = QdrantDB()


def main():
    config = load_config()
    question = "what data they use to experiment the model?"

    if qdrant_db.client.collection_exists(qdrant_db.collection_name):
        print(f"Collection '{qdrant_db.collection_name}' already exists.")
    else:
        print(f"Collection '{qdrant_db.collection_name}' does not exist. Creating...")
        documents = load_data()
        chunks = chunk_data(documents)
        texts = [chunk.page_content for chunk in chunks]
        points = create_points(texts)
        setup_index(points)

    contexts = retrieve_relevant_chunks(question)
    context = "\n".join([point.payload["text"] for point in contexts.points])
    prompt = build_prompt(context, question)

    print(f"Prompt: {prompt}\n")
    response = generate_answer(prompt)

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)


if __name__ == "__main__":
    main()
