import streamlit as st
import pandas as pd
from datetime import datetime, date

# =========================================================
# VELORA 3.0
# Intelligent Money Management
# DEMO ONLY — NO REAL PAYMENTS
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM FINTECH UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% -15%,
            #202437 0%,
            #0D0F15 34%,
            #08090D 75%
        );
    color: #F5F5F7;
}

.block-container {
    max-width: 570px;
    padding: 22px 18px 90px;
}

/* Hide Streamlit chrome */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Typography */

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #969AA6 !important;
}

/* Buttons */

.stButton > button {
    background: #151820 !important;
    color: #F4F5F7 !important;
    border: 1px solid #2B2F39 !important;
    border-radius: 13px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background: #1C2029 !important;
    border-color: #777D8C !important;
}

/* Metrics */

[data-testid="stMetric"] {
    background: #11141A;
    border: 1px solid #292D37;
    border-radius: 18px;
    padding: 14px 16px;
}

[data-testid="stMetricLabel"] {
    color: #858A97 !important;
}

[data-testid="stMetricValue"] {
    color: #F5F5F7 !important;
    font-weight: 850 !important;
}

/* Progress */

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

/* Inputs */

.stTextInput input,
.stNumberInput input {
    background: #101218 !important;
    color: #FFFFFF !important;
    border-color: #292D36 !important;
}

div[data-baseweb="select"] {
    background: #101218 !important;
}

/* Divider */

hr {
    border-color: #252932 !important;
}

/* =========================================================
   BRAND
   ========================================================= */

.brand {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: 3px;
    color: #FFFFFF;
}

.tagline {
    font-size: 11px;
    color: #777C89;
    letter-spacing: 0.7px;
}

/* =========================================================
   BALANCE
   ========================================================= */

.balance-card {
    background:
        linear-gradient(
            145deg,
            #191C25,
            #0E1015
        );
    border: 1px solid #323642;
    border-radius: 25px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 20px 50px rgba(0,0,0,.28);
}

.balance-label {
    color: #818692;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 800;
}

.balance {
    color: #FFFFFF;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 5px;
}

.balance-note {
    color: #6E7380;
    font-size: 10px;
    margin-top: 8px;
}

/* =========================================================
   SECTION
   ========================================================= */

.section-title {
    color: #F2F3F5;
    font-size: 17px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* =========================================================
   INTELLIGENCE
   ========================================================= */

.intelligence {
    background:
        linear-gradient(
            145deg,
            #191521,
            #0F1016
        );
    border: 1px solid #45385A;
    border-radius: 21px;
    padding: 20px;
    margin: 15px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 9px;
    letter-spacing: 2px;
    font-weight: 900;
}

.intel-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 850;
    margin-top: 7px;
}

.intel-text {
    color: #9B9DA8;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 6px;
}

/* =========================================================
   CARD
   ========================================================= */

.virtual-card {
    background:
        linear-gradient(
            135deg,
            #292D38,
            #101218
        );
    border: 1px solid #555A67;
    border-radius: 25px;
    padding: 24px;
    height: 165px;
    margin: 15px 0;
}

.card-brand {
    color: #FFFFFF;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-chip {
    color: #A8ACB7;
    font-size: 10px;
    margin-top: 28px;
}

.card-number {
    color: #FFFFFF;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 12px;
}

.card-footer {
    color: #777C87;
    font-size: 9px;
    margin-top: 12px;
    letter-spacing: 1px;
}

/* =========================================================
   GOAL
   ========================================================= */

.goal-card {
    background: #11141A;
    border: 1px solid #292D37;
    border-radius: 20px;
    padding: 18px;
    margin: 8px 0;
}

.goal-title {
    color: #FFFFFF;
    font-size: 16px;
    font-weight: 800;
}

.goal-meta {
    color: #777C87;
    font-size: 11px;
    margin-top: 5px;
}

/* =========================================================
   TRANSACTION
   ========================================================= */

.transaction {
    background: #101218;
    border: 1px solid #252932;
    border-radius: 16px;
    padding: 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F3F4F6;
    font-weight: 750;
    font-size: 13px;
}

.tx-category {
    color: #707580;
    font-size: 10px;
    margin-top: 3px;
}

/* =========================================================
   SCORE
   ========================================================= */

.score-card {
    background:
        linear-gradient(
            145deg,
            #14151C,
            #0D0F13
        );
    border: 1px solid #30343E;
    border-radius: 21px;
    padding: 20px;
    margin: 12px 0;
}

.score-number {
    font-size: 38px;
    font-weight: 900;
    color: #FFFFFF;
}

.score-label {
    color: #818591;
    font-size: 10px;
    letter-spacing: 1px;
}

/* =========================================================
   STATUS
   ========================================================= */

.status-good {
    color: #91D7B4;
    font-weight: 800;
}

.status-warning {
    color: #DCCB91;
    font-weight: 800;
}

.status-danger {
    color: #E99A9A;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {

    "page": "Home",

    "name": "Tejal",

    "balance": 5000.0,

    "monthly_limit": 2000.0,

    "goal_name": "New Headphones",

    "goal_target": 5000.0,

    "goal_saved": 3400.0,

    "card_frozen": False,

    "notifications": [],

    "show_add": False,

    "show_request": False,

    "transactions": [
        {
            "name": "Pocket Money",
            "category": "Income",
            "amount": 2000.0,
            "date": "Today"
        },
        {
            "name": "Food",
            "category": "Food",
            "amount": -250.0,
            "date": "Today"
        },
        {
            "name": "Study Material",
            "category": "Education",
            "amount": -500.0,
            "date": "Yesterday"
        },
        {
            "name": "Shopping",
            "category": "Shopping",
            "amount": -350.0,
            "date": "Yesterday"
        },
        {
            "name": "Gaming",
            "category": "Entertainment",
            "amount": -180.0,
            "date": "2 days ago"
        }
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


def add_transaction(
    name,
    category,
    amount
):

    st.session_state.transactions.insert(
        0,
        {
            "name": name,
            "category": category,
            "amount": amount,
            "date": "Just now"
        }
    )


def spending_total():

    return sum(
        abs(t["amount"])
        for t in st.session_state.transactions
        if t["amount"] < 0
    )


def income_total():

    return sum(
        t["amount"]
        for t in st.session_state.transactions
        if t["amount"] > 0
    )


def category_total(category):

    return sum(
        abs(t["amount"])
        for t in st.session_state.transactions
        if (
            t["category"] == category
            and t["amount"] < 0
        )
    )


def get_score():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    budget_score = max(
        0,
        100 - int(
            (spent / limit) * 45
        )
    )

    goal_ratio = (
        st.session_state.goal_saved /
        max(
            st.session_state.goal_target,
            1
        )
    )

    saving_score = min(
        int(goal_ratio * 30),
        30
    )

    transaction_score = min(
        len(
            st.session_state.transactions
        ) * 2,
        20
    )

    score = (
        budget_score * 0.5
        + saving_score
        + transaction_score
    )

    return int(
        max(
            0,
            min(score, 100)
        )
    )


def get_budget_status():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    if ratio < 0.60:

        return (
            "On track",
            "Your spending is comfortably "
            "below your monthly limit.",
            "good"
        )

    if ratio < 0.85:

        return (
            "Watch your pace",
            "You're approaching your monthly "
            "spending limit.",
            "warning"
        )

    return (
        "Budget risk",
        "Your current spending pace may "
        "push you beyond your limit.",
        "danger"
    )


def biggest_category():

    categories = {}

    for category in [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel",
        "Other"
    ]:

        value = category_total(category)

        if value > 0:

            categories[category] = value

    if not categories:

        return None, 0

    category = max(
        categories,
        key=categories.get
    )

    return (
        category,
        categories[category]
    )


# =========================================================
# BRAND
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">'
    'Intelligent money management'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

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


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption(
        "GOOD EVENING"
    )

    st.subheader(
        st.session_state.name
    )

    # -----------------------------------------------------
    # BALANCE
    # -----------------------------------------------------

    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">'
        'AVAILABLE BALANCE'
        '</div>'
        '<div class="balance">'
        '₹'
        + "{:,.2f}".format(
            st.session_state.balance
        )
        + '</div>'
        '<div class="balance-note">'
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

        st.subheader(
            "Add money"
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
            placeholder="Pocket money / gift / income",
            key="add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True
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


    # -----------------------------------------------------
    # REQUEST
    # -----------------------------------------------------

    if st.session_state.show_request:

        st.subheader(
            "Request money"
        )

        person = st.text_input(
            "Request from",
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
            use_container_width=True
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


    # =====================================================
    # FINANCIAL SNAPSHOT
    # =====================================================

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    score = get_score()

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
            "Goal savings",
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:

        st.metric(
            "VELORA Score",
            str(score) + " / 100"
        )


    # =====================================================
    # INTELLIGENCE
    # =====================================================

    status, status_text, status_type = (
        get_budget_status()
    )

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">'
        'VELORA INTELLIGENCE'
        '</div>'
        '<div class="intel-title">'
        + status +
        '</div>'
        '<div class="intel-text">'
        + status_text +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # SPENDING BREAKDOWN
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'Spending breakdown'
        '</div>',
        unsafe_allow_html=True
    )

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel",
        "Other"
    ]

    for category in categories:

        value = category_total(
            category
        )

        if value > 0:

            st.write(
                category
                + " · ₹"
                + "{:,.0f}".format(
                    value
                )
            )

            st.progress(
                min(
                    value / max(
                        spent,
                        1
                    ),
                    1
                )
            )


    # =====================================================
    # GOAL
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'Savings goal'
        '</div>',
        unsafe_allow_html=True
    )

    goal_progress = (
        st.session_state.goal_saved /
        max(
            st.session_state.goal_target,
            1
        )
    )

    st.markdown(
        '<div class="goal-card">'
        '<div class="goal-title">'
        + st.session_state.goal_name +
        '</div>'
        '<div class="goal-meta">'
        '₹'
        + "{:,.0f}".format(
            st.session_state.goal_saved
        )
        + ' saved of ₹'
        + "{:,.0f}".format(
            st.session_state.goal_target
        )
        + '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(
        min(
            goal_progress,
            1
        )
    )

    remaining_goal = max(
        st.session_state.goal_target
        - st.session_state.goal_saved,
        0
    )

    st.caption(
        "₹{:,.0f} remaining to reach your goal.".format(
            remaining_goal
        )
    )


    # =====================================================
    # SMART INSIGHT
    # =====================================================

    biggest, biggest_value = (
        biggest_category()
    )

    if biggest:

        st.info(
            "Smart insight: "
            + biggest
            + " is currently your largest "
            "spending category at ₹"
            + "{:,.0f}".format(
                biggest_value
            )
            + "."
        )


# =========================================================
# PAY
# =========================================