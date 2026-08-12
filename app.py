import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================
# DATA
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Pocket Money", 2000),
        ("Food", -250),
        ("Study", -500),
        ("Shopping", -350),
        ("Gaming", -180)
    ]


# =========================
# STYLE
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

.brand {
    color: white;
    font-size: 32px;
    font-weight: 900;
    letter-spacing: -1px;
}

.tagline {
    color: #858994;
    font-size: 12px;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(
        135deg,
        #280B18,
        #721D3E,
        #A62C52
    );
    border-radius: 26px;
    padding: 25px;
    margin: 15px 0 25px;
}

.hero-label {
    color: #DCC5CD;
    font-size: 10px;
    letter-spacing: 2px;
}

.hero-money {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin: 5px 0;
}

.hero-note {
    color: #D8BBC5;
    font-size: 10px;
}

.section {
    color: white;
    font-size: 14px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 12px;
}

.app-card {
    background: #13151A;
    border: 1px solid #292C35;
    border-radius: 20px;
    padding: 18px;
    margin: 8px 0;
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

.score {
    color: white;
    font-size: 34px;
    font-weight: 900;
}

.score-good {
    color: #A7E8C2;
    font-size: 11px;
    margin-bottom: 5px;
}

.goal-title {
    color: white;
    font-size: 16px;
    font-weight: 800;
}

.goal-money {
    color: #858994;
    font-size: 11px;
    margin-top: 4px;
}

.virtual-card {
    background: linear-gradient(
        135deg,
        #17191F,
        #3D4049
    );
    border: 1px solid #4A4D57;
    border-radius: 24px;
    padding: 24px;
    min-height: 155px;
}

.card-top {
    color: #B2B4BB;
    font-size: 10px;
    letter-spacing: 2px;
}

.card-chip {
    color: #D5D6DA;
    font-size: 25px;
    margin-top: 22px;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 15px;
}

.card-bottom {
    color: #A5A7AE;
    font-size: 9px;
    margin-top: 20px;
}

.stButton > button {
    background: #15171D !important;
    color: white !important;
    border: 1px solid #292C35 !important;
    border-radius: 14px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

[data-testid="stMetric"] {
    background: #13151A;
    border: 1px solid #292C35;
    border-radius: 18px;
}

[data-testid="stMetricLabel"] {
    color: #858994 !important;
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
    '<div class="tagline">Smart money, made simple.</div>',
    unsafe_allow_html=True
)

st.caption("GOOD EVENING")

st.markdown("### Welcome back 👋")


# =========================
# BALANCE
# =========================

st.markdown(
    f"""
    <div class="hero">

        <div class="hero-label">
            AVAILABLE BALANCE
        </div>

        <div class="hero-money">
            ₹{st.session_state.balance:,.0f}
        </div>

        <div class="hero-note">
            DEMO WALLET · NO REAL MONEY
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# QUICK ACTIONS
# =========================

st.markdown(
    '<div class="section">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    add_button = st.button(
        "＋ Add",
        use_container_width=True
    )

with col2:
    send_button = st.button(
        "↗ Send",
        use_container_width=True
    )

with col3:
    card_button = st.button(
        "▣ Card",
        use_container_width=True
    )


# =========================
# ADD MONEY
# =========================

if add_button:

    st.markdown(
        '<div class="section">ADD MONEY</div>',
        unsafe_allow_html=True
    )

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
        "Add to wallet",
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
            f"₹{amount:,.0f} added!"
        )


# =========================
# SEND MONEY
# =========================

if send_button:

    st.markdown(
        '<div class="section">SEND MONEY</div>',
        unsafe_allow_html=True
    )

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
        "Send money",
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
                ("Sent to " + person, -amount)
            )

            st.success(
                f"₹{amount:,.0f} sent!"
            )


# =========================
# VELORA CARD
# =========================

if card_button:

    st.markdown(
        '<div class="section">VELORA CARD</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="virtual-card">

            <div class="card-top">
                VELORA · DEMO
            </div>

            <div class="card-chip">
                ▰
            </div>

            <div class="card-number">
                ••••  ••••  ••••  2840
            </div>

            <div class="card-bottom">
                VELORA MEMBER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("Demo card · No real payments")


# =========================
# MONEY OVERVIEW
# =========================

st.markdown(
    '<div class="section">MONEY OVERVIEW</div>',
    unsafe_allow_html=True
)

remaining = max(
    2000 - st.session_state.spent,
    0
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Spent",
        f"₹{st.session_state.spent:,.0f}"
    )

with col2:

    st.metric(
        "Remaining",
        f"₹{remaining:,.0f}"
    )


# =========================
# VELORA SCORE
# =========================

st.markdown(
    '<div class="section">VELORA SCORE</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="app-card">

        <div class="score">
            84
        </div>

        <div class="score-good">
            ● GOOD MONEY HABITS
        </div>

        <div class="small">
            Based on your spending and saving activity.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# SPENDING GRAPH
# =========================

st.markdown(
    '<div class="section">SPENDING TREND</div>',
    unsafe_allow_html=True
)

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


# =========================
# SAVINGS GOAL
# =========================

st.markdown(
    '<div class="section">SAVINGS GOAL</div>',
    unsafe_allow_html=True
)

saved = st.session_state.goal_saved
target = st.session_state.goal_target

progress = min(
    saved / target,
    1.0
)

st.markdown(
    f"""
    <div class="app-card">

        <div class="goal-title">
            🎧 {st.session_state.goal_name}
        </div>

        <div class="goal-money">
            ₹{saved:,.0f} saved of ₹{target:,.0f}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.progress(progress)

st.caption(
    f"{progress * 100:.0f}% complete"
)


# =========================
# RECENT ACTIVITY
# =========================

st.markdown(
    '<div class="section">RECENT ACTIVITY</div>',
    unsafe_allow_html=True
)

for name, amount in st.session_state.transactions[:5]:

    if amount >= 0:

        st.markdown(
            f"""
            <div class="app-card">

                <div class="big">
                    🟢 {name}
                </div>

                <div class="small">
                    Money added
                </div>

                <div style="
                    color:#A7E8C2;
                    font-weight:800;
                    margin-top:5px;
                ">
                    +₹{amount:,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="app-card">

                <div class="big">
                    ⚪ {name}
                </div>

                <div class="small">
                    Payment
                </div>

                <div style="
                    color:white;
                    font-weight:800;
                    margin-top:5px;
                ">
                    −₹{abs(amount):,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# INSIGHT
# =========================

st.markdown(
    '<div class="section">✦ VELORA INSIGHT</div>',
    unsafe_allow_html=True
)

if st.session_state.spent > 1600:

    st.warning(
        "You're getting close to your monthly spending limit."
    )

else:

    st.success(
        "You're currently spending within your planned limit."
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)