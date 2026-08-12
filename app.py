import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# ---------- DATA ----------

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

# ---------- STYLE ----------

st.markdown("""
<style>
.stApp {
    background-color: #08090D;
}

.block-container {
    max-width: 520px;
    padding-top: 30px;
}

h1, h2, h3, p, label {
    color: white;
}

.brand {
    font-size: 32px;
    font-weight: 800;
    color: white;
}

.subtitle {
    color: #888B95;
    font-size: 13px;
}

.balance {
    background: linear-gradient(135deg, #32101E, #8C2348);
    padding: 25px;
    border-radius: 25px;
    margin-top: 25px;
}

.balance-label {
    color: #D8C2CA;
    font-size: 11px;
    letter-spacing: 2px;
}

.balance-number {
    color: white;
    font-size: 42px;
    font-weight: 800;
}

.info-box {
    background: #14161C;
    border: 1px solid #292C34;
    border-radius: 18px;
    padding: 18px;
    margin-top: 12px;
}

.small {
    color: #888B95;
    font-size: 12px;
}

.big {
    color: white;
    font-size: 24px;
    font-weight: 700;
}

.stButton button {
    border-radius: 14px;
    min-height: 45px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart money, made simple.</div>',
    unsafe_allow_html=True
)

# ---------- BALANCE ----------

st.markdown(
    f"""
    <div class="balance">
        <div class="balance-label">AVAILABLE BALANCE</div>
        <div class="balance-number">
            ₹{st.session_state.balance:,.0f}
        </div>
        <div class="small">
            DEMO WALLET · NO REAL MONEY
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- QUICK ACTIONS ----------

st.subheader("Quick actions")

col1, col2, col3 = st.columns(3)

with col1:
    add = st.button("＋ Add", use_container_width=True)

with col2:
    send = st.button("↗ Send", use_container_width=True)

with col3:
    card = st.button("▣ Card", use_container_width=True)

# ---------- ADD ----------

if add:

    st.subheader("Add money")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money"
    )

    if st.button("Add to wallet", use_container_width=True):

        st.session_state.balance += amount

        st.success(
            "₹{:,.0f} added!".format(amount)
        )

# ---------- SEND ----------

if send:

    st.subheader("Send money")

    person = st.text_input(
        "Recipient",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=100
    )

    if st.button("Send", use_container_width=True):

        if amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        elif person == "":
            st.error("Enter recipient name.")

        else:
            st.session_state.balance -= amount
            st.session_state.spent += amount

            st.success(
                "₹{:,.0f} sent to {}.".format(
                    amount,
                    person
                )
            )

# ---------- CARD ----------

if card:

    st.subheader("Velora Card")

    st.markdown(
        """
        <div class="info-box">
            <div class="small">VELORA · DEMO</div>
            <br>
            <div style="font-size:28px;">▰</div>
            <br>
            <div class="big">
                •••• •••• •••• 2840
            </div>
            <br>
            <div class="small">
                VELORA MEMBER
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- OVERVIEW ----------

st.subheader("Money overview")

remaining = max(
    2000 - st.session_state.spent,
    0
)

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Spent",
        "₹{:,.0f}".format(
            st.session_state.spent
        )
    )

with c2:
    st.metric(
        "Remaining",
        "₹{:,.0f}".format(
            remaining
        )
    )

# ---------- GRAPH ----------

st.subheader("Spending trend")

st.line_chart(
    {
        "Mon": 120,
        "Tue": 180,
        "Wed": 90,
        "Thu": 240,
        "Fri": 160,
        "Sat": 280,
        "Sun": 110
    }
)

# ---------- GOAL ----------

st.subheader("Savings goal")

target = 5000
progress = st.session_state.goal_saved / target

st.markdown(
    """
    <div class="info-box">
        <div class="big">🎧 New Headphones</div>
        <div class="small">
            ₹3,400 saved of ₹5,000
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.progress(progress)

st.caption(
    "{:.0f}% complete".format(progress * 100)
)

# ---------- INSIGHT ----------

st.subheader("✦ Velora insight")

if st.session_state.spent > 1600:

    st.warning(
        "You're getting close to your monthly limit."
    )

else:

    st.success(
        "Your spending is currently under control."
    )

# ---------- FOOTER ----------

st.divider()

st.caption(
    "VELORA · Demo Prototype"
)