import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =====================================================
# DATA
# =====================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Pocket Money", 2000),
        ("Food", -250),
        ("Study", -500),
        ("Shopping", -350),
        ("Gaming", -180)
    ]


# =====================================================
# PREMIUM DESIGN
# =====================================================

st.markdown("""
<style>

.stApp {
    background: #07080C;
}

.block-container {
    max-width: 520px;
    padding: 25px 18px 80px;
}

#MainMenu,
header,
footer {
    visibility: hidden;
}

.brand {
    font-size: 31px;
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: -1px;
}

.tagline {
    color: #777B86;
    font-size: 12px;
    margin-top: -5px;
    margin-bottom: 25px;
}

.hero {
    background:
        radial-gradient(
            circle at top right,
            #A52B52 0%,
            transparent 42%
        ),
        linear-gradient(
            135deg,
            #210A14,
            #631833,
            #8F2447
        );

    border-radius: 28px;
    padding: 25px;
    min-height: 180px;
    box-shadow: 0 18px 50px rgba(130,20,60,.25);
}

.hero-label {
    color: #D9C3CC;
    font-size: 10px;
    letter-spacing: 2px;
}

.hero-money {
    color: white;
    font-size: 43px;
    font-weight: 900;
    margin-top: 5px;
}

.hero-note {
    color: #D7BBC5;
    font-size: 10px;
    margin-top: 8px;
}

.section {
    color: white;
    font-size: 14px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 12px;
}

.app-card {
    background: #12141A;
    border: 1px solid #252832;
    border-radius: 21px;
    padding: 18px;
}

.app-card:hover {
    border-color: #7D2949;
}

.small {
    color: #858994;
    font-size: 11px;
}

.white {
    color: white;
    font-weight: 800;
}

.score {
    color: white;
    font-size: 34px;
    font-weight: 900;
}

.score-good {
    color: #A7E8C2;
    font-size: 11px;
}

.goal-title {
    color: white;
    font-size: 15px;
    font-weight: 800;
}

.goal-money {
    color: #858994;
    font-size: 11px;
}

.virtual-card {
    background:
        radial-gradient(
            circle at 85% 15%,
            #777B87,
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #17191F,
            #3A3D47
        );

    border-radius: 25px;
    padding: 23px;
    border: 1px solid #484B55;
    min-height: 160px;
}

.card-top {
    color: #B0B2B9;
    font-size: 10px;
    letter-spacing: 2px;
}

.card-chip {
    font-size: 24px;
    margin-top: 22px;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 18px;
}

.card-bottom {
    color: #A3A5AC;
    font-size: 9px;
    margin-top: 20px;
}

.stButton > button {
    background: #15171D !important;
    color: white !important;
    border: 1px solid #292C35 !important;
    border-radius: 15px !important;
    min-height: 46px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

[data-testid="stMetric"] {
    background: #12141A;
    border: 1px solid #252832;
    border-radius: 18px;
    padding: 13px;
}

[data-testid="stMetricLabel"] {
    color: #858994 !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

.stProgress > div > div > div > div {
    background-color: #A52B52;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">Smart money, made simple.</div>',
    unsafe_allow_html=True
)

st.caption("GOOD EVENING")

st.markdown(
    "### Welcome back 👋"
)


# =====================================================
# BALANCE
# =====================================================

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


# =====================================================
# QUICK ACTIONS
# =====================================================

st.markdown(
    '<div class="section">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    add = st.button(
        "＋ Add",
        use_container_width=True
    )

with b:
    send = st.button(
        "↗ Send",
        use_container_width=True
    )

with c:
    card = st.button(
        "▣ Card",
        use_container_width=True
    )


# =====================================================
# ADD MONEY
# =====================================================

if add:

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

        st.session_state.balance += amount

        st.session_state.transactions.insert(
            0,
            (source if source else "Added Money", amount)
        )

        st.success(
            f"₹{amount:,.0f} added!"
        )


# =====================================================
# SEND MONEY
# =====================================================

if send:

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

        if person == "":
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


# =====================================================
# CARD
# =====================================================

if card:

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


# =====================================================
# MONEY OVERVIEW
# =====================================================

st.markdown(
    '<div class="section">MONEY OVERVIEW</div>',
    unsafe_allow_html=True
)

remaining = max(
    2000 - st.session_state.spent,
    0
)

x, y = st.columns(2)

with x:
    st.metric(
        "Spent",
        f"₹{st.session_state.spent:,.0f}"
    )

with y:
    st.metric(
        "Remaining",
        f"₹{remaining:,.0f}"
    )


# =====================================================
# MONEY SCORE
# =====================================================

st.markdown(
    '<div class="section">VELORA SCORE</div>',
    unsafe_allow_html=True
)

score = 84

st.markdown(
    f"""
    <div class="app-card">

        <div class="score">
            {score}
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


# =====================================================
# GRAPH
# =====================================================

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


# =====================================================
# SAVINGS GOAL
# =====================================================

st.markdown(
    '<div class="section">SAVINGS GOAL</div>',
    unsafe_allow_html=True
)

target = 5000
saved = st.session_state.goal_saved

progress = min(
    saved / target,
    1
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


# =====================================================
# RECENT ACTIVITY
# =====================================================

st.markdown(
    '<div class="section">RECENT ACTIVITY</div>',
    unsafe_allow_html=True
)

for name, amount in st.session_state.transactions[:5]:

    if amount >= 0:

        st.markdown(
            f"""
            <div class="app-card">

                <div class="white">
                    🟢 {name}
                </div>

                <div class="small">
                    Money added
                </div>

                <div style="color:#A7E8C2;font-weight:800;">
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

                <div class="white">
                    ⚪ {name}
                </div>

                <div class="small">
                    Payment
                </div>

                <div style="color:white;font-weight:800;">
                    −₹{abs(amount):,.0f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# INSIGHT
# =====================================================

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


st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)