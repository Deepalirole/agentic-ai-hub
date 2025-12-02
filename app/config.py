import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load .env file
load_dotenv()


@dataclass
class Settings:
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_api_base: str = os.getenv("LLM_API_BASE", "")
    llm_model_name: str = os.getenv("LLM_MODEL_NAME", "llama-3.1-70b-versatile")
    temperature_default: float = 0.3
    debug_mode: bool = bool(int(os.getenv("DEBUG_MODE", "0")))


# Create global settings object
settings = Settings()



