import streamlit as st

def app():
    # Layout with image beside the text horizontally aligned and vertically centered
    with st.container():
        col1, col2 = st.columns([1, 3], gap="medium")

        with col1:
            st.image("assets/logo.jpeg", width=150)

        with col2:
            st.markdown(
                """
                ## 📰 Fake News Detection

                by Mangam Sai Ram Bhargavi

                Welcome to the **Fake News Detection Web App** 🧠

                - Detect fake news using Machine Learning
                - Enter any news article and get a prediction instantly
                - Clean and interactive user experience

                Use the sidebar to navigate between **Home**, **Detector**, **About**.
                """
            )
