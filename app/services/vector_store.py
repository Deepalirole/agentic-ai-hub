# app/services/vector_store.py

from dataclasses import dataclass
from typing import Any, Dict, List
import re


@dataclass
class FAQVectorStore:
    """Simple in-memory FAQ store with naive keyword matching."""

    faqs: List[Dict[str, str]]

    def search_faq(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Return top_k FAQs that loosely match the query."""
        query_lower = query.lower().strip()
        if not query_lower:
            return []

        def score(faq: Dict[str, str]) -> int:
            text = (faq.get("question", "") + " " + faq.get("answer", "")).lower()
            # Simple word overlap scoring
            tokens = re.findall(r"\w+", query_lower)
            return sum(1 for t in tokens if t in text)

        ranked = sorted(self.faqs, key=score, reverse=True)
        # Filter out entries with score 0
        scored = [faq for faq in ranked if score(faq) > 0]
        return scored[:top_k]


# 🧾 Demo FAQ data – you can later load this from a file if you want
DEFAULT_FAQS: List[Dict[str, str]] = [
    {
        "question": "What is your return policy?",
        "answer": "You can return any product within 7 days of delivery in its original condition for a full refund."
    },
    {
        "question": "How long does standard shipping take?",
        "answer": "Standard shipping usually takes 3–5 business days depending on your location."
    },
    {
        "question": "Do you offer international shipping?",
        "answer": "Yes, we ship to selected countries. Shipping fees and delivery times vary by region."
    },
    {
        "question": "How can I track my order?",
        "answer": "Once your order is shipped, we email you a tracking link. You can also find it in your account’s Orders section."
    },
]


# ✅ Global FAQ store instance – THIS is what Orchestrator imports
faq_store = FAQVectorStore(faqs=DEFAULT_FAQS)
