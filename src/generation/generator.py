def generate_answer(prompt, llm_model, stream=True):
    """Generates an answer from the LLM based on the prompt."""
    response = llm_model.generate_response(prompt, stream=stream)
    return response
