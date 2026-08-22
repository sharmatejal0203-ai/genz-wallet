import streamlit as st
import pandas as pd
from datetime import date, timedelta

# =========================================================
# VELORA 2.0
# Intelligent money management
# Demo application — no real payments
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM DARK FINTECH UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #1c2030 0%, #0b0c10 38%, #08090c 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 22px 18px 90px;
}

/* Hide Streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
    letter-spacing: -0.4px;
}

p, label, .stCaption {
    color: #9A9DA8 !important;
}

/* Buttons */

.stButton > button {
    background: #15171D !important;
    color: #F5F5F7 !important;
    border: 1px solid #292D36 !important;
    border-radius: 13px !important;
    min-height: 44px !important;
    font-weight: 650 !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    border-color: #858A98 !important;
    background: #1B1E26 !important;
}

/* Primary button */

.primary-btn .stButton > button {
    background: #F1F2F4 !important;
    color: #090A0D !important;
    border: none !important;
}

/* Metrics */

[data-testid="stMetric"] {
    background: #121419;
    border: 1px solid #272A33;
    border-radius: 18px;
    padding: 14px 16px;
}

[data-testid="stMetricLabel"] {
    color: #858995 !important;
}

[data-testid="stMetricValue"] {
    color: #F5F5F7 !important;
    font-weight: 800 !important;
}

/* Progress */

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

/* Inputs */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #111318 !important;
    color: #FFFFFF !important;
    border-color: #292D36 !important;
}

/* Divider */

hr {
    border-color: #242730 !important;
}

/* =====================================================
   CUSTOM COMPONENTS
   ===================================================== */

.brand {
    font-size: 25px;
    font-weight: 850;
    letter-spacing: 3px;
    color: #FFFFFF;
}

.tagline {
    color: #858995;
    font-size: 12px;
    letter-spacing: 0.5px;
}

.greeting {
    color: #858995;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 28px;
}

.balance-card {
    background:
        linear-gradient(145deg, #171A22, #0F1116);
    border: 1px solid #30343E;
    border-radius: 25px;
    padding: 24px;
    margin: 12px 0 16px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.28);
}

.balance-label {
    color: #858995;
    font-size: 10px;
    letter-spacing: 1.8px;
    font-weight: 700;
}

.balance {
    color: #FFFFFF;
    font-size: 42px;
    line-height: 1.1;
    font-weight: 850;
    letter-spacing: -1.8px;
    margin-top: 7px;
}

.balance-sub {
    color: #777C88;
    font-size: 11px;
    margin-top: 7px;
}

.intelligence {
    background:
        linear-gradient(145deg, #17151F, #101117);
    border: 1px solid #393149;
    border-radius: 20px;
    padding: 19px;
    margin: 14px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 10px;
    letter-spacing: 1.7px;
    font-weight: 800;
}

.intel-title {
    color: #F5F5F7;
    font-size: 18px;
    font-weight: 750;
    margin-top: 8px;
}

.intel-text {
    color: #9B9EAA;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 6px;
}

.stat-card {
    background: #111318;
    border: 1px solid #262A33;
    border-radius: 17px;
    padding: 16px;
}

.stat-label {
    color: #777C87;
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.stat-value {
    color: #F5F5F7;
    font-size: 20px;
    font-weight: 800;
    margin-top: 5px;
}

.stat-note {
    color: #737782;
    font-size: 10px;
    margin-top: 4px;
}

.goal-card {
    background: #111318;
    border: 1px solid #282C35;
    border-radius: 19px;
    padding: 18px;
    margin-top: 10px;
}

.goal-title {
    color: #F5F5F7;
    font-weight: 750;
    font-size: 15px;
}

.goal-meta {
    color: #7E828D;
    font-size: 11px;
    margin-top: 4px;
}

.goal-amount {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 800;
}

.transaction {
    background: #101217;
    border: 1px solid #22262F;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F2F3F5;
    font-size: 13px;
    font-weight: 650;
}

.tx-category {
    color: #707580;
    font-size: 10px;
    margin-top: 3px;
}

.tx-positive {
    color: #91D7B4;
    font-weight: 750;
}

.tx-negative {
    color: #F0F1F4;
    font-weight: 700;
}

.pay-card {
    background:
        linear-gradient(145deg, #181B24, #0D0F14);
    border: 1px solid #30343E;
    border-radius: 23px;
    padding: 23px;
    margin: 10px 0;
}

.pay-title {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: 800;
}

.virtual-card {
    background:
        linear-gradient(135deg, #20232D, #111319);
    border: 1px solid #454A56;
    border-radius: 24px;
    padding: 24px;
    height: 165px;
    margin: 12px 0 18px;
}

.card-logo {
    color: #FFFFFF;
    font-weight: 850;
    letter-spacing: 3px;
}

.card-chip {
    color: #A5A8B2;
    font-size: 10px;
    margin-top: 26px;
}

.card-number {
    color: #FFFFFF;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 13px;
}

.card-footer {
    color: #777C87;
    font-size: 9px;
    margin-top: 13px;
    letter-spacing: 1px;
}

.premium {
    background:
        linear-gradient(145deg, #17131F, #0F1015);
    border: 1px solid #4A3C61;
    border-radius: 22px;
    padding: 22px;
    margin-top: 15px;
}

.premium-title {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 850;
}

.premium-sub {
    color: #979AA6;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 5px;
}

.nav-label {
    text-align: center;
    color: #777C87;
    font-size: 9px;
    margin-top: -6px;
}

.section-title {
    color: #F1F2F4;
    font-size: 17px;
    font-weight: 780;
    margin-top: 24px;
}

.muted {
    color: #777C87;
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,
    "card_frozen": False,
    "name": "Tejal",
    "page": "Home",
    "notifications": [],
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
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def spending_total():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def income_total():
    return sum(
        x[2]
        for x in st.session_state.transactions
        if x[2] > 0
    )


def category_total(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


def projected_balance():
    spent = spending_total()

    if spent <= 0:
        return st.session_state.balance

    daily_rate = spent / 30
    projected_spend = daily_rate * 30

    return max(
        st.session_state.balance - projected_spend + spent,
        0
    )


def goal_progress():
    return min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )


# =========================================================
# TOP BRAND
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("HOME", use_container_width=True):
        go("Home")

with n2:
    if st.button("PAY", use_container_width=True):
        go("Pay")

with n3:
    if st.button("ACTIVITY", use_container_width=True):
        go("Activity")

with n4:
    if st.button("INTEL", use_container_width=True):
        go("Intelligence")

with n5:
    if st.button("PROFILE", use_container_width=True):
        go("Profile")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div class="greeting">GOOD EVENING</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        st.session_state.name
    )

    # Balance

    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹'
        + "{:,.2f}".format(st.session_state.balance)
        + '</div>'
        '<div class="balance-sub">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Primary actions

    a, b, c = st.columns(3)

    with a:
        if st.button("＋  ADD", use_container_width=True):
            st.session_state.show_add = True

    with b:
        if st.button("↗  SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⌁  REQUEST", use_container_width=True):
            st.session_state.show_request = True

    # Add money

    if st.session_state.get("show_add", False):

        st.markdown(
            '<div class="pay-card">'
            '<div class="pay-title">Add money</div>'
            '</div>',
            unsafe_allow_html=True
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_amount"
        )

        source = st.text_input(
            "Source",
            placeholder="Income, gift, allowance...",
            key="add_source"
        )

        if st.button(
            "Confirm",
            use_container_width=True,
            key="confirm_add"
        ):

            source = source.strip() or "Income"

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added successfully.".format(amount)
            )

            st.session_state.show_add = False
            st.success("Balance updated.")
            st.rerun()

    # Request

    if st.session_state.get("show_request", False):

        st.markdown(
            '<div class="pay-card">'
            '<div class="pay-title">Request money</div>'
            '</div>',
            unsafe_allow_html=True
        )

        person = st.text_input(
            "From",
            placeholder="Name",
            key="request_person"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True,
            key="confirm_request"
        ):

            if not person.strip():
                st.error("Enter a name.")

            else:

                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} created.".format(amount)
                )

                st.session_state.show_request = False
                st.success("Request created.")
                st.rerun()

    # =====================================================
    # FINANCIAL SNAPSHOT
    # =====================================================

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    spending_ratio = (
        spent /
        max(st.session_state.monthly_limit, 1)
    )

    if spending_ratio < 0.6:
        status = "On track"
        status_text = (
            "Your spending is comfortably below "
            "your monthly limit."
        )
    elif spending_ratio < 0.85:
        status = "Watch your pace"
        status_text = (
            "You're approaching your monthly "
            "spending limit."
        )
    else:
        status = "Budget risk"
        status_text = (
            "Your current spending pace may "
            "push you beyond your limit."
        )

    st.markdown(
        '<div class="section-title">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    s1, s2 = st.columns(2)
with s1:
    st.metric(
        "Spent this month",
        "₹{:,.0f}".format(spent)
    )

with s2:
    st.metric(
        "Budget remaining",
        "₹{:,.0f}".format(remaining)
    )

s3, s4 = st.columns(2)

with s3:
    st.metric(
        "Savings",
        "₹{:,.0f}".format(st.session_state.goal_saved)
    )

with s4:
    st.metric(
        "VELORA Score",
        "84 / 100"
    )