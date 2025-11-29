import streamlit as st

from app.ui.themes import apply_theme
from app.ui.components import section_header, card
from app.agents.orchestrator import Orchestrator
from app.config import settings


@st.cache_resource
def get_orchestrator() -> Orchestrator:
    """Create and cache Orchestrator once."""
    return Orchestrator.create()


def page_support(orchestrator: Orchestrator) -> None:
    section_header("🛠 Support Assistant")
    query = st.text_area("Describe your issue or question", height=150)

    if st.button("Get Support", key="support_btn", type="primary"):
        if not query.strip():
            st.warning("Please enter a query.")
            return

        with st.spinner("Talking to Support Agent..."):
            result = orchestrator.run_support(query)

        badge = (
            "Resolved via FAQ"
            if result["from_faq"] and not result["needs_escalation"]
            else "Escalate to Human"
        )
        card("Support Response", result["answer"], badge=badge)


def page_recommendation(orchestrator: Orchestrator) -> None:
    section_header("🛒 Product Recommendation")
    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox("Category", ["", "Furniture", "Electronics"])
    with col2:
        budget = st.slider(
            "Max Budget (₹)", min_value=1000, max_value=20000, value=10000, step=500
        )

    preferences = st.text_input("Additional preferences (style, use-case, etc.)")

    if st.button("Get Recommendations", key="reco_btn", type="primary"):
        with st.spinner("Finding the best products for you..."):
            result = orchestrator.run_recommendation(category, budget, preferences)
        card("Recommendations", result["recommendations_text"])


def page_social(orchestrator: Orchestrator) -> None:
    section_header("📣 Social Media Studio")
    brand_desc = st.text_area("Brand description", height=120)
    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "X (Twitter)"])
    with col2:
        tone = st.selectbox("Tone", ["Fun", "Professional", "Luxury", "Casual"])

    if st.button("Generate Plan", key="social_btn", type="primary"):
        with st.spinner("Brainstorming your content plan..."):
            result = orchestrator.run_social_media(brand_desc, platform, tone)
        card("Content Plan", result["plan_text"])


def main() -> None:
    st.set_page_config(
        page_title="Sales, Marketing & Support AI Hub",
        page_icon="🤖",
        layout="wide",
    )
    apply_theme()

    # Sidebar
    st.sidebar.title("🤖 AI Hub")
    st.sidebar.caption("Sales • Marketing • Support")

    mode = st.sidebar.radio(
        "Choose mode",
        ["Support Assistant", "Product Recommendation", "Social Media Studio"],
    )

    st.sidebar.markdown("---")
    st.sidebar.write(f"Model: `{settings.llm_model_name}`")
    st.sidebar.write(f"Debug mode: {'ON' if settings.debug_mode else 'OFF'}")

    # 👉 Dynamic tool descriptions
    mode_descriptions = {
        "Support Assistant": (
            "Resolve customer FAQs instantly using a hybrid of knowledge search "
            "and LLM reasoning. Escalates complex issues to human agents with "
            "a clean summary."
        ),
        "Product Recommendation": (
            "Recommend the best products based on user preferences, budget and "
            "category. Uses LLM reasoning on a structured product catalog."
        ),
        "Social Media Studio": (
            "Generate content ideas, daily captions and a 7-day posting plan for "
            "your brand across Instagram, LinkedIn and X."
        ),
    }

    orchestrator = get_orchestrator()

    # 👉 Top hero section with description
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([2.5, 1.5])
        with col1:
            st.markdown("## ✨ Agentic Console")
            st.markdown(
                f"**Active tool:** `{mode}`  \n"
                f"{mode_descriptions.get(mode, '')}"
            )
        with col2:
            st.markdown("###### Tool Overview")
            if mode == "Support Assistant":
                st.markdown(
                    "- 🧠 FAQ-aware LLM support\n"
                    "- 📚 Vector search over common questions\n"
                    "- 🚨 Auto-escalation for complex issues"
                )
            elif mode == "Product Recommendation":
                st.markdown(
                    "- 🛒 Catalog-aware recommendations\n"
                    "- 💰 Budget-aware ranking\n"
                    "- ⭐ Highlights a single *Best Pick*"
                )
            else:
                st.markdown(
                    "- 📅 7-day content calendar\n"
                    "- ✍️ Captions + CTAs + hashtags\n"
                    "- 📈 Platform-specific tone & style"
                )
        st.markdown("</div>", unsafe_allow_html=True)

    # 👉 Render the active tool page below the description card
    if mode == "Support Assistant":
        page_support(orchestrator)
    elif mode == "Product Recommendation":
        page_recommendation(orchestrator)
    else:
        page_social(orchestrator)



if __name__ == "__main__":
    main()
