import streamlit as st
import pandas as pd

# =========================================================
# VELORA — COMPLETE STABLE DEMO
# Intelligent Money Management
# Demo only — no real money / UPI / bank connection
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #20243A 0%, #0B0C11 38%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 580px;
    padding: 22px 17px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: #F5F5F7 !important;
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
    background: #1B1E28 !important;
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
    color: #858B98 !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background: #11141A !important;
    color: #FFFFFF !important;
}

.stSelectbox div[data-baseweb="select"] {
    background: #11141A !important;
    color: #FFFFFF !important;
}

hr {
    border-color: #252A34 !important;
}

.brand {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 4px;
}

.tagline {
    color: #858B98;
    font-size: 11px;
    letter-spacing: 1px;
}

.card {
    background: linear-gradient(145deg, #1A1E28, #101217);
    border: 1px solid #303542;
    border-radius: 24px;
    padding: 22px;
    margin: 14px 0;
}

.balance-label {
    color: #858B98;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}

.balance {
    color: #FFFFFF;
    font-size: 43px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 6px;
}

.muted {
    color: #858B98 !important;
    font-size: 11px;
}

.section {
    color: #F5F5F7;
    font-size: 18px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 9px;
}

.insight {
    background: linear-gradient(145deg, #191522, #101116);
    border: 1px solid #44365D;
    border-radius: 21px;
    padding: 20px;
    margin: 13px 0;
}

.insight-label {
    color: #A98CFF;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
}

.insight-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 850;
    margin-top: 7px;
}

.insight-text {
    color: #9A9DA8;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 5px;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.tx-title {
    color: #F4F5F7;
    font-weight: 700;
    font-size: 13px;
}

.tx-cat {
    color: #777D89;
    font-size: 10px;
}

.virtual-card {
    background: linear-gradient(135deg, #242735, #101218);
    border: 1px solid #4A4F5D;
    border-radius: 25px;
    padding: 25px;
    min-height: 165px;
    margin: 15px 0;
}

.card-brand {
    font-weight: 900;
    letter-spacing: 3px;
}

.card-number {
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 28px;
}

.card-small {
    color: #858B98;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 15px;
}

.goal {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 19px;
    padding: 18px;
    margin: 10px 0;
}

.goal-title {
    font-weight: 800;
    font-size: 15px;
}

.goal-money {
    font-size: 21px;
    font-weight: 850;
}

.notice {
    background: #151821;
    border: 1px solid #303542;
    border-radius: 15px;
    padding: 13px;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "name": "Tejal",
    "page": "Home",
    "card_frozen": False,
    "show_add": False,
    "show_request": False,
    "notifications": [],
    "goals": [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ],
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
        [name, category, float(amount)]
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


def get_score():
    spent = spending_total()
    limit = max(st.session_state.monthly_limit, 1)
    ratio = spent / limit

    if ratio < 0.50:
        return 94
    if ratio < 0.70:
        return 88
    if ratio < 0.85:
        return 80
    if ratio < 1.00:
        return 70
    return 58


def biggest_category():
    data = {}

    for item in st.session_state.transactions:
        if item[2] < 0:
            category = item[1]
            data[category] = data.get(category, 0) + abs(item[2])

    if not data:
        return "None", 0

    biggest = max(data, key=data.get)

    return biggest, data[biggest]


def reset_demo():
    st.session_state.balance = 5000.0
    st.session_state.monthly_limit = 2000.0
    st.session_state.name = "Tejal"
    st.session_state.card_frozen = False
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
    '<div class="tagline">Intelligent money management</div>',
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
    st.subheader(st.session_state.name + " 👋")

    # Balance
    st.markdown(
        '<div class="card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹{:,.2f}</div>'
        '<div class="muted">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>'.format(st.session_state.balance),
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
        if st.button("⇄ REQUEST", use_container_width=True):
            st.session_state.show_request = True

    # Add money
    if st.session_state.show_add:

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_money_amount"
        )

        source = st.text_input(
            "Source",
            value="Pocket Money",
            key="add_money_source"
        )

        x1, x2 = st.columns(2)

        with x1:
            if st.button(
                "Confirm",
                use_container_width=True,
                key="add_confirm"
            ):
                st.session_state.balance += amount

                add_transaction(
                    source.strip() or "Income",
                    "Income",
                    amount
                )

                st.session_state.notifications.insert(
                    0,
                    "₹{:,.0f} added successfully.".format(amount)
                )

                st.session_state.show_add = False
                st.rerun()

        with x2:
            if st.button(
                "Cancel",
                use_container_width=True,
                key="add_cancel"
            ):
                st.session_state.show_add = False
                st.rerun()

    # Request money
    if st.session_state.show_request:

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

        x1, x2 = st.columns(2)

        with x1:
            if st.button(
                "Create request",
                use_container_width=True,
                key="request_confirm"
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

        with x2:
            if st.button(
                "Cancel",
                use_container_width=True,
                key="request_cancel"
            ):
                st.session_state.show_request = False
                st.rerun()

    # Financial snapshot
    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = spent / max(
        st.session_state.monthly_limit,
        1
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Spent this month",
            "₹{:,.0f}".format(spent)
        )

    with c2:
        st.metric(
            "Budget remaining",
            "₹{:,.0f}".format(remaining)
        )

    c3, c4 = st.columns(2)

    with c3:
        savings = sum(
            goal["saved"]
            for goal in st.session_state.goals
        )

        st.metric(
            "Savings",
            "₹{:,.0f}".format(savings)
        )

    with c4:
        st.metric(
            "VELORA Score",
            "{}/100".format(get_score())
        )

    if ratio < 0.60:
        st.success(
            "You're on track. Spending is comfortably below your limit."
        )
    elif ratio < 0.85:
        st.warning(
            "Watch your pace. You're approaching your monthly limit."
        )
    else:
        st.error(
            "Budget risk. Your spending is getting high."
        )

    # Intelligence
    biggest, biggest_value = biggest_category()

    if biggest != "None":

        st.markdown(
            '<div class="insight">'
            '<div class="insight-label">VELORA INTELLIGENCE</div>'
            '<div class="insight-title">'
            '{} is your biggest category'
            '</div>'
            '<div class="insight-text">'
            '₹{:,.0f} has been spent here. '
            'VELORA is tracking your spending patterns.'
            '</div>'
            '</div>'.format(
                biggest,
                biggest_value
            ),
            unsafe_allow_html=True
        )

    # Spending trend
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

    # Categories
    st.markdown(
        '<div class="section">Where your money goes</div>',
        unsafe_allow_html=True
    )

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    for category in categories:

        value = category_total(category)

        if value > 0:

            st.write(
                "{} · ₹{:,.0f}".format(
                    category,
                    value
                )
            )

            st.progress(
                min(value / max(spent, 1), 1.0)
            )

    # Goals
    st.markdown(
        '<div class="section">Your goals</div>',
        unsafe_allow_html=True
    )

    for goal in st.session_state.goals:

        progress = min(
            goal["saved"] /
            max(goal["target"], 1),
            1
        )

        st.markdown(
            '<div class="goal">'
            '<div class="goal-title">{}</div>'
            '<div class="goal-money">'
            '₹{:,.0f} / ₹{:,.0f}'
            '</div>'
            '</div>'.format(
                goal["name"],
                goal["saved"],
                goal["target"]
            ),
            unsafe_allow_html=True
        )

        st.progress(progress)


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Payments")

    st.caption(
        "Simulated payment · No real UPI or bank connection"
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Friend or contact",
        key="pay_recipient"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0,
        key="pay_amount"
    )

    category = st.select