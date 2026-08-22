import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================================
# VELORA 3.0
# Intelligent Money Management
# Demo Prototype — No real money / UPI / bank connection
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
        radial-gradient(circle at 50% -10%, #202435 0%, #0B0C10 38%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 570px;
    padding: 24px 18px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: #F5F5F7 !important;
}

.stButton > button {
    background: #151820 !important;
    color: #FFFFFF !important;
    border: 1px solid #303542 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
    background: #1C202A !important;
}

[data-testid="stMetric"] {
    background: #12151C;
    border: 1px solid #292E38;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #8D929E !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background: #11141A !important;
    color: white !important;
}

.stSelectbox div[data-baseweb="select"] {
    background: #11141A !important;
}

hr {
    border-color: #282D37 !important;
}

/* CUSTOM */

.brand {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 4px;
}

.tagline {
    color: #858B98;
    font-size: 11px;
    letter-spacing: 1px;
}

.hero {
    background: linear-gradient(145deg, #1D202A, #101217);
    border: 1px solid #343945;
    border-radius: 25px;
    padding: 24px;
    margin: 18px 0;
    box-shadow: 0 18px 45px rgba(0,0,0,.25);
}

.hero-label {
    color: #858B98;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 800;
}

.hero-balance {
    color: white;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 7px;
}

.muted {
    color: #858B98 !important;
    font-size: 11px;
}

.section {
    color: white;
    font-size: 18px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
}

.intelligence {
    background: linear-gradient(145deg, #191521, #101117);
    border: 1px solid #43365A;
    border-radius: 21px;
    padding: 20px;
    margin: 15px 0;
}

.intel-label {
    color: #AA8EFF;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 2px;
}

.intel-title {
    color: white;
    font-size: 19px;
    font-weight: 800;
    margin-top: 8px;
}

.intel-text {
    color: #9B9EAA;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 5px;
}

.card-ui {
    background: linear-gradient(135deg, #252936, #101218);
    border: 1px solid #474C59;
    border-radius: 25px;
    padding: 25px;
    height: 165px;
    margin: 15px 0;
}

.card-logo {
    color: white;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-number {
    color: white;
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 32px;
}

.card-meta {
    color: #777D8A;
    font-size: 9px;
    margin-top: 16px;
    letter-spacing: 1px;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 16px;
    padding: 14px;
    margin: 8px 0;
}

.tx-title {
    color: white;
    font-size: 13px;
    font-weight: 750;
}

.tx-category {
    color: #777D89;
    font-size: 10px;
    margin-top: 4px;
}

.goal {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 20px;
    padding: 18px;
    margin-top: 10px;
}

.goal-name {
    color: white;
    font-weight: 800;
    font-size: 16px;
}

.score {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
}

.score-number {
    color: white;
    font-size: 34px;
    font-weight: 900;
}

.badge {
    background: #1B1924;
    border: 1px solid #403653;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    color: #B39BFF;
    font-size: 11px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "name": "Tejal",

    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,

    "card_frozen": False,

    "page": "Home",

    "notifications": [],

    "streak": 7,

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


def budget_ratio():
    return spending_total() / max(
        st.session_state.monthly_limit,
        1
    )


def score():
    ratio = budget_ratio()

    if ratio < 0.50:
        return 95
    elif ratio < 0.70:
        return 88
    elif ratio < 0.85:
        return 78
    elif ratio < 1:
        return 68
    return 55


def goal_percentage():
    return min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )


def notify(message):
    st.session_state.notifications.insert(
        0,
        message
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">INTELLIGENT MONEY MANAGEMENT</div>',
    unsafe_allow_html=True
)

st.write("")


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
    if st.button("INSIGHT", use_container_width=True):
        go("Insight")

with n5:
    if st.button("PROFILE", use_container_width=True):
        go("Profile")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader(
        st.session_state.name + " 👋"
    )

    # BALANCE
    st.markdown(
        '<div class="hero">'
        '<div class="hero-label">AVAILABLE BALANCE</div>'
        '<div class="hero-balance">₹{:,.2f}</div>'
        '<div class="muted">'
        'DEMO WALLET · NO REAL MONEY CONNECTED'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
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
            st.session_state.show_add = True

    with q2:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with q3:
        if st.button("⇄ REQUEST", use_container_width=True):
            st.session_state.show_request = True


    # ADD MONEY
    if st.session_state.get("show_add", False):

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="home_add_amount"
        )

        source = st.text_input(
            "Source",
            placeholder="Pocket money, gift, allowance...",
            key="home_add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="home_confirm_add"
        ):

            source = source.strip() or "Income"

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            notify(
                "₹{:,.0f} added to your wallet.".format(amount)
            )

            st.session_state.show_add = False

            st.success("Balance updated.")
            st.rerun()


    # REQUEST
    if st.session_state.get("show_request", False):

        st.markdown("### Request money")

        person = st.text_input(
            "Request from",
            placeholder="Friend's name",
            key="home_request_person"
        )

        amount = st.number_input(
            "Request amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="home_request_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True,
            key="home_create_request"
        ):

            if not person.strip():

                st.error("Enter a name.")

            else:

                notify(
                    "₹{:,.0f} request created for {}.".format(
                        amount,
                        person.strip()
                    )
                )

                st.session_state.show_request = False

                st.success("Request created.")
                st.rerun()


    # ========================================================
    # FINANCIAL SNAPSHOT
    # ========================================================

    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = budget_ratio()

    s1, s2 = st.columns(2)

    with s1:
        st.metric(
            "Spent",
            "₹{:,.0f}".format(spent)
        )

    with s2:
        st.metric(
            "Budget left",
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
            "{}/100".format(score())
        )


    # BUDGET STATUS
    if ratio < 0.60:

        st.success(
            "You're on track. Your spending is comfortably below your limit."
        )

    elif ratio < 0.85:

        st.warning(
            "Watch your pace. You're approaching your monthly limit."
        )

    else:

        st.error(
            "Budget risk. Your spending is getting high."
        )


    # ========================================================
    # INTELLIGENCE
    # ========================================================

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

    if categories:

        biggest = max(
            categories,
            key=categories.get
        )

        biggest_amount = categories[biggest]

    else:

        biggest = "None"
        biggest_amount = 0


    if ratio < 0.60:

        intel_title = "You're spending with control."

        intel_text = (
            "Your current spending is comfortably below "
            "your planned monthly budget."
        )

    elif ratio < 0.85:

        intel_title = "Keep an eye on your pace."

        intel_text = (
            "You're approaching your monthly limit. "
            "A little planning now can prevent overspending later."
        )

    else:

        intel_title = "Your budget needs attention."

        intel_text = (
            "Your spending is close to or above your "
            "planned monthly limit."
        )


    st.markdown(
        '<div class="intelligence">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        '<div class="intel-title">{}</div>'
        '<div class="intel-text">{}</div>'
        '</div>'.format(
            intel_title,
            intel_text
        ),
        unsafe_allow_html=True
    )


    # ========================================================
    # SAVING STREAK
    # ========================================================

    st.markdown(
        '<div class="section">🔥 Saving streak</div>',
        unsafe_allow_html=True
    )

    st.metric(
        "Current streak",
        "{} days".format(
            st.session_state.streak
        )
    )

    st.caption(
        "Consistent habits matter more than one perfect day."
    )


    # ========================================================
    # SPENDING TREND
    # ========================================================

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


    # ========================================================
    # CATEGORIES
    # ========================================================

    st.markdown(
        '<div class="section">Where your money goes</div>',
        unsafe_allow_html=True
    )

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

            st.write(
                "{} · ₹{:,.0f}".format(
                    category,
                    value
                )
            )

            st.progress(
                min(
                    value / max(spent, 1),
                    1
                )
            )


    # ========================================================
    # SAVINGS GOAL
    # ========================================================

    st.markdown(
        '<div class="section">Savings goal</div>',
        unsafe_allow_html=True
    )

    progress = goal_percentage()

    st.markdown(
        '<div class="goal">'
        '<div class="goal-name">🎯 {}</div>'
        '<div class="muted">₹{:,.0f} of ₹{:,.0f}</div>'
        '</div>'.format(
            st.session_state.goal_name,
            st.session_state.goal_saved,
            st.session_state.goal_target
        ),
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.caption(
        "{:.0f}% complete".format(
            progress * 100
        )
    )


    # ========================================================
    # RECENT ACTIVITY
    # ========================================================

    st.markdown(
        '<div class="section">Recent activity</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.transactions[:4]:

        name, category, amount = item

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-title">{}</div>'
            '<div class="tx-category">{}</div>'
            '<div style="text-align:right;">'
            '{}₹{:,.0f}'
            '</div>'
            '</div>'.format(
                name,
                category,
                sign,
                abs(amount)
            ),
            unsafe_allow_html=True
        )


# ============================================================
# PAY
# ============================================================

elif st.session_state.page == "Pay":

    st.subheader("Payments")

    st.caption(
        "Simulated payment · No real UPI or bank connection"
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Friend or contact"
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

            st.error("Enter recipient.")

        elif amount > st.session_state.balance:

            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= amount

            add_transaction(
                "Sent to " + recipient.strip(),
                category,
                -amount
            )

            notify(
                "₹{:,.0f} sent to {}.".format(
                    amount,
                    recipient.strip()
                )
            )

            st.success(
                "Payment simulated successfully."
            )

            st.rerun()


    st.divider()

    # CARD
    st.subheader("VELORA Card")

    st.markdown(
        '<div class="card-ui">'
        '<div class="card-logo">VELORA</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-meta">'
        'DEMO VIRTUAL CARD · NO REAL PAYMENTS'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.error("🔒 CARD FROZEN")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = False

            notify("VELORA Card unfrozen.")

            st.rerun()

    else:

        st.success("🟢 CARD ACTIVE")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = True

            notify("VELORA Card frozen.")

            st.rerun()


# ============================================================
# ACTIVITY
# ============================================================

elif st.session_state.page == "Activity":

    st.subheader("Activity")

    st.caption(
        "Your simulated money activity"
    )

    search = st.text_input(
        "Search",
        placeholder="Food, shopping, recipient..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

