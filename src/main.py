import os

import streamlit as st
import torch

from generation.generator import generate_answer
from generation.prompt_builder import build_prompt
from ingest.chunker import chunk_data
from ingest.data_loader import load_url
from ingest.indexer import create_points, setup_index
from models.embedding import HFEmbeddings
from models.llm import OllamaLLM
from models.qdrant_client import QdrantDB
from retrieval.retriever import retrieve_relevant_chunks

# Silent warnings
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)]

qdrant_db = QdrantDB()


# Cache the embedding model
@st.cache_resource
def load_embedding_model():
    """
    Loads the embedding model and caches it using Streamlit's `st.cache_resource`.
    """
    return HFEmbeddings()


@st.cache_resource
def load_llm_model():
    return OllamaLLM()


embedding_model = load_embedding_model()
llm_model = load_llm_model()


def initialize_qdrant(documents):
    """
    Initializes the Qdrant database with provided documents.
    """
    if qdrant_db.client.collection_exists(qdrant_db.collection_name):
        qdrant_db.client.delete_collection(collection_name=qdrant_db.collection_name)

    chunks = chunk_data(documents)
    texts = [chunk.page_content for chunk in chunks]
    points = create_points(texts, embedding_model)
    setup_index(points, qdrant_db)

    return True


def main():
    st.title("Document Chatbot")

    urls_input = st.text_area("Enter URLs (one per line):", "")
    urls = [url.strip() for url in urls_input.splitlines() if url.strip()]

    if "qdrant_initialized" not in st.session_state:
        st.session_state.qdrant_initialized = False

    if st.button("Load Data and Initialize"):
        with st.spinner("Loading data, chunking, and indexing..."):
            documents = []
            if urls:
                documents.extend(load_url(urls))

            if documents:
                st.session_state.qdrant_initialized = initialize_qdrant(documents)

                st.success("Data loaded and Qdrant database initialized.")
            else:
                st.error("No documents were loaded. Please check the URLs.")

    question = st.text_input("Ask a question about the document:", "")

    if question and st.session_state.qdrant_initialized:
        with st.spinner("Thinking..."):
            try:
                contexts = retrieve_relevant_chunks(
                    question, embedding_model, qdrant_db, limit=5
                )
                context = "\n".join(
                    [point.payload["text"] for point in contexts.points]
                )
                prompt = build_prompt(context, question)

                # Debugging prompt
                with st.expander("See Prompt"):
                    st.markdown(f"```\n{prompt}\n```")

                response_stream = generate_answer(prompt, llm_model)

                full_response = ""
                message_placeholder = st.empty()
                for chunk in response_stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.error("Check the backend logs for more details.")
    elif question and not st.session_state.qdrant_initialized:
        st.warning(
            "Please load data and initialize the Qdrant database before asking questions."
        )


if __name__ == "__main__":
    main()
