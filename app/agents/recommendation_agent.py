from dataclasses import dataclass
from typing import List, Dict, Any

from app.services.llm_client import LlamaClient
from app.services.data_loader import load_sample_products
from app.utils.prompts import RECOMMENDATION_SYSTEM_PROMPT
from app.utils.logging_utils import log_agent_interaction


@dataclass
class RecommendationAgent:
    llm: LlamaClient
    products: List[Dict[str, Any]]

    @classmethod
    def with_default_products(cls, llm: LlamaClient) -> "RecommendationAgent":
        return cls(llm=llm, products=load_sample_products())

    def handle(self, category: str, budget: int, preferences: str) -> Dict[str, Any]:
        filtered = [
            p
            for p in self.products
            if (not category or p["category"].lower() == category.lower())
            and p["price"] <= budget
        ] or self.products  # if nothing matches, fall back to all

        product_text = "\n".join(
            [
                f"{p['id']}: {p['name']} | Category: {p['category']} | "
                f"Price: {p['price']} | Rating: {p['rating']} | Tags: {', '.join(p['tags'])}"
                for p in filtered
            ]
        )

        prompt = f"""
User preferences:
- Category: {category or "any"}
- Budget (max): {budget}
- Extra preferences: {preferences or "none"}

Available products (already filtered by category/budget if possible):
{product_text}

Choose 3–5 best matching products.
Explain briefly why each one fits.
Then select ONE BEST PICK and clearly label it.
"""

        response = self.llm.complete(prompt, system_prompt=RECOMMENDATION_SYSTEM_PROMPT)
        log_agent_interaction("RecommendationAgent", prompt, response)

        return {
            "recommendations_text": response,
            "raw_products": filtered,
        }
