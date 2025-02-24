import streamlit as st
import requests
import base64
st.set_page_config(page_title="Sentiment Analysis", page_icon="🎭", layout="centered")
def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)
set_background("interface.jpg")
#st.image("sentiment_banner.png", caption="AI Sentiment Analysis")
# Giao diện phần đầu trang
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🎬 Deep Learning In Sentiment Analysis - IMDB Movie Reviews</h1>
    <p style='text-align: center; font-size:18px;'>Enter a movie review and let AI analyze its sentiment!</p>
    <hr>
""", unsafe_allow_html=True)

# Ô nhập bình luận
user_input = st.text_area("✍️ **Enter your comment:**", height=150, placeholder="Type your review here...")

# Nút dự đoán
if st.button("🔍 **Analyze**", use_container_width=True):
    if user_input:
        with st.spinner("⏳ Analyzing sentiment... Please wait!"):
            response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})

            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]

                # Cải thiện hiển thị kết quả
                if prediction == "positive":
                    st.markdown("""
    <div style="background-color: #DFF6FF; padding: 10px; border-radius: 10px; text-align: center;">
        <h3 style="color: #0077b6; font-weight: bold;">✅ Positive Sentiment! 🎉😊</h3>
    </div>
""", unsafe_allow_html=True)
                    st.markdown("""
    <div style='background-color:#DDFFDD; padding: 10px; border-radius: 10px; text-align: center;'>
        <h3 style='color: green;'>🎯 This is a positive review! 👍</h3>
        <p style='color: darkblue; font-weight: bold;'>Keep up the positive vibes! 🎉</p>
    </div>
""", unsafe_allow_html=True)
                else:
                    st.markdown("""
    <div style="background-color: #FFD6D6; padding: 10px; border-radius: 10px; text-align: center;">
        <h3 style="color: #D90429; font-weight: bold;">❌ Negative Sentiment! 😞</h3>
    </div>
""", unsafe_allow_html=True)
                    st.markdown("""
    <div style='background-color:#FFDDDD; padding: 10px; border-radius: 10px; text-align: center;'>
        <h3 style='color: red;'>⚠️ This review has a negative sentiment.</h3>
        <p style='color: darkred; font-weight: bold;'>Try rephrasing it to express a more positive tone.</p>
    </div>
""", unsafe_allow_html=True)

            else:
                st.error("⚠️ **Error:** Unable to connect to API! Please try again later.", icon="🚨")
    else:
        st.warning("⚠️ **Please enter a comment before analyzing!**", icon="⚠️")

# Chân trang cải thiện
st.markdown("""
    <br><hr>
    <p style='text-align: center; font-size: 14px;'>
        🚀 Powered by AI | Sentiment Analysis for IMDb Movie Reviews 🎭
    </p>
""", unsafe_allow_html=True)


