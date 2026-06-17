import streamlit as st
import pickle
import re
import plotly.graph_objects as go

# LOAD MODELS
LR = pickle.load(open("LR.pkl","rb"))
DTC = pickle.load(open("DTC.pkl","rb"))
rfc = pickle.load(open("rfc.pkl","rb"))
MNB = pickle.load(open("MNB.pkl","rb"))

vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.markdown("""
    <style>
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

# PREPROCESSING
def preprocess(text):

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    text = text.lower()

    return text

# NAVBAR

col1,col2,col3=st.columns([8,2,2])

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
# Initialize theme
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# Theme toggle
theme = st.toggle(
    "🌙 Mode",
    value=(st.session_state.theme == "Dark")
)

if theme:
    st.session_state.theme = "Dark"
else:
    st.session_state.theme = "Light"

if st.session_state.theme == "Dark":

    st.markdown("""
    <style>

    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1,h2,h3,h4,h5,h6,p,label {
        color: white !important;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #262730 !important;
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp {
        background-color: white;
        color: black;
    }

    h1,h2,h3,h4,h5,h6,p,label {
        color: black !important;
    }

    </style>
    """, unsafe_allow_html=True)

# TITLE

st.markdown(
    """
    <div style='text-align:center'>
        <h1>Check Article Credibility</h1>
        <p>
        Paste the text of a news article below.
        Our AI will analyze it for misinformation,
        bias and reliability.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# FORM

title = st.text_input(
    "Article Title (Optional)"
)


url = st.text_input(
    "Article URL (Optional)"
)

article = st.text_area(
    "Article Content",
    height=200
)

model_choice = st.selectbox(
    "Select Model",
    [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "Multinomial Naive Bayes"
    ]
)

# ANALYZE BUTTON

if st.button(
    "Analyze Article",
    use_container_width=True
):

    if article.strip() == "":
        st.warning(
            "Please paste article text."
        )

    else:

        cleaned = preprocess(article)

        vectorized = vectorizer.transform(
            [cleaned]
        )

        if model_choice == "Logistic Regression":
            model = LR

        elif model_choice == "Decision Tree":
            model = DTC

        elif model_choice == "Random Forest":
            model = rfc

        else:
            model = MNB

        prediction = model.predict(
            vectorized
        )[0]

        probability = model.predict_proba(
            vectorized
        )[0]

        fake_score = probability[0] * 100
        real_score = probability[1] * 100

        st.markdown("---")

        # RESULT

        if prediction == 1:

            st.success(
                f"✅ REAL NEWS ({real_score:.2f}%)"
            )

        else:

            st.error(
                f"❌ FAKE NEWS ({fake_score:.2f}%)"
            )

        # GAUGE

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=real_score,
                title={
                    'text':
                    "Authenticity Score"
                },
                gauge={
                    'axis':{
                        'range':[0,100]
                    },
                    'bar':{
                        'color':'green'
                    }
                }
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "Confidence Scores"
        )

        st.write(
            f"Fake News: {fake_score:.2f}%"
        )

        st.progress(
            int(fake_score)
        )

        st.write(
            f"Real News: {real_score:.2f}%"
        )

        st.progress(
            int(real_score)
        )