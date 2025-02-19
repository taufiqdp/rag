from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_data(data_path="data/"):
    """Loads data from a directory of PDFs."""
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()
    return documents
