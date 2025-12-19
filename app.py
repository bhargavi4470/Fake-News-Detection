import streamlit as st

# Set page config only once at the very beginning
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

# Hide Streamlit default menu, footer, header, and left sidebar navigation
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* Hide left sidebar navigation */
    [data-testid="stSidebar"] {
        display: none;
    }
    /* Style navigation buttons horizontally */
    .nav-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Navigation links as buttons on page horizontally
nav_links = [
    ("Home", "🏠 Home"),
    ("About", "ℹ️ About"),
    ("Detector", "🔍 Detector")
]

current_page = st.session_state.get("page", "Home")

nav_container = st.container()
with nav_container:
    cols = st.columns(len(nav_links))
    for idx, (key, label) in enumerate(nav_links):
        if cols[idx].button(label):
            st.session_state["page"] = key
            st.rerun()

if current_page == "Home":
    import pages.Home as home
    home.app()
elif current_page == "Detector":
    import pages.Detector as detector
    detector.app()
elif current_page == "About":
    import pages.About as about
    about.app()
else:
    st.error(f"Page '{current_page}' not found.")

st.markdown("---")
st.caption("© 2025 Mangam Sai Ram Bhargavi | [GitHub](https://github.com/) • [LinkedIn](https://linkedin.com/)")
