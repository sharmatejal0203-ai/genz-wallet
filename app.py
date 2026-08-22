import streamlit as st
import pandas as pd

# =========================================================
# VELORA — SMART MONEY MANAGEMENT
# Demo prototype — no real payments
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM DARK UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #20243A 0%, #0B0C11 38%, #07080B 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 24px 18px 90px;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #989BA7 !important;
}

.stButton > button {
    background: #15171D !important;
    color: #F5F5F7 !important;
    border: 1px solid #2A2D36 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background: #1D2028 !important;
    border-color: #777D8D !important;
}

[data-testid="stMetric"] {
    background: #111318;
    border: 1px solid #282B34;
    border-radius: 17px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #858995 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background: #111318 !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] {
    background: #111318 !important;
}

hr {
    border-color: #262932 !important;
}

/* Brand */

.brand {
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 4px;
    color: #FFFFFF;
}

.tagline {
    color: #777C88;
    font-size: 11px;
    letter-spacing: 0.7px;
}

/* Balance */

.greeting {
    color: #777C88;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 28px;
}

.balance-card {
    background: linear-gradient(145deg, #1A1D27, #0E1015);
    border: 1px solid #343843;
    border-radius: 25px;
    padding: 25px;
    margin: 12px 0 18px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.balance-label {
    color: #858995;
    font-size: 10px;
    letter-spacing: 1.8px;
    font-weight: 800;
}

.balance {
    color: #FFFFFF;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 6px;
}

.balance-sub {
    color: #737783;
    font-size: 10px;
    margin-top: 7px;
}

/* Sections */

.section-title {
    color: #F2F3F5;
    font-size: 17px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 8px;
}

.muted {
    color: #777C87;
    font-size: 11px;
}

/* Intelligence */

.intelligence {
    background: linear-gradient(145deg, #191522, #0F1015);
    border: 1px solid #3D3450;
    border-radius: 20px;
    padding: 19px;
    margin: 15px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 1.8px;
}

.intel-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 800;
    margin-top: 7px;
}

.intel-text {
    color: #9A9DA8;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 6px;
}

/* Transaction */

.transaction {
    background: #101217;
    border: 1px solid #242730;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F3F4F6;
    font-size: 13px;
    font-weight: 700;
}

.tx-category {
    color: #707580;
    font-size: 10px;
    margin-top: 3px;
}

/* Pay */

.pay-card {
    background: linear-gradient(145deg, #181B23, #0E1014);
    border: 1px solid #30343D;
    border-radius: 22px;
    padding: 21px;
    margin: 12px 0;
}

.pay-title {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: 800;
}

/* Card */

.virtual-card {
    background: linear-gradient(135deg, #252936, #101218);
    border: 1px solid #484D5A;
    border-radius: 24px;
    padding: 24px;
    height: 165px;
    margin: 15px 0;
}

.card-logo {
    color: #FFFFFF;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-chip {
    color: #999EAA;
    font-size: 10px;
    margin-top: 27px;
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
    margin-top: 13px;
}

/* Goal */

.goal-card {
    background: #111318;
    border: 1px solid #282C35;
    border-radius: 19px;
    padding: 18px;
    margin-top: 10px;
}

.goal-title {
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 800;
}

.goal-meta {
    color: #7E828D;
    font-size: 11px;
    margin-top: 4px;
}

/* Premium */

.premium {
    background: linear-gradient(145deg, #1A1523, #101116);
    border: 1px solid #463A5D;
    border-radius: 22px;
    padding: 21px;
    margin-top: 16px;
}

.premium-title {
    color: #FFFFFF;
    font-size: 21px;
    font-weight: 850;
}

.premium-text {
    color: #979AA6;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 6px;
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
        ["Gaming", "Entertainment", -180.0],
    ],
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


def score():
    spent = spending_total()
    limit = st.session_state.monthly_limit

    if spent >= limit:
        return 55

    if spent >= limit * 0.85:
        return 68

    if spent >= limit * 0.65:
        return 76

    return 88


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

    st.subheader(st.session_state.name)

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

    # Quick actions
    a, b, c = st.columns(3)

    with a:
        if st.button("＋ ADD", use_container_width=True):
            st.session_state.show_add = True

    with b:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⌁ REQUEST", use_container_width=True):
            st.session_state.show_request = True

    # Add money
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
            placeholder="Allowance, gift, income...",
            key="add_source"
        )

        if st.button(
            "Confirm add",
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
                "₹{:,.0f} added to your wallet.".format(amount)
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()

    # Request
    if st.session_state.show_request:

        st.markdown(
            '<div class="pay-card">'
            '<div class="pay-title">Request money</div>'
            '</div>',
            unsafe_allow_html=True
        )

        person = st.text_input(
            "From",
            placeholder="Person name",
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
            key="create_request"
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

    ratio = spent / max(
        st.session_state.monthly_limit,
        1
    )

    if ratio < 0.60:
        status = "ON TRACK"
        status_text = (
            "Your spending is comfortably below "
            "your monthly limit."
        )
    elif ratio < 0.85:
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
        st.metric(
            "VELORA Score",
            "{} / 100".format(score())
        )

    # Budget status
    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">BUDGET STATUS</div>'
        '<div class="intel-title">'
        + status +
        '</div>'
        '<div class="intel-text">'
        + status_text +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Spending trend
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

    st.line_chart(chart)

    # Savings goal
    st.markdown(
        '<div class="section-title">Savings goal</div>',
        unsafe_allow_html=True
    )

    progress = goal_progress()

    st.markdown(
        '<div class="goal-card">'
        '<div class="goal-title">'
        + st.session_state.goal_name +
        '</div>'
        '<div class="goal-meta">'
        + "₹{:,.0f} saved of ₹{:,.0f}".format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        )
        + '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.caption(
        "{:.0f}% complete".format(progress * 100)
    )

    # Latest activity
    st.markdown(
        '<div class="section-title">Recent activity</div>',
        unsafe_allow_html=True
    )

    for name, category, amount in st.session_state.transactions[:4]:

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name +
            '<span style="float:right;">'
            + sign +
            '₹'
            + "{:,.0f}".format(abs(amount))
            + '</span>'
            '</div>'
            '<div class="tx-category">'
            + category +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if st.button(
        "View all activity",
        use_container_width=True
    ):
        go("Activity")


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section-title">Send money</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Demo payment flow — no real transaction is processed."
    )

    st.markdown(
        '<div class="pay-card">'
        '<div class="pay-title">New payment</div>'
        '</div>',
        unsafe_allow_html=True
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Name or UPI ID"
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

    note = st.text_input(
        "Note",
        placeholder="Optional"
    )

    if st.button(
        "Review payment",
        use_container_width=True
    ):

        if not recipient.strip():
            st.error("Enter a recipient.")

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

            st.success(
                "Payment simulated successfully."
            )

            st.rerun()

    st.markdown(
        '<div class="section-title">Velora Card</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-chip">VIRTUAL CARD · DEMO</div>'
        '<div class="card-number">••••  ••••  ••••  2840</div>'
        '<div class="card-footer">VELORA MEMBER</div>'
        '</div>',
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

        if st.button(
            "Freeze card",
            use_container_width=True
        ):
            st.session_state.card_frozen = True
            st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.markdown(
        '<div class="section-title">Activity</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search",
        placeholder="Food, shopping, person..."
    )

    filtered = []

    for item in st.session_state.transactions:

        name, category, amount = item

        text = (
            name + " " + category
        ).lower()

        if search.lower() in text:
            filtered.append(item)

    if not filtered:

        st.info("No matching transactions.")

    else:

        for name, category, amount in filtered:

            sign = "+" if amount >= 0 else "−"

            st.markdown(
                '<div class="transaction">'
                '<div class="tx-name">'
                + name +
                '<span style="float:right;">'
                + sign +
                '₹'
                + "{:,.0f}".format(abs(amount))
                + '</span>'
                '</div>'
                '<div class="tx-category">'
                + category +
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )


# =========================================================
# INTELLIGENCE
# =========================================================

elif st.session_state.page == "Intelligence":

    st.markdown(
        '<div class="section-title">Velora Intelligence</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()
    limit = st.session_state.monthly_limit
    current_score = score()

    if spent == 0:

        title = "Your spending is clear."
        message = (
            "Start tracking transactions to build "