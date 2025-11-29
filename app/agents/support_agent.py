from dataclasses import dataclass
from typing import Any, Dict, List

from app.services.llm_client import LlamaClient
from app.services.vector_store import FAQVectorStore
from app.utils.prompts import SUPPORT_SYSTEM_PROMPT
from app.utils.logging_utils import log_agent_interaction


@dataclass
class SupportAgent:
    llm: LlamaClient
    faq_store: FAQVectorStore

    def handle(self, user_query: str) -> Dict[str, Any]:
        faqs: List[Dict[str, Any]] = self.faq_store.search_faq(user_query, top_k=3)

        if faqs:
            context_lines = []
            for idx, faq in enumerate(faqs, start=1):
                context_lines.append(
                    f"FAQ {idx}:\nQ: {faq.get('question')}\nA: {faq.get('answer')}"
                )
            context = "\n\n".join(context_lines)
        else:
            context = "No relevant FAQ found."

        prompt = f"""
User query:
{user_query}

Relevant FAQs:
{context}

You MUST:
- First, try to answer using the FAQ content above.
- If you are not confident or FAQs are not enough, clearly say:
  "This issue should be escalated to a human support agent."
  and provide a short summary of the problem in bullet points.
"""

        response = self.llm.complete(prompt, system_prompt=SUPPORT_SYSTEM_PROMPT)
        log_agent_interaction("SupportAgent", prompt, response)

        lower = response.lower()
        needs_escalation = (
            "escalated to a human" in lower
            or "escalate to a human" in lower
            or "human support" in lower
        )

        return {
            "answer": response,
            "from_faq": bool(faqs),
            "needs_escalation": needs_escalation,
            "faqs_used": faqs,
        }
