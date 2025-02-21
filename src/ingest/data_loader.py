from typing import List

from langchain_community.document_loaders import (PyPDFDirectoryLoader,
                                                  WebBaseLoader)


def load_pdf(data_path="data/"):
    """Loads data from a directory of PDFs."""
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()
    return documents


def load_url(url: List[str]):
    """Loads data from a list of URLs."""
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents
