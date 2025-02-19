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
