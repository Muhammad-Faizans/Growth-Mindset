# Streamlit
import streamlit as st

# Page Configurations
st.set_page_config(
    page_title="Growth Mindset",
    layout="wide",
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #2E86C1;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #2E86C1;
            padding: 10px;
        }
        .stButton > button {
            border-radius: 8px;
            background-color: #2E86C1;
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Container
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Header Section
st.header("🚀 Welcome to Your Growth Journey")
st.write(
    "Embrace challenges, learn from mistakes, and unlock your full potential. "
    "This AI-powered tool will help you stay motivated and focused on your goals."
)

# Quote Section
st.header("🌟 Today's Growth Mindset Quote")
st.markdown(
    """
    > **“Success is not final, failure is not fatal: It is the courage to continue that counts.”**  
    > — *Winston Churchill*
    """
)

# Challenge Section
st.header("💡 What's Your Challenge Today?")
user_input = st.text_input("Describe the challenge you're facing today")

if user_input:
    st.success(f"💪 Keep pushing forward! You are facing: **{user_input}**. Stay strong!")
else:
    st.warning("⚡ Please enter your challenge to continue.")

# Reflection Section
st.header("📝 Reflect on Your Progress")
reflection = st.text_input("What have you learned from your journey so far?")

if reflection:
    st.success(f"🌱 Growth in progress! **{reflection}**")
else:
    st.info("🧠 Reflection helps us learn and grow. Share your insights!")

# Achievements Section
st.header("🏆 Celebrate Your Achievements")
achievements = st.text_input("Share your achievements and milestones")

if achievements:
    st.success(f"🎉 Congratulations! **{achievements}** Keep shining!")
else:
    st.info("👏 Celebrating your milestones keeps you motivated!")

# Footer Section
st.write("---")
st.markdown(
    "<p style='text-align: center; font-size: 18px; color: #2E86C1;'>"
    "💙 Keep believing in yourself—You can achieve anything! 💙"
    "</p>",
    unsafe_allow_html=True,
)

# Copyright
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "© 2025 Muhammad Faizan. All rights reserved."
    "</p>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
