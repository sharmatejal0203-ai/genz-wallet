import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# VELORA 3.0
# Intelligent Money Management
# Demo only — no real payments
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
        radial-gradient(circle at 50% -10%, #20243A 0%, #0B0C10 38%, #08090C 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 22px 18px 90px;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #9A9DA8 !important;
}

.stButton > button {
    background: #15171D !important;
    color: #F5F5F7 !important;
    border: 1px solid #292D36 !important;
    border-radius: 13px !important;
    min-height: 44px !important;
    font-weight: 650 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
    background: #1B1E26 !important;
}

[data-testid="stMetric"] {
    background: #111318;
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

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #111318 !important;
    color: #FFFFFF !important;
    border-color: #292D36 !important;
}

hr {
    border-color: #242730 !important;
}

.brand {
    font-size: 25px;
    font-weight: 850;
    letter-spacing: 3px;
    color: #FFFFFF;
}

.tagline {
    color: #858995;
    font-size: 12px;
}

.greeting {
    color: #858995;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 28px;
}

.balance-card {
    background: linear-gradient(145deg, #191C25, #0F1116);
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
    font-weight: 850;
    letter-spacing: -1.8px;
    margin-top: 7px;
}

.balance-sub {
    color: #777C88;
    font-size: 11px;
    margin-top: 7px;
}

.section-title {
    color: #F1F2F4;
    font-size: 17px;
    font-weight: 780;
    margin-top: 24px;
    margin-bottom: 10px;
}

.intelligence {
    background: linear-gradient(145deg, #181520, #101117);
    border: 1px solid #393149;
    border-radius: 20px;
    padding: 19px;
    margin: 15px 0;
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

.pay-card {
    background: linear-gradient(145deg, #181B24, #0D0F14);
    border: 1px solid #30343E;
    border-radius: 23px;
    padding: 23px;
    margin: 12px 0;
}

.pay-title {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: 800;
}

.virtual-card {
    background: linear-gradient(135deg, #242735, #111319);
    border: 1px solid #454A56;
    border-radius: 24px;
    padding: 24px;
    min-height: 165px;
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
    margin-top: 42px;
}

.card-footer {
    color: #777C87;
    font-size: 9px;
    margin-top: 15px;
    letter-spacing: 1px;
}

.goal-card {
    background: #111318;
    border: 1px solid #282C35;
    border-radius: 19px;
    padding: 18px;
    margin-top: 10px;
}

.transaction {
    background: #101217;
    border: 1px solid #22262F;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.premium {
    background: linear-gradient(145deg, #17131F, #0F1015);
    border: 1px solid #4A3C61;
    border-radius: 22px;
    padding: 22px;
    margin-top: 15px;
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
        abs(item[2])
        for item in st.session_state.transactions
        if item[2] < 0
    )


def income_total():
    return sum(
        item[2]
        for item in st.session_state.transactions
        if item[2] > 0
    )


def category_total(category):
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[1] == category and item[2] < 0
    )


def goal_progress():
    return min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )


# =========================================================
# HEADER
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

    st.subheader(st.session_state.name)

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
        if st.button("＋ ADD", use_container_width=True):
            st.session_state.show_add = True
            st.session_state.show_request = False

    with b:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⌁ REQUEST", use_container_width=True):
            st.session_state.show_request = True
            st.session_state.show_add = False

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
                "₹{:,.0f} added successfully.".format(amount)
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()

    # -----------------------------------------------------
    # REQUEST MONEY
    # -----------------------------------------------------

    if st.session_state.show_request:

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

        reason = st.text_input(
            "Reason",
            placeholder="Lunch, trip, movie...",
            key="request_reason"
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

    if spending_ratio < 0.60:

        status = "ON TRACK"

        status_text = (
            "Your spending is comfortably below "
            "your monthly limit."
        )

    elif spending_ratio < 0.85:

        status = "WATCH YOUR PACE"

        status_text = (
            "You're approaching your monthly "
            "spending limit."
        )

    else:

        status = "BUDGET RISK"

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
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:
        score = 84

        if spending_ratio >= 1:
            score = 58
        elif spending_ratio >= 0.85:
            score = 68
        elif spending_ratio >= 0.60:
            score = 76

        st.metric(
            "VELORA Score",
            str(score) + " / 100"
        )

    # -----------------------------------------------------
    # INTELLIGENCE CARD
    # -----------------------------------------------------

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        '<div class="intel-title">'
        + status +
        '</div>'
        '<div class="intel-text">'
        + status_text +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SPENDING TREND
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Spending trend</div>',
        unsafe_allow_html=True
    )

    chart = pd.DataFrame(
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

    st.line_chart(chart, height=220)

    # -----------------------------------------------------
    # SAVINGS GOAL
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Active goal</div>',
        unsafe_allow_html=True
    )

    progress = goal_progress()

    st.markdown(
        '<div class="goal-card">'
        '<div class="goal-title">'
        '🎯 ' + st.session_state.goal_name +
        '</div>'
        '<div class="goal-meta">'
        'Savings progress'
        '</div>'
        '<div class="goal-amount">'
        '₹{:,.0f} / ₹{:,.0f}'.format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        ) +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.caption(
        "{:.0f}% complete".format(progress * 100)
    )

    # -----------------------------------------------------
    # RECENT ACTIVITY
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Recent activity</div>',
        unsafe_allow_html=True
    )

    for name, category, amount in st.session_state.transactions[:4]:

        if amount >= 0:
            value = "+₹{:,.0f}".format(amount)
            value_class = "tx-positive"
        else:
            value = "−₹{:,.0f}".format(abs(amount))
            value_class = "tx-negative"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name +
            '<span style="float:right;" class="'
            + value_class +
            '">'
            + value +
            '</span>'
            '</div>'
            '<div class="tx-category">'
            + category +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Payments")

    st.caption(
        "Simple actions. Fewer taps. Demo environment."
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-footer">'
        'VIRTUAL DEMO CARD · NO REAL PAYMENTS'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    p1, p2 = st.columns(2)

    with p1:
        if st.button("SEND MONEY", use_container_width=True):
            st.session_state.pay_mode = "send"

    with p2:
        if st.button("REQUEST", use_container_width=True):
            st.session_state.pay_mode = "request"

    mode = st.session_state.get("pay_mode", "send")

    if mode == "send":

        st.markdown(
            '<div class="pay-card">'
            '<div class="pay-title">Send money</div>'
            '</div>',
            unsafe_allow_html=True
        )

        recipient = st.text_input(
            "Recipient",
            placeholder="Friend or contact",
            key="recipient"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=100.0,
            step=50.0,
            key="send_amount"
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
            ],
            key="send_category"
        )

        if st.button(
            "Confirm payment",
            use_container_width=True
        ):

            if not recipient.strip():

                st.error("Enter recipient.")

            elif amount > st.session_state.balance:

                st.error("Insufficient demo balance.")

            else:

                st.session_state.balance -= amount

                add_transaction(
                    "Sent to " + recipient,
                    category,
                    -amount
                )

                st.session_state.notifications.insert(
                    0,
                    "₹{:,.0f} sent to {}.".format(
                        amount,
                        recipient
                    )
                )

                st.success("Payment simulated.")
                st.rerun()

    else:

        st.markdown(
            '<div class="pay-card">'
            '<div class="pay-title">Request money</div>'
            '</div>',
            unsafe_allow_html=True
        )

        person = st.text_input(
            "Request from",
            placeholder="Friend or contact",
            key="request_from_pay"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_pay_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True
        ):

            if not person.strip():

                st.error("Enter a name.")

            else:

                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} sent to {}.".format(
                        amount,
                        person
                    )
                )

                st.success("Request created.")


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.subheader("Activity")

    st.caption(
        "Your complete demo transaction history."
    )

    search = st.text_input(
        "Search",
        placeholder="Food, shopping, friend..."
    )

    filtered = []

    for item in st.session_state.transactions:

        name, category, amount = item

        text = (