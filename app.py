import streamlit as st


# PAGE CONFIG

st.set_page_config(
    page_title="VeritasAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# THEME STATE

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# THEME TOGGLE

theme_col1, theme_col2 = st.columns([10, 1])

with theme_col2:
    dark_mode = st.toggle(
        "🌙",
        value=(st.session_state.theme == "Dark")
    )

if dark_mode:
    st.session_state.theme = "Dark"
else:
    st.session_state.theme = "Light"

# CSS

if st.session_state.theme == "Light":

    st.markdown("""
    <style>

    .stApp{
        background:#f8fafc;
    }

    .hero-title{
        text-align:center;
        font-size:clamp(40px,8vw,90px);
        font-weight:800;
        color:#0f172a;
        line-height:1.1;
    }

    .hero-subtitle{
        text-align:center;
        font-size:clamp(18px,2vw,28px);
        color:#64748b;
        max-width:900px;
        margin:auto;
        line-height:1.8;
    }

    .blue{
        color:#2563eb;
    }

    .badge{
        display:inline-block;
        background:#dbeafe;
        color:#2563eb;
        padding:10px 20px;
        border-radius:25px;
        font-weight:600;
        font-size:14px;
    }

    .info-card{
        background:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0px 4px 15px rgba(0,0,0,.08);
    }

    .logo{
        color:#2563eb;
        font-size:42px;
        font-weight:bold;
    }

    .stButton > button{
        background:#2563eb !important;
        color:white !important;
        border:none !important;
        border-radius:10px !important;
        height:55px !important;
        font-size:18px !important;
        font-weight:600 !important;
        width:100%;
    }

    .stButton > button:hover{
        background:#1d4ed8 !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp{
        background:#0E1117;
    }

    h1,h2,h3,h4,h5,h6,p,label{
        color:white !important;
    }

    .hero-title{
        text-align:center;
        font-size:clamp(40px,8vw,90px);
        font-weight:800;
        color:white;
        line-height:1.1;
    }

    .hero-subtitle{
        text-align:center;
        font-size:clamp(18px,2vw,28px);
        color:#cbd5e1;
        max-width:900px;
        margin:auto;
        line-height:1.8;
    }

    .blue{
        color:#3b82f6;
    }

    .badge{
        display:inline-block;
        background:#1e3a8a;
        color:white;
        padding:10px 20px;
        border-radius:25px;
        font-weight:600;
    }

    .info-card{
        background:#161b22;
        padding:30px;
        border-radius:20px;
    }

    .logo{
        color:#3b82f6;
        font-size:42px;
        font-weight:bold;
    }

    .stButton > button{
        background:#2563eb !important;
        color:white !important;
        border:none !important;
        border-radius:10px !important;
        height:55px !important;
        font-size:18px !important;
        width:100%;
    }

    </style>
    """, unsafe_allow_html=True)

# NAVIGATION BAR
nav1, nav2, nav3 = st.columns([6, 2, 2])

with nav1:
    st.markdown(
        "<div class='logo'>🛡️ VeritasAI</div>",
        unsafe_allow_html=True
    )

with nav2:
    st.page_link(
        "app.py",
        label="🏠 Home"
    )

with nav3:
    st.page_link(
        "pages/1_Check_Article.py",
        label="📰 Check Article"
    )

st.markdown("<br>", unsafe_allow_html=True)

# HERO SECTION

st.markdown(f"""
<div style="text-align:center;">
    <div class="badge">
        New: Detailed Source Analysis
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="hero-title">
Verify News With<br>
<span class="blue">AI Precision</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="hero-subtitle">
Our advanced machine learning algorithms analyze
articles for credibility, bias and factual accuracy
in seconds.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# START BUTTON

if st.button(
    "🚀 Start Analysis",
    use_container_width=True
):
    st.switch_page("pages/1_Check_Article.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# ABOUT CARD

st.markdown("""
<div class="info-card">

<h3 style="color:#2563eb;">
About VeritasAI
</h3>

<p>
VeritasAI is a Machine Learning powered Fake News
Detection System developed to help users verify
news articles, combat misinformation and improve
information credibility through automated analysis.
</p>

</div>
""", unsafe_allow_html=True)