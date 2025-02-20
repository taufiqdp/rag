from openai import OpenAI

from utils.utils import load_config

config = load_config()


class TogetherLLM:
    def __init__(self):
        together_config = config["together_ai"]
        self.client = OpenAI(
            base_url="https://api.together.xyz/v1",
            api_key=together_config["api_key"],
        )
        self.model_name = together_config["model"]

    def generate_response(self, prompt, stream=True):
        """Generates a response from the Together AI LLM."""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt},
                ],
                stream=stream,
            )
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None


class OllamaLLM:
    def __init__(self):
        ollama_config = config["ollama"]
        self.client = OpenAI(
            base_url=ollama_config["base_url"],
            api_key="ollama",
        )
        self.model_name = ollama_config["model"]

    def generate_response(self, prompt, stream=True):
        """Generates a response from the Ollama LLM."""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt},
                ],
                stream=stream,
            )
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None
