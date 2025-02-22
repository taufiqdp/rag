# Local Retrieval Augmented Generation (RAG)

## Tools

- [Ollama](https://ollama.com/)
- [LangChain](https://langchain.com/)
- [Qdrant](https://qdrant.tech/)
- [Sentence Transformers](https://sbert.net/)

## Pre-requisites

- Docker

## Setup

1. Clone the repository

```bash
git clone https://github.com/taufiqdp/rag.git
cd rag
```

2. Configure the configuration file

Rename `config.example.yaml` to `config.yaml` and configure the file according to your needs.

3. Build and start the docker container

```bash
docker compose up -d --build
```

4. Access the application

The application should now be running on http://localhost:8501
