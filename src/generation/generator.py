from models.llm import TogetherLLM
from retrieval.retriever import retrieve_relevant_chunks

llm_model = TogetherLLM()


def generate_answer(prompt, stream=True):
    """Generates an answer from the LLM based on the prompt."""
    response = llm_model.generate_response(prompt, stream=stream)
    return response
