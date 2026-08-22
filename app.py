import streamlit as st
import pandas as pd

# =========================================================
# VELORA — PREMIUM FINTECH DEMO
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>
.stApp {
    background: #08090D;
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
    color: #FFFFFF !important;
}

p, label {
    color: #9296A3 !important;
}

.stButton > button {
    width: 100%;
    background: #15171E !important;
    color: #FFFFFF !important;
    border: 1px solid #2B2E38 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
    background: #1B1D26 !important;
}

[data-testid="stMetric"] {
    background: #12141A;
    border: 1px solid #292C35;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #858995 !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

hr {
    border-color: #252832 !important;
}

input {
    color: white !important;
}

.brand {
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 4px;
    color: white;
}

.tagline {
    color: #777C88;
    font-size: 11px;
    letter-spacing: 1px;
}

.balance-card {
    background: linear-gradient(145deg, #191C25, #0F1116);
    border: 1px solid #343844;
    border-radius: 25px;
    padding: 25px;
    margin: 18px 0;
}

.balance-label {
    color: #858995;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}

.balance {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin-top: 7px;
}

.balance-note {
    color: #666B77;
    font-size: 10px;
    margin-top: 8px;
}

.section {
    color: white;
    font-size: 18px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
}

.intel {
    background: linear-gradient(145deg, #191522, #101116);
    border: 1px solid #3B3150;
    border-radius: 21px;
    padding: 20px;
    margin: 15px 0;
}

.intel-label {
    color: #A88BFF;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
}

.intel-title {
    color: white;
    font-size: 18px;
    font-weight: 800;
    margin-top: 8px;
}

.intel-text {
    color: #999CAA;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 5px;
}

.card {
    background: linear-gradient(135deg, #242833, #111319);
    border: 1px solid #4A4E59;
    border-radius: 24px;
    padding: 24px;
    height: 155px;
    margin: 15px 0;
}

.card-brand {
    color: white;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 3px;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 38px;
}

.card-small {
    color: #777C88;
    font-size: 9px;
    margin-top: 10px;
    letter-spacing: 1px;
}

.tx {
    background: #111318;
    border: 1px solid #252832;
    border-radius: 15px;
    padding: 14px;
    margin: 8px 0;
}

.tx-name {
    color: white;
    font-size: 13px;
    font-weight: 700;
}

.tx-category {
    color: #707581;
    font-size: 10px;
    margin-top: 3px;
}

.goal {
    background: #111318;
    border: 1px solid #292D36;
    border-radius: 19px;
    padding: 18px;
    margin-top: 10px;
}

.goal-name {
    color: white;
    font-size: 16px;
    font-weight: 800;
}

.goal-money {
    color: #A88BFF;
    font-size: 21px;
    font-weight: 850;
    margin-top: 7px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "limit" not in st.session_state:
    st.session_state.limit = 2000.0

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000.0

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400.0

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180]
    ]

# =========================================================
# FUNCTIONS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def spent():
    total = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            total += abs(item[2])

    return total


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def category_spending(category):
    total = 0

    for item in st.session_state.transactions:
        if item[1] == category and item[2] < 0:
            total += abs(item[2])

    return total


# =========================================================
# BRAND
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">INTELLIGENT MONEY MANAGEMENT</div>',
    unsafe_allow_html=True
)

# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("HOME"):
        go("Home")

with n2:
    if st.button("PAY"):
        go("Pay")

with n3:
    if st.button("ACTIVITY"):
        go("Activity")

with n4:
    if st.button("INTEL"):
        go("Intel")

with n5:
    if st.button("PROFILE"):
        go("Profile")

# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader("Welcome back")

    st.markdown(
        '<div class="balance-card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹'
        + format(st.session_state.balance, ",.2f")
        + '</div>'
        '<div class="balance-note">DEMO WALLET · NO REAL MONEY</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # QUICK ACTIONS
    st.markdown(
        '<div class="section">Quick actions</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        add_clicked = st.button("＋ ADD")

    with b:
        send_clicked = st.button("↗ SEND")

    with c:
        request_clicked = st.button("⇄ REQUEST")

    if add_clicked:
        st.session_state.show_add = True

    if send_clicked:
        go("Pay")

    if request_clicked:
        st.session_state.show_request = True

    # ADD MONEY
    if st.session_state.get("show_add", False):

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="money_amount"
        )

        source = st.text_input(
            "Source",
            placeholder="Pocket money, gift, income...",
            key="money_source"
        )

        if st.button("Confirm add"):

            source = source.strip()

            if source == "":
                source = "Income"

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.session_state.show_add = False

            st.success(
                "₹{:,.0f} added.".format(amount)
            )

            st.rerun()

    # REQUEST
    if st.session_state.get("show_request", False):

        st.markdown("### Request money")

        person = st.text_input(
            "From",
            placeholder="Friend's name",
            key="request_name"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_money"
        )

        if st.button("Create request"):

            if person.strip() == "":
                st.error("Enter a name.")

            else:
                st.session_state.show_request = False

                st.success(
                    "Request of ₹{:,.0f} created.".format(amount)
                )

                st.rerun()

    # SNAPSHOT
    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    total_spent = spent()

    remaining = max(
        st.session_state.limit - total_spent,
        0
    )

    s1, s2 = st.columns(2)

    with s1:
        st.metric(
            "Spent",
            "₹{:,.0f}".format(total_spent)
        )

    with s2:
        st.metric(
            "Budget left",
            "₹{:,.0f}".format(remaining)
        )

    s3, s4 = st.columns(2)

    with s3:
        st.metric(
            "Saved",
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:
        score = 84

        if total_spent > st.session_state.limit:
            score = 58
        elif total_spent > st.session_state.limit * 0.8:
            score = 72

        st.metric(
            "VELORA Score",
            str(score) + " / 100"
        )

    # INTELLIGENCE
    ratio = total_spent / max(st.session_state.limit, 1)

    if ratio < 0.6:
        title = "You're on track."
        message = "Your current spending is comfortably below your monthly limit."

    elif ratio < 0.85:
        title = "Watch your spending pace."
        message = "You're getting closer to your monthly limit."

    else:
        title = "Budget attention required."
        message = "Your current spending could push you beyond your monthly limit."

    st.markdown(
        '<div class="intel">'
        '<div class="intel-label">VELORA INTELLIGENCE</div>'
        '<div class="intel-title">'
        + title +
        '</div>'
        '<div class="intel-text">'
        + message +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # SPENDING TREND
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
        '<div class="section">Active goal</div>',
        unsafe_allow_html=True
    )

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-name">'
        + st.session_state.goal_name +
        '</div>'
        '<div class="goal-money">₹'
        + format(st.session_state.goal_saved, ",.0f") +
        ' / ₹'
        + format(st.session_state.goal_target, ",.0f") +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(min(progress, 1.0))

    st.caption(
        "{:.0f}% complete".format(progress * 100)
    )

# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Pay")

    st.caption("Demo payment flow · No real transaction")

    st.markdown(
        '<div class="card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">•••• •••• •••• 2840</div>'
        '<div class="card-small">VIRTUAL DEMO CARD</div>'
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

    if st.button("Send payment"):

        if recipient.strip() == "":
            st.error("Enter recipient.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:
            st.session_state.balance -= amount

            add_transaction(
                "To " + recipient,
                category,
                -amount
            )

            st.success(
                "₹{:,.0f} payment simulated.".format(amount)
            )

            st.rerun()

# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.subheader("Activity")

    search = st.text_input(
        "Search",
        placeholder="Food, shopping, name..."
    )

    found = False

    for item in st.session_state.transactions:

        name = item[0]
        category = item[1]
        amount = item[2]

        searchable = (
            name + " " + category
        ).lower()

        if search.lower() not in searchable:
            continue

        found = True

        if amount >= 0:
            value = "+₹{:,.0f}".format(amount)
        else:
            value = "-₹{:,.0f}".format(abs(amount))

        st.markdown(
            '<div class="tx">'
            '<div class="tx-name">'
            + name +
            '</div>'
            '<div class="tx-category">'
            + category +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(value)

    if not found:
        st.info("No transactions found.")

# =========================================================
# INTELLIGENCE
# =========================================================

elif st.session_state.page == "Intel":

    st.subheader("Velora Intelligence")

    total = spent()
    ratio = total / max(st.session_state.limit, 1)

    if ratio < 0.6:
        title = "Healthy spending pattern"
        text = "Your spending is currently well below your monthly limit."

    elif ratio < 0.85:
        title = "Moderate spending"
        text = "You're approaching your planned monthly spending level."

    else:
        title = "High spending pressure"
        text = "Consider slowing discretionary spending to stay within your plan."

    st.markdown(
        '<div class="intel">'
        '<div class="intel-label">AI MONEY INSIGHT</div>'
        '<div class="intel-title">'
        + title +
        '</div>'
        '<div class="intel-text">'
        + text +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Category analysis")

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    for category in categories:

        value = category_spending(category)

        if value > 0:

            st.write(
                category +
                " — ₹{:,.0f}".format(value)
            )

            st.progress(
                min(value / max(total, 1), 1)
            )

    st.markdown("### Money health")

    st.metric(
        "VELORA Score",
        "84 / 100",
        "Good financial habits"
    )

# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.subheader("Profile")

    name = st.text_input(
        "Name",
        value="Tejal"
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100.0,
        value=float(st.session_state.limit),
        step=100.0
    )

    if st.button("Save settings"):

        st.session_state.limit = limit

        st.success("Settings saved.")

    st.markdown("### Velora Card")

    st.markdown(
        '<div class="card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">•••• •••• •••• 2840</div>'
        '<div class="card-small">DEMO VIRTUAL CARD</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.frozen:

        st.warning("Card is frozen.")

        if st.button("Unfreeze card"):
            st.session_state.frozen = False
            st.rerun()

    else:

        st.success("Card is active.")

        if st.button("Freeze card"):
            st.session_state.frozen = True
            st.rerun()

    st.info(
        "VELORA is a prototype. No real bank account, "
        "UPI or payment network is connected."
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "VELORA · Intelligent Money Management · Demo Mode"
)