import streamlit as st
import joblib
from src.preprocess import clean_text
import numpy as np

def app():
    @st.cache_resource
    def load_resources():
        model = joblib.load('model.pkl')
        vectorizer = joblib.load('vectorizer.pkl')
        return model, vectorizer

    model, vectorizer = load_resources()

    st.image("assets/logo.jpeg", width=80)
    st.title("🔍 Fake News Detector")

    news_text = st.text_area("📝 Enter News Text", height=200, placeholder="Paste your news here...")

    if st.button("Predict"):
        if news_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            with st.spinner("Analyzing..."):
                cleaned = clean_text(news_text)
                st.write("**Debug Info:**")
                st.write(f"Cleaned Text: {cleaned}")
                vect = vectorizer.transform([cleaned])
                proba = model.predict_proba(vect)[0]
                st.write(f"Prediction Probabilities: Fake={proba[1]*100:.2f}%, Real={proba[0]*100:.2f}%")
                prediction = np.argmax(proba)
                confidence = proba[prediction] * 100
                st.write(f"Prediction Value: {prediction} (1=Real, 0=Fake)")

            if confidence < 70:
                st.warning(f"⚠️ Prediction is uncertain ({confidence:.2f}% confidence). Please verify manually.")
            elif prediction == 0:
                st.error(f"🟥 This news is likely FAKE ({confidence:.2f}% confidence)")
            else:
                st.success(f"🟩 This news is likely REAL ({confidence:.2f}% confidence)")

    st.markdown("---")
    st.caption("© 2025 Mangam Sai Ram Bhargavi | [GitHub](https://github.com/) • [LinkedIn](https://linkedin.com/)")
