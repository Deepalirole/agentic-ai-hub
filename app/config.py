import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


@dataclass
class Settings:
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_api_base: str = os.getenv("LLM_API_BASE", "")
    llm_model_name: str = os.getenv("LLM_MODEL_NAME", "llama-3.3-70b-versatile")
    model_name: str = os.getenv("LLM_MODEL_NAME", "llama-3.3-70b-versatile")  # alias
    temperature_default: float = 0.3
    debug_mode: bool = bool(int(os.getenv("DEBUG_MODE", "0")))

settings = Settings()
