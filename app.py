import streamlit as st
from streamlit_lottie import st_lottie
import json
from pathlib import Path

st.set_page_config(page_title="Digital Love Card ❤️", page_icon="💌", layout="centered")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_heart = load_lottiefile(Path("assets/hearts.json"))

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        height: 100%;
        margin: 0;
        overflow: hidden;
        background-color: #fff0f5;
    }
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .title {
        text-align: center;
        color: #ff4b4b;
        font-size: 40px;
        font-weight: 700;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .message {
        background-color: #ffe6eb;
        padding: 15px 25px;
        border-radius: 20px;
        font-size: 18px;
        color: #333;
        text-align: center;
        line-height: 1.6;
        max-width: 600px;
        box-shadow: 0px 4px 12px rgba(255, 0, 102, 0.2);
        margin-top: 10px;
    }
    .heart-btn button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        font-size: 50px;
        animation: heartbeat 1.5s infinite;
        transition: transform 0.2s ease-in-out;
    }
    .heart-btn button:hover {
        transform: scale(1.3);
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("<div class='title'>💖My Love, Sanjida Haque Saima💖</div>", unsafe_allow_html=True)

    st_lottie(lottie_heart, height=180, key="heart")

    st.markdown(
        """
        <div class='message'>
            Hey my beautiful Saima 💕,<br><br>
            You are the reason my world feels brighter every single day.<br>
            Your smile can fix any bad mood, and your voice feels like music to my heart 🎶.<br><br>
            No code, no AI, no algorithm could ever express how much you mean to me 💞.<br><br>
            With all my love,<br>
            <b>Rakib 💌</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='margin-top:15px;'>Click the heart if you love me too 😘</div>", unsafe_allow_html=True)
    col = st.columns([1,1,1])[1]
    with col:
        if st.button("❤️"):
            st.success("Awwww Saima clicked the heart! 💞 You just made my day babe❤️")
            st.balloons()
