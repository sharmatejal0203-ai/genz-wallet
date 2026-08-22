import streamlit as st
import pandas as pd

# =========================================================
# VELORA — PREMIUM FINTECH DEMO
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
        radial-gradient(circle at 50% -10%, #202333 0%, #0B0C10 38%, #07080B 100%);
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

/* Buttons */

.stButton > button {
    background: #14161C !important;
    color: #F5F5F7 !important;
    border: 1px solid #292D36 !important;
    border-radius: 13px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background: #1C1F27 !important;
    border-color: #8E93A1 !important;
}

/* Metrics */

[data-testid="stMetric"] {
    background: #111319;
    border: 1px solid #282C35;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #858995 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* Progress */

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

/* Inputs */

.stTextInput input,
.stNumberInput input {
    background: #101217 !important;
    color: white !important;
}

div[data-baseweb="select"] {
    background: #101217 !important;
}

/* Brand */

.brand {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: 4px;
    color: white;
}

.tagline {
    color: #777C88;
    font-size: 11px;
    letter-spacing: 1px;
}

/* Balance */

.balance-card {
    background: linear-gradient(145deg, #1A1D27, #0F1116);
    border: 1px solid #30343E;
    border-radius: 25px;
    padding: 25px;
    margin: 16px 0;
    box-shadow: 0 20px 50px rgba(0,0,0,.28);
}

.balance-label {
    color: #858995;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 800;
}

.balance {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin-top: 7px;
}

.balance-sub {
    color: #707580;
    font-size: 10px;
    margin-top: 7px;
}

/* Intelligence */

.intelligence {
    background: linear-gradient(145deg, #181521, #101117);
    border: 1px solid #403451;
    border-radius: 20px;
    padding: 19px;
    margin: 16px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 800;
}

.intel-title {
    color: white;
    font-size: 18px;
    font-weight: 800;
    margin-top: 7px;
}

.intel-text {
    color: #999CA7;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 5px;
}

/* Section */

.section-title {
    color: #F5F5F7;
    font-size: 17px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* Transaction */

.transaction {
    background: #101217;
    border: 1px solid #232730;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.tx-name {
    color: #F5F5F7;
    font-size: 13px;
    font-weight: 700;
}

.tx-category {
    color: #707580;
    font-size: 10px;
    margin-top: 3px;
}

/* Card */

.virtual-card {
    background: linear-gradient(135deg, #242733, #101217);
    border: 1px solid #454A56;
    border-radius: 25px;
    padding: 24px;
    height: 165px;
    margin: 15px 0;
}

.card-logo {
    color: white;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-chip {
    color: #A5A8B2;
    font-size: 10px;
    margin-top: 25px;
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

/* Goal */

.goal-card {
    background: #111319;
    border: 1px solid #292D36;
    border-radius: 19px;
    padding: 18px;
    margin: 10px 0;
}

/* Footer */

.muted {
    color: #707580;
    font-size: 10px;
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

    st.caption("GOOD EVENING")

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
            placeholder="Income, gift, allowance...",
            key="add_source"
        )

        c1, c2 = st.columns(2)

        with c1:
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

        with c2:
            if st.button(
                "Cancel",
                use_container_width=True,
                key="cancel_add"
            ):
                st.session_state.show_add = False
                st.rerun()

    # Request money
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

        c1, c2 = st.columns(2)

        with c1:
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

        with c2:
            if st.button(
                "Cancel",
                use_container_width=True,
                key="cancel_request"
            ):
                st.session_state.show_request = False
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

        if spending_ratio >= 0.85:
            score = 68
        elif spending_ratio >= 0.60:
            score = 76

        st.metric(
            "VELORA Score",
            str(score) + " / 100"
        )

    # Intelligence
    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        '<div class="intel-title">'
        + status
        + '</div>'
        '<div class="intel-text">'
        + status_text
        + '</div>'
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

    progress = min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )

    st.markdown(
        '<div class="goal-card">'
        '<div class="goal-title">'
        + st.session_state.goal_name
        + '</div>'
        '<div class="goal-meta">'
        'Progress toward your target'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.caption(
        "₹{:,.0f} saved of ₹{:,.0f} · {:.0f}%".format(
            st.session_state.goal_saved,
            st.session_state.goal_target,
            progress * 100
        )
    )

    # Recent activity
    st.markdown(
        '<div class="section-title">Recent activity</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.transactions[:5]:

        name, category, amount = item

        if amount >= 0:
            amount_text = "+₹{:,.0f}".format(amount)
        else:
            amount_text = "−₹{:,.0f}".format(abs(amount))

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name
            + '</div>'
            '<div class="tx-category">'
            + category
            + ' · '
            + amount_text
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section-title">Pay</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Demo payment experience · No real transactions"
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-chip">VIRTUAL CARD · DEMO</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-footer">'
        'VELORA MEMBER · DEMO ONLY'
        '</div>'
        '</div>',
        unsafe_allow_html=True
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

        if not recipient.strip():
            st.error("Enter a recipient.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        elif st.session_state.card_frozen:
            st.error("Your card is frozen.")

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
        placeholder="Search transactions..."
    )

    found = False

    for item in st.session_state.transactions:

        name, category, amount = item

        searchable = (
            name + " " + category
        ).lower()

        if search.lower() not in searchable:
            continue

        found = True

        if amount >= 0:
            amount_text = "+₹{:,.0f}".format(amount)
        else:
            amount_text = "−₹{:,.0f}".format(abs(amount))

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-name">'
            + name
            + '</div>'
            '<div class="tx-category">'
            + category
            + ' · '
            + amount_text
            + '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if not found:
        st.info("No transactions found.")


# =========================================================
# INTELLIGENCE
# =========================================================

elif st.session_state.page == "Intelligence":

    st.markdown(
        '<div class="section-title">VELORA Intelligence</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()

    ratio = (
        spent /
        max(st.session_state.monthly_limit, 1)
    )

    if ratio < 0.60:

        title = "You're financially on track."

        text = (
            "Your current spending is well within "
            "your planned monthly budget. "
            "You have room to continue saving."
        )

    elif ratio < 0.85:

        title = "Your spending needs attention."

        text = (
            "You're using a significant portion "
            "of your monthly budget. "
            "Consider slowing discretionary spending."
        )

    else:

        title = "Budget pressure detected."

        text = (
            "Your current spending is close to "
            "or above your planned monthly limit."
        )

    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">AI MONEY INSIGHT</div>'
        '<div class="intel-title">'
        + title
        + '</div>'
        '<div class="intel-text">'
        + text
        + '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Spending categories</div>',
        unsafe_allow_html=True
    )

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    data = {}

    for category in categories:

        value = category_total(category)

        if value > 0:
            data[category] = value

    if data:

        chart_data = pd.DataFrame(
            {"Amount": data}
        )

        st.bar_chart(chart_data)

        biggest = max(
            data,
            key=data.get
        )

        st.info(
            "{} is currently your largest "
            "tracked spending category.".format(
                biggest
 