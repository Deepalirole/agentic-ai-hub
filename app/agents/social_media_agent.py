# app/agents/social_media_agent.py

from dataclasses import dataclass
from typing import Any, Dict

from app.services.llm_client import LlamaClient
from app.utils.logging_utils import log_agent_interaction


@dataclass
class SocialMediaAgent:
    """Agent that generates social media content ideas and plans."""

    llm: LlamaClient

    def generate_content(self, brand: str, platform: str, tone: str) -> Dict[str, Any]:
        """Generate ideas, captions, and a short posting plan."""

        brand = brand.strip() if brand else "A generic modern brand"
        platform = (platform or "Instagram").strip()
        tone = (tone or "Friendly").strip()

        prompt = f"""
You are a senior social media strategist.

Brand description:
{brand}

Target platform: {platform}
Tone of voice: {tone}

You MUST respond in three clear sections:

1. CONTENT IDEAS
   - 3–5 post ideas tailored to the brand and platform.
   - Each idea in 1–2 lines.

2. CAPTION OPTIONS
   - 3–5 example captions matching the tone.
   - Include relevant emojis and hashtags where appropriate.

3. 7-DAY PLAN
   - A simple day-wise plan (Day 1 to Day 7)
   - For each day: content type + short description.

Keep it concise and easy to read.
"""

        full_answer = self.llm.complete(prompt)
        log_agent_interaction("SocialMediaAgent", prompt, full_answer)

        # For simplicity, we reuse the same text in multiple keys so that
        # different UIs can pick what they need without KeyError.
        return {
            "full_text": full_answer,
            "ideas": full_answer,
            "ideas_text": full_answer,
            "captions": full_answer,
            "captions_text": full_answer,
            "plan": full_answer,
            "plan_text": full_answer,
        }
