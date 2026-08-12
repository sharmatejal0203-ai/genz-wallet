import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================
# PREMIUM THEME
# =========================

st.markdown("""
<style>
.stApp {
    background-color: #08090D;
}

.block-container {
    max-width: 520px;
    padding: 25px 18px 70px;
}

h1, h2, h3 {
    color: white !important;
}

p, label {
    color: #A5A7B0 !important;
}

[data-testid="stMetric"] {
    background-color: #14161D;
    border: 1px solid #292C36;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: #9295A0 !important;
}

.stButton > button {
    background-color: #15171E !important;
    color: white !important;
    border: 1px solid #30333D !important;
    border-radius: 14px !important;
    min-height: 46px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

.stProgress > div > div > div > div {
    background-color: #A52B52;
}

[data-testid="stExpander"] {
    background-color: #12141A;
    border: 1px solid #292C36;
    border-radius: 16px;
}

hr {
    border-color: #292C36 !important;
}
</style>
""", unsafe_allow_html=True)


# =========================
# STARTING DATA
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000

if "card_frozen" not in st.session_state:
    st.session_state.card_frozen = False

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Pocket Money", "Income", 2000),
        ("Food", "Food", -250),
        ("Study", "Education", -500),
        ("Shopping", "Shopping", -350),
        ("Gaming", "Entertainment", -180)
    ]


# =========================
# HEADER
# =========================

st.title("VELORA")
st.caption("Smart money, made simple.")

st.caption("GOOD EVENING")
st.subheader("Welcome back 👋")


# =========================
# BALANCE
# =========================

st.subheader("Available balance")

st.metric(
    "VELORA WALLET",
    "₹{:,.0f}".format(st.session_state.balance)
)

st.caption("Demo wallet · No real money")


# =========================
# QUICK ACTIONS
# =========================

st.subheader("Quick actions")

a, b, c = st.columns(3)

with a:
    add_button = st.button(
        "＋ Add",
        use_container_width=True
    )

with b:
    send_button = st.button(
        "↗ Send",
        use_container_width=True
    )

with c:
    request_button = st.button(
        "⇄ Request",
        use_container_width=True
    )


# =========================
# ADD MONEY
# =========================

if add_button:

    st.subheader("Add money")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money / Gift / Other"
    )

    if st.button(
        "Confirm add",
        use_container_width=True
    ):

        if source.strip() == "":
            source = "Added Money"

        st.session_state.balance += amount

        st.session_state.transactions.insert(
            0,
            (source, "Income", amount)
        )

        st.success(
            "₹{:,.0f} added successfully.".format(amount)
        )


# =========================
# SEND MONEY
# =========================

if send_button:

    st.subheader("Send money")

    person = st.text_input(
        "Recipient",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Send amount",
        min_value=1,
        value=100,
        step=50
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
        "Confirm send",
        use_container_width=True
    ):

        if person.strip() == "":
            st.error("Enter recipient name.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= amount
            st.session_state.spent += amount

            st.session_state.transactions.insert(
                0,
                ("Sent to " + person, category, -amount)
            )

            st.success(
                "₹{:,.0f} sent.".format(amount)
            )


# =========================
# REQUEST MONEY
# =========================

if request_button:

    st.subheader("Request money")

    person = st.text_input(
        "Request from",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=200,
        step=50
    )

    reason = st.text_input(
        "Reason",
        placeholder="Lunch / Movie / Trip"
    )

    if st.button(
        "Create request",
        use_container_width=True
    ):

        if person.strip() == "":
            st.error("Enter a name.")

        else:
            st.success(
                "Request of ₹{:,.0f} created.".format(amount)
            )


# =========================
# MONEY OVERVIEW
# =========================

st.divider()

st.subheader("Money overview")

remaining = max(
    2000 - st.session_state.spent,
    0
)

a, b = st.columns(2)

with a:
    st.metric(
        "Spent",
        "₹{:,.0f}".format(st.session_state.spent)
    )

with b:
    st.metric(
        "Remaining",
        "₹{:,.0f}".format(remaining)
    )


# =========================
# VELORA SCORE
# =========================

st.subheader("VELORA Score")

st.metric(
    "Money health",
    "84 / 100",
    "Good habits"
)

st.caption(
    "Based on your spending and saving activity."
)


# =========================
# SPENDING TREND
# =========================

st.subheader("Spending trend")

chart_data = {
    "Monday": 120,
    "Tuesday": 180,
    "Wednesday": 90,
    "Thursday": 240,
    "Friday": 160,
    "Saturday": 280,
    "Sunday": 110
}

st.line_chart(chart_data)


# =========================
# SAVINGS GOAL
# =========================

st.subheader("Savings goal")

st.write(
    "🎧 " + st.session_state.goal_name
)

st.caption(
    "₹{:,.0f} saved of ₹{:,.0f}".format(
        st.session_state.goal_saved,
        st.session_state.goal_target
    )
)

progress = (
    st.session_state.goal_saved /
    st.session_state.goal_target
)

st.progress(min(progress, 1.0))

st.write(
    "{:.0f}% complete".format(progress * 100)
)


# =========================
# EDIT GOAL
# =========================

with st.expander("Edit savings goal"):

    new_name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    new_target = st.number_input(
        "Target amount",
        min_value=1,
        value=st.session_state.goal_target,
        step=100
    )

    new_saved = st.number_input(
        "Already saved",
        min_value=0,
        value=st.session_state.goal_saved,
        step=100
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal_name = new_name
        st.session_state.goal_target = new_target
        st.session_state.goal_saved = new_saved

        st.success("Goal updated.")


# =========================
# RECENT ACTIVITY
# =========================

st.subheader("Recent activity")

for name, category, amount in st.session_state.transactions[:6]:

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


# =========================
# VELORA INSIGHT
# =========================

st.subheader("✦ Velora insight")

if st.session_state.spent >= 1600:

    st.warning(
        "You're getting close to your monthly spending limit."
    )

else:

    st.success(
        "Your spending is currently within your planned limit."
    )


# =========================
# VIRTUAL CARD
# =========================

st.divider()

st.subheader("💳 Velora Card")

st.info(
    "VELORA · DEMO CARD\n\n"
    "••••  ••••  ••••  2840\n\n"
    "VELORA MEMBER"
)

if st.session_state.card_frozen:

    st.warning("🔒 Card is frozen.")

    if st.button(
        "Unfreeze card",
        use_container_width=True
    ):

        st.session_state.card_frozen = False
        st.rerun()

else:

    st.success("🟢 Card is active.")

    if st.button(
        "Freeze card",
        use_container_width=True
    ):

        st.session_state.card_frozen = True
        st.rerun()

st.caption("Demo card · No real payments")


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)