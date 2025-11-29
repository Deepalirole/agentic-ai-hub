import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("sales_ai_hub")


def log_agent_interaction(agent_name: str, prompt: str, response: str) -> None:
    logger.info("Agent: %s\nPrompt: %s\nResponse: %s", agent_name, prompt, response[:500])
