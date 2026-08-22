import streamlit as st
import pandas as pd

# ============================================================
# VELORA
# Premium intelligent money-management prototype
# Demo only — no real payments
# ============================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
# PREMIUM DARK UI
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
        radial-gradient(circle at 50% -10%, #202536 0%, #0C0E13 38%, #07080B 100%);
        color: #F5F6F8;
    }

    .block-container {
        max-width: 560px;
        padding: 22px 18px 80px;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    h1, h2, h3, h4 {
        color: #F5F6F8 !important;
    }

    p, label {
        color: #969BA8 !important;
    }

    .stButton > button {
        background: #14171D !important;
        color: #F5F6F8 !important;
        border: 1px solid #292E38 !important;
        border-radius: 14px !important;
        min-height: 44px !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        background: #1B1F28 !important;
        border-color: #858B99 !important;
    }

    [data-testid="stMetric"] {
        background: #11141A;
        border: 1px solid #282D37;
        border-radius: 18px;
        padding: 14px;
    }

    [data-testid="stMetricLabel"] {
        color: #858B99 !important;
    }

    [data-testid="stMetricValue"] {
        color: #F5F6F8 !important;
        font-weight: 850 !important;
    }

    .stProgress > div > div > div > div {
        background: #9B7BFF;
    }

    .stTextInput input,
    .stNumberInput input {
        background: #101319 !important;
        color: white !important;
    }

    hr {
        border-color: #252A33 !important;
    }

    .brand {
        font-size: 27px;
        font-weight: 900;
        letter-spacing: 4px;
        color: white;
    }

    .tagline {
        color: #777D89;
        font-size: 11px;
        letter-spacing: 0.8px;
    }

    .greeting {
        color: #777D89;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-top: 28px;
    }

    .balance-card {
        background: linear-gradient(145deg, #1A1E27, #0E1015);
        border: 1px solid #343A46;
        border-radius: 25px;
        padding: 24px;
        margin: 12px 0 17px;
        box-shadow: 0 18px 45px rgba(0,0,0,0.28);
    }

    .balance-label {
        color: #858B98;
        font-size: 10px;
        letter-spacing: 1.8px;
        font-weight: 800;
    }

    .balance {
        color: white;
        font-size: 42px;
        line-height: 1.1;
        font-weight: 900;
        letter-spacing: -2px;
        margin-top: 7px;
    }

    .balance-sub {
        color: #737986;
        font-size: 10px;
        margin-top: 8px;
    }

    .section-title {
        color: #F2F3F5;
        font-size: 17px;
        font-weight: 800;
        margin-top: 24px;
        margin-bottom: 10px;
    }

    .intel {
        background: linear-gradient(145deg, #191620, #101116);
        border: 1px solid #3C3350;
        border-radius: 20px;
        padding: 19px;
        margin: 15px 0;
    }

    .intel-label {
        color: #A88BFF;
        font-size: 10px;
        letter-spacing: 1.7px;
        font-weight: 850;
    }

    .intel-title {
        color: white;
        font-size: 18px;
        font-weight: 800;
        margin-top: 7px;
    }

    .intel-text {
        color: #999DA9;
        font-size: 12px;
        line-height: 1.55;
        margin-top: 6px;
    }

    .transaction {
        background: #101319;
        border: 1px solid #232832;
        border-radius: 15px;
        padding: 14px;
        margin: 7px 0;
    }

    .tx-name {
        color: #F1F2F4;
        font-size: 13px;
        font-weight: 700;
    }

    .tx-category {
        color: #707684;
        font-size: 10px;
        margin-top: 3px;
    }

    .virtual-card {
        background: linear-gradient(135deg, #242934, #11141A);
        border: 1px solid #484F5C;
        border-radius: 24px;
        padding: 24px;
        height: 165px;
        margin: 12px 0 18px;
    }

    .card-logo {
        color: white;
        font-weight: 900;
        letter-spacing: 3px;
    }

    .card-chip {
        color: #A7ABB5;
        font-size: 10px;
        margin-top: 27px;
    }

    .card-number {
        color: white;
        font-size: 17px;
        letter-spacing: 3px;
        margin-top: 13px;
    }

    .card-footer {
        color: #777D89;
        font-size: 9px;
        margin-top: 13px;
        letter-spacing: 1px;
    }

    .goal-card {
        background: #11141A;
        border: 1px solid #282D37;
        border-radius: 19px;
        padding: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

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
        ["Gaming", "Entertainment", -180.0],
    ],
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


def spending_total():
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[2] < 0
    )


def category_total(category):
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[1] == category and item[2] < 0
    )


def goal_progress():
    return min(
        st.session_state.goal_saved
        / max(st.session_state.goal_target, 1),
        1.0
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True,
)

# ============================================================
# NAVIGATION
# ============================================================

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


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div class="greeting">GOOD EVENING</div>',
        unsafe_allow_html=True,
    )

    st.subheader(st.session_state.name)

    # BALANCE
    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹'
        + f'{st.session_state.balance:,.2f}'
        + '</div>'
        '<div class="balance-sub">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # QUICK ACTIONS
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

    # ADD MONEY
    if st.session_state.show_add:

        st.markdown(
            '<div class="section-title">Add money</div>',
            unsafe_allow_html=True,
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_amount",
        )

        source = st.text_input(
            "Source",
            placeholder="Allowance, gift, income...",
            key="add_source",
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="confirm_add",
        ):
            source = source.strip() or "Income"

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount,
            )

            st.session_state.notifications.insert(
                0,
                f"₹{amount:,.0f} added successfully.",
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()

    # REQUEST MONEY
    if st.session_state.show_request:

        st.markdown(
            '<div class="section-title">Request money</div>',
            unsafe_allow_html=True,
        )

        person = st.text_input(
            "From",
            placeholder="Name",
            key="request_person",
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_amount",
        )

        if st.button(
            "Create request",
            use_container_width=True,
            key="create_request",
        ):
            if not person.strip():
                st.error("Enter a name.")
            else:
                st.session_state.notifications.insert(
                    0,
                    f"Request of ₹{amount:,.0f} created from {person.strip()}.",
                )

                st.session_state.show_request = False

                st.success("Request created.")
                st.rerun()

    # FINANCIAL SNAPSHOT
    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0,
    )

    ratio = (
        spent
        / max(st.session_state.monthly_limit, 1)
    )

    if ratio < 0.60:
        status = "ON TRACK"
        status_text = (
            "Your spending is comfortably below your monthly limit."
        )
    elif ratio < 0.85:
        status = "WATCH YOUR PACE"
        status_text = (
            "You're approaching your monthly spending limit."
        )
    else:
        status = "BUDGET RISK"
        status_text = (
            "Your current spending pace may push you beyond your limit."
        )

    st.markdown(
        '<div class="section-title">Financial snapshot</div>',
        unsafe_allow_html=True,
    )

    s1, s2 = st.columns(2)

    with s1:
        st.metric(
            "Spent this month",
            f"₹{spent:,.0f}",
        )

    with s2:
        st.metric(
            "Budget remaining",
            f"₹{remaining:,.0f}",
        )

    s3, s4 = st.columns(2)

    with s3:
        st.metric(
            "Savings",
            f"₹{st.session_state.goal_saved:,.0f}",
        )

    with s4:
        score = 84 if ratio < 0.85 else 72

        st.metric(
            "VELORA Score",
            f"{score} / 100",
        )

    # INTELLIGENCE
    st.markdown(
        '<div class="intel">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        f'<div class="intel-title">{status}</div>'
        f'<div class="intel-text">{status_text}</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # SPENDING TREND
    st.markdown(
        '<div class="section-title">Spending trend</div>',
        unsafe_allow_html=True,
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
                110,
            ]
        },
        index=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun",
        ],
    )

    st.line_chart(
        chart,
        height=220,
    )

    # SAVINGS GOAL
    st.markdown(
        '<div class="section-title">Savings goal</div>',
        unsafe_allow_html=True,
    )

    progress = goal_progress()

    st.markdown(
        '<div class="goal-card">'
        f'<b>{st.session_state.goal_name}</b><br>'
        f'<span style="color:#777D89;font-size:11px;">'
        f'₹{st.session_state.goal_saved:,.0f} saved of '
        f'₹{st.session_state.goal_target:,.0f}'
        '</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.progress(progress)

    st.caption(
        f"{progress * 100:.0f}% complete"
    )

    # SPENDING CATEGORIES
    st.markdown(
        '<div class="section-title">Where your money goes</div>',
        unsafe_allow_html=True,
    )

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel",
    ]

    for category in categories:

        value = category_total(category)

        if value > 0:

            st.write(
                f"**{category}** — ₹{value:,.0f}"
            )

            st.progress(
                min(
                    value / max(spent, 1),
                    1.0,
                )
            )

    # RECENT ACTIVITY
    st.markdown(
        '<div class="section-title">Recent activity</div>',
        unsafe_allow_html=True,
    )

    for name, category, amount in st.session_state.transactions[:4]:

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            f'<div class="tx-name">'
            f'{name}'
            f'<span style="float:right;">'
            f'{sign}₹{abs(amount):,.0f}'
            f'</span>'
            f'</div>'
            f'<div class="tx-category">{category}</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    if st.button(
        "View all activity",
        use_container_width=True,
    ):
        go("Activity")


# ============================================================
# PAY
# ============================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section-title">Pay</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Fast demo payments with a simple fintech flow."
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-chip">DEMO VIRTUAL CARD</div>'
        '<div class="card-number">•••• •••• •••• 2840</div>'
        '<div class="card-footer">'
        'PROTOTYPE · NO REAL PAYMENTS'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Name or UPI ID",
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0,
        key="payment_amount",
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Other",
        ],
    )

    note = st.text_input(
        "Note",
        placeholder="Optional",
    )

    if st.button(
        "Send payment",
        use_container_width=True,
    ):

        if not recipient.strip():

            st.error(
                "Enter a recipient."
            )

        elif amount > st.session_state.balance:

            st.error(
                "Insufficient demo balance."
            )

        else:

            st.session_state.balance -= amount

            add_transaction(
                f"Sent to {recipient.strip()}",
                category,
                -amount,
            )

            st.session_state.notifications.insert(
                0,
                f"₹{amount:,.0f} sent to {recipient.strip()}.",
            )

            st.success(
                "Payment simulated successfully."
            )

            st.rerun()

    st.divider()

    st.write("**Quick amount**")

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button("₹50", use_container_width=True):
            st.session_state.payment_amount = 50.0
            st.rerun()

    with q2:
        if st.button("₹100", use_container_width=True):
            st.session_state.payment_amount = 100.0
            st.rerun()

    with q3:
        if st.button("₹250", use_container_width=True):
            st.session_state.payment_amount = 250.0
            st.rerun()


# ============================================================
# ACTIVITY
# ============================================================

elif st.session_state.page == "Activity":

    st.markdown(
        '<div class="section-title">Activity</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, recipient...",
    )

    shown = 0

    for name, category, amount in st.session_state.transactions:

        searchable = (
            f"{name} {category}"
        ).lower()

        if search.strip().lower() not in searchable:
            continue

        shown += 1

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            f'<div class="tx-name">'
            f'{name}'
            f'<span style="float:right;">'
            f'{sign}₹{abs(amount):,.0f}'
            f'</span>'
            f'</div>'
            f'<div class="tx-category">{category}</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    if shown == 0:

        st.info(
            "No matching transactions."
        )


# ============================================================
# INTELLIGENCE
# ============================================================

elif st.session_state.page == "Intelligence":

    spent = spending_total()

    ratio = (
        spent
        / max(st.session_state.monthly_limit, 1)
    )

    st.markdown(
        '<div class="section-title">'
        'VELORA Intelligence'
        '</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Your financial command center."
    )

    if ratio < 0.60:

        title = "You're in control."
        text = (
            "Your spending is comfortably below "
            "your planned monthly limit."
        )

    elif ratio < 0.85:

        title = "Slow down slightly."
        text = (
            "Your spending is moving toward "
            "your monthly limit."
        )

    else:

        title = "Budget pressure detected."
        text = (
            "Your spending is high relative "
            "to your current monthly limit."
        )

    st.markdown(
        '<div class="intel">'
        '<div class="intel-label">LIVE MONEY SIGNAL</div>'
        f'<div class="intel-title">{title}</div>'
        f'<div class="intel