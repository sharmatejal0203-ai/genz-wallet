import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================================
# VELORA — SMART MONEY
# Complete Streamlit demo
# No real payments / no real bank connection
# ============================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# ============================================================
# PREMIUM UI
# ============================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 50% -20%, #25283A 0%, #0B0C10 38%, #07080B 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 22px 18px 90px;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

h1,h2,h3,h4 {
    color:#FFFFFF !important;
}

p,label {
    color:#9296A3 !important;
}

.stButton > button {
    background:#14161C !important;
    color:#FFFFFF !important;
    border:1px solid #292D37 !important;
    border-radius:14px !important;
    min-height:44px !important;
    font-weight:700 !important;
}

.stButton > button:hover {
    background:#1C1F28 !important;
    border-color:#827A92 !important;
}

[data-testid="stMetric"] {
    background:#111318;
    border:1px solid #292D36;
    border-radius:18px;
    padding:14px;
}

[data-testid="stMetricLabel"] {
    color:#7F8390 !important;
}

[data-testid="stMetricValue"] {
    color:#FFFFFF !important;
    font-weight:850 !important;
}

.stProgress > div > div > div > div {
    background:#9B7BFF;
}

input {
    color:#FFFFFF !important;
}

.brand {
    font-size:27px;
    font-weight:900;
    letter-spacing:4px;
}

.tagline {
    color:#737783;
    font-size:11px;
    margin-top:-4px;
}

.greeting {
    color:#747884;
    font-size:10px;
    font-weight:800;
    letter-spacing:2px;
    margin-top:28px;
}

.balance-card {
    background:linear-gradient(145deg,#1B1E28,#0F1116);
    border:1px solid #30343F;
    border-radius:25px;
    padding:24px;
    margin:12px 0 18px;
    box-shadow:0 18px 45px rgba(0,0,0,.25);
}

.balance-label {
    color:#858995;
    font-size:10px;
    letter-spacing:2px;
    font-weight:800;
}

.balance {
    color:#FFFFFF;
    font-size:42px;
    line-height:1.1;
    font-weight:900;
    margin-top:7px;
}

.balance-note {
    color:#6E727D;
    font-size:10px;
    margin-top:7px;
}

.section {
    color:#F3F4F6;
    font-size:18px;
    font-weight:800;
    margin-top:25px;
    margin-bottom:9px;
}

.intelligence {
    background:linear-gradient(145deg,#191622,#101116);
    border:1px solid #3A3049;
    border-radius:20px;
    padding:19px;
    margin:14px 0;
}

.intel-label {
    color:#A88CFF;
    font-size:10px;
    font-weight:800;
    letter-spacing:2px;
}

.intel-title {
    color:#FFFFFF;
    font-size:18px;
    font-weight:850;
    margin-top:7px;
}

.intel-text {
    color:#999CA8;
    font-size:12px;
    line-height:1.5;
    margin-top:6px;
}

.card {
    background:linear-gradient(135deg,#252936,#101218);
    border:1px solid #464B58;
    border-radius:24px;
    padding:24px;
    height:165px;
    margin:12px 0 18px;
}

.card-brand {
    color:#FFFFFF;
    font-weight:900;
    letter-spacing:3px;
}

.card-chip {
    color:#A3A6B0;
    font-size:10px;
    margin-top:28px;
}

.card-number {
    color:#FFFFFF;
    font-size:17px;
    letter-spacing:3px;
    margin-top:12px;
}

.card-foot {
    color:#777B87;
    font-size:9px;
    margin-top:12px;
    letter-spacing:1px;
}

.transaction {
    background:#101217;
    border:1px solid #242832;
    border-radius:15px;
    padding:13px;
    margin:7px 0;
}

.tx-name {
    color:#FFFFFF;
    font-size:13px;
    font-weight:700;
}

.tx-meta {
    color:#737783;
    font-size:10px;
    margin-top:4px;
}

.goal {
    background:#111318;
    border:1px solid #292D36;
    border-radius:20px;
    padding:18px;
    margin-top:10px;
}

.goal-title {
    color:#FFFFFF;
    font-size:16px;
    font-weight:800;
}

.goal-meta {
    color:#777B87;
    font-size:11px;
    margin-top:5px;
}

.demo {
    color:#626671;
    font-size:10px;
    text-align:center;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# STATE
# ============================================================

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
# HELPERS
# ============================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_tx(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def spent():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def income():
    return sum(
        x[2]
        for x in st.session_state.transactions
        if x[2] > 0
    )


def category_amount(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


def score():
    ratio = spent() / max(st.session_state.monthly_limit, 1)

    if ratio < 0.50:
        return 92
    if ratio < 0.70:
        return 86
    if ratio < 0.85:
        return 78
    if ratio < 1:
        return 68
    return 55


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True
)

# ============================================================
# NAV
# ============================================================

a, b, c, d, e = st.columns(5)

with a:
    if st.button("HOME", use_container_width=True):
        go("Home")

with b:
    if st.button("PAY", use_container_width=True):
        go("Pay")

with c:
    if st.button("ACTIVITY", use_container_width=True):
        go("Activity")

with d:
    if st.button("INSIGHT", use_container_width=True):
        go("Insight")

with e:
    if st.button("PROFILE", use_container_width=True):
        go("Profile")

# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div class="greeting">GOOD EVENING</div>',
        unsafe_allow_html=True
    )

    st.subheader(st.session_state.name)

    # BALANCE
    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹'
        + "{:,.2f}".format(st.session_state.balance)
        + '</div>'
        '<div class="balance-note">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # QUICK ACTIONS
    st.markdown(
        '<div class="section">Quick actions</div>',
        unsafe_allow_html=True
    )

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button("＋ ADD", use_container_width=True):
            st.session_state.show_add = not st.session_state.get(
                "show_add", False
            )

    with q2:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with q3:
        if st.button("⇄ REQUEST", use_container_width=True):
            st.session_state.show_request = not st.session_state.get(
                "show_request", False
            )

    # ADD
    if st.session_state.get("show_add", False):

        st.markdown(
            '<div class="section">Add money</div>',
            unsafe_allow_html=True
        )

        add_amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_amount"
        )

        add_source = st.text_input(
            "Source",
            placeholder="Pocket money / Gift / Allowance",
            key="add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="confirm_add"
        ):

            source = add_source.strip()

            if not source:
                source = "Income"

            st.session_state.balance += add_amount

            add_tx(
                source,
                "Income",
                add_amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to wallet.".format(add_amount)
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()

    # REQUEST
    if st.session_state.get("show_request", False):

        st.markdown(
            '<div class="section">Request money</div>',
            unsafe_allow_html=True
        )

        request_from = st.text_input(
            "From",
            placeholder="Friend name",
            key="request_from"
        )

        request_amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True,
            key="create_request"
        ):

            if not request_from.strip():
                st.error("Enter a name.")

            else:
                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} created.".format(
                        request_amount
                    )
                )

                st.session_state.show_request = False

                st.success("Request created.")
                st.rerun()

    # SNAPSHOT
    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    total_spent = spent()

    remaining = max(
        st.session_state.monthly_limit - total_spent,
        0
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Spent this month",
            "₹{:,.0f}".format(total_spent)
        )

    with col2:
        st.metric(
            "Budget remaining",
            "₹{:,.0f}".format(remaining)
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "Savings",
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with col4:
        st.metric(
            "VELORA Score",
            str(score()) + " / 100"
        )

    # INTELLIGENCE
    ratio = (
        total_spent /
        max(st.session_state.monthly_limit, 1)
    )

    if ratio < 0.60:
        title = "You're on track."
        text = (
            "Your spending is comfortably below "
            "your monthly limit."
        )
    elif ratio < 0.85:
        title = "Watch your spending."
        text = (
            "You're approaching your monthly "
            "budget."
        )
    else:
        title = "Budget pressure detected."
        text = (
            "Your current spending pace may "
            "push you beyond your limit."
        )

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        '<div class="intel-title">'
        + title +
        '</div>'
        '<div class="intel-text">'
        + text +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # BUDGET
    st.markdown(
        '<div class="section">Monthly budget</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "₹{:,.0f} of ₹{:,.0f} used".format(
            total_spent,
            st.session_state.monthly_limit
        )
    )

    st.progress(
        min(
            total_spent /
            max(st.session_state.monthly_limit, 1),
            1
        )
    )

    # CHART
    st.markdown(
        '<div class="section">Spending trend</div>',
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

    st.line_chart(chart)

    # GOAL
    st.markdown(
        '<div class="section">Savings goal</div>',
        unsafe_allow_html=True
    )

    goal_ratio = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-title">'
        + st.session_state.goal_name +
        '</div>'
        '<div class="goal-meta">₹'
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
        min(goal_ratio, 1)
    )

    st.caption(
        "{:.0f}% complete".format(
            goal_ratio * 100
        )
    )

    # RECENT
    st.markdown(
        '<div class="section">Recent activity</div>',
        unsafe_allow_html=True
    )

    for tx in st.session_state.transactions[:5]:

        name = tx[0]
        category = tx[1]
        amount = tx[2]

        if amount >= 0:
            amount_html = (
                '<span style="color:#8ED6B0;">+₹'
                + "{:,.0f}".format(amount)
                + '</span>'
            )
        else:
            amount_html = (
                '<span style="color:#FFFFFF;">−₹'
                + "{:,.0f}".format(abs(amount))
                + '</span>'
            )

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name +
            '</div>'
            '<div class="tx-meta">'
            + category +
            ' · '
            + amount_html +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

# ============================================================
# PAY
# ============================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section">Pay</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Fast demo payments · No real money"
    )

    st.markdown(
        '<div class="card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-chip">VIRTUAL DEMO CARD</div>'
        '<div class="card-number">•••• •••• •••• 2840</div>'
        '<div class="card-foot">VELORA MEMBER · DEMO</div>'
        '</div>',
        unsafe_allow_html=True
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Name or contact"
    )

    payment_amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0
    )

    payment_category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Bills",
            "Other"
        ]
    )

    if st.button(
        "Send payment",
        use_container_width=True
    ):

        if not recipient.strip():
            st.error("Enter recipient.")

        elif payment_amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= payment_amount

            add_tx(
                "Sent to " + recipient.strip(),
                payment_category,
                -payment_amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} sent to {}.".format(
                    payment_amount,
                    recipient.strip()
                )
            )

            st.success("Payment simulated.")
            st.rerun()

    st.markdown(
        '<div class="section">Card control</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.warning("CARD FROZEN")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):
            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("CARD ACTIVE")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):
            st.session_state.card_frozen = True
            st.rerun()

# ============================================================
# ACTIVITY
# ============================================================

elif st.session_state.page == "Activity":

    st.markdown(
        '<div class="section">Activity</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, friend..."
    )

    found = False

    for tx in st.session_state.transactions:

        name = tx[0]
        category = tx[1]
        amount = tx[2]

        searchable = (
            name + " " + category
        ).lower()

        if search.lower() not in searchable:
            continue

        found = True

        if amount >= 0:

            amount_html = (
                '<span style="color:#8ED6B0;">+₹'
                + "{:,.0f}".format(amount)
                + '</span>'
            )

        else:

            amount_html = (
                '<span style="color:#FFFFFF;">−₹'
                + "{:,.0f}".format(abs(amount))
                + '</span>'
            )

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name +
            '</div>'
            '<div class="tx-meta">'
            + category +
            ' · '
            + amount_html +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if not found:
        st.info("No matching transactions.")

# ============================================================
# INSIGHT
# ============================================================

elif st.session_state.page == "Insight":

    st.markdown(
        '<div class="section">VELORA Intelligence</div>',
        unsafe_allow_html=True
    )

    total_spent = spent()
    total_income = income()

    ratio = (
        total_spent /
        max(st.session_state.monthly_limit, 1)
    )

    if ratio < 0.60:

        title = "Healthy spending pattern"
        message = (
            "You're spending below your planned "
            "monthly budget."
        )

    elif ratio < 0.85:

        title = "Spending is accelerating"
        message = (
            "You're getting closer to your monthly "
            "limit. Keep discretionary spending controlled."
        )

    else:

        title = "Budget pressure"
        message = (
            "Your spending is close to or above "
            "your planned monthly limit."
        )

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">MONEY INTELLIGENCE</div>'
        '<div class="intel-title">'
        + title +
        '</div>'
        '<div class="intel