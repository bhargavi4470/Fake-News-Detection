import streamlit as st

def app():
    st.image("assets/logo.jpeg", width=120)
    st.title("ℹ️ About This Project")
    st.write("---")

    # 📖 Project Overview
    st.subheader("📖 Project Overview")
    st.markdown("""
    The **Fake News Detection System** is an intelligent web application that detects and classifies news articles as **Real or Fake** using advanced 
    **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques.

    This project aims to **combat the spread of misinformation** and help users verify the authenticity of online news content quickly and accurately.
    """)

    # 🎯 Objectives
    st.subheader("🎯 Objectives")
    st.markdown("""
    - Detect misleading or fabricated news articles accurately  
    - Provide a simple and user-friendly interface for everyone  
    - Raise awareness about the danger of fake news  
    - Encourage critical thinking and digital media literacy
    """)

    # 📊 Dataset
    st.subheader("📊 Dataset")
    st.markdown("""
    - **Dataset:** [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)  
    - **Source:** Kaggle  
    - Contains over **40,000 news articles** with fields like `title`, `text`, `subject`, and `date`.  
    - Articles are labeled as either **Fake** or **True**.
    """)

    # 🧠 Model
    st.subheader("🧠 Machine Learning Model")
    st.markdown("""
    - Text preprocessing using NLTK (stopword removal, stemming, tokenization)  
    - Feature extraction using Scikit-learn's **TF-IDF Vectorizer**  
    - Classification using **Logistic Regression** algorithm  
    - Achieved high accuracy and F1-score during testing
    """)

    # ⚙️ Technologies Used
    st.subheader("⚙️ Technologies Used")
    st.markdown("""
    - **Frontend:** Streamlit for interactive UI  
    - **Backend/Modeling:** Python, Pandas, NumPy  
    - **Machine Learning:** Scikit-learn, NLTK  
    - **Deployment (optional):** Streamlit Cloud or Heroku
    """)

    # 👤 Developer
    st.subheader("👤 About the Developer")
    st.markdown("""
    **Mangam Sai Ram Bhargavi**  
    - B.Tech (Data Science Student)  
    - Passionate about AI, Machine Learning, and building impactful projects that solve real-world problems.  
    - This project is part of personal initiative to fight misinformation using technology.
    """)

    st.markdown("---")
    st.caption("© 2025 Mangam Sai Ram Bhargavi | [GitHub](https://github.com/) • [LinkedIn](https://linkedin.com/)")
