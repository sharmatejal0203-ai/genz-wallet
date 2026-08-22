import streamlit as st
import pandas as pd

# =========================================================
# VELORA 2.1
# Intelligent Money Management
# Demo only — no real payments
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# =========================================================
# PREMIUM UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -15%, #24283A 0%, #0C0D12 35%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 570px;
    padding: 24px 18px 90px;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #979BA7 !important;
}

/* BUTTONS */

.stButton > button {
    background: #14171F !important;
    color: #F5F5F7 !important;
    border: 1px solid #2B303B !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background: #1B1E28 !important;
    border-color: #9B7BFF !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #858A96 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input {
    background: #11141A !important;
    color: white !important;
    border-color: #2B303A !important;
}

/* DIVIDER */

hr {
    border-color: #242832 !important;
}

/* =====================================================
CUSTOM COMPONENTS
===================================================== */

.brand {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: 3px;
    color: #FFFFFF;
}

.tagline {
    font-size: 11px;
    color: #747986;
    letter-spacing: 0.7px;
}

.greeting {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #777C89;
    margin-top: 27px;
}

.balance-card {
    background:
        linear-gradient(145deg, #1A1D27, #101218);
    border: 1px solid #353A46;
    border-radius: 26px;
    padding: 25px;
    margin: 12px 0 17px;
    box-shadow: 0 20px 55px rgba(0,0,0,0.3);
}

.balance-label {
    color: #858A96;
    font-size: 10px;
    letter-spacing: 1.8px;
    font-weight: 800;
}

.balance {
    color: #FFFFFF;
    font-size: 43px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 6px;
}

.balance-sub {
    color: #707581;
    font-size: 10px;
    margin-top: 7px;
}

.section-title {
    color: #F4F5F7;
    font-size: 17px;
    font-weight: 800;
    margin-top: 23px;
    margin-bottom: 8px;
}

.intelligence {
    background:
        linear-gradient(145deg, #191622, #101117);
    border: 1px solid #3C3350;
    border-radius: 21px;
    padding: 19px;
    margin: 13px 0;
}

.intel-label {
    color: #A98CFF;
    font-size: 9px;
    font-weight: 900;
    letter-spacing: 1.8px;
}

.intel-title {
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 800;
    margin-top: 7px;
}

.intel-text {
    color: #979BA7;
    font-size: 11px;
    line-height: 1.55;
    margin-top: 6px;
}

.goal {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 20px;
    padding: 18px;
    margin-top: 10px;
}

.goal-name {
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 800;
}

.goal-meta {
    color: #777C87;
    font-size: 10px;
    margin-top: 4px;
}

.goal-money {
    color: #FFFFFF;
    font-size: 21px;
    font-weight: 850;
}

.transaction {
    background: #101318;
    border: 1px solid #252A34;
    border-radius: 15px;
    padding: 13px 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F1F2F4;
    font-size: 12px;
    font-weight: 700;
}

.tx-category {
    color: #707581;
    font-size: 9px;
    margin-top: 3px;
}

.tx-positive {
    color: #8DD3B0;
    font-weight: 800;
}

.tx-negative {
    color: #F0F1F4;
    font-weight: 750;
}

.card {
    background:
        linear-gradient(145deg, #1A1D26, #101217);
    border: 1px solid #303641;
    border-radius: 23px;
    padding: 22px;
    margin: 12px 0;
}

.virtual-card {
    background:
        linear-gradient(135deg, #222632, #111319);
    border: 1px solid #474D59;
    border-radius: 25px;
    padding: 24px;
    height: 165px;
    margin: 12px 0 18px;
}

.purple {
    color: #A98CFF !important;
}

.muted {
    color: #777D89 !important;
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
    "name": "Tejal",
    "page": "Home",
    "card_frozen": False,
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


def total_spending():
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[2] < 0
    )


def category_spending(category):
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[1] == category and item[2] < 0
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
    if st.button("INSIGHT", use_container_width=True):
        go("Insight")

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
        '<div class="balance">₹{:,.2f}</div>'
        '<div class="balance-sub">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # QUICK ACTIONS
    # -----------------------------------------------------

    a, b, c = st.columns(3)

    with a:
        if st.button("＋ ADD", use_container_width=True):
            st.session_state.show_add = True

    with b:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⇄ REQUEST", use_container_width=True):
            st.session_state.show_request = True

    # -----------------------------------------------------
    # ADD
    # -----------------------------------------------------

    if st.session_state.get("show_add", False):

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_amount"
        )

        source = st.text_input(
            "Source",
            value="Pocket Money",
            key="add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="confirm_add"
        ):

            st.session_state.balance += amount

            add_transaction(
                source.strip() or "Income",
                "Income",
                amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to wallet.".format(amount)
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()

    # -----------------------------------------------------
    # REQUEST
    # -----------------------------------------------------

    if st.session_state.get("show_request", False):

        st.markdown("### Request money")

        person = st.text_input(
            "From",
            placeholder="Friend's name",
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

    # -----------------------------------------------------
    # FINANCIAL SNAPSHOT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = total_spending()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = (
        spent /
        max(st.session_state.monthly_limit, 1)
    )

    if ratio < 0.6:
        score = 84
        status = "On track"
    elif ratio < 0.85:
        score = 72
        status = "Watch your pace"
    else:
        score = 58
        status = "Budget risk"

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
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:
        st.metric(
            "VELORA Score",
            "{}/100".format(score)
        )

    st.caption(
        "{} · {:.0