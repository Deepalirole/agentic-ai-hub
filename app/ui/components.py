import streamlit as st


def section_header(text: str) -> None:
    st.markdown(f"### {text}")


def card(title: str, body: str, badge: str | None = None) -> None:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    top_line = f"**{title}**"
    if badge:
        top_line += f" &nbsp; <span class='tag'>{badge}</span>"
        st.markdown(top_line, unsafe_allow_html=True)
    else:
        st.markdown(top_line, unsafe_allow_html=True)
    st.markdown(body)
    st.markdown("</div>", unsafe_allow_html=True)

