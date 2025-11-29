from dataclasses import dataclass
from typing import Dict, Any

from app.services.llm_client import LlamaClient
from app.utils.prompts import SOCIAL_MEDIA_SYSTEM_PROMPT
from app.utils.logging_utils import log_agent_interaction


@dataclass
class SocialMediaAgent:
    llm: LlamaClient

    def handle(self, brand_desc: str, platform: str, tone: str) -> Dict[str, Any]:
        prompt = f"""
Brand description:
{brand_desc}

Platform: {platform}
Tone: {tone}

Tasks:
1. Give 5 content ideas for this platform.
2. Give 5 caption options for a post for TODAY.
3. Create a 7-day content plan in a table format:
   Day | Post idea | Caption (short) | CTA | Hashtags
"""
        response = self.llm.complete(prompt, system_prompt=SOCIAL_MEDIA_SYSTEM_PROMPT)
        log_agent_interaction("SocialMediaAgent", prompt, response)

        return {"plan_text": response}
