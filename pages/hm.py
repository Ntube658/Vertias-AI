#import streamlit as st

#st.set_page_config(
    #page_title="VeritasAI",
   # page_icon="🛡️",
   # layout="wide"
#)

#st.markdown("""
# 🛡️ VeritasAI

## Verify News With AI Precision

#Our advanced machine learning algorithms analyze articles
#for credibility, bias, and factual accuracy in seconds.
#""")

#st.page_link(
    #"pages/1_Check_Article.py",
    #label="🚀 Start Analysis"
#)

import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="VeritasAI",
    page_icon="🛡️",
    layout="wide"
)

# NAVBAR
col1, col2, col3 = st.columns([8,2,2])

with col1:
    st.markdown(
        """
        <h2 style='color:#2563eb'>
        🛡️ VeritasAI
        </h2>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.page_link(
        "app.py",
        label="🏠 Home"
    )

with col3:
    st.page_link(
        "pages/1_Check_Article.py",
        label="📰 Check Article"
    )

# HERO SECTION

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align:center'>
        <h1 style='font-size:70px'>
        Verify News With<br>
        <span style='color:#2563eb'>
        AI Precision
        </span>
        </h1>

        <h4 style='color:gray'>
        Our machine learning algorithms analyze articles
        for credibility, bias and factual accuracy in seconds.
        </h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

col1,col2,col3=st.columns([3,2,3])

with col2:

    st.page_link(
        "pages/1_Check_Article.py",
        label="🚀 Start Analysis",
        use_container_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

st.info(
    """
    VeritasAI is a Machine Learning powered Fake News
    Detection System developed to help users verify
    news articles and reduce misinformation.
    """
)