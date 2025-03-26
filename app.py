import streamlit as st
import joblib
import numpy as np


# Load the pre-trained model and vectorizer
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# Streamlit App Title
st.title("📰 Fake News Detector")
st.markdown("## 🔍 Enter a news article below to check if it's **Fake** or **Real**")

# Input Text Area with Styled Border
st.markdown("""
    <style>
        .stTextArea textarea {
            border: 2px solid #FF4B4B;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
inputn = st.text_area("📝 News Article:", "", height=200)

# Interactive Button
if st.button("🔎 Check News", help="Click to analyze the news article"): 
    if inputn.strip():
        try:
            # Transform input
            transformed_input = vectorizer.transform([inputn])
            prediction = model.predict(transformed_input)
            probability = model.predict_proba(transformed_input)
            confidence = np.max(probability) * 100
            
            # Display Result with Animated Status
            if prediction[0] == 1:
                st.success("✅ The News appears to be **Real**!")
                st.balloons()
                st.info(f"Confidence Score: {confidence:.2f}%")
            else:
                st.error("🚨 The News appears to be **Fake**!")
                st.snow()
                st.warning(f"Confidence Score: {confidence:.2f}%")
        except Exception as e:
            st.error("⚠️ An error occurred while processing the text. Please try again.")
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# Footer with Interactive Elements
st.markdown("---")
st.markdown("💡 **Note:** This model is trained on a specific dataset and may not be 100% accurate. Always verify information from trusted sources.")

