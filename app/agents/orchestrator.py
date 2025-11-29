from dataclasses import dataclass
from typing import Any, Dict

from app.services.llm_client import LlamaClient
from app.services.vector_store import FAQVectorStore
from app.services.data_loader import load_sample_products
from app.agents.support_agent import SupportAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.social_media_agent import SocialMediaAgent


@dataclass
class Orchestrator:
    llm: LlamaClient
    support_agent: SupportAgent
    recommendation_agent: RecommendationAgent
    social_agent: SocialMediaAgent

    @classmethod
    def create(cls) -> "Orchestrator":
        llm = LlamaClient()
        faq_store = FAQVectorStore()
        support_agent = SupportAgent(llm=llm, faq_store=faq_store)
        recommendation_agent = RecommendationAgent.with_default_products(llm)
        social_agent = SocialMediaAgent(llm=llm)

        return cls(
            llm=llm,
            support_agent=support_agent,
            recommendation_agent=recommendation_agent,
            social_agent=social_agent,
        )

    def run_support(self, user_query: str) -> Dict[str, Any]:
        return self.support_agent.handle(user_query)

    def run_recommendation(self, category: str, budget: int, preferences: str) -> Dict[str, Any]:
        return self.recommendation_agent.handle(category, budget, preferences)

    def run_social_media(self, brand_desc: str, platform: str, tone: str) -> Dict[str, Any]:
        return self.social_agent.handle(brand_desc, platform, tone)
