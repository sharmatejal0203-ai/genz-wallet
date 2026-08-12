import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳"
)

# ---------------- DATA ----------------

 "balance" not in st.session_state:
    st.session_state.balance = 5000

"transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", 2000],
        ["Food", -250],
        ["Study", -500],
        ["Shopping", -350],
        ["Gaming", -180],
    ]

# ---------------- HEADER ----------------

st.title("VELORA")
st.caption("Smart money, made simple.")

# ---------------- BALANCE ----------------

st.subheader("Available Balance")

st.markdown(
    "## ₹{:,.0f}".format(
        st.session_state.balance
    )
)

st.info("DEMO WALLET · No real money")

# ---------------- QUICK ACTIONS ----------------

st.subheader("Quick Actions")

add = st.button("➕ Add Money")
send = st.button("↗ Send Money")

# ---------------- ADD MONEY ----------------

if add:

    amount = st.number_input(
        "Enter amount",
        min_value=1,
        value=500
    )

    if st.button("Confirm Add"):

        st.session_state.balance += amount

        st.session_state.transactions.insert(
            0,
            ["Added Money", amount]
        )

        st.success(
            "₹{:,.0f} added!".format(amount)
        )

# ---------------- SEND MONEY ----------------

if send:

    person = st.text_input(
        "Send to"
    )

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=100
    )

    if st.button("Confirm Send"):

        if person == "":
            st.error("Enter a name.")

        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")

        else:

            st.session_state.balance -= amount

            st.session_state.transactions.insert(
                0,
                ["Sent to " + person, -amount]
            )

            st.success(
                "₹{:,.0f} sent!".format(amount)
            )

# ---------------- OVERVIEW ----------------

st.subheader("Money Overview")

spent = 0

for transaction in st.session_state.transactions:

    if transaction[1] < 0:
        spent += abs(transaction[1])

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Spent",
        "₹{:,.0f}".format(spent)
    )

with col2:
    st.metric(
        "Balance",
        "₹{:,.0f}".format(
            st.session_state.balance
        )
    )

# ---------------- GOAL ----------------

st.subheader("Savings Goal")

goal = 3400
target = 5000

st.write("🎧 New Headphones")

st.progress(
    goal / target
)

st.caption(
    "₹{:,.0f} saved of ₹{:,.0f}".format(
        goal,
        target
    )
)

# ---------------- SPENDING ----------------

st.subheader("Weekly Spending")

st.bar_chart(
    {
        "Monday": 120,
        "Tuesday": 180,
        "Wednesday": 90,
        "Thursday": 240,
        "Friday": 160,
        "Saturday": 280,
        "Sunday": 110
    }
)

# ---------------- ACTIVITY ----------------

st.subheader("Recent Activity")

for name, amount in st.session_state.transactions:

    if amount >= 0:
        st.write(
            "🟢 {}   +₹{:,.0f}".format(
                name,
                amount
            )
        )

    else:
        st.write(
            "⚪ {}   -₹{:,.0f}".format(
                name,
                abs(amount)
            )
        )

st.divider()

st.caption(
    "VELORA · Demo Prototype"
)