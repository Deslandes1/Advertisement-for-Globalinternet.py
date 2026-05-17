import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="GlobalInternet.py - Build Your Website",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS FOR ANIMATED, COLORFUL AD ----------
st.markdown(
    """
    <style>
    /* Full page background gradient */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
        background-attachment: fixed;
        overflow-x: hidden;
    }
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .ad-container {
        position: relative;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        z-index: 2;
        padding: 2rem;
    }
    /* Central card */
    .offer-card {
        background: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(12px);
        border-radius: 60px;
        padding: 2.5rem 3rem;
        max-width: 900px;
        margin: 2rem auto;
        box-shadow: 0 25px 45px rgba(0,0,0,0.3);
        border: 2px solid #ffd966;
        animation: glowPulse 2s infinite alternate;
    }
    @keyframes glowPulse {
        0% { box-shadow: 0 0 5px #ffd966, 0 0 10px #ffaa33; }
        100% { box-shadow: 0 0 25px #ffd966, 0 0 40px #ffaa33; }
    }
    .company-name {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffd966, #ffaa33, #ff6b6b);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    .tagline {
        font-size: 1.8rem;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 2px 2px 4px #000;
        margin-bottom: 1rem;
    }
    .description {
        font-size: 1.3rem;
        color: #fef9e6;
        line-height: 1.5;
        margin: 1rem 0;
    }
    .highlight {
        font-size: 1.6rem;
        font-weight: bold;
        color: #ffd966;
        margin-top: 0.5rem;
    }
    .contact-info {
        background: rgba(0,0,0,0.5);
        border-radius: 50px;
        padding: 0.8rem 1.5rem;
        display: inline-block;
        margin-top: 1rem;
        font-size: 1rem;
        color: #fff;
    }
    .contact-info a {
        color: #ffd966;
        text-decoration: none;
    }
    /* Animated stars and balloons */
    .star {
        position: fixed;
        color: #ffd700;
        font-size: 2rem;
        animation: spinStar 4s linear infinite, floatStar 3s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }
    @keyframes spinStar {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes floatStar {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .balloon {
        position: fixed;
        font-size: 2.5rem;
        animation: floatBalloon 6s ease-in-out infinite, sway 4s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
        opacity: 0.8;
    }
    @keyframes floatBalloon {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-30px); }
        100% { transform: translateY(0px); }
    }
    @keyframes sway {
        0% { transform: translateX(0px); }
        50% { transform: translateX(15px); }
        100% { transform: translateX(0px); }
    }
    /* Music placeholder button */
    .music-btn {
        background-color: #e94560;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        margin-top: 2rem;
        transition: 0.3s;
    }
    .music-btn:hover {
        background-color: #ff6b6b;
        transform: scale(1.05);
    }
    /* Responsive */
    @media (max-width: 768px) {
        .company-name { font-size: 2.5rem; }
        .tagline { font-size: 1.3rem; }
        .description { font-size: 1rem; }
        .offer-card { padding: 1.5rem; margin: 1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HTML WITH ANIMATED STARS AND BALLOONS ----------
# Generate random positions for stars and balloons
import random

stars_html = ""
for i in range(30):
    left = random.randint(0, 100)
    top = random.randint(0, 100)
    delay = random.randint(0, 5)
    size = random.choice(["1.5rem", "2rem", "2.5rem"])
    stars_html += f'<div class="star" style="left: {left}%; top: {top}%; animation-delay: {delay}s; font-size: {size};">⭐</div>'

balloons_html = ""
balloon_emojis = ["🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈"]
for i in range(20):
    left = random.randint(0, 100)
    top = random.randint(0, 100)
    delay = random.randint(0, 8)
    duration = random.randint(5, 10)
    balloon = random.choice(balloon_emojis)
    balloons_html += f'<div class="balloon" style="left: {left}%; top: {top}%; animation-duration: {duration}s; animation-delay: {delay}s;">{balloon}</div>'

st.markdown(f'{stars_html}{balloons_html}', unsafe_allow_html=True)

# ---------- MAIN CONTENT ----------
st.markdown(
    """
    <div class="ad-container">
        <div class="offer-card">
            <div class="company-name">🌐 GlobalInternet.py</div>
            <div class="tagline">Build any website you wish</div>
            <div class="description">
                Make your business work online and be seen <strong>worldwide</strong>.<br>
                We create custom websites, web apps, and digital solutions –<br>
                fully tailored to your needs.
            </div>
            <div class="highlight">👉 You dream it, we code it. 👈</div>
            <div class="contact-info">
                <strong>Gesner Deslandes</strong> – Founder & Lead Engineer<br>
                📞 <a href="tel:+50947385663">+509 4738-5663</a> &nbsp;|&nbsp;
                ✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a><br>
                🌐 <a href="https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/" target="_blank">globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/</a>
            </div>
        </div>
        <button class="music-btn" id="musicPlaceholder">🎵 Add your music track here (click to simulate)</button>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- SIMPLE MUSIC PLACEHOLDER (can be replaced with actual audio later) ----------
st.markdown(
    """
    <script>
    const btn = document.getElementById('musicPlaceholder');
    if (btn) {
        btn.addEventListener('click', () => {
            alert('You can add your own music track to this video recording. In the final software, we can integrate an audio player.');
        });
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Optional: a note that music will be added during video recording
st.caption("🎬 For your video recording, play your own music in the background. This ad is ready to be captured.")
