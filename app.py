import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VELORA",
    page_icon="✦",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "monthly_limit" not in st.session_state:
    st.session_state.monthly_limit = 2000.0

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000.0

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400.0

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180],
    ]


# =========================
# STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top, #24104F 0%, #08090D 35%);
    color: white;
}

.block-container {
    max-width: 560px;
    padding: 25px 18px 100px;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* TEXT */

h1, h2, h3 {
    color: white !important;
}

/* BRAND */

.brand {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -1px;
}

.brand-v {
    color: #A78BFA;
}

.subtitle {
    color: #8B8D99;
    font-size: 12px;
}

/* HERO */

.hero {
    margin-top: 18px;
    padding: 25px;
    border-radius: 27px;
    background:
    linear-gradient(135deg,#32106F,#6D28D9,#4C1D95);
    border: 1px solid #7652C7;
    box-shadow: 0 20px 60px rgba(124,58,237,.30);
}

.hero-label {
    color: #DDD6FE;
    font-size: 10px;
    letter-spacing: 2px;
}

.hero-money {
    color: white;
    font-size: 43px;
    font-weight: 900;
    margin: 4px 0;
}

.hero-note {
    color: #DDD6FE;
    font-size: 10px;
}

/* CARDS */

.box {
    background: #12141C;
    border: 1px solid #292C38;
    border-radius: 21px;
    padding: 18px;
    margin: 10px 0;
}

.box-title {
    color: white;
    font-weight: 800;
    font-size: 14px;
}

.box-sub {
    color: #777B88;
    font-size: 11px;
}

/* SCORE */

.score {
    font-size: 40px;
    font-weight: 900;
    color: white;
}

.good {
    color: #A7F3D0;
    font-size: 10px;
    font-weight: 800;
}

/* GOAL */

.goal {
    background:
    linear-gradient(135deg,#1E123D,#11131B);
    border: 1px solid #50368B;
    border-radius: 22px;
    padding: 20px;
}

.goal-name {
    color: white;
    font-weight: 800;
}

.goal-value {
    color: #9A9DA8;
    font-size: 11px;
}

/* CARD */

.virtual-card {
    padding: 25px;
    min-height: 180px;
    border-radius: 25px;
    background:
    linear-gradient(135deg,#4C1D95,#7C3AED,#9333EA);
    box-shadow: 0 20px 55px rgba(124,58,237,.3);
}

.card-brand {
    font-size: 18px;
    font-weight: 900;
}

.card-number {
    margin-top: 55px;
    font-size: 17px;
    letter-spacing: 3px;
}

.card-bottom {
    margin-top: 22px;
    font-size: 9px;
    color: #DDD6FE;
}

/* TRANSACTION */

.transaction {
    padding: 13px 0;
    border-bottom: 1px solid #292C38;
}

.transaction-name {
    color: white;
    font-weight: 700;
}

.transaction-cat {
    color: #777B88;
    font-size: 10px;
}

.income {
    color: #A7F3C4;
    font-weight: 800;
}

.expense {
    color: white;
    font-weight: 800;
}

/* BUTTONS */

.stButton > button {
    background: #151720 !important;
    color: white !important;
    border: 1px solid #2D3040 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #8B5CF6 !important;
}

/* INPUTS */

input {
    color: white !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background: #8B5CF6;
}

hr {
    border-color: #292C38;
}

</style>
""", unsafe_allow_html=True)


# =========================
# FUNCTIONS
# =========================

def home():
    st.session_state.page = "Home"
    st.rerun()


def add_money():
    st.session_state.page = "Add"
    st.rerun()


def send_money():
    st.session_state.page = "Send"
    st.rerun()


def card_page():
    st.session_state.page = "Card"
    st.rerun()


def goals_page():
    st.session_state.page = "Goals"
    st.rerun()


def profile_page():
    st.session_state.page = "Profile"
    st.rerun()


def spending_total():
    return sum(
        abs(t[2])
        for t in st.session_state.transactions
        if t[2] < 0
    )


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="brand"><span class="brand-v">V</span>ELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart money, made simple.</div>',
    unsafe_allow_html=True
)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")

    st.markdown("## Welcome back 👋")

    # HERO
    st.markdown(
        '<div class="hero">'
        '<div class="hero-label">AVAILABLE BALANCE</div>'
        '<div class="hero-money">₹{:,.0f}</div>'
        '<div class="hero-note">'
        'DEMO WALLET · NO REAL MONEY · •••• 2840'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    # QUICK ACTIONS

    st.subheader("Quick actions")

    a, b, c, d = st.columns(4)

    with a:
        if st.button("＋", use_container_width=True):
            add_money()
        st.caption("Add")

    with b:
        if st.button("↗", use_container_width=True):
            send_money()
        st.caption("Send")

    with c:
        if st.button("🎯", use_container_width=True):
            goals_page()
        st.caption("Goals")

    with d:
        if st.button("▣", use_container_width=True):
            card_page()
        st.caption("Card")

    # MONEY OVERVIEW

    st.subheader("Money overview")

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    x, y = st.columns(2)

    with x:
        st.metric(
            "Spent",
            "₹{:,.0f}".format(spent)
        )

    with y:
        st.metric(
            "Remaining",
            "₹{:,.0f}".format(remaining)
        )

    # SCORE

    st.markdown(
        '<div class="box">'
        '<div class="box-title">VELORA SCORE</div>'
        '<div class="box-sub">Your money habit snapshot</div>'
        '<div class="score">84</div>'
        '<div class="good">● GOOD MONEY HABITS</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # CHART

    st.subheader("Spending trend")

    chart = pd.DataFrame(
        {
            "Spending": [
                120,
                180,
                90,
                240,
                160,
                280,
                110
            ]
        },
        index=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]
    )

    st.line_chart(
        chart,
        height=190
    )

    # GOAL

    st.subheader("Savings goal")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-name">🎧 {}</div>'
        '<div class="goal-value">₹{:,.0f} saved of ₹{:,.0f}</div>'
        '</div>'.format(
            st.session_state.goal_name,
            st.session_state.goal_saved,
            st.session_state.goal_target
        ),
        unsafe_allow_html=True
    )

    st.progress(
        min(progress, 1.0)
    )

    st.caption(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    # ACTIVITY

    st.subheader("Recent activity")

    for name, category, amount in st.session_state.transactions[:5]:

        if amount >= 0:

            money = (
                '<span class="income">+₹{:,.0f}</span>'
                .format(amount)
            )

        else:

            money = (
                '<span class="expense">−₹{:,.0f}</span>'
                .format(abs(amount))
            )

        st.markdown(
            '<div class="transaction">'
            '<div class="transaction-name">{}</div>'
            '<div class="transaction-cat">{}</div>'
            '<div>{}</div>'
            '</div>'.format(
                name,
                category,
                money
            ),
            unsafe_allow_html=True
        )

    # INSIGHT

    st.markdown(
        '<div class="box">'
        '<div class="box-title">✦ VELORA INSIGHT</div>'
        '<div class="box-sub">'
        "You're currently spending within your planned limit."
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state.page == "Add":

    st.header("Add money")

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=500.0,
        step=100.0
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money / Gift"
    )

    if st.button(
        "Add to wallet",
        use_container_width=True
    ):

        if not source:
            source = "Pocket Money"

        st.session_state.balance += amount

        add_transaction(
            source,
            "Income",
            amount
        )

        st.success(
            "₹{:,.0f} added successfully.".format(amount)
        )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# SEND
# =========================================================

elif st.session_state.page == "Send":

    st.header("Send money")

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

        if not person:
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

            st.success(
                "₹{:,.0f} sent successfully.".format(amount)
            )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# CARD
# =========================================================

elif st.session_state.page == "Card":

    st.header("Velora Card")

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-brand">VELORA ✦</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-bottom">'
        'VELORA MEMBER &nbsp;&nbsp;&nbsp; DEMO'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.frozen:

        st.warning("🔒 Card is frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):
            st.session_state.frozen = False
            st.rerun()

    else:

        st.success("● Card is active.")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):
            st.session_state.frozen = True
            st.rerun()

    st.caption("Prototype card · No real payments")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        home()


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.header("Savings goals")

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
        "Saved amount",
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

        st.success("Goal saved.")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-name">🎯 {}</div>'
        '<div class="goal-value">'
        '₹{:,.0f} / ₹{:,.0f}'
        '</div>'
        '</div>'.format(
            st.session_state.goal_name,
            st.session_state.goal_saved,
            st.session_state.goal_target
        ),
        unsafe_allow_html=True
    )

    st.progress(
        min(progress, 1.0)
    )

    if st.button(
        "← Home",
        use_container_width=True
    ):
        home()


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.header("Profile")

    name = st.text_input(
        "Your name",
        value="Tejal"
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

        st.session_state.monthly_limit = limit

        st.success("Profile updated.")

    st.markdown(
        '<div class="box">'
        '<div class="box-title">VELORA</div>'
        '<div class="box-sub">'
        'Smart money, made simple.'
        '</div>'
        '<br>'
        '<div class="box-sub">'
        'Demo mode · No real payments'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "← Home",
        use_container_width=True
    ):
        home()


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:
    if st.button("⌂ Home", use_container_width=True):
        home()

with n2:
    if st.button("▣ Card", use_container_width=True):
        card_page()

with n3:
    if st.button("🎯 Goals", use_container_width=True):
        goals_page()

with n4:
    if st.button("◉ Profile", use_container_width=True):
        profile_page()