import streamlit as st

def apply_theme() -> None:
    css = """
    <style>

    /* Remove Streamlit top whitespace */
 /* Slim top header so the sidebar toggle arrow is visible */
[data-testid="stHeader"] {
    background: linear-gradient(90deg, #4C1D95 0%, #020617 60%, #000000 100%);
    height: 3rem;
    padding: 0 1rem;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.45);
}

/* Make the arrow / menu icon visible on dark background */
[data-testid="stHeader"] button {
    color: #EDE9FE !important;
}

/* Remove extra padding inside header container */
[data-testid="stHeader"] > div {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}


    /* Fix the blank white bar created by padding */
    .stApp {
        padding-top: 0 !important;
    }

    /* Background gradient */
    .stApp {
        background: radial-gradient(circle at top left, #4C1D95 0%, #020617 45%, #000000 100%);
        color: #F3F4F6;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #101625 60%, #1C1F27 100%);
        color: #E5E7EB !important;
        border-right: 1px solid rgba(148, 163, 184, 0.2);
    }

    /* Sidebar labels */
    [data-testid="stSidebar"] label {
        color: #E5E7EB !important;
    }

    /* White Glass Cards (unchanged) */
    .glass-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 1.5rem 1.75rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1.25rem;
    }

    /* Lavender input boxes */
    .stTextInput input, 
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #EDE9FE !important;    /* Light lavender */
        color: #111827 !important;              /* Dark text */
        border-radius: 12px !important;
        border: 1px solid #C4B5FD !important;
        padding: 8px 12px !important;
    }

    /* Input box placeholder text */
    ::placeholder {
        color: #6B21A8 !important;
        opacity: 1 !important;
    }

    /* Fix label text (make visible on dark background) */
    .stTextInput label, 
    .stTextArea label, 
    .stSelectbox label {
        color: #EDE9FE !important;   /* Lavender text */
        font-weight: 500;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6D28D9, #A855F7) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        box-shadow: 0 8px 24px rgba(109, 40, 217, 0.35) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #7C3AED, #C084FC) !important;
        transform: translateY(-2px);
    }

    /* Improve card styles */
    .card {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        color: #F3F4F6 !important;
    }

    .card h3, .card h4 {
        color: #FDFDFE !important;
    }

    /* Fix Radio styles */
    [data-testid="stSidebar"] .stRadio label {
        color: #EDE9FE !important;
    }
/* ------------------------ */
/*      SIDEBAR FIXES       */
/* ------------------------ */

/* Sidebar title "AI Hub" */
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3 {
    color: #F4F3FF !important;   /* visible lavender-white */
    font-weight: 700 !important;
}

/* Sidebar labels (Choose mode, Model, Debug mode) */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #EDEAFF !important;   /* brighter lavender */
    font-size: 0.92rem !important;
}

/* Radio button labels (Support Assistant, Product...) */
[data-testid="stSidebar"] .stRadio div div label {
    color: #ECECFE !important;
    font-size: 0.95rem !important;
    padding: 6px 0 !important; /* spacing between items */
}

/* Add extra spacing between radio items */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
    margin-bottom: 8px !important;
}

/* Model + Debug text styling */
[data-testid="stSidebar"] .css-17eq0hr, 
[data-testid="stSidebar"] .css-1cvrr1i,
[data-testid="stSidebar"] .stMarkdown {
    color: #F0EFFF !important;
    font-size: 0.95rem !important;
}

/* Horizontal divider color soft */
[data-testid="stSidebar"] hr {
    border-color: rgba(255, 255, 255, 0.1) !important;
    margin: 18px 0 !important;
}
/* Center main content and limit width for a premium feel */
.block-container {
    max-width: 1180px;
    padding-top: 1.25rem !important;
    margin-left: auto;
    margin-right: auto;
}

/* Slightly tighter spacing under the hero "Agentic Console" card */
.glass-card {
    margin-top: 0.75rem;
}

/* Make section titles pop a bit more */
h2, h3 {
    letter-spacing: 0.02em;
}


    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

