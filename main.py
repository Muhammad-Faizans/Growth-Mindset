# Streamlit
import streamlit as st

st.set_page_config(
    page_title="Growth Mindset",
    layout="wide",
)

st.header("Welcome to your Growth Journey")
st.write("Embrace challenges and learn from mistakes,and unlock your full potential.This AI-powered tool will help you stay motivated and focused on your goals.")    

# Quote Section
st.header("Today's Growth Mindset Quote")
st.write("**Success is not final, failure is not fatal: It is the courage to continue that counts.** — Winston Churchill")

st.header("Whats Your Challenge today?")
user_input = st.text_input("Descibe your challenge you're facing today")

if user_input:
    st.success(f"You are facing {user_input}. Keep pushing forward toward your goals.")
    # st.write("Remember, every challenge is an opportunity to grow and learn. Embrace it and take action to overcome it.")
else:
    st.warning("Please enter your challenge to continue.")
    

    st.header("Reflect on your progress")
    reflection = st.text_input("Reflect on your progress and what you've learned so far")
    
if reflection:
    st.success(f"Great Insights! {reflection}")
else:
    st.info("Reflection on past experience help us learn and grow. Share your insights with us.")
    

# acheivments section
st.header("Celebrate Your Achievements")
acheivements = st.text_input("Share your achievements and milestones")

if acheivements:
    st.success(f"Congratulations! {acheivements}")
else:
    st.info("Celebrate your achievements and milestones to stay motivated and inspired.")


# footer
st.write("- - - - - -")
st.write("Keep Believing in yourself, you can achieve anything you set your mind to.")

# copyright
st.write("© 2025 Muhammad Faizan. All rights reserved.")
    