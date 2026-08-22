import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# VELORA — PREMIUM INTELLIGENT MONEY MANAGEMENT
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

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #292A45 0%, #0B0C11 35%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 620px;
    padding: 20px 16px 100px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1,h2,h3,h4,p,label {
    color:#F5F5F7 !important;
}

.stButton > button {
    background:#151821 !important;
    color:#FFFFFF !important;
    border:1px solid #303542 !important;
    border-radius:14px !important;
    min-height:44px !important;
    font-weight:750 !important;
}

.stButton > button:hover {
    border-color:#9B7BFF !important;
    background:#1D202B !important;
}

[data-testid="stMetric"] {
    background:#12151C;
    border:1px solid #292E38;
    border-radius:18px;
    padding:15px;
}

[data-testid="stMetricValue"] {
    color:#FFFFFF !important;
    font-weight:850 !important;
}

[data-testid="stMetricLabel"] {
    color:#858B98 !important;
}

.stTextInput input,
.stNumberInput input {
    background:#11141A !important;
    color:#FFFFFF !important;
}

.stSelectbox div[data-baseweb="select"] {
    background:#11141A !important;
}

.stProgress > div > div > div > div {
    background:#9B7BFF;
}

hr {
    border-color:#252A34 !important;
}

.brand {
    font-size:30px;
    font-weight:950;
    letter-spacing:5px;
}

.tagline {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
}

.card {
    background:linear-gradient(145deg,#1B1F2A,#101217);
    border:1px solid #303542;
    border-radius:25px;
    padding:22px;
    margin:14px 0;
}

.balance-label {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
    font-weight:700;
}

.balance {
    color:#FFFFFF;
    font-size:44px;
    font-weight:900;
    letter-spacing:-2px;
    margin-top:5px;
}

.muted {
    color:#858B98 !important;
    font-size:11px;
}

.section {
    color:#F5F5F7;
    font-size:18px;
    font-weight:850;
    margin-top:25px;
    margin-bottom:9px;
}

.insight {
    background:linear-gradient(145deg,#1A1624,#101116);
    border:1px solid #493960;
    border-radius:22px;
    padding:20px;
    margin:14px 0;
}

.insight-label {
    color:#A98CFF;
    font-size:10px;
    font-weight:850;
    letter-spacing:2px;
}

.insight-title {
    color:#FFFFFF;
    font-size:18px;
    font-weight:850;
    margin-top:7px;
}

.insight-text {
    color:#999DA9;
    font-size:12px;
    line-height:1.55;
    margin-top:5px;
}

.transaction {
    background:#11141A;
    border:1px solid #252A34;
    border-radius:16px;
    padding:14px;
    margin:7px 0;
}

.tx-title {
    color:#F4F5F7;
    font-weight:750;
    font-size:13px;
}

.tx-cat {
    color:#777D89;
    font-size:10px;
}

.tx-income {
    color:#6EE7A0;
    font-weight:800;
}

.tx-expense {
    color:#FF7D91;
    font-weight:800;
}

.goal {
    background:#11141A;
    border:1px solid #292E38;
    border-radius:20px;
    padding:18px;
    margin:10px 0;
}

.goal-title {
    font-weight:800;
    font-size:15px;
}

.goal-money {
    font-size:21px;
    font-weight:850;
}

.virtual-card {
    background:
        radial-gradient(circle at 80% 10%,#5A4E82 0%,transparent 35%),
        linear-gradient(135deg,#292D3C,#101218);
    border:1px solid #505566;
    border-radius:26px;
    padding:25px;
    min-height:165px;
    margin:15px 0;
    box-shadow:0 15px 45px rgba(0,0,0,.35);
}

.card-brand {
    font-weight:900;
    letter-spacing:4px;
}

.card-number {
    font-size:19px;
    letter-spacing:3px;
    margin-top:30px;
}

.card-small {
    color:#858B98;
    font-size:9px;
    letter-spacing:1px;
    margin-top:15px;
}

.score {
    background:linear-gradient(145deg,#211A31,#111219);
    border:1px solid #46365B;
    border-radius:22px;
    padding:20px;
    text-align:center;
    margin:15px 0;
}

.score-number {
    font-size:42px;
    font-weight:950;
}

.score-label {
    color:#9A9DA8;
    font-size:10px;
    letter-spacing:2px;
}

.jar {
    background:linear-gradient(145deg,#171923,#101116);
    border:1px solid #303542;
    border-radius:22px;
    padding:20px;
    margin:12px 0;
}

.jar-title {
    font-size:17px;
    font-weight:850;
}

.jar-money {
    font-size:27px;
    font-weight:900;
    margin:5px 0;
}

.notice {
    background:#151821;
    border:1px solid #303542;
    border-radius:15px;
    padding:13px;
    margin:8px 0;
}

.stat-card {
    background:#11141A;
    border:1px solid #292E38;
    border-radius:18px;
    padding:17px;
    text-align:center;
}

.stat-value {
    font-size:25px;
    font-weight:900;
}

.stat-label {
    color:#858B98;
    font-size:10px;
    margin-top:4px;
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
    "notifications": [],
    "jar": 850.0,

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
        [
            name,
            category,
            float(amount),
            datetime.now().strftime("%d %b")
        ]
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


def biggest_category():

    data = {}

    for item in st.session_state.transactions:

        if item[2] < 0:

            category = item[1]

            data[category] = (
                data.get(category, 0)
                + abs(item[2])
            )

    if not data:
        return "None", 0

    category = max(data, key=data.get)

    return category, data[category]


def category_data():

    data = {}

    for item in st.session_state.transactions:

        if item[2] < 0:

            cat = item[1]

            data[cat] = (
                data.get(cat, 0)
                + abs(item[2])
            )

    return data


def get_score():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    if ratio <= .50:
        score = 94

    elif ratio <= .70:
        score = 88

    elif ratio <= .85:
        score = 80

    elif ratio <= 1:
        score = 70

    else:
        score = 58

    if st.session_state.jar >= 1000:
        score += 3

    return min(score, 100)


def get_insight():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    biggest, value = biggest_category()

    if ratio >= 1:

        return (
            "Budget Alert",
            "You've crossed your monthly spending limit. "
            "Prioritise essential expenses."
        )

    if ratio >= .80:

        return (
            "Watch Your Spending",
            "{} is your biggest category at ₹{:,.0f}. "
            "You're getting close to your limit."
            .format(biggest, value)
        )

    if st.session_state.jar >= 1000:

        return (
            "Great Saving Behaviour",
            "Your Savings Jar contains ₹{:,.0f}. "
            "You're building a healthy saving habit."
            .format(st.session_state.jar)
        )

    return (
        "Spending Pattern Detected",
        "{} is currently your biggest spending category "
        "at ₹{:,.0f}."
        .format(biggest, value)
    )


def reset_demo():

    st.session_state.balance = 5000.0
    st.session_state.monthly_limit = 2000.0
    st.session_state.name = "Tejal"
    st.session_state.page = "Home"
    st.session_state.card_frozen = False
    st.session_state.notifications = []
    st.session_state.jar = 850.0

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
    '<div class="tagline">'
    'INTELLIGENT MONEY MANAGEMENT'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# NAVIGATION
# =========================================================

n1,n2,n3,n4,n5 = st.columns(5)

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

    # BALANCE

    st.markdown(
        '<div class="card">'
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

    # QUICK ACTIONS

    a,b,c = st.columns(3)

    with a:
        if st.button("＋ ADD", use_container_width=True):

            amount = st.number_input(
                "Add amount",
                min_value=1.0,
                value=500.0,
                step=100.0,
                key="home_add_amount"
            )

            source = st.text_input(
                "Source",
                value="Pocket Money",
                key="home_add_source"
            )

            if st.button(
                "Confirm Add",
                use_container_width=True,
                key="home_confirm_add"
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

                st.rerun()

    with b:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⇄ REQUEST", use_container_width=True):

            st.info(
                "Demo request created. "
                "No real payment request is sent."
            )

    # SNAPSHOT

    st.markdown(
        '<div class="section">Financial Snapshot</div>',
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

    c1,c2 = st.columns(2)

    with c1:
        st.metric(
            "Spent",
            "₹{:,.0f}".format(spent)
        )

    with c2:
        st.metric(
            "Remaining",
            "₹{:,.0f}".format(remaining)
        )

    c3,c4 = st.columns(2)

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
            "{}/100".format(get_score())
        )

    # BUDGET BAR

    st.markdown(
        '<div class="muted">'
        'MONTHLY BUDGET USAGE'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(
        min(ratio,1.0)
    )

    st.caption(
        "₹{:,.0f} of ₹{:,.0f} used"
        .format(
            spent,
            st.session_state.monthly_limit
        )
    )

    if ratio < .60:

        st.success(
            "You're on track. Spending is comfortably below your limit."
        )

    elif ratio < .85:

        st.warning(
            "You're approaching your monthly limit."
        )

    else:

        st.error(
            "Budget risk detected."
        )

    # AI

    title,text = get_insight()

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">'
        'VELORA AI COACH'
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

    # TREND

    st.markdown(
        '<div class="section">Spending Trend</div>',
        unsafe_allow_html=True
    )

    trend = pd.DataFrame(
        {
            "Spending":[
                120,180,90,240,160,280,110
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

    st.line_chart(trend)

    # SAVINGS JAR

    st.markdown(
        '<div class="section">Savings Jar</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="jar">'
        '<div class="jar-title">Future Fund</div>'
        '<div class="jar-money">'
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

    jar_action = st.selectbox(
        "Savings Jar action",
        [
            "No action",
            "Add to Jar",
            "Withdraw from Jar"
        ],
        key="home_jar_action"
    )

    if jar_action != "No action":

        jar_amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=100.0,
            step=50.0,
            key="home_jar_amount"
        )

        if st.button(
            "Confirm Jar Action",
            use_container_width=True,
            key="home_jar_confirm"
        ):

            if jar_action == "Add to Jar":

                if jar_amount > st.session_state.balance:

                    st.error(
                        "Insufficient demo balance."
                    )

                else:

                    st.session_state.balance -= jar_amount
                    st.session_state.jar += jar_amount

                    add_transaction(
                        "Savings Jar",
                        "Savings",
                        -jar_amount
                    )

                    st.rerun()

            else:

                if jar_amount > st.session_state.jar:

                    st.error(
                        "Not enough money in jar."
                    )

                else:

                    st.session_state.jar -= jar_amount
                    st.session_state.balance += jar_amount

                    add_transaction(
                        "Jar Withdrawal",
                        "Savings",
                        jar_amount
                    )

                    st.rerun()

    # GOALS

    st.markdown(
        '<div class="section">Savings Goals</div>',
        unsafe_allow_html=True
    )

    for i,goal in enumerate(
        st.session_state.goals
    ):

        progress = min(
            goal["saved"] /
            max(goal["target"],1),
            1
        )

        st.markdown(
            '<div class="goal">'
            '<div class="goal-title">'
            '{}'
            '</div>'
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

        if progress >= 1:

            st.success(
                "Goal completed 🎉"
            )

        else:

            amount = st.number_input(
                "Add to goal",
                min_value=1.0,
                value=100.0,
                step=50.0,
                key="goal_amount_"+str(i)
            )

            if st.button(
                "Save to Goal",
                use_container_width=True,
                key="goal_button_"+str(i)
            ):

                if amount > st.session_state.balance:

                    st.error(
                        "Insufficient balance."
                    )

                else:

                    st.session_state.balance -= amount

                    goal["saved"] = min(
                        goal["saved"] + amount,
                        goal["target"]
                    )

                    add_transaction(
                        goal["name"],
                        "Savings",
                        -amount
                    )

                    st.rerun()

# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Payments")

    st.caption(
        "Simulated payment · No real UPI or bank connection"
    )

    if st.session_state.card_frozen:

        st.error(
            "🔒 VELORA Card is currently frozen."
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
            "Bills",
            "Other"
        ]
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

            add