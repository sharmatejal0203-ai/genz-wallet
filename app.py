import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# -----------------------------
# SESSION DATA
# -----------------------------

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0]
    ]

# -----------------------------
# FUNCTIONS
# -----------------------------

def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )

# -----------------------------
# HEADER
# -----------------------------

st.title("VELORA")
st.caption("INTELLIGENT MONEY MANAGEMENT")

st.divider()

st.subheader("Good evening, Tejal 👋")

# -----------------------------
# BALANCE
# -----------------------------

st.metric(
    "Available Balance",
    f"₹{st.session_state.balance:,.0f}"
)

st.caption("Demo wallet • No real money connected")

st.divider()

# -----------------------------
# QUICK ACTIONS
# -----------------------------

st.subheader("Quick Actions")

add_tab, send_tab = st.tabs(
    ["＋ Add Money", "↗ Send Money"]
)

# -----------------------------
# ADD MONEY
# -----------------------------

with add_tab:

    amount = st.number_input(
        "Amount to add",
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
        "Add Money",
        use_container_width=True,
        key="add_money_button"
    ):

        st.session_state.balance += amount

        add_transaction(
            source,
            "Income",
            amount
        )

        st.success(
            f"₹{amount:,.0f} added successfully."
        )

# -----------------------------
# SEND MONEY
# -----------------------------

with send_tab:

    recipient = st.text_input(
        "Recipient",
        placeholder="Enter name",
        key="recipient"
    )

    send_amount = st.number_input(
        "Amount to send",
        min_value=1.0,
        value=100.0,
        step=50.0,
        key="send_amount"
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Shopping",
            "Education",
            "Entertainment",
            "Travel",
            "Other"
        ],
        key="send_category"
    )

    if st.button(
        "Send Money",
        use_container_width=True,
        key="send_money_button"
    ):

        if recipient.strip() == "":
            st.error("Please enter recipient name.")

        elif send_amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= send_amount

            add_transaction(
                f"Sent to {recipient}",
                category,
                -send_amount
            )

            st.success(
                f"₹{send_amount:,.0f} sent to {recipient}."
            )

# -----------------------------
# ACTIVITY
# -----------------------------

st.divider()

st.subheader("Recent Activity")

for transaction in st.session_state.transactions:

    name = transaction[0]
    category = transaction[1]
    amount = transaction[2]

    if amount >= 0:

        st.write(
            f"🟢 **{name}**  •  {category}  "
            f"**+₹{amount:,.0f}**"
        )

    else:

        st.write(
            f"🔴 **{name}**  •  {category}  "
            f"**-₹{abs(amount):,.0f}**"
        )