import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VELORA",
    page_icon="✦",
    layout="centered"
)

# =========================================================
# DATA
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400.0

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000.0

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food & Drinks", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180],
    ]


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% -10%,
            rgba(124,58,237,.20),
            transparent 35%
        ),
        #07080D;
}

.block-container {
    max-width: 560px;
    padding: 28px 18px 100px;
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

/* REMOVE DEFAULT GAP */

[data-testid="stVerticalBlock"] {
    gap: 0.55rem;
}

/* TEXT */

h1 {
    font-size: 34px !important;
    letter-spacing: -1.5px;
}

h2 {
    font-size: 23px !important;
    letter-spacing: -.8px;
}

h3 {
    font-size: 17px !important;
}

p {
    color: #9699A5;
}

/* BRAND */

.brand-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 4px;
}

.brand {
    font-size: 29px;
    font-weight: 900;
    letter-spacing: -1.5px;
    color: white;
}

.brand span {
    color: #8B5CF6;
}

.live-dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #A78BFA;
    box-shadow: 0 0 15px #8B5CF6;
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    margin-top: 18px;
    padding: 24px;
    border-radius: 26px;
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(196,181,253,.25),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #35117A,
            #6D28D9 55%,
            #4C1D95
        );
    border: 1px solid rgba(196,181,253,.22);
    box-shadow:
        0 20px 60px rgba(76,29,149,.35);
}

.hero-small {
    font-size: 11px;
    color: #DDD6FE;
    letter-spacing: 1.7px;
}

.hero-money {
    color: white;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: -2px;
    margin: 4px 0;
}

.hero-bottom {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    color: #DDD6FE;
    font-size: 11px;
}

/* GLASS CARDS */

.glass {
    background: rgba(19,20,29,.88);
    border: 1px solid #292B38;
    border-radius: 21px;
    padding: 18px;
    margin: 9px 0;
}

.card-title {
    color: white;
    font-size: 14px;
    font-weight: 800;
}

.card-sub {
    color: #858894;
    font-size: 11px;
}

/* QUICK ACTION */

.action-box {
    text-align: center;
    padding: 14px 5px;
    border-radius: 18px;
    background: #12141B;
    border: 1px solid #282A35;
}

.action-icon {
    font-size: 21px;
    color: #A78BFA;
}

.action-text {
    font-size: 10px;
    color: #B8BAC3;
    margin-top: 5px;
}

/* SCORE */

.score-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.score-number {
    font-size: 38px;
    font-weight: 900;
    color: white;
}

.score-good {
    color: #A7F3D0;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .8px;
}

/* GOAL */

.goal-card {
    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,.18),
            rgba(20,20,29,.95)
        );
    border: 1px solid #40306C;
    border-radius: 21px;
    padding: 19px;
}

.goal-head {
    display: flex;
    justify-content: space-between;
}

.goal-title {
    color: white;
    font-weight: 800;
}

.goal-percent {
    color: #A78BFA;
    font-weight: 800;
}

.goal-money {
    color: #8D909C;
    font-size: 11px;
    margin: 8px 0;
}

/* CARD */

.virtual-card {
    min-height: 190px;
    padding: 23px;
    border-radius: 25px;
    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(255,255,255,.22),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #4C1D95,
            #7C3AED,
            #9333EA
        );
    box-shadow:
        0 20px 55px rgba(124,58,237,.28);
}

.vcard-top {
    display: flex;
    justify-content: space-between;
    color: white;
    font-weight: 900;
    letter-spacing: 1px;
}

.vcard-number {
    margin-top: 48px;
    color: white;
    letter-spacing: 3px;
    font-size: 17px;
}

.vcard-bottom {
    display: flex;
    justify-content: space-between;
    color: #DDD6FE;
    font-size: 9px;
    margin-top: 22px;
}

/* TRANSACTIONS */

.tx {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 13px 0;
    border-bottom: 1px solid #252732;
}

.tx-name {
    color: white;
    font-size: 13px;
    font-weight: 700;
}

.tx-cat {
    color: #777B87;
    font-size: 10px;
    margin-top: 3px;
}

.tx-positive {
    color: #A7F3C4;
    font-weight: 800;
}

.tx-negative {
    color: white;
    font-weight: 800;
}

/* BUTTONS */

.stButton > button {
    background: #151720 !important;
    color: white !important;
    border: 1px solid #2C2F3B !important;
    border-radius: 14px !important;
    min-height: 43px !important;
    font-weight: 700 !important;
    transition: .2s;
}

.stButton > button:hover {
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 18px rgba(139,92,246,.18);
}

/* METRICS */

[data-testid="stMetric"] {
    background: #12141B;
    border: 1px solid #282A35;
    border-radius: 18px;
    padding: 13px;
}

[data-testid="stMetricValue"] {
    color: white !important;
    font-weight: 900 !important;
}

[data-testid="stMetricLabel"] {
    color: #858894 !important;
}

/* INPUTS */

input, textarea {
    background: #12141B !important;
    color: white !important;
}

[data-baseweb="select"] > div {
    background: #12141B !important;
    border-color: #30323E !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background: linear-gradient(
        90deg,
        #7C3AED,
        #A78BFA
    );
}

/* DIVIDER */

hr {
    border-color: #252732 !important;
}

/* FOOTER NAV */

.nav-text {
    text-align: center;
    color: #717480;
    font-size: 9px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def spending():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def add_tx(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="brand-row">
    <div class="brand">
        <span>V</span>ELORA
    </div>
    <div class="live-dot"></div>
</div>
""", unsafe_allow_html=True)

st.caption("Smart money, made simple.")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")

    st.markdown(
        "<h2 style='margin-top:0'>Welcome back 👋</h2>",
        unsafe_allow_html=True
    )

    # HERO
    st.markdown("""
    <div class="hero">
        <div class="hero-small">
            AVAILABLE BALANCE
        </div>

        <div class="hero-money">
            ₹{balance:,.0f}
        </div>

        <div class="hero-bottom">
            <span>DEMO WALLET</span>
            <span>NO REAL MONEY · •••• 2840</span>
        </div>
    </div>
    """.format(
        balance=st.session_state.balance
    ), unsafe_allow_html=True)

    # QUICK ACTIONS
    st.subheader("Quick actions")

    a, b, c, d = st.columns(4)

    with a:
        if st.button("＋", use_container_width=True):
            go("Add")
        st.markdown(
            '<div class="nav-text">Add money</div>',
            unsafe_allow_html=True
        )

    with b:
        if st.button("↗", use_container_width=True):
            go("Send")
        st.markdown(
            '<div class="nav-text">Send</div>',
            unsafe_allow_html=True
        )

    with c:
        if st.button("⇄", use_container_width=True):
            go("Request")
        st.markdown(
            '<div class="nav-text">Request</div>',
            unsafe_allow_html=True
        )

    with d:
        if st.button("▣", use_container_width=True):
            go("Card")
        st.markdown(
            '<div class="nav-text">My card</div>',
            unsafe_allow_html=True
        )

    # OVERVIEW
    st.subheader("Money overview")

    spent = spending()

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
    st.markdown("""
    <div class="glass">
        <div class="score-box">
            <div>
                <div class="card-title">
                    VELORA SCORE
                </div>
                <div class="card-sub">
                    Your money habit snapshot
                </div>
            </div>

            <div style="text-align:right">
                <div class="score-number">84</div>
                <div class="score-good">
                    ● GOOD HABITS
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # TREND
    st.subheader("Spending trend")

    data = pd.DataFrame({
        "Spending": [
            120,
            180,
            90,
            240,
            160,
            280,
            110
        ]
    }, index=[
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ])

    st.line_chart(
        data,
        height=190
    )

    # GOAL
    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown("""
    <div class="goal-card">
        <div class="goal-head">
            <div class="goal-title">
                🎧 {name}
            </div>
            <div class="goal-percent">
                {percent:.0f}%
            </div>
        </div>

        <div class="goal-money">
            ₹{saved:,.0f} saved of ₹{target:,.0f}
        </div>
    </div>
    """.format(
        name=st.session_state.goal_name,
        percent=progress * 100,
        saved=st.session_state.goal_saved,
        target=st.session_state.goal_target
    ), unsafe_allow_html=True)

    st.progress(min(progress, 1))

    # RECENT
    st.subheader("Recent activity")

    for name, category, amount in st.session_state.transactions[:5]:

        if amount >= 0:
            amount_html = (
                '<div class="tx-positive">'
                '+₹{:,.0f}'
                '</div>'
            ).format(amount)
        else:
            amount_html = (
                '<div class="tx-negative">'
                '−₹{:,.0f}'
                '</div>'
            ).format(abs(amount))

        st.markdown("""
        <div class="tx">
            <div>
                <div class="tx-name">
                    {name}
                </div>
                <div class="tx-cat">
                    {category}
                </div>
            </div>

            {amount}
        </div>
        """.format(
            name=name,
            category=category,
            amount=amount_html
        ), unsafe_allow_html=True)

    # INSIGHT
    st.markdown("""
    <div class="glass">
        <div class="card-title">
            ✦ VELORA INSIGHT
        </div>

        <div class="card-sub" style="margin-top:7px">
            You're currently spending within
            your planned monthly limit.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ADD
# =========================================================

elif st.session_state.page == "Add":

    st.header("Add money")

    st.caption(
        "Simulate adding money to your demo wallet."
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=500.0,
        step=100.0
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money / Gift / Other"
    )

    if st.button(
        "Add to wallet",
        use_container_width=True
    ):

        if not source:
            source = "Pocket Money"

        st.session_state.balance += amount

        add_tx(
            source,
            "Income",
            amount
        )

        st.success(
            "₹{:,.0f} added.".format(amount)
        )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


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
            "Food & Drinks",
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

            add_tx(
                "Sent to " + person,
                category,
                -amount
            )

            st.success(
                "₹{:,.0f} sent.".format(amount)
            )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# REQUEST
# =========================================================

elif st.session_state.page == "Request":

    st.header("Request money")

    person = st.text_input(
        "Request from",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=200.0,
        step=50.0
    )

    reason = st.text_input(
        "Reason",
        placeholder="Lunch / Movie / Trip"
    )

    if st.button(
        "Create request",
        use_container_width=True
    ):

        if not person:
            st.error("Enter a name.")
        else:
            st.success(
                "₹{:,.0f} request created.".format(amount)
            )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# CARD
# =========================================================

elif st.session_state.page == "Card":

    st.header("My Card")

    st.markdown("""
    <div class="virtual-card">

        <div class="vcard-top">
            <span>VELORA</span>
            <span>✦</span>
        </div>

        <div class="vcard-number">
            •••• &nbsp; •••• &nbsp; •••• &nbsp; 2840
        </div>

        <div class="vcard-bottom">
            <span>VELORA MEMBER</span>
            <span>DEMO</span>
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.session_state.frozen:

        st.warning("🔒 Your card is frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):
            st.session_state.frozen = False
            st.rerun()

    else:

        st.success("● Card active")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):
            st.session_state.frozen = True
            st.rerun()

    st.caption(
        "Prototype card · No real payments"
    )

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.header("Savings goals")

    name = st.text_input(
        "Goal",
        value=st.session_state.goal_name
    )

    target = st.number_input(
        "Target",
        min_value=1.0,
        value=float(st.session_state.goal_target),
        step=100.0
    )

    saved = st.number_input(
        "Already saved",
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

        st.success("Goal updated.")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.markdown("""
    <div class="goal-card">
        <div class="goal-title">
            🎯 {name}
        </div>

        <div class="goal-money">
            ₹{saved:,.0f} / ₹{target:,.0f}
        </div>
    </div>
    """.format(
        name=st.session_state.goal_name,
        saved=st.session_state.goal_saved,
        target=st.session_state.goal_target
    ), unsafe_allow_html=True)

    st.progress(min(progress, 1))

    st.write(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    st.divider()

    st.subheader("Add savings")

    contribution = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0
    )

    if st.button(
        "Add to goal",
        use_container_width=True
    ):

        if contribution <= st.session_state.balance:

            st.session_state.balance -= contribution

            st.session_state.goal_saved += contribution

            add_tx(
                "Savings Goal",
                "Savings",
                -contribution
            )

            st.success(
                "₹{:,.0f} saved.".format(
                    contribution
                )
            )

        else:
            st.error("Not enough demo balance.")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# BOTTOM NAV
# =========================================================

st.divider()

b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button("⌂ Home", use_container_width=True):
        go("Home")

with b2:
    if st.button("▣ Card", use_container_width=True):
        go("Card")

with b3:
    if st.button("🎯 Goals", use_container_width=True):
        go("Goals")

with b4:
    if st.button("◉ Profile", use_container_width=True):
        go("Profile")


# =========================================