# --- Fix import errors on Streamlit Cloud ---
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # /app
PROJECT_ROOT = ROOT.parent                      # project root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# ---------------------------------------------

import streamlit as st

from app.ui.themes import apply_theme
from app.ui.components import section_header, card
from app.agents.orchestrator import Orchestrator
from app.config import settings

# Apply theme
apply_theme()

@st.cache_resource
def get_orchestrator():
    return Orchestrator()

def page_support(orc):
    section_header("Customer Support Assistant")
    query = st.text_input("Enter your support question")
    if st.button("Ask"):
        result = orc.run_support(query)
        card("Answer", result["answer"])
        if result["needs_escalation"]:
            card("⚠ Human Escalation Needed", "This issue must be handled manually.")

def page_recommendation(orc):
    section_header("Product Recommendation Engine")
    category = st.selectbox("Category", ["electronics", "fashion", "fitness"])
    budget = st.slider("Budget (₹)", 500, 50000)
    prefs = st.text_area("Enter your preferences")
    if st.button("Recommend"):
        result = orc.run_recommendation(category, budget, prefs)
        card("Recommendations", result["recommendations_text"])

def page_social(orc):
    section_header("Social Media Content Generator")
    brand = st.text_area("Describe your brand")
    platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter"])
    tone = st.selectbox("Tone", ["Professional", "Funny", "Bold"])
    if st.button("Generate Content"):
        result = orc.run_social_media(brand, platform, tone)
        card("Generated Post", result["content"])

def main():
    st.sidebar.title("Agentic AI Hub")
    page = st.sidebar.radio("Select a tool", ["Support", "Recommendation", "Social Media"])

    orc = get_orchestrator()

    if page == "Support":
        page_support(orc)
    elif page == "Recommendation":
        page_recommendation(orc)
    else:
        page_social(orc)

if __name__ == "__main__":
    main()
