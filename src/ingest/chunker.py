from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.utils import load_config

config = load_config()


def chunk_data(documents):
    """Chunks the documents into smaller pieces."""
    chunking_config = config["chunking"]
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunking_config["chunk_size"],
        chunk_overlap=chunking_config["chunk_overlap"],
        separators=chunking_config["separators"],
    )
    chunks = splitter.split_documents(documents)
    return chunks
