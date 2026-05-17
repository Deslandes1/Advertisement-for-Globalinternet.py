import streamlit as st
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="GlobalInternet.py - Build Your Website",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- TRANSLATIONS ----------
def get_translations(lang):
    texts = {
        "en": {
            "company_name": "🌐 GlobalInternet.py",
            "tagline": "Build any website you wish",
            "description1": "Make your business work online and be seen worldwide.",
            "description2": "We create custom websites, web apps, and digital solutions – fully tailored to your needs.",
            "highlight": "👉 You dream it, we code it. 👈",
            "contact_name": "Gesner Deslandes – Founder & Lead Engineer",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "music_btn": "🎵 Add your music track here (click to simulate)",
            "footer_note": "🎬 For your video recording, play your own music in the background. This ad is ready to be captured.",
            "sidebar_title": "🌐 Language",
            "sidebar_instruction": "Select your language"
        },
        "fr": {
            "company_name": "🌐 GlobalInternet.py",
            "tagline": "Créez n'importe quel site web",
            "description1": "Faites fonctionner votre entreprise en ligne et soyez vu dans le monde entier.",
            "description2": "Nous créons des sites web personnalisés, des applications web et des solutions numériques – entièrement adaptés à vos besoins.",
            "highlight": "👉 Vous rêvez, nous codons. 👈",
            "contact_name": "Gesner Deslandes – Fondateur et ingénieur principal",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "music_btn": "🎵 Ajoutez votre piste musicale ici (cliquez pour simuler)",
            "footer_note": "🎬 Pour votre enregistrement vidéo, jouez votre propre musique en arrière‑plan. Cette publicité est prête à être capturée.",
            "sidebar_title": "🌐 Langue",
            "sidebar_instruction": "Choisissez votre langue"
        },
        "es": {
            "company_name": "🌐 GlobalInternet.py",
            "tagline": "Construye cualquier sitio web que desees",
            "description1": "Haga que su negocio funcione en línea y sea visto en todo el mundo.",
            "description2": "Creamos sitios web personalizados, aplicaciones web y soluciones digitales – totalmente adaptados a sus necesidades.",
            "highlight": "👉 Usted lo sueña, nosotros lo codificamos. 👈",
            "contact_name": "Gesner Deslandes – Fundador e ingeniero principal",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "music_btn": "🎵 Agrega tu pista de música aquí (haz clic para simular)",
            "footer_note": "🎬 Para tu grabación de video, reproduce tu propia música de fondo. Este anuncio está listo para ser capturado.",
            "sidebar_title": "🌐 Idioma",
            "sidebar_instruction": "Seleccione su idioma"
        },
        "ht": {
            "company_name": "🌐 GlobalInternet.py",
            "tagline": "Konstwi nenpòt sit wèb ou vle",
            "description1": "Fè biznis ou travay sou entènèt epi yo wè ou atravè lemond.",
            "description2": "Nou kreye sit wèb pèsonalize, aplikasyon entènèt, ak solisyon dijital – konplètman adapte ak bezwen ou yo.",
            "highlight": "👉 Ou reve l, nou kode l. 👈",
            "contact_name": "Gesner Deslandes – Fondatè ak enjenyè prensipal",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "music_btn": "🎵 Ajoute mizik ou la (klike pou simulation)",
            "footer_note": "🎬 Pou anrejistreman videyo w, jwe pwòp mizik ou nan fon. Piblisite sa a pare pou kaptire.",
            "sidebar_title": "🌐 Lang",
            "sidebar_instruction": "Chwazi lang ou"
        }
    }
    return texts[lang]

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
    /* Sidebar language selector styling */
    [data-testid="stSidebar"] {
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(10px);
        border-right: 2px solid #ffd966;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
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

# ---------- ANIMATED STARS AND BALLOONS (random positions) ----------
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

# ---------- LANGUAGE SELECTION (SIDEBAR) ----------
st.sidebar.markdown("## 🌐 Language / Langue")
lang_choice = st.sidebar.selectbox(
    "Select your language",
    ["English", "Français", "Español", "Kreyòl Ayisyen"]
)
lang_map = {
    "English": "en",
    "Français": "fr",
    "Español": "es",
    "Kreyòl Ayisyen": "ht"
}
t = get_translations(lang_map[lang_choice])

# ---------- MAIN CONTENT (USING TRANSLATIONS) ----------
st.markdown(
    f"""
    <div class="ad-container">
        <div class="offer-card">
            <div class="company-name">{t['company_name']}</div>
            <div class="tagline">{t['tagline']}</div>
            <div class="description">
                {t['description1']}<br>
                {t['description2']}
            </div>
            <div class="highlight">{t['highlight']}</div>
            <div class="contact-info">
                <strong>{t['contact_name']}</strong><br>
                {t['phone']} &nbsp;|&nbsp; {t['email']}<br>
                <a href="{t['website']}" target="_blank">{t['website']}</a>
            </div>
        </div>
        <button class="music-btn" id="musicPlaceholder">{t['music_btn']}</button>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- SIMPLE MUSIC PLACEHOLDER ----------
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

# ---------- FOOTER NOTE ----------
st.caption(t['footer_note'])

