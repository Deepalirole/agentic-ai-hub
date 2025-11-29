from typing import Optional

from openai import OpenAI

from app.config import settings


class LlamaClient:
    """
    Thin wrapper over an OpenAI-compatible Llama endpoint (Groq in your case).

    Requires .env:
      - LLM_API_KEY
      - LLM_API_BASE (https://api.groq.com/openai/v1)
      - LLM_MODEL_NAME (e.g., llama-3.1-70b-versatile)
    """

    def __init__(self, model_name: Optional[str] = None) -> None:
        self.client = OpenAI(
            api_key=settings.llm_api_key or None,
            base_url=settings.llm_api_base or None,
        )
        self.model_name = model_name or settings.llm_model_name

    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        if not settings.llm_api_key:
            return "⚠️ LLM_API_KEY is not set. Please configure your .env."

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature if temperature is not None else settings.temperature_default,
        )
        return completion.choices[0].message.content or ""
