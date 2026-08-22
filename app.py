import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================================
# VELORA
# Premium Intelligent Money Management
# Demo Prototype — No Real Payments
# ============================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -15%, #222638 0%, #0D0E13 35%, #07080B 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 570px;
    padding: 20px 17px 90px;
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
    color: #9699A5 !important;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    background: #14161D !important;
    color: #F4F5F7 !important;
    border: 1px solid #292D37 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
    transition: all .2s ease;
}

.stButton > button:hover {
    background: #1B1E27 !important;
    border-color: #858A98 !important;
}

/* ---------- METRICS ---------- */

[data-testid="stMetric"] {
    background: #111319;
    border: 1px solid #282C35;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #7F8390 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 850 !important;
}

/* ---------- INPUTS ---------- */

.stTextInput input,
.stNumberInput input {
    background: #101217 !important;
    color: white !important;
    border-color: #292D36 !important;
}

div[data-baseweb="select"] {
    background: #101217 !important;
}

/* ---------- PROGRESS ---------- */

.stProgress > div > div > div > div {
    background: #9B7BFF !important;
}

/* ---------- DIVIDER ---------- */

hr {
    border-color: #252832 !important;
}

/* ---------- BRAND ---------- */

.brand {
    color: #FFFFFF;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 4px;
}

.tagline {
    color: #737783;
    font-size: 11px;
    letter-spacing: 1px;
    margin-top: -4px;
}

/* ---------- GREETING ---------- */

.greeting {
    color: #777B87;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 28px;
}

/* ---------- BALANCE ---------- */

.balance-card {
    background:
        linear-gradient(145deg, #1A1D27, #0F1116);
    border: 1px solid #303540;
    border-radius: 26px;
    padding: 25px;
    margin: 15px 0 17px;
    box-shadow: 0 20px 55px rgba(0,0,0,.30);
}

.balance-label {
    color: #858995;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
}

.balance {
    color: #FFFFFF;
    font-size: 43px;
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 8px;
}

.balance-sub {
    color: #707580;
    font-size: 10px;
    margin-top: 8px;
}

/* ---------- SECTION ---------- */

.section-title {
    color: #F4F5F7;
    font-size: 17px;
    font-weight: 800;
    margin-top: 26px;
    margin-bottom: 10px;
}

/* ---------- INTELLIGENCE ---------- */

.intelligence {
    background:
        linear-gradient(145deg, #181521, #101117);
    border: 1px solid #413652;
    border-radius: 21px;
    padding: 19px;
    margin: 16px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 2px;
}

.intel-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 800;
    margin-top: 7px;
}

.intel-text {
    color: #999CA7;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 6px;
}

/* ---------- CARDS ---------- */

.panel {
    background: #111319;
    border: 1px solid #292D36;
    border-radius: 19px;
    padding: 18px;
    margin: 10px 0;
}

.virtual-card {
    background:
        linear-gradient(135deg, #252936, #111319);
    border: 1px solid #464B57;
    border-radius: 25px;
    padding: 24px;
    height: 165px;
    margin: 15px 0 20px;
}

.card-logo {
    color: white;
    font-size: 17px;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-chip {
    color: #A5A8B2;
    font-size: 10px;
    margin-top: 27px;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 12px;
}

.card-footer {
    color: #777C87;
    font-size: 9px;
    margin-top: 13px;
    letter-spacing: 1px;
}

/* ---------- TRANSACTIONS ---------- */

.transaction {
    background: #101217;
    border: 1px solid #232730;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F3F4F6;
    font-size: 13px;
    font-weight: 700;
}

.tx-meta {
    color: #707580;
    font-size: 10px;
    margin-top: 4px;
}

/* ---------- GOAL ---------- */

.goal-card {
    background: #111319;
    border: 1px solid #292D36;
    border-radius: 19px;
    padding: 18px;
    margin: 10px 0;
}

.goal-title {
    color: white;
    font-size: 16px;
    font-weight: 800;
}

.goal-meta {
    color: #777C87;
    font-size: 10px;
    margin-top: 4px;
}

/* ---------- STATUS ---------- */

.status-good {
    color: #8FD4B1;
    font-weight: 800;
}

.status-watch {
    color: #D7C486;
    font-weight: 800;
}

.status-risk {
    color: #D68A94;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

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


# ============================================================
# FUNCTIONS
# ============================================================

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
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def total_income():

    return sum(
        x[2]
        for x in st.session_state.transactions
        if x[2] > 0
    )


def category_spending(category):

    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


def get_score():

    spent = total_spending()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    if ratio < 0.50:
        return 92

    if ratio < 0.70:
        return 84

    if ratio < 0.85:
        return 76

    return 64


def get_budget_status():

    spent = total_spending()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    if ratio < 0.60:

        return (
            "ON TRACK",
            "Your spending is comfortably below "
            "your planned monthly limit.",
            "good"
        )

    if ratio < 0.85:

        return (
            "WATCH YOUR PACE",
            "You're approaching your monthly "
            "spending limit.",
            "watch"
        )

    return (
        "BUDGET RISK",
        "Your current spending pace is high "
        "relative to your monthly limit.",
        "risk"
    )


# ============================================================
# BRAND
# ============================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True
)


# ============================================================
# NAVIGATION
# ============================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:

    if st.button(
        "HOME",
        use_container_width=True
    ):

        go("Home")


with n2:

    if st.button(
        "PAY",
        use_container_width=True
    ):

        go("Pay")


with n3:

    if st.button(
        "ACTIVITY",
        use_container_width=True
    ):

        go("Activity")


with n4:

    if st.button(
        "INTEL",
        use_container_width=True
    ):

        go("Intelligence")


with n5:

    if st.button(
        "PROFILE",
        use_container_width=True
    ):

        go("Profile")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div class="greeting">GOOD EVENING</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        st.session_state.name
    )

    # --------------------------------------------------------
    # BALANCE
    # --------------------------------------------------------

    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹'
        + "{:,.2f}".format(
            st.session_state.balance
        )
        + '</div>'
        '<div class="balance-sub">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # QUICK ACTIONS
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # ADD MONEY
    # --------------------------------------------------------

    if st.session_state.show_add:

        st.markdown(
            '<div class="section-title">Add money</div>',
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
            placeholder="Allowance, gift, income...",
            key="add_source"
        )

        x1, x2 = st.columns(2)

        with x1:

            if st.button(
                "Confirm",
                use_container_width=True,
                key="confirm_add"
            ):

                source = (
                    source.strip()
                    or "Income"
                )

                st.session_state.balance += amount

                add_transaction(
                    source,
                    "Income",
                    amount
                )

                st.session_state.notifications.insert(
                    0,
                    "₹{:,.0f} added to your wallet.".format(
                        amount
                    )
                )

                st.session_state.show_add = False

                st.success(
                    "Balance updated."
                )

                st.rerun()

        with x2:

            if st.button(
                "Cancel",
                use_container_width=True,
                key="cancel_add"
            ):

                st.session_state.show_add = False

                st.rerun()

    # --------------------------------------------------------
    # REQUEST
    # --------------------------------------------------------

    if st.session_state.show_request:

        st.markdown(
            '<div class="section-title">Request money</div>',
            unsafe_allow_html=True
        )

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

        x1, x2 = st.columns(2)

        with x1:

            if st.button(
                "Create request",
                use_container_width=True,
                key="create_request"
            ):

                if not person.strip():

                    st.error(
                        "Enter a name."
                    )

                else:

                    st.session_state.notifications.insert(
                        0,
                        "Request of ₹{:,.0f} created.".format(
                            amount
                        )
                    )

                    st.session_state.show_request = False

                    st.success(
                        "Request created."
                    )

                    st.rerun()

        with x2:

            if st.button(
                "Cancel",
                use_container_width=True,
                key="cancel_request"
            ):

                st.session_state.show_request = False

                st.rerun()

    # --------------------------------------------------------
    # FINANCIAL SNAPSHOT
    # --------------------------------------------------------

    spent = total_spending()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    score = get_score()

    status, status_text, status_type = (
        get_budget_status()
    )

    st.markdown(
        '<div class="section-title">'
        'Financial snapshot'
        '</div>',
        unsafe_allow_html=True
    )

    s1, s2 = st.columns(2)

    with s1:

        st.metric(
            "Spent this month",
            "₹{:,.0f}".format(
                spent
            )
        )

    with s2:

        st.metric(
            "Budget remaining",
            "₹{:,.0f}".format(
                remaining
            )
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
            str(score) + " / 100"
        )

    # --------------------------------------------------------
    # INTELLIGENCE
    # --------------------------------------------------------

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">'
        'VELORA INTELLIGENCE'
        '</div>'
        '<div class="intel-title">'
        + status
        + '</div>'
        '<div class="intel-text">'
        + status_text
        + '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SPENDING TREND
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        'Spending trend'
        '</div>',
        unsafe_allow_html=True
    )

    trend = pd.DataFrame(
        {
            "Spending": [
                120,
                180,
                90,
                240,
                160,
                280,
                110
            ]
        },
        index=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]
    )

    st.line_chart(
        trend,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SAVINGS GOAL
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        'Savings goal'
        '</div>',
        unsafe_allow_html=True
    )

    progress = min(
        st.session_state.goal_saved /
        max(
            st.session_state.goal_target,
            1
        ),
        1
    )

    st.markdown(
        '<div class="goal-card">'
        '<div class="goal-title">'
        + st.session_state.goal_name
        + '</div>'
        '<div class="goal-meta">'
        'Personal savings target'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(
        progress
    )

    st.caption(
        "₹{:,.0f} saved of ₹{:,.0f} · {:.0f}% complete".format(
            st.session_state.goal_saved,
            st.session_state.goal_target,
            progress * 100
        )
    )

    # --------------------------------------------------------
    # RECENT ACTIVITY
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        'Recent activity'
        '</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.transactions[:5]:

        name, category, amount = item

        if amount >= 0:

            amount_text = (
                "+₹{:,.0f}".format(
                    amount
                )
            )

        else:

            amount_text = (
                "−₹{:,.0f}".format(
                    abs(amount)
                )
            )

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name
            + '</div>'
            '<div class="tx-meta">'
            + category
            + ' · '
            + amount_text
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# PAY
# ============================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section-title">Pay</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Fast demo payments · No real money"
    )

    # Card

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-chip">'
        'VIRTUAL CARD · DEMO'
        '</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-footer">'
        'VELORA MEMBER · DEMO ONLY'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.error(
            "CARD FROZEN"
        )

    else:

        st.success(
            "CARD ACTIVE"
        )

    recipient = st.text_input(
        "Recipient",
        placeholder="Name or payment ID"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Other"
        ]
    )

    if st.button(
        "Send payment",
        use_container_width=True
    ):

        if st.session_state.card_frozen:

            st.error(
                "Unfreeze the card before making a payment."
            )

        elif not recipient.strip():

            st.error(
                "Enter a recipient."
            )

        elif amount > st.session_state.balance:

            st.error(
    