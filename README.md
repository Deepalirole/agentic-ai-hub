## Sales, Marketing & Support AI Hub

An end-to-end AI SaaS-style application built with **Python**, **Streamlit**, **CrewAI**, **Llama**, and **ChromaDB**.

This app provides three AI assistants:

- **Support Assistant** – resolves FAQs and flags complex issues for human escalation.
- **Product Recommendation Agent** – suggests products based on budget, category, and preferences.
- **Social Media Agent** – generates content ideas, captions, and a 7‑day content plan.

### Features

- **Multi-agent orchestration** with CrewAI for support, recommendations, and social media.
- **Llama-based LLM client** via a generic OpenAI-compatible HTTP API.
- **FAQ retrieval** using a lightweight in-memory ChromaDB vector store.
- **Modern Streamlit UI** with a purple & lavender theme and reusable UI components.
- **Configurable settings** (model, temperature, debug mode) via environment variables.

### Project Structure

- `app/main.py` – Streamlit entrypoint.
- `app/config.py` – Environment-based configuration.
- `app/agents/` – CrewAI agents and orchestrator.
- `app/services/` – LLM client, vector store, and mock data loaders.
- `app/ui/` – Theming and reusable UI components.
- `app/utils/` – Logging utilities and prompt templates.

### Stack

- **Python**
- **Streamlit**
- **CrewAI**
- **Llama** (via an OpenAI-compatible API endpoint)
- **ChromaDB** (FAQ vector store)

### Setup

1. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**

   At minimum configure:

   - `LLM_API_BASE` – Base URL for an OpenAI-compatible endpoint (e.g. a Llama server).
   - `LLM_API_KEY` – API key if required (optional for some local setups).
   - `LLM_MODEL_NAME` – Model name (default: `llama3.1`).
   - `DEBUG_MODE` – `true`/`false` to show or hide agent logs in the UI.

4. **Run the app**

   ```bash
   streamlit run app/main.py
   ```

### How Each Mode Works

- **Support Assistant**
  - Uses a ChromaDB vector store of FAQs.
  - Retrieves the most relevant entries and asks the LLM to draft a resolution.
  - If the issue appears unclear or out-of-scope, the response suggests escalation to human support.

- **Product Recommendation Agent**
  - Loads a small in-memory catalog of products.
  - Filters by category and budget, then asks the LLM to choose 3–5 items and a final **Best Pick**.

- **Social Media Agent**
  - Takes a brand description, tone, and platform (Instagram, LinkedIn, X).
  - Generates 5 content ideas, 5 caption options, and a 7‑day posting plan including CTA and hashtags.

### Notes

- The LLM client is intentionally generic so you can plug in:
  - A local Llama server exposing an OpenAI-compatible API, or
  - A hosted provider with the same interface.
- Error handling is kept friendly: if configuration is missing or a call fails, Streamlit will surface readable errors in the UI and logs.



