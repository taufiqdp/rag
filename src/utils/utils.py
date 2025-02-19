import re

import yaml
from dotenv import load_dotenv

load_dotenv()


def load_config(config_path="config/config.yaml"):
    """Loads configuration from a YAML file."""
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error: Could not parse YAML file: {e}")
        return None


def clean_text(text):
    """Cleans up text by removing extra whitespace and newlines."""
    text = text.strip()
    text = re.sub(r"\n+", "\n", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    return text
