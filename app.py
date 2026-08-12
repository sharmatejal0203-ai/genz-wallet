import streamlit as st

# ==============================
# VELORA
# ==============================

st.set_page_config(
    page_title="VELORA",
    page_icon="✦",
    layout="centered"
)

# ==============================
# DATA
# ==============================

if "balance" not in st.session_state:
    st.session_state["balance"] = 5000

if "spent" not in st.session_state:
    st.session_state["spent"] = 1260

if "limit" not in st.session_state:
    st.session_state["limit"] = 2000

if "goal_name" not in st.session_state:
    st.session_state["goal_name"] = "New Headphones"

if "goal_saved" not in st.session_state:
    st.session_state["goal_saved"] = 3400

if "goal_target" not in st.session_state:
    st.session_state["goal_target"] = 5000

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if "card_frozen" not in st.session_state:
    st.session_state["card_frozen"] = False


# ==============================
# STYLE
# ==============================

st.markdown("""
<style>

.stApp {
    background: #08090D;
    color: white;
}

.block-container {
    max-width: 560px;
    padding: 28px 18px 90px;
}

header,
footer,
#MainMenu {
    visibility: hidden;
}

/* BRAND */

.logo {
    font-size: 30px;
    font-weight: 900;
    color: white;
}

.logo span {
    color: #A855F7;
}

.tagline {
    color: #858591;
    font-size: 12px;
    margin-top: -5px;
}

/* HERO */

.hero {
    margin-top: 22px;
    padding: 26px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #32105F,
        #7C3AED,
        #4C1D95
    );
    border: 1px solid #8B5CF6;
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
    margin: 5px 0 15px;
}

.hero-bottom {
    display: flex;
    justify-content: space-between;
    color: #DDD6FE;
    font-size: 9px;
}

/* BOX */

.box {
    background: #12131A;
    border: 1px solid #292B35;
    border-radius: 21px;
    padding: 18px;
    margin: 10px 0;
}

.box-title {
    color: white;
    font-weight: 800;
    font-size: 13px;
}

.box-small {
    color: #777A86;
    font-size: 10px;
}

/* SCORE */

.score {
    font-size: 42px;
    font-weight: 900;
    margin-top: 5px;
}

.good {
    color: #A7F3D0;
    font-size: 10px;
    font-weight: 800;
}

/* GOAL */

.goal {
    background: linear-gradient(
        135deg,
        #25133D,
        #111219
    );
    border: 1px solid #573A7F;
    border-radius: 22px;
    padding: 20px;
}

.goal-name {
    color: white;
    font-size: 15px;
    font-weight: 800;
}

.goal-money {
    color: #888B97;
    font-size: 11px;
    margin-top: 6px;
}

/* ACTIVITY */

.activity {
    padding: 14px 0;
    border-bottom: 1px solid #252631;
}

.activity-name {
    color: white;
    font-weight: 700;
}

.activity-small {
    color: #777A86;
    font-size: 10px;
    margin-top: 3px;
}

.green {
    color: #A7F3C2;
    font-weight: 800;
}

.white {
    color: white;
    font-weight: 800;
}

/* CARD */

.virtual-card {
    margin-top: 20px;
    padding: 25px;
    height: 180px;
    border-radius: 27px;
    background: linear-gradient(
        135deg,
        #32105F,
        #7C3AED,
        #A855F7
    );
    box-shadow: 0 25px 60px rgba(124,58,237,.30);
}

.card-brand {
    font-size: 18px;
    font-weight: 900;
}

.card-chip {
    margin-top: 32px;
    font-size: 22px;
}

.card-number {
    margin-top: 10px;
    letter-spacing: 3px;
    font-size: 15px;
}

.card-bottom {
    color: #DDD6FE;
    font-size: 9px;
    margin-top: 15px;
}

/* BUTTONS */

.stButton > button {
    background: #15161D !important;
    color: white !important;
    border: 1px solid #30323E !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #8B5CF6 !important;
}

hr {
    border-color: #292B35;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# NAVIGATION
# ==============================

def go(page):
    st.session_state["page"] = page
    st.rerun()


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="logo"><span>V</span>ELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">Smart money, made simple.</div>',
    unsafe_allow_html=True
)


# =========================================================
# HOME
# =========================================================

if st.session_state["page"] == "Home":

    st.caption("GOOD EVENING")

    st.markdown("## Welcome back 👋")

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-label">
                AVAILABLE BALANCE
            </div>

            <div class="hero-money">
                ₹{st.session_state["balance"]:,}
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
        if st.button("＋", key="add_btn", use_container_width=True):
            go("Add")
        st.caption("Add money")

    with b:
        if st.button("↗", key="send_btn", use_container_width=True):
            go("Send")
        st.caption("Send")

    with c:
        if st.button("⇄", key="request_btn", use_container_width=True):
            go("Request")
        st.caption("Request")

    with d:
        if st.button("▣", key="card_btn", use_container_width=True):
            go("Card")
        st.caption("My card")

    # MONEY OVERVIEW

    st.markdown("### Money overview")

    remaining = max(
        st.session_state["limit"] -
        st.session_state["spent"],
        0
    )

    x, y = st.columns(2)

    with x:
        st.markdown(
            f"""
            <div class="box">
                <div class="box-small">SPENT</div>
                <div style="font-size:25px;font-weight:900;">
                    ₹{st.session_state["spent"]:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with y:
        st.markdown(
            f"""
            <div class="box">
                <div class="box-small">REMAINING</div>
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
        <div class="box">
            <div class="box-title">
                VELORA SCORE
            </div>

            <div class="box-small">
                Based on your spending and saving activity.
            </div>

            <div class="score">
                84
            </div>

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
            "Spending": [350, 410, 520, 440, 480, 390, 460]
        },
        height=190
    )

    # GOAL

    st.markdown("### Savings goal")

    progress = (
        st.session_state["goal_saved"] /
        max(st.session_state["goal_target"], 1)
    )

    st.markdown(
        f"""
        <div class="goal">
            <div class="goal-name">
                🎧 {st.session_state["goal_name"]}
            </div>

            <div class="goal-money">
                ₹{st.session_state["goal_saved"]:,}
                saved of
                ₹{st.session_state["goal_target"]:,}
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

    # ACTIVITY

    st.markdown("### Recent activity")

    activities = [
        ("🟢 Pocket Money", "Money added", "+₹2,000", "green"),
        ("⚪ Food", "Payment", "−₹250", "white"),
        ("⚪ Study", "Payment", "−₹500", "white"),
        ("⚪ Shopping", "Payment", "−₹350", "white"),
        ("⚪ Gaming", "Payment", "−₹180", "white")
    ]

    for name, small, money, style in activities:

        st.markdown(
            f"""
            <div class="activity">
                <div class="activity-name">
                    {name}
                </div>

                <div class="activity-small">
                    {small}
                </div>

                <div class="{style}">
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
            <div class="box-title">
                ✦ VELORA INSIGHT
            </div>

            <div class="box-small">
                You're currently spending within your planned limit.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state["page"] == "Add":

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
        key="add_money_action",
        use_container_width=True
    ):

        st.session_state["balance"] += amount

        st.success(
            f"₹{amount:,} added successfully."
        )

    if st.button(
        "← Back",
        key="add_back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# SEND
# =========================================================

elif st.session_state["page"] == "Send":

    st.header("Send money")

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
        key="send_action",
        use_container_width=True
    ):

        if person == "":
            st.error("Enter recipient name.")

        elif amount > st.session_state["balance"]:
            st.error("Insufficient demo balance.")

        else:
            st.session_state["balance"] -= amount
            st.session_state["spent"] += amount

            st.success(
                f"₹{amount:,} sent successfully."
            )

    if st.button(
        "← Back",
        key="send_back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# REQUEST
# =========================================================

elif st.session_state["page"] == "Request":

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
        key="request_action",
        use_container_width=True
    ):

        st.success(
            f"₹{amount:,} request created."
        )

    if st.button(
        "← Back",
        key="request_back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# CARD
# =========================================================

elif st.session_state["page"] == "Card":

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

            <div class="card-bottom">
                VELORA MEMBER &nbsp;&nbsp; DEMO
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state["card_frozen"]:

        st.warning("🔒 Card is frozen.")

        if st.button(
            "Unfreeze card",
            key="unfreeze",
            use_container_width=True
        ):
            st.session_state["card_frozen"] = False
            st.rerun()

    else:

        st.success("● Card is active.")

        if st.button(
            "Freeze card",
            key="freeze",
            use_container_width=True
        ):
            st.session_state["card_frozen"] = True
            st.rerun()

    st.caption(
        "DEMO CARD · NO REAL PAYMENTS"
    )

    if st.button(
        "← Home",
        key="card_back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# BOTTOM NAV
# =========================================================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:
    if st.button(
        "⌂ Home",
        key="nav_home",
        use_container_width=True
    ):
        go("Home")

with n2:
    if st.button(
        "▣ Card",
        key="nav_card",
        use_container_width=True
    ):
        go("Card")

with n3:
    if st.button(
        "🎯 Goals",
        key="nav_goals",
        use_container_width=True
    ):
        st.info("Your savings goal is on the Home screen.")

with n4:
    if st.button(
        "◉ Profile",
        key="nav_profile",
        use_container_width=True
    ):
        st.info("Profile settings coming soon.")