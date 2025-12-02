# app/agents/recommendation_agent.py

from dataclasses import dataclass
from typing import Any, Dict, List

from app.services.llm_client import LlamaClient
from app.utils.logging_utils import log_agent_interaction


@dataclass
class RecommendationAgent:
    """Agent that recommends products based on category, budget, and preferences."""

    llm: LlamaClient
    products: List[Dict[str, Any]]

    def recommend(self, category: str, budget: int, preferences: str) -> Dict[str, Any]:
        # 1️⃣ Filter products by category + budget
        category_lower = (category or "").lower().strip()

        filtered: List[Dict[str, Any]] = []
        for p in self.products:
            p_cat = str(p.get("category", "")).lower()
            p_price = float(p.get("price", 0))

            if category_lower and p_cat != category_lower:
                continue

            if budget and p_price > float(budget):
                continue

            filtered.append(p)

        # If nothing matched, fall back to all products
        candidates = filtered or self.products

        # 2️⃣ Build context for the LLM
        product_lines = []
        for idx, p in enumerate(candidates, start=1):
            product_lines.append(
                f"{idx}. {p.get('name')}  "
                f"(Category: {p.get('category')}, Price: {p.get('price')}, "
                f"Tags: {', '.join(p.get('tags', []))})"
            )

        product_context = "\n".join(product_lines) if product_lines else "No products available."

        prompt = f"""
You are a helpful e-commerce product recommendation assistant.

User preferences:
- Category: {category or "Not specified"}
- Budget: {budget or "Not specified"}
- Extra preferences: {preferences or "None"}

Available products:
{product_context}

Instructions:
1. Pick 1–3 products that best match the user's category, budget, and preferences.
2. Clearly mention a single **Best Pick** and explain why.
3. If nothing fits the budget perfectly, suggest the closest alternatives and explain the trade-offs.
4. Answer in a friendly, concise tone, using bullet points.
"""

        answer = self.llm.complete(prompt)
        log_agent_interaction("RecommendationAgent", prompt, answer)

        # 3️⃣ Choose a simple "best pick" (first candidate) for structured data
        best_pick = candidates[0] if candidates else None

        return {
            "recommendations_text": answer,
            "matched_products": candidates,
            "best_pick": best_pick,
        }

