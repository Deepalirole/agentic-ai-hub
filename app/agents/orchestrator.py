from dataclasses import dataclass

from app.agents.support_agent import SupportAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.social_media_agent import SocialMediaAgent

from app.services.llm_client import LlamaClient
from app.services.vector_store import FAQVectorStore
from app.services.data_loader import load_sample_products


@dataclass
class Orchestrator:
    def __post_init__(self):
        self.llm = LlamaClient()
        self.faq_store = FAQVectorStore()

        self.support_agent = SupportAgent(self.llm, self.faq_store)
        self.recommendation_agent = RecommendationAgent(self.llm)
        self.social_media_agent = SocialMediaAgent(self.llm)

    def run_support(self, query: str):
        return self.support_agent.handle(query)

    def run_recommendation(self, category, budget, prefs):
        return self.recommendation_agent.recommend(category, budget, prefs)

    def run_social_media(self, brand_desc, platform, tone):
        return self.social_media_agent.generate_content(brand_desc, platform, tone)
