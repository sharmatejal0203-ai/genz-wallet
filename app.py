import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="✦",
    layout="centered"
)

# =========================
# VELORA DATA
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "limit" not in st.session_state:
    st.session_state.limit = 2000

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("🟢 Pocket Money", "Money added", "+₹2,000"),
        ("⚪ Food", "Payment", "−₹250"),
        ("⚪ Study", "Payment", "−₹500"),
        ("⚪ Shopping", "Payment", "−₹350"),
        ("⚪ Gaming", "Payment", "−₹180"),
    ]


# =========================
# DESIGN
# =========================

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(
        circle at 50% -10%,
        #4c1d95 0%,
        #171329 22%,
        #09090d 55%
    );
    color: white;
}

.block-container {
    max-width: 560px;
    padding: 28px 18px 90px;
}

header, footer, #MainMenu {
    visibility: hidden;
}

/* BRAND */

.logo {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -1.5px;
}

.logo span {
    color: #a78bfa;
}

.tagline {
    color: #858591;
    font-size: 12px;
    margin-top: -4px;
}

/* HERO */

.hero {
    margin-top: 22px;
    padding: 26px;
    border-radius: 28px;
    background:
        linear-gradient(
            135deg,
            #32105f,
            #7027c9 55%,
            #4c1d95
        );
    border: 1px solid #8b5cf6;
    box-shadow:
        0 20px 70px rgba(124,58,237,.30);
}

.hero-label {
    color: #ddd6fe;
    font-size: 10px;
    letter-spacing: 2px;
}

.hero-money {
    font-size: 43px;
    font-weight: 900;
    margin: 5px 0 14px;
}

.hero-bottom {
    display: flex;
    justify-content: space-between;
    color: #d8ccef;
    font-size: 9px;
}

/* QUICK ACTION */

.action {
    background: #15151d;
    border: 1px solid #292936;
    border-radius: 18px;
    padding: 12px 5px;
    text-align: center;
}

/* BOX */

.box {
    background: rgba(20,20,29,.92);
    border: 1px solid #292936;
    border-radius: 22px;
    padding: 19px;
    margin: 12px 0;
}

.title {
    font-size: 13px;
    font-weight: 800;
}

.muted {
    color: #777783;
    font-size: 11px;
}

/* SCORE */

.score-box {
    background:
        linear-gradient(
            135deg,
            #1d1237,
            #111119
        );
    border: 1px solid #4c3575;
    border-radius: 22px;
    padding: 20px;
}

.score {
    font-size: 42px;
    font-weight: 900;
    margin: 5px 0;
}

.good {
    color: #a7f3d0;
    font-size: 10px;
    font-weight: 800;
}

/* GOAL */

.goal {
    background:
        linear-gradient(
            135deg,
            #251340,
            #111119
        );
    border: 1px solid #593a86;
    border-radius: 22px;
    padding: 20px;
}

.goal-name {
    font-size: 15px;
    font-weight: 800;
}

.goal-money {
    color: #8c8c99;
    font-size: 11px;
    margin-top: 6px;
}

/* ACTIVITY */

.activity {
    padding: 13px 0;
    border-bottom: 1px solid #272732;
}

.activity-name {
    font-weight: 700;
}

.activity-small {
    color: #777783;
    font-size: 10px;
    margin-top: 3px;
}

.activity-money {
    font-weight: 800;
}

/* CARD */

.virtual-card {
    margin-top: 20px;
    padding: 25px;
    height: 180px;
    border-radius: 27px;
    background:
        linear-gradient(
            135deg,
            #32105f,
            #7c3aed,
            #a855f7
        );
    box-shadow:
        0 25px 60px rgba(124,58,237,.32);
}

.card-brand {
    font-size: 18px;
    font-weight: 900;
}

.card-chip {
    margin-top: 32px;
    font-size: 23px;
}

.card-number {
    margin-top: 10px;
    font-size: 15px;
    letter-spacing: 3px;
}

.card-small {
    color: #ddd6fe;
    font-size: 9px;
    margin-top: 15px;
}

/* BUTTON */

.stButton > button {
    background: #15151d !important;
    color: white !important;
    border: 1px solid #2d2d3a !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #8b5cf6 !important;
    color: white !important;
}

/* INPUT */

.stTextInput input,
.stNumberInput input {
    background: #14141c !important;
    color: white !important;
    border-color: #30303c !important;
}

hr {
    border-color: #292936;
}

</style>
""", unsafe_allow_html=True)


# =========================
# NAVIGATION
# =========================

def go(page):
    st.session_state.page = page
    st.rerun()


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="logo"><span>V</span>ELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">Smart money, made simple.</div>',
    unsafe_allow_html=True
)


# =========================
# HOME
# =========================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")

    st.markdown("## Welcome back 👋")

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-label">
                AVAILABLE BALANCE
            </div>

            <div class="hero-money">
                ₹{st.session_state.balance:,}
            </div>

            <div class="hero-bottom">
                <span>DEMO WALLET</span>
                <span>NO REAL MONEY · •••• 2840</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # QUICK ACTIONS

    st.markdown("### Quick actions")

    a, b, c, d = st.columns(4)

    with a:
        if st.button("＋", use_container_width=True):
            go("Add")
        st.caption("Add money")

    with b:
        if st.button("↗", use_container_width=True):
            go("Send")
        st.caption("Send")

    with c:
        if st.button("⇄", use_container_width=True):
            go("Request")
        st.caption("Request")

    with d:
        if st.button("▣", use_container_width=True):
            go("Card")
        st.caption("My card")

    # MONEY OVERVIEW

    st.markdown("### Money overview")

    c1, c2 = st.columns(2)

    remaining = max(
        st.session_state.limit -
        st.session_state.spent,
        0
    )

    with c1:
        st.markdown(
            f"""
            <div class="box">
                <div class="muted">SPENT</div>
                <div style="font-size:25px;font-weight:900;">
                    ₹{st.session_state.spent:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="box">
                <div class="muted">REMAINING</div>
                <div style="font-size:25px;font-weight:900;">
                    ₹{remaining:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # SCORE

    st.markdown(
        """
        <div class="score-box">
            <div class="title">VELORA SCORE</div>
            <div class="muted">
                Based on your spending and saving activity.
            </div>
            <div class="score">84</div>
            <div class="good">
                ● GOOD MONEY HABITS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # TREND

    st.markdown("### Spending trend")

    st.line_chart(
        {
            "Fri": 350,
            "Mon": 410,
            "Sat": 520,
            "Sun": 440,
            "Thu": 480,
            "Tue": 390,
            "Wed": 460
        },
        height=190
    )

    # GOAL

    st.markdown("### Savings goal")

    progress = (
        st.session_state.goal_saved /
        st.session_state.goal_target
    )

    st.markdown(
        f"""
        <div class="goal">
            <div class="goal-name">
                🎧 {st.session_state.goal_name}
            </div>

            <div class="goal-money">
                ₹{st.session_state.goal_saved:,}
                saved of
                ₹{st.session_state.goal_target:,}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(min(progress, 1.0))

    st.caption(
        f"{progress * 100:.0f}% complete"
    )

    # ACTIVITY

    st.markdown("### Recent activity")

    for name, small, money in st.session_state.transactions:

        st.markdown(
            f"""
            <div class="activity">
                <div class="activity-name">
                    {name}
                </div>

                <div class="activity-small">
                    {small}
                </div>

                <div class="activity-money">
                    {money}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # INSIGHT

    st.markdown(
        """
        <div class="box">
            <div class="title">
                ✦ VELORA INSIGHT
            </div>

            <div class="muted">
                You're currently spending within
                your planned limit.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# ADD MONEY
# =========================

elif st.session_state.page == "Add":

    st.header("Add money")

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money / Gift"
    )

    if st.button(
        "Add to wallet",
        use_container_width=True
    ):

        st.session_state.balance += amount

        st.session_state.transactions.insert(
            0,
            (
                "🟢 " + (source or "Pocket Money"),
                "Money added",
                f"+₹{amount:,}"
            )
        )

        st.success(
            f"₹{amount:,} added."
        )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================
# SEND
# =========================

elif st.session_state.page == "Send":

    st.header("Send money")

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

    if st.button(
        "Send money",
        use_container_width=True
    ):

        if not person:
            st.error("Enter a name.")

        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")

        else:

            st.session_state.balance -= amount
            st.session_state.spent += amount

            st.session_state.transactions.insert(
                0,
                (
                    "⚪ " + person,
                    "Payment",
                    f"−₹{amount:,}"
                )
            )

            st.success(
                f"₹{amount:,} sent."
            )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================
# REQUEST
# =========================

elif st.session_state.page == "Request":

    st.header("Request money")

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
        placeholder="Lunch / Movie / Trip"
    )

    if st.button(
        "Create request",
        use_container_width=True
    ):

        st.success(
            f"₹{amount:,} request created."
        )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================
# CARD
# =========================

elif st.session_state.page == "Card":

    st.header("My card")

    st.markdown(
        """
        <div class="virtual-card">

            <div class="card-brand">
                VELORA ✦
            </div>

            <div class="card-chip">
                ▰
            </div>

            <div class="card-number">
                •••• •••• •••• 2840
            </div>

            <div class="card-small">
                VELORA MEMBER
                &nbsp;&nbsp;&nbsp;&nbsp;
                DEMO
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.frozen:

        st.warning("🔒 Your demo card is frozen.")

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

    st.caption(
        "Prototype only · No real payments"
    )

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("Home")


# =========================
# BOTTOM NAVIGATION
# =========================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:
    if st.button("⌂ Home", use_container_width=True):
        go("Home")

with n2:
    if st.button("▣ Card", use_container_width=True):
        go("Card")

with n3:
    if st.button("🎯 Goals", use_container_width=True):
        st.info("Savings goal is shown on Home.")

with n4:
    if st.button("◉ Profile", use_container_width=True):
        st.info("Profile settings coming next.")