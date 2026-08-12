import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# ---------------- DATA ----------------

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Pocket Money", "Income", 2000),
        ("Food", "Food", -250),
        ("Study", "Education", -500),
        ("Shopping", "Shopping", -350),
        ("Gaming", "Entertainment", -180)
    ]

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000


# ---------------- HEADER ----------------

st.title("VELORA")
st.caption("Smart money, made simple.")

st.write("GOOD EVENING")
st.subheader("Welcome back 👋")


# ---------------- BALANCE ----------------

st.subheader("Available balance")

st.metric(
    "VELORA WALLET",
    "₹{:,.0f}".format(st.session_state.balance)
)

st.caption("Demo wallet · No real money")


# ---------------- QUICK ACTIONS ----------------

st.subheader("Quick actions")

col1, col2, col3 = st.columns(3)

with col1:
    add_money = st.button(
        "＋ Add",
        use_container_width=True
    )

with col2:
    send_money = st.button(
        "↗ Send",
        use_container_width=True
    )

with col3:
    request_money = st.button(
        "⇄ Request",
        use_container_width=True
    )


# ---------------- ADD MONEY ----------------

if add_money:

    st.subheader("Add money")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Where is it from?",
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


# ---------------- SEND MONEY ----------------

if send_money:

    st.subheader("Send money")

    person = st.text_input(
        "Send to",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Amount",
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
                "₹{:,.0f} sent to {}.".format(
                    amount,
                    person
                )
            )


# ---------------- REQUEST MONEY ----------------

if request_money:

    st.subheader("Request money")

    person = st.text_input(
        "Request from",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Request amount",
        min_value=1,
        value=200,
        step=50
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
            st.success(
                "₹{:,.0f} request created for {}.".format(
                    amount,
                    person
                )
            )


# ---------------- OVERVIEW ----------------

st.divider()

st.subheader("Money overview")

remaining = max(
    2000 - st.session_state.spent,
    0
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Spent this month",
        "₹{:,.0f}".format(
            st.session_state.spent
        )
    )

with col2:
    st.metric(
        "Budget remaining",
        "₹{:,.0f}".format(
            remaining
        )
    )


# ---------------- SCORE ----------------

st.subheader("VELORA Score")

st.metric(
    "Money health",
    "84 / 100",
    "Good habits"
)

st.caption(
    "Based on your spending and saving activity."
)


# ---------------- GRAPH ----------------

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


# ---------------- GOAL ----------------

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

goal_progress = (
    st.session_state.goal_saved /
    st.session_state.goal_target
)

st.progress(
    min(goal_progress, 1.0)
)

st.write(
    "{:.0f}% complete".format(
        goal_progress * 100
    )
)


# ---------------- GOAL EDIT ----------------

with st.expander("Edit savings goal"):

    new_name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    new_target = st.number_input(
        "Target",
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


# ---------------- ACTIVITY ----------------

st.subheader("Recent activity")

for name, category, amount in st.session_state.transactions[:6]:

    if amount >= 0:

        st.write(
            "🟢 **{}**  +₹{:,.0f}".format(
                name,
                amount
            )
        )

        st.caption(category)

    else:

        st.write(
            "⚪ **{}**  −₹{:,.0f}".format(
                name,
                abs(amount)
            )
        )

        st.caption(category)


# ---------------- INSIGHT ----------------

st.subheader("✦ Velora insight")

if st.session_state.spent >= 1600:

    st.warning(
        "You're getting close to your monthly spending limit."
    )

else:

    st.success(
        "Your spending is currently within your planned limit."
    )


# ---------------- DEMO CARD ----------------

st.divider()

st.subheader("💳 Velora Card")

st.info(
    "••••  ••••  ••••  2840\n\n"
    "VELORA MEMBER · DEMO CARD"
)

st.caption(
    "Prototype only · No real payments"
)


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "VELORA · Smart Money Prototype"
)