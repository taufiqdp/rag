from utils.utils import clean_text


def build_prompt(context, question):
    """Builds the prompt for the LLM."""
    template = """You are an expert at summarizing and resolving contradictory information. Answer the following question based on the provided context.
If user asks basic questions, forget about the context and answer the question directly.

Context:

{context}

Question:

{question}

"""
    prompt = template.format(context=clean_text(context), question=question)
    return prompt
