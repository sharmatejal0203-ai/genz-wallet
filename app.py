import streamlit as st
import pandas as pd

# =========================================================
# VELORA V3
# Premium Intelligent Money Management Demo
# DEMO ONLY — NO REAL MONEY / UPI / BANK CONNECTION
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 50% -10%,
                #292D46 0%,
                #0B0C11 38%,
                #08090D 100%
            );
        color: #F5F5F7;
    }

    .block-container {
        max-width: 620px;
        padding: 24px 16px 80px;
    }

    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }

    h1, h2, h3, h4, p, label {
        color: #F5F5F7 !important;
    }

    .brand {
        font-size: 30px;
        font-weight: 950;
        letter-spacing: 5px;
    }

    .tagline {
        color: #858B98;
        font-size: 10px;
        letter-spacing: 2px;
    }

    .hero {
        background: linear-gradient(
            145deg,
            #1B1F2A,
            #101217
        );
        border: 1px solid #303542;
        border-radius: 26px;
        padding: 24px;
        margin: 18px 0;
    }

    .balance-label {
        color: #858B98;
        font-size: 10px;
        letter-spacing: 2px;
        font-weight: 700;
    }

    .balance {
        color: #FFFFFF;
        font-size: 44px;
        font-weight: 900;
        margin: 4px 0;
    }

    .muted {
        color: #858B98 !important;
        font-size: 11px;
    }

    .section {
        color: #FFFFFF;
        font-size: 18px;
        font-weight: 850;
        margin-top: 26px;
        margin-bottom: 10px;
    }

    .insight {
        background: linear-gradient(
            145deg,
            #1A1624,
            #101116
        );
        border: 1px solid #493960;
        border-radius: 22px;
        padding: 20px;
        margin: 15px 0;
    }

    .insight-label {
        color: #A98CFF;
        font-size: 10px;
        font-weight: 850;
        letter-spacing: 2px;
    }

    .insight-title {
        color: #FFFFFF;
        font-size: 18px;
        font-weight: 850;
        margin-top: 7px;
    }

    .insight-text {
        color: #999DA9;
        font-size: 12px;
        line-height: 1.55;
        margin-top: 5px;
    }

    .transaction {
        background: #11141A;
        border: 1px solid #252A34;
        border-radius: 16px;
        padding: 14px;
        margin: 8px 0;
    }

    .tx-title {
        color: #F4F5F7;
        font-weight: 750;
        font-size: 13px;
    }

    .tx-cat {
        color: #777D89;
        font-size: 10px;
    }

    .tx-income {
        color: #6EE7A0;
        font-weight: 800;
    }

    .tx-expense {
        color: #FF7D91;
        font-weight: 800;
    }

    .goal {
        background: #11141A;
        border: 1px solid #292E38;
        border-radius: 20px;
        padding: 18px;
        margin: 10px 0;
    }

    .goal-title {
        color: #FFFFFF;
        font-weight: 800;
        font-size: 15px;
    }

    .goal-money {
        color: #FFFFFF;
        font-size: 21px;
        font-weight: 850;
    }

    .virtual-card {
        background:
            radial-gradient(
                circle at 80% 10%,
                #5A4E82 0%,
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #292D3C,
                #101218
            );
        border: 1px solid #505566;
        border-radius: 27px;
        padding: 25px;
        min-height: 170px;
        margin: 18px 0;
        box-shadow: 0 15px 45px rgba(0,0,0,.35);
    }

    .card-brand {
        color: #FFFFFF;
        font-weight: 900;
        letter-spacing: 4px;
    }

    .card-number {
        color: #FFFFFF;
        font-size: 19px;
        letter-spacing: 3px;
        margin-top: 32px;
    }

    .card-small {
        color: #858B98;
        font-size: 9px;
        letter-spacing: 1px;
        margin-top: 16px;
    }

    .score {
        background: linear-gradient(
            145deg,
            #211A31,
            #111219
        );
        border: 1px solid #46365B;
        border-radius: 22px;
        padding: 20px;
        text-align: center;
    }

    .score-number {
        color: #FFFFFF;
        font-size: 42px;
        font-weight: 950;
    }

    .score-label {
        color: #9A9DA8;
        font-size: 10px;
        letter-spacing: 2px;
    }

    .notice {
        background: #151821;
        border: 1px solid #303542;
        border-radius: 15px;
        padding: 13px;
        margin: 8px 0;
    }

    .stButton > button {
        background: #151821 !important;
        color: #FFFFFF !important;
        border: 1px solid #303542 !important;
        border-radius: 14px !important;
        min-height: 44px !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        border-color: #9B7BFF !important;
        background: #1D202B !important;
    }

    [data-testid="stMetric"] {
        background: #12151C;
        border: 1px solid #292E38;
        border-radius: 18px;
        padding: 15px;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    [data-testid="stMetricLabel"] {
        color: #858B98 !important;
    }

    .stTextInput input,
    .stNumberInput input {
        background: #11141A !important;
        color: #FFFFFF !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        background: #11141A !important;
    }

    .stProgress > div > div > div > div {
        background: #9B7BFF;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "monthly_limit" not in st.session_state:
    st.session_state.monthly_limit = 2000.0

if "name" not in st.session_state:
    st.session_state.name = "Tejal"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "card_frozen" not in st.session_state:
    st.session_state.card_frozen = False

if "jar" not in st.session_state:
    st.session_state.jar = 850.0

if "notifications" not in st.session_state:
    st.session_state.notifications = []

if "goals" not in st.session_state:
    st.session_state.goals = [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ]

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ]

# =========================================================
# FUNCTIONS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, float(amount)]
    )


def spending_total():
    total = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            total += abs(item[2])

    return total


def income_total():
    total = 0

    for item in st.session_state.transactions:
        if item[2] > 0:
            total += item[2]

    return total


def category_totals():
    result = {}

    for item in st.session_state.transactions:

        if item[2] < 0:

            category = item[1]

            if category not in result:
                result[category] = 0

            result[category] += abs(item[2])

    return result


def biggest_category():

    data = category_totals()

    if not data:
        return "None", 0

    category = max(
        data,
        key=data.get
    )

    return category, data[category]


def financial_score():

    spent = spending_total()

    limit = max(
        float(st.session_state.monthly_limit),
        1
    )

    ratio = spent / limit

    if ratio <= 0.50:
        score = 94

    elif ratio <= 0.70:
        score = 88

    elif ratio <= 0.85:
        score = 80

    elif ratio <= 1:
        score = 70

    else:
        score = 55

    if st.session_state.jar >= 1000:
        score += 3

    return min(score, 100)


def ai_insight():

    spent = spending_total()

    limit = max(
        float(st.session_state.monthly_limit),
        1
    )

    ratio = spent / limit

    biggest, value = biggest_category()

    if ratio > 1:

        return (
            "Budget Alert",
            "You've crossed your monthly limit. "
            "Consider reducing non-essential spending."
        )

    if ratio >= 0.80:

        return (
            "Watch Your Spending",
            "{} is your biggest category at ₹{:,.0f}."
            .format(biggest, value)
        )

    if st.session_state.jar >= 1000:

        return (
            "Strong Saving Behaviour",
            "Your Savings Jar has ₹{:,.0f}. "
            "You're building a consistent saving habit."
            .format(st.session_state.jar)
        )

    if biggest != "None":

        return (
            "Spending Pattern Detected",
            "{} is currently your biggest category at ₹{:,.0f}."
            .format(biggest, value)
        )

    return (
        "VELORA is Ready",
        "Start adding transactions to unlock more insights."
    )


def reset_demo():

    st.session_state.balance = 5000.0
    st.session_state.monthly_limit = 2000.0
    st.session_state.name = "Tejal"
    st.session_state.page = "Home"
    st.session_state.card_frozen = False
    st.session_state.jar = 850.0
    st.session_state.notifications = []

    st.session_state.goals = [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ]

    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ]

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">INTELLIGENT MONEY MANAGEMENT</div>',
    unsafe_allow_html=True
)

st.write("")

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

    st.caption("GOOD EVENING")
    st.subheader(
        st.session_state.name + " 👋"
    )

    st.markdown(
        '<div class="hero">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹{:,.0f}</div>'
        '<div class="muted">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:

        if st.button(
            "＋ ADD",
            use_container_width=True
        ):
            go("Add")

    with b:

        if st.button(
            "↗ SEND",
            use_container_width=True
        ):
            go("Pay")

    with c:

        if st.button(
            "🎯 GOALS",
            use_container_width=True
        ):
            go("Goals")

    # -----------------------------------------------------
    # SNAPSHOT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Financial Snapshot</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Spent",
            "₹{:,.0f}".format(spent)
        )

    with c2:

        st.metric(
            "Budget Left",
            "₹{:,.0f}".format(remaining)
        )

    c3, c4 = st.columns(2)

    with c3:

        st.metric(
            "Savings Jar",
            "₹{:,.0f}".format(
                st.session_state.jar
            )
        )

    with c4:

        st.metric(
            "VELORA Score",
            "{}/100".format(
                financial_score()
            )
        )

    # -----------------------------------------------------
    # BUDGET STATUS
    # -----------------------------------------------------

    ratio = spent / max(
        float(st.session_state.monthly_limit),
        1
    )

    if ratio < 0.60:

        st.success(
            "You're on track. Spending is under control."
        )

    elif ratio < 0.85:

        st.warning(
            "You're getting close to your monthly limit."
        )

    else:

        st.error(
            "Budget risk detected."
        )

    # -----------------------------------------------------
    # INTELLIGENCE
    # -----------------------------------------------------

    biggest, value = biggest_category()

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">'
        'VELORA INTELLIGENCE'
        '</div>'
        '<div class="insight-title">'
        '{} is your biggest category'
        '</div>'
        '<div class="insight-text">'
        '₹{:,.0f} spent in this category.'
        '</div>'
        '</div>'.format(
            biggest,
            value
        ),
        unsafe_allow_html=True
    )

    title, text = ai_insight()

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">'
        'AI FINANCIAL COACH'
        '</div>'
        '<div class="insight-title">'
        '{}'
        '</div>'
        '<div class="insight-text">'
        '{}'
        '</div>'
        '</div>'.format(
            title,
            text
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # CHART
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Spending Trend</div>',
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

    # -----------------------------------------------------
    # SAVINGS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Savings Jar</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-title">'
        'Future Fund'
        '</div>'
        '<div class="goal-money">'
        '₹{:,.0f}'
        '</div>'
        '<div class="muted">'
        'Money intentionally set aside'
        '</div>'
        '</div>'.format(
            st.session_state.jar
        ),
        unsafe_allow_html=True
    )

# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state.page == "Add":

    st.subheader("Add Money")

    st.caption(
        "Demo transaction only."
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
        value="Pocket Money",
        key="add_source"
    )

    if st.button(
        "Add to Wallet",
        use_container_width=True
    ):

        st.session_state.balance += amount

        add_transaction(
            source.strip() or "Income",
            "Income",
            amount
        )

        st.session_state.notifications.insert(
            0,
            "₹{:,.0f} added successfully."
            .format(amount)
        )

        st.success(
            "Money added to demo wallet."
        )

        go("Home")

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")

# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Send Money")

    st.caption(
        "Simulated payment — no real UPI."
    )

    if st.session_state.card_frozen:

        st.error(
            "🔒 VELORA Card is Frozen."
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
        key="pay_amount"
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Bills",
            "Other"
        ],
        key="pay_category"
    )

    if st.button(
        "Send Payment",
        use_container_width=True
    ):

        if not recipient.strip():

            st.error(
                "Enter recipient."
            )

        elif amount > st.session_state.balance:

            st.error(
                "Insufficient demo balance."
            )

        elif st.session_state.card_frozen:

            st.error(
                "Card is frozen."
            )

        else:

            st.session_state.balance -= amount

            add_transaction(
                "Sent to " + recipient.strip(),
                category,
                -amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} sent to {}."
                .format(
                    amount,
                    recipient.strip()
                )
            )

            st.success(
                "Payment simulated successfully."
            )

    # -----------------------------------------------------
    # VIRTUAL CARD
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">VELORA Card</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-small">'
        'DEMO VIRTUAL CARD · 09/30'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        if st.button(
            "UNFREEZE CARD",
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        if st.button(
            "FREEZE C