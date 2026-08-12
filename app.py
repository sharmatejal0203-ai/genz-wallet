import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================================================
# VELORA — COMPLETE DEMO APP
# =========================================================

st.markdown("""
<style>
.stApp {
    background: #08090D;
}

.block-container {
    max-width: 540px;
    padding: 24px 18px 80px;
}

h1, h2, h3 {
    color: #FFFFFF !important;
}

p, label {
    color: #A6A8B2 !important;
}

[data-testid="stMetric"] {
    background: #14161D;
    border: 1px solid #292C36;
    border-radius: 18px;
    padding: 14px;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #8E919B !important;
}

.stButton > button {
    background: #15171E !important;
    color: #FFFFFF !important;
    border: 1px solid #30333D !important;
    border-radius: 14px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

.stProgress > div > div > div > div {
    background: #A52B52;
}

[data-testid="stExpander"] {
    background: #12141A;
    border: 1px solid #292C36;
    border-radius: 16px;
}

hr {
    border-color: #292C36 !important;
}

.small-card {
    background: #14161D;
    border: 1px solid #292C36;
    border-radius: 18px;
    padding: 16px;
    margin: 8px 0;
}

.hero {
    background: linear-gradient(135deg, #35101D, #7E2040);
    border-radius: 24px;
    padding: 24px;
    margin: 15px 0;
}

.hero-title {
    color: #D8C3CB;
    font-size: 11px;
    letter-spacing: 2px;
}

.hero-money {
    color: white;
    font-size: 40px;
    font-weight: 900;
    margin: 5px 0;
}

.hero-note {
    color: #D9C5CC;
    font-size: 11px;
}

.card-ui {
    background: linear-gradient(135deg, #1C1E25, #353844);
    border: 1px solid #464955;
    border-radius: 24px;
    padding: 25px;
    min-height: 180px;
    margin: 12px 0;
}

.card-brand {
    color: white;
    font-weight: 800;
    letter-spacing: 2px;
}

.card-number {
    color: white;
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 35px;
}

.card-footer {
    color: #B1B3BB;
    font-size: 10px;
    margin-top: 25px;
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
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def category_total(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


# =========================================================
# HEADER
# =========================================================

st.title("VELORA")
st.caption("Smart money, made simple.")


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("⌂", use_container_width=True):
        go("Home")

with n2:
    if st.button("💳", use_container_width=True):
        go("Card")

with n3:
    if st.button("🎯", use_container_width=True):
        go("Goals")

with n4:
    if st.button("🔔", use_container_width=True):
        go("Notifications")

with n5:
    if st.button("◉", use_container_width=True):
        go("Profile")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader(
        "Welcome back, " +
        st.session_state.name +
        " 👋"
    )

    # HERO
    st.markdown(
        '<div class="hero">'
        '<div class="hero-title">AVAILABLE BALANCE</div>'
        '<div class="hero-money">₹'
        + "{:,.0f}".format(st.session_state.balance)
        + '</div>'
        '<div class="hero-note">'
        'DEMO WALLET · NO REAL MONEY'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # QUICK ACTIONS
    st.subheader("Quick actions")

    a, b, c, d = st.columns(4)

    with a:
        add = st.button("＋", use_container_width=True)

    with b:
        send = st.button("↗", use_container_width=True)

    with c:
        request = st.button("⇄", use_container_width=True)

    with d:
        activity = st.button("☷", use_container_width=True)

    st.caption("Add        Send       Request     Activity")

    # ADD
    if add:

        st.write("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0
        )

        source = st.text_input(
            "Source",
            placeholder="Pocket money / Gift / Other"
        )

        st.write("Quick amount")

        q1, q2, q3 = st.columns(3)

        with q1:
            q100 = st.button("₹100")

        with q2:
            q250 = st.button("₹250")

        with q3:
            q500 = st.button("₹500")

        if q100:
            amount = 100

        if q250:
            amount = 250

        if q500:
            amount = 500

        if st.button(
            "Add to wallet",
            use_container_width=True
        ):

            if source.strip() == "":
                source = "Pocket Money"

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

            st.success("Money added successfully.")

    # SEND
    if send:

        st.write("### Send money")

        person = st.text_input(
            "Recipient",
            placeholder="Friend's name"
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
            "Send money",
            use_container_width=True
        ):

            if person.strip() == "":
                st.error("Enter recipient.")

            elif amount > st.session_state.balance:
                st.error("Insufficient demo balance.")

            else:

                st.session_state.balance -= amount

                add_transaction(
                    "Sent to " + person,
                    category,
                    -amount
                )

                st.session_state.notifications.insert(
                    0,
                    "₹{:,.0f} sent.".format(amount)
                )

                st.success("Payment simulated.")

    # REQUEST
    if request:

        st.write("### Request money")

        person = st.text_input(
            "Request from",
            placeholder="Friend's name"
        )

        amount = st.number_input(
            "Request amount",
            min_value=1.0,
            value=200.0,
            step=50.0
        )

        reason = st.text_input(
            "Reason",
            placeholder="Lunch / Trip / Movie"
        )

        if st.button(
            "Create request",
            use_container_width=True
        ):

            if person.strip() == "":
                st.error("Enter a name.")

            else:

                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} created.".format(amount)
                )

                st.success("Request created.")

    # ACTIVITY
    if activity:
        go("Activity")

    # OVERVIEW
    st.divider()

    st.subheader("Money overview")

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
            "Remaining",
            "₹{:,.0f}".format(remaining)
        )

    # SCORE
    st.subheader("VELORA Score")

    score = 84

    if spent > st.session_state.monthly_limit:
        score = 62

    elif spent > st.session_state.monthly_limit * 0.8:
        score = 74

    st.metric(
        "Money health",
        str(score) + " / 100",
        "Good habits"
    )

    # STREAK
    st.subheader("🔥 Saving streak")

    st.metric(
        "Current streak",
        str(st.session_state.streak) + " days"
    )

    st.caption(
        "Keep building consistent money habits."
    )

    # GRAPH
    st.subheader("Spending trend")

    chart = pd.DataFrame({
        "Spending": [
            120,
            180,
            90,
            240,
            160,
            280,
            110
        ]
    }, index=[
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ])

    st.line_chart(chart)

    # CATEGORY
    st.subheader("Where your money goes")

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    category_data = {}

    for category in categories:

        value = category_total(category)

        if value > 0:
            category_data[category] = value

            st.write(
                "{} — ₹{:,.0f}".format(
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

    # GOAL
    st.subheader("Savings goal")

    st.write(
        "🎧 " + st.session_state.goal_name
    )

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.caption(
        "₹{:,.0f} saved of ₹{:,.0f}".format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        )
    )

    st.progress(min(progress, 1.0))

    st.write(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    # INSIGHT
    st.subheader("✦ Velora Insight")

    if category_data:

        biggest = max(
            category_data,
            key=category_data.get
        )

        st.info(
            "{} is currently your biggest spending category.".format(
                biggest
            )
        )

    if spent < st.session_state.monthly_limit * 0.8:

        st.success(
            "You're currently within your planned budget."
        )

    else:

        st.warning(
            "You're getting close to your monthly budget."
        )


# =========================================================
# CARD
# =========================================================

elif st.session_state.page == "Card":

    st.subheader("💳 Velora Card")

    st.markdown(
        '<div class="card-ui">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-footer">'
        'VELORA MEMBER · DEMO CARD'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.warning("🔒 CARD FROZEN")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("🟢 CARD ACTIVE")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = True
            st.rerun()

    st.caption(
        "Prototype card · No real payments"
    )


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.subheader("🎯 Savings Goals")

    st.caption(
        "Plan something you want instead of spending randomly."
    )

    name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    target = st.number_input(
        "Target amount",
        min_value=1.0,
        value=float(st.session_state.goal_target),
        step=100.0
    )

    saved = st.number_input(
        "Already saved",
        min_value=0.0,
        value=float(st.session_state.goal_saved),
        step=100.0
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal_name = name
        st.session_state.goal_target = target
        st.session_state.goal_saved = saved

        st.success("Goal updated.")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.write(
        "🎯 " + st.session_state.goal_name
    )

    st.progress(min(progress, 1.0))

    st.write(
        "₹{:,.0f} / ₹{:,.0f}".format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        )
    )

    st.caption(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    st.divider()

    st.write("### Add to goal")

    contribution = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0
    )

    if st.button(
        "Add savings",
        use_container_width=True
    ):

        if contribution <= st.session_state.balance:

            st.session_state.balance -= contribution

            st.session_state.goal_saved += contribution

            add_transaction(
                "Savings Goal",
                "Savings",
                -contribution
            )

            st.success(
                "₹{:,.0f} moved to your goal.".format(
                    contribution
                )
            )

        else:

            st.error(
                "Not enough demo balance."
            )


# =========================================================
# NOTIFICATIONS
# =========================================================

elif st.session_state.page == "Notifications":

    st.subheader("🔔 Notifications")

    if not st.session_state.notifications:

        st.info(
            "No new notifications."
        )

    else:

        for notification in st.session_state.notifications:

            st.write(
                "• " + notification
            )

    if st.session_state.notifications:

        if st.button(
            "Clear notifications",
            use_container_width=True
        ):

            st.session_state.notifications = []

            st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.subheader("☷ Activity")

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, friend..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        text = (
            name + " " + category
        ).lower()

        if search.lower() not in text:
            continue

        found = True

        if amount >= 0:

            st.write(
                "🟢 {}   +₹{:,.0f}".format(
                    name,
                    amount
                )
            )

        else:

            st.write(
                "⚪ {}   −₹{:,.0f}".format(
                    name,
                    abs(amount)
                )
            )

        st.caption(category)

    if not found:

        st.info(
            "No matching transactions."
        )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.subheader("◉ Profile")

    name = st.text_input(
        "Your name",
        value=st.session_state.name
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100.0,
        value=float(st.session_state.monthly_limit),
        step=100.0
    )

    if st.button(
        "Save profile",
        use_container_width=True
    ):

        st.session_state.name = name
        st.session_state.monthly_limit = limit

        st.success(
            "Profile updated."
        )

    st.divider()

    st.write("### Demo settings")

    st.info(
        "VELORA is a prototype. "
        "No real bank account or payment is connected."
    )

    st.write(
        "Version 2.0"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)