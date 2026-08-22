import streamlit as st
import pandas as pd

# =========================================================
# VELORA 2.0
# Intelligent Money Management
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

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #9A9DA8 !important;
}

/* BUTTONS */

.stButton > button {
    background: #15171D !important;
    color: #F5F5F7 !important;
    border: 1px solid #292D36 !important;
    border-radius: 13px !important;
    min-height: 44px !important;
    font-weight: 650 !important;
}

.stButton > button:hover {
    border-color: #858A98 !important;
    background: #1B1E26 !important;
}

/* METRICS */

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

/* PROGRESS */

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #111318 !important;
    color: #FFFFFF !important;
    border-color: #292D36 !important;
}

/* DIVIDER */

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
    margin: 18px 0;
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

.section-title {
    color: #F1F2F4;
    font-size: 17px;
    font-weight: 780;
    margin-top: 24px;
    margin-bottom: 10px;
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

.goal-card {
    background: #111318;
    border: 1px solid #282C35;
    border-radius: 19px;
    padding: 18px;
    margin-top: 10px;
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

.card-number {
    color: #FFFFFF;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 45px;
}

.card-footer {
    color: #777C87;
    font-size: 9px;
    margin-top: 13px;
    letter-spacing: 1px;
}

.transaction {
    background: #101217;
    border: 1px solid #22262F;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
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
    "show_add": False,
    "show_request": False,
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


# =========================================================
# BRAND
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

    # -----------------------------------------------------
    # BALANCE
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # QUICK ACTIONS
    # -----------------------------------------------------

    a, b, c = st.columns(3)

    with a:

        if st.button(
            "＋ ADD",
            use_container_width=True
        ):

            st.session_state.show_add = True

    with b:

        if st.button(
            "↗ SEND",
            use_container_width=True
        ):

            go("Pay")

    with c:

        if st.button(
            "⌁ REQUEST",
            use_container_width=True
        ):

            st.session_state.show_request = True


    # -----------------------------------------------------
    # ADD MONEY
    # -----------------------------------------------------

    if st.session_state.show_add:

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
                "₹{:,.0f} added successfully.".format(
                    amount
                )
            )

            st.session_state.show_add = False

            st.success("Balance updated.")

            st.rerun()


    # -----------------------------------------------------
    # REQUEST MONEY
    # -----------------------------------------------------

    if st.session_state.show_request:

        st