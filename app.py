
import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Pocket Money", 2000),
        ("Food", -250),
        ("Study", -500),
        ("Shopping", -350),
        ("Gaming", -180)
    ]

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

# =========================
# DESIGN
# =========================

st.markdown("""
<style>

.stApp {
    background: #08090D;
}

.block-container {
    max-width: 520px;
    padding: 25px 18px 70px;
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

h1, h2, h3 {
    color: white !important;
}

.brand {
    font-size: 32px;
    font-weight: 900;
    color: white;
}

.sub {
    color: #858994;
    font-size: 12px;
    margin-bottom: 25px;
}

.balance {
    background: linear-gradient(
        135deg,
        #260B17,
        #711C3D,
        #A52B52
    );
    padding: 26px;
    border-radius: 26px;
    margin: 15px 0 25px;
}

.balance-label {
    color: #E0C6D0;
    font-size: 10px;
    letter-spacing: 2px;
}

.balance-number {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin: 5px 0;
}

.balance-note {
    color: #D7BBC5;
    font-size: 11px;
}

.box {
    background: #13151A;
    border: 1px solid #272A32;
    border-radius: 20px;
    padding: 18px;
    margin: 10px 0;
}

.big {
    color: white;
    font-size: 25px;
    font-weight: 800;
}

.small {
    color: #858994;
    font-size: 11px;
}

.card-ui {
    background: linear-gradient(
        135deg,
        #181A20,
        #41444D
    );
    border-radius: 25px;
    padding: 25px;
    border: 1px solid #4B4E58;
}

.card-number {
    color: white;
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 35px;
}

.stButton > button {
    background: #15171D !important;
    color: white !important;
    border: 1px solid #2A2D36 !important;
    border-radius: 14px !important;
    min-height: 45px !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

[data-testid="stMetric"] {
    background: #13151A;
    border: 1px solid #272A32;
    border-radius: 18px;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">Smart money, made simple.</div>',
    unsafe_allow_html=True
)

# =========================
# BALANCE
# =========================

st.markdown(
    f"""
    <div class="balance">
        <div class="balance-label">
            AVAILABLE BALANCE
        </div>

        <div class="balance-number">
            ₹{st.session_state.balance:,.0f}
        </div>

        <div class="balance-note">
            DEMO WALLET · NO REAL MONEY
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# QUICK ACTIONS
# =========================

st.subheader("Quick actions")

a, b, c = st.columns(3)

with a:
    add_money = st.button(
        "＋ Add",
        use_container_width=True
    )

with b:
    send_money = st.button(
        "↗ Send",
        use_container_width=True
    )

with c:
    card = st.button(
        "▣ Card",
        use_container_width=True
    )

# =========================
# ADD MONEY
# =========================

if add_money:

    st.markdown("### Add money")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money, gift..."
    )

    if st.button(
        "Confirm",
        use_container_width=True
    ):

        if source.strip() == "":
            source = "Added Money"

        st.session_state.balance += amount

        st.session_state.transactions.insert(
            0,
            (source, amount)
        )

        st.success(
            f"₹{amount:,.0f} added successfully."
        )

# =========================
# SEND MONEY
# =========================

if send_money:

    st.markdown("### Send money")

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

    if st.button(
        "Send",
        use_container_width=True
    ):

        if person.strip() == "":
            st.error("Enter recipient name.")

        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")

        else:

            st.session_state.balance -= amount

            st.session_state.transactions.insert(
                0,
                ("Sent to " + person, -amount)
            )

            st.success(
                f"₹{amount:,.0f} sent."
            )

# =========================
# VIRTUAL CARD
# =========================

if card:

    st.markdown("### Velora Card")

    st.markdown(
        """
        <div class="card-ui">

            <div class="small">
                VELORA · DEMO
            </div>

            <div style="
                font-size:28px;
                margin-top:22px;
            ">
                ▰
            </div>

            <div class="card-number">
                •••• •••• •••• 2840
            </div>

            <div class="small" style="
                margin-top:25px;
            ">
                VELORA MEMBER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Demo card · No real payments")

# =========================
# MONEY OVERVIEW
# =========================

st.subheader("Money overview")

total_spent = 0

for name, amount in st.session_state.transactions:

    if amount < 0:
        total_spent += abs(amount)

remaining = max(
    0,
    2000 - total_spent
)

x, y = st.columns(2)

with x:
    st.metric(
        "Spent",
        f"₹{total_spent:,.0f}"
    )

with y:
    st.metric(
        "Remaining",
        f"₹{remaining:,.0f}"
    )

# =========================
# SPENDING GRAPH
# =========================

st.subheader("Spending trend")

st.bar_chart(
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

# =========================
# SAVINGS GOAL
# =========================

st.subheader("Savings goal")

progress = (
    st.session_state.goal_saved /
    st.session_state.goal_target
)

st.markdown(
    f"""
    <div class="box">

        <div class="big">
            🎧 {st.session_state.goal_name}
        </div>

        <div class="small">
            ₹{st.session_state.goal_saved:,.0f}
            saved of
            ₹{st.session_state.goal_target:,.0f}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.progress(
    min(progress, 1.0)
)

st.caption(
    f"{progress * 100:.0f}% complete"
)

# =========================
# RECENT ACTIVITY
# =========================

st.subheader("Recent activity")

for name, amount in st.session_state.transactions[:5]:

    if amount >= 0:
        st.write(
            f"🟢 **{name}**  +₹{amount:,.0f}"
        )
    else:
        st.write(
            f"⚪ **{name}**  −₹{abs(amount):,.0f}"
        )

# =========================
# INSIGHT
# =========================

st.markdown("### ✦ Velora insight")

if total_spent > 1600:

    st.warning(
        "You're getting close to your monthly spending limit."
    )

else:

    st.success(
        "Your spending is currently under control."
    )

st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)