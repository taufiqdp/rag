from models.llm import OllamaLLM, TogetherLLM

# llm_model = TogetherLLM()
llm_model = OllamaLLM()


def generate_answer(prompt, stream=True):
    """Generates an answer from the LLM based on the prompt."""
    response = llm_model.generate_response(prompt, stream=stream)
    return response
