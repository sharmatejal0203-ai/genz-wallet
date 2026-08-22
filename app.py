import streamlit as st
import pandas as pd

# =========================================================
# VELORA — PREMIUM INTELLIGENT MONEY MANAGEMENT
# DEMO ONLY — NO REAL MONEY / UPI / BANK CONNECTION
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #292D46 0%, #0B0C11 35%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 620px;
    padding: 22px 16px 80px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: #F5F5F7 !important;
}

.stButton > button {
    background: #151821 !important;
    color: white !important;
    border: 1px solid #303542 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
    background: #1D202B !important;
}

[data-testid="stMetric"] {
    background: #12151C;
    border: 1px solid #292E38;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: white !important;
    font-weight: 850 !important;
}

[data-testid="stMetricLabel"] {
    color: #858B98 !important;
}

.stTextInput input,
.stNumberInput input {
    background: #11141A !important;
    color: white !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

hr {
    border-color: #252A34 !important;
}

.brand {
    font-size: 30px;
    font-weight: 950;
    letter-spacing: 5px;
}

.tagline {
    color: #858B98;
    font-size: 10px;
    letter-spacing: 2px;
}

.card {
    background: linear-gradient(145deg,#1B1F2A,#101217);
    border: 1px solid #303542;
    border-radius: 25px;
    padding: 22px;
    margin: 14px 0;
}

.balance-label {
    color: #858B98;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}

.balance {
    color: white;
    font-size: 44px;
    font-weight: 900;
    letter-spacing: -2px;
}

.muted {
    color: #858B98 !important;
    font-size: 11px;
}

.section {
    color: white;
    font-size: 18px;
    font-weight: 850;
    margin-top: 25px;
    margin-bottom: 9px;
}

.insight {
    background: linear-gradient(145deg,#1A1624,#101116);
    border: 1px solid #493960;
    border-radius: 22px;
    padding: 20px;
    margin: 14px 0;
}

.insight-label {
    color: #A98CFF;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 2px;
}

.insight-title {
    color: white;
    font-size: 18px;
    font-weight: 850;
    margin-top: 7px;
}

.insight-text {
    color: #999DA9;
    font-size: 12px;
    line-height: 1.55;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 16px;
    padding: 14px;
    margin: 7px 0;
}

.tx-title {
    color: #F4F5F7;
    font-weight: 750;
    font-size: 13px;
}

.tx-cat {
    color: #777D89;
    font-size: 10px;
}

.tx-income {
    color: #6EE7A0;
    font-weight: 800;
}

.tx-expense {
    color: #FF7D91;
    font-weight: 800;
}

.goal {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 20px;
    padding: 18px;
    margin: 10px 0;
}

.virtual-card {
    background:
        radial-gradient(circle at 80% 10%,#5A4E82 0%,transparent 35%),
        linear-gradient(135deg,#292D3C,#101218);
    border: 1px solid #505566;
    border-radius: 26px;
    padding: 25px;
    min-height: 165px;
    margin: 15px 0;
}

.score {
    background: linear-gradient(145deg,#211A31,#111219);
    border: 1px solid #46365B;
    border-radius: 22px;
    padding: 20px;
    text-align: center;
}

.score-number {
    font-size: 42px;
    font-weight: 950;
}

.notice {
    background: #151821;
    border: 1px solid #303542;
    border-radius: 15px;
    padding: 13px;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "monthly_limit" not in st.session_state:
    st.session_state.monthly_limit = 2000.0

if "name" not in st.session_state:
    st.session_state.name = "Tejal"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "card_frozen" not in st.session_state:
    st.session_state.card_frozen = False

if "jar" not in st.session_state:
    st.session_state.jar = 850.0

if "notifications" not in st.session_state:
    st.session_state.notifications = []

if "show_add" not in st.session_state:
    st.session_state.show_add = False

if "show_request" not in st.session_state:
    st.session_state.show_request = False

if "show_jar" not in st.session_state:
    st.session_state.show_jar = False

if "goals" not in st.session_state:
    st.session_state.goals = [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ]

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income