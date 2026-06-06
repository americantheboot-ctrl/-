import streamlit as st
import google.generativeai as genai
import base64

---------------- PAGE CONFIG ----------------

st.set_page_config(
page_title="PROMPT FACTORY",
page_icon="🏭",
layout="wide"
)

---------------- LOAD FONT ----------------

def get_base64_font(font_file):
with open(font_file, "rb") as f:
data = f.read()
return base64.b64encode(data).decode()

font_base64 = get_base64_font("assets/Vazir.ttf")

---------------- CUSTOM CSS ----------------

st.markdown(f"""

<style>

@font-face {{
    font-family: 'Vazir';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

html, body, [class*="st-"] {{
    font-family: 'Vazir', sans-serif;
}}

.stApp {{
    background: #0e1117;
    color: white;
}}

.block-container {{
    padding-top: 2rem;
}}

h1 {{
    font-weight: 800;
    font-size: 58px;
    letter-spacing: -2px;
}}

.glass {{
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 24px;
}}

.stButton>button {{
    width: 100%;
    height: 60px;

    background: linear-gradient(
        135deg,
        #6C63FF,
        #A855F7
    );

    border: none;
    border-radius: 18px;

    color: white;

    font-size: 16px;
    font-weight: 700;
    letter-spacing: 2px;

    box-shadow:
        0 10px 40px rgba(111,76,255,0.35);

    transition: all .3s ease;
}}

.stButton>button:hover {{
    transform: translateY(-3px);
    opacity: 0.95;
}}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {{
    background: #1a1c23 !important;
    color: white !important;
    border-radius: 14px !important;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

</style>""", unsafe_allow_html=True)

---------------- GEMINI SETUP ----------------

try:
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
except:
st.error("کلید API پیدا نشد.")
st.stop()

---------------- UI ----------------

st.title("🏭 PROMPT FACTORY")
st.caption("موتور مهندسی پرامپت سینمایی با هوش مصنوعی")

st.write("")

col1, col2 = st.columns(2)

with col1:

st.markdown("## 🎯 مرکز فرمان خلاقیت")

subject = st.text_input(
    "چه چیزی می‌خواهی خلق شود؟",
    placeholder="مثلاً: فضانوردی در حال نواختن پیانو در مریخ"
)

style = st.selectbox(
    "DNA بصری پروژه",
    [
        "Cyberpunk Neon",
        "Hyper Realistic",
        "Bauhaus Minimal",
        "Renaissance Oil Painting",
        "Cinematic Sci-Fi",
        "Dark Fantasy"
    ]
)

with col2:

st.markdown("## 💡 موتور جزئیات سینمایی")

lighting = st.selectbox(
    "امضای نوری صحنه",
    [
        "Cinematic Mist",
        "Deep Shadows",
        "Studio Soft Light",
        "Volumetric Lighting",
        "Neon Glow"
    ]
)

details = st.text_area(
    "جزئیاتی که اثر را فراموش‌نشدنی می‌کند"
)

st.write("")

---------------- GENERATE ----------------

if st.button("GENERATE MASTERPIECE"):

if subject:

    with st.spinner("در حال مهندسی پرامپت سینمایی..."):

        instruction = f'''

You are an elite AI Prompt Architect.

Generate a highly cinematic AI image prompt.

Subject:
{subject}

Visual Style:
{style}

Lighting:
{lighting}

Additional Details:
{details}

Requirements:

- cinematic composition
- ultra detailed
- realistic textures
- advanced lighting
- depth and atmosphere
- visually powerful
- emotionally immersive

Return only the final polished prompt.
'''

        response = model.generate_content(instruction)

        st.success("پرامپت حرفه‌ای شما آماده شد.")

        st.code(response.text)

else:
    st.warning("ابتدا ایده یا سوژه را وارد کن.")
