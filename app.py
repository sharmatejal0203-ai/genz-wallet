import streamlit as st
import pandas as pd

# =========================================================
# VELORA — PREMIUM INTELLIGENT MONEY MANAGEMENT
# Demo only — no real money / UPI / bank connection
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #252944 0%, #0B0C11 35%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 600px;
    padding: 20px 16px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1,h2,h3,h4,p,label {
    color:#F5F5F7 !important;
}

.stButton > button {
    background:#151821 !important;
    color:#FFFFFF !important;
    border:1px solid #303542 !important;
    border-radius:14px !important;
    min-height:44px !important;
    font-weight:700 !important;
}

.stButton > button:hover {
    border-color:#9B7BFF !important;
    background:#1D202B !important;
}

[data-testid="stMetric"] {
    background:#12151C;
    border:1px solid #292E38;
    border-radius:18px;
    padding:15px;
}

[data-testid="stMetricValue"] {
    color:#FFFFFF !important;
    font-weight:850 !important;
}

[data-testid="stMetricLabel"] {
    color:#858B98 !important;
}

.stProgress > div > div > div > div {
    background:#9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background:#11141A !important;
    color:#FFFFFF !important;
}

.stSelectbox div[data-baseweb="select"] {
    background:#11141A !important;
}

hr {
    border-color:#252A34 !important;
}

/* BRAND */

.brand {
    font-size:30px;
    font-weight:950;
    letter-spacing:5px;
}

.tagline {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
}

/* CARDS */

.card {
    background:linear-gradient(145deg,#1B1F2A,#101217);
    border:1px solid #303542;
    border-radius:25px;
    padding:22px;
    margin:14px 0;
}

.balance-label {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
    font-weight:700;
}

.balance {
    color:#FFFFFF;
    font-size:44px;
    font-weight:900;
    letter-spacing:-2px;
    margin-top:5px;
}

.muted {
    color:#858B98 !important;
    font-size:11px;
}

.section {
    color:#F5F5F7;
    font-size:18px;
    font-weight:850;
    margin-top:25px;
    margin-bottom:9px;
}

/* INSIGHT */

.insight {
    background:linear-gradient(145deg,#1A1624,#101116);
    border:1px solid #493960;
    border-radius:22px;
    padding:20px;
    margin:14px 0;
}

.insight-label {
    color:#A98CFF;
    font-size:10px;
    font-weight:850;
    letter-spacing:2px;
}

.insight-title {
    color:#FFFFFF;
    font-size:18px;
    font-weight:850;
    margin-top:7px;
}

.insight-text {
    color:#999DA9;
    font-size:12px;
    line-height:1.55;
    margin-top:5px;
}

/* TRANSACTIONS */

.transaction {
    background:#11141A;
    border:1px solid #252A34;
    border-radius:16px;
    padding:14px;
    margin:7px 0;
}

.tx-title {
    color:#F4F5F7;
    font-weight:750;
    font-size:13px;
}

.tx-cat {
    color:#777D89;
    font-size:10px;
}

.tx-income {
    color:#6EE7A0;
    font-weight:800;
}

.tx-expense {
    color:#FF7D91;
    font-weight:800;
}

/* GOALS */

.goal {
    background:#11141A;
    border:1px solid #292E38;
    border-radius:20px;
    padding:18px;
    margin:10px 0;
}

.goal-title {
    font-weight:800;
    font-size:15px;
}

.goal-money {
    font-size:21px;
    font-weight:850;
}

/* CARD */

.virtual-card {
    background:
        radial-gradient(circle at 80% 10%,#5A4E82 0%,transparent 35%),
        linear-gradient(135deg,#292D3C,#101218);
    border:1px solid #505566;
    border-radius:26px;
    padding:25px;
    min-height:165px;
    margin:15px 0;
    box-shadow:0 15px 45px rgba(0,0,0,.35);
}

.card-brand {
    font-weight:900;
    letter-spacing:4px;
}

.card-number {
    font-size:19px;
    letter-spacing:3px;
    margin-top:30px;
}

.card-small {
    color:#858B98;
    font-size:9px;
    letter-spacing:1px;
    margin-top:15px;
}

/* SCORE */

.score {
    background:linear-gradient(145deg,#211A31,#111219);
    border:1px solid #46365B;
    border-radius:22px;
    padding:20px;
    text-align:center;
}

.score-number {
    font-size:42px;
    font-weight:950;
}

.score-label {
    color:#9A9DA8;
    font-size:10px;
    letter-spacing:2px;
}

/* JAR */

.jar {
    background:linear-gradient(145deg,#171923,#101116);
    border:1px solid #303542;
    border-radius:22px;
    padding:20px;
    margin:12px 0;
}

.jar-title {
    font-size:17px;
    font-weight:850;
}

.jar-money {
    font-size:27px;
    font-weight:900;
    margin:5px 0;
}

/* NOTICE */

.notice {
    background:#151821;
    border:1px solid #303542;
    border-radius:15px;
    padding:13px;
    margin:8px 0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "name": "Tejal",
    "page": "Home",

    "card_frozen": False,

    "show_add": False,
    "show_request": False,
    "show_jar": False,

    "notifications": [],

    "goals": [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ],

    "jar": 850.0,

    "transactions": [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ]
}


for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# FUNCTIONS
# =========================================================

def go(page):

    st.session_state.page =