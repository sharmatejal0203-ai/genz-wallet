import streamlit as st

# ==============================
# VELORA
# ==============================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# ==============================
# SESSION DATA
# ==============================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350]
    ]

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ==============================
# STYLE
# ==============================

st.markdown("""
<style>

.stApp {
    background: #08090c;
}

.block-container {
    max-width: 480px;
    padding: 25px 18px 80px;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Brand */

.brand {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
}

.tagline {
    color: #777b86;
    font-size: 12px;
    margin-bottom: 25px;
}

/* Balance */

.balance {
    background: linear-gradient(135deg, #401323, #8d2143);
    padding: 27px;
    border-radius: 26px;
    margin: 20px 0;
}

.balance-title {
    color: #d9bdc7;
    font-size: 10px;
    letter-spacing: 2px;
}

.balance-value {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin: 6px 0;
}

.balance-sub {
    color: #d8c5cb;
    font-size: 11px;
}

/* Cards */

.card {
    background: #13151a;
    border: 1px solid #252831;
    border-radius: 20px;
    padding: 18px;
    margin: 12px 0;
}

.section {
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* Buttons */

.stButton > button {
    background: #15171c !important;
    color: white !important;
    border: 1px solid #292c35 !important;
    border-radius: 14px !important;
    height: 45px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    border-color: #a52a50 !important;
}

/* Inputs */

input {
    background: #13151a !important;
    color: white !important;
}

/* Metric */

[data-testid="stMetric"] {
    background: #13151a;
    border: 1px solid #252831;
    border-radius: 18px;
    padding: 14px;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

/* Progress */

.stProgress > div > div > div > div {
    background: #a52a50;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">A smarter way to manage your money.</div>',
    unsafe_allow_html=True
)


# ==============================
# HOME
# ==============================

if st.session_state.page == "Home":

    st.caption("GOOD AFTERNOON")

    # Balance

    st.markdown(
        '<div class="balance">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="balance-title">AVAILABLE BALANCE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="balance-value">₹{st.session_state.balance:,.0f}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="balance-sub">DEMO WALLET • No real money</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Quick actions

    st.markdown(
        '<div class="section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("＋", use_container_width=True):
            st.session_state.page = "Add"
            st.rerun()
        st.caption("Add")

    with c2:
        if st.button("↗", use_container_width=True):
            st.session_state.page = "Send"
            st.rerun()
        st.caption("Send")

    with c3:
        if st.button("⇄", use_container_width=True):
            st.session_state.page = "Request"
            st.rerun()
        st.caption("Request")

    with c4:
        if st.button("⌁", use_container_width=True):
            st.session_state.page = "Activity"
            st.rerun()
        st.caption("Activity")


    # Overview

    st.markdown(
        '<div class="section">MONEY OVERVIEW</div>',
        unsafe_allow_html=True
    )

    spent = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            spent += abs(item[2])

    remaining = max(0, 2000 - spent)

    a, b = st.columns(2)

    with a:
        st.metric("Spent", f"₹{spent:,.0f}")

    with b:
        st.metric("Remaining", f"₹{remaining:,.0f}")


    # Chart

    st.markdown(
        '<div class="section">WEEKLY SPENDING</div>',
        unsafe_allow_html=True
    )

    chart = {
        "Mon": 120,
        "Tue": 180,
        "Wed": 90,
        "Thu": 240,
        "Fri": 160,
        "Sat": 280,
        "Sun": 110
    }

    st.line_chart(chart, height=220)


    # Monthly limit

    st.markdown(
        '<div class="section">MONTHLY LIMIT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write("Monthly spending")

    st.markdown(
        f"### ₹{spent:,.0f} / ₹2,000"
    )

    progress = min(spent / 2000, 1)

    st.progress(progress)

    st.caption(
        f"{progress * 100:.0f}% of your monthly limit used"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Savings

    st.markdown(
        '<div class="section">SAVINGS GOAL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write("**New Headphones**")

    st.caption("₹3,400 saved of ₹5,000")

    st.progress(0.68)

    st.caption("68% complete")

    st.markdown("</div>", unsafe_allow_html=True)


    # Recent activity

    st.markdown(
        '<div class="section">RECENT ACTIVITY</div>',
        unsafe_allow_html=True
    )

    for name, category, amount in st.session_state.transactions[:5]:

        left, right = st.columns([3, 1])

        with left:
            st.write(f"**{name}**")
            st.caption(category)

        with right:

            if amount >= 0:
                st.write(f"**+₹{amount:,.0f}**")
            else:
                st.write(f"**−₹{abs(amount):,.0f}**")

        st.divider()


    # Insight

    if spent < 1000:

        st.success(
            "VELORA INSIGHT  ·  You're comfortably within your spending limit."
        )

    elif spent < 1600:

        st.info(
            "VELORA INSIGHT  ·  Your spending is on track."
        )

    else:

        st.warning(
            "VELORA INSIGHT  ·  You're getting close to your limit."
        )


# ==============================
# ADD MONEY
# ==============================

elif st.session_state.page == "Add":

    st.header("Add money")

    st.caption("Update your demo wallet.")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money, gift, etc."
    )

    if st.button(
        "Add money",
        use_container_width=True
    ):

        if source == "":
            st.error("Please enter the source.")

        else:

            st.session_state.balance += amount

            st.session_state.transactions.insert(
                0,
                [source, "Income", amount]
            )

            st.success(
                f"₹{amount:,.0f} added successfully."
            )

            st.session_state.page = "Home"

            st.rerun()


    if st.button(
        "← Back",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


# ==============================
# SEND MONEY
# ==============================

elif st.session_state.page == "Send":

    st.header("Send money")

    st.caption("Simulated transfer for your demo.")

    person = st.text_input(
        "Recipient",
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
        "Send money",
        use_container_width=True
    ):

        if person == "":
            st.error("Enter recipient name.")

        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")

        else:

            st.session_state.balance -= amount

            st.session_state.transactions.insert(
                0,
                [
                    f"Sent to {person}",
                    category,
                    -amount
                ]
            )

            st.success("Transfer completed.")

            st.session_state.page = "Home"

            st.rerun()


    if st.button(
        "← Back",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


# ==============================
# REQUEST MONEY
# ==============================

elif st.session_state.page == "Request":

    st.header("Request money")

    st.caption("Create a simulated payment request.")

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
        placeholder="Movie, food, trip..."
    )

    if st.button(
        "Create request",
        use_container_width=True
    ):

        if person == "":
            st.error("Enter a name.")

        else:
            st.success(
                f"₹{amount:,.0f} request created for {person}."
            )


    if st.button(
        "← Back",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


# ==============================
# ACTIVITY
# ==============================

elif st.session_state.page == "Activity":

    st.header("Activity")

    st.caption("Your complete demo wallet history.")

    for name, category, amount in st.session_state.transactions:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        left, right = st.columns([3, 1])

        with left:

            st.write(f"**{name}**")
            st.caption(category)

        with right:

            if amount >= 0:

                st.markdown(
                    f'<div style="color:#63d395;'
                    f'font-weight:700;text-align:right;">'
                    f'+₹{amount:,.0f}</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f'<div style="color:white;'
                    f'font-weight:700;text-align:right;">'
                    f'−₹{abs(amount):,.0f}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)


    if st.button(
        "← Back",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


# ==============================
# BOTTOM NAVIGATION
# ==============================

st.divider()

n1, n2, n3 = st.columns(3)

with n1:

    if st.button(
        "⌂  Home",
        use_container_width=True
    ):

        st.session_state.page = "Home"
        st.rerun()

with n2:

    if st.button(
        "↕  Activity",
        use_container_width=True
    ):

        st.session_state.page = "Activity"
        st.rerun()

with n3:

    if st.button(
        "⚙  Settings",
        use_container_width=True
    ):

        st.info(
            "VELORA Demo · Personal finance prototype"
        )