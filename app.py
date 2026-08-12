import streamlit as st

# =========================================================
# VELORA — PREMIUM FINANCE PROTOTYPE
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DEFAULT DATA
# =========================================================

def default_data():
    return {
        "balance": 5000.0,
        "user_name": "Alex",
        "monthly_limit": 2000.0,
        "goal_name": "New Headphones",
        "goal_target": 5000.0,
        "goal_saved": 3400.0,
        "onboarded": True,
        "card_frozen": False,
        "transactions": [
            ["Pocket Money", "Income", 2000],
            ["Food", "Food", -250],
            ["Study", "Education", -500],
            ["Shopping", "Shopping", -350],
            ["Gaming", "Entertainment", -180],
        ]
    }


if "data" not in st.session_state:
    st.session_state.data = default_data()

if "page" not in st.session_state:
    st.session_state.page = "Home"

d = st.session_state.data


# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #08090c;
    color: #f5f5f7;
}

.block-container {
    max-width: 520px;
    padding: 24px 18px 90px;
}

header, footer, #MainMenu {
    visibility: hidden;
}

/* BRAND */

.brand {
    font-family: Arial, sans-serif;
    font-size: 29px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #ffffff;
}

.tagline {
    color: #747780;
    font-size: 12px;
    margin-top: 2px;
    margin-bottom: 24px;
}

/* HERO */

.hero {
    padding: 28px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #32101d 0%,
        #701b38 55%,
        #a72b50 100%
    );
    box-shadow: 0 20px 55px rgba(120,20,55,.20);
    margin: 15px 0 20px;
}

.hero-label {
    color: #d7bec7;
    font-size: 10px;
    letter-spacing: 2px;
}

.hero-number {
    color: white;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -2px;
    margin: 5px 0;
}

.hero-small {
    color: #ddcbd2;
    font-size: 11px;
}

/* CARDS */

.card {
    background: #121419;
    border: 1px solid #242831;
    border-radius: 21px;
    padding: 19px;
    margin: 12px 0;
}

.section {
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin-top: 27px;
    margin-bottom: 10px;
}

/* HEALTH SCORE */

.score {
    text-align: center;
    padding: 20px;
}

.score-number {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
}

.score-label {
    color: #858891;
    font-size: 11px;
}

/* BUTTONS */

.stButton > button {
    background: #15171c !important;
    color: #ffffff !important;
    border: 1px solid #292d36 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    border-color: #a72b50 !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #121419;
    border: 1px solid #242831;
    border-radius: 18px;
    padding: 14px;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

/* INPUTS */

input {
    background: #121419 !important;
    color: white !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background: #a72b50;
}

/* NOTIFICATION */

.notice {
    background: #15171c;
    border: 1px solid #292d36;
    border-radius: 17px;
    padding: 15px;
    margin: 9px 0;
}

.notice-title {
    color: white;
    font-weight: 700;
    font-size: 13px;
}

.notice-text {
    color: #858891;
    font-size: 11px;
    margin-top: 3px;
}

/* VIRTUAL CARD */

.virtual-card {
    background: linear-gradient(
        135deg,
        #181a20,
        #343740
    );
    border: 1px solid #41444e;
    border-radius: 24px;
    padding: 24px;
    margin: 15px 0;
}

.card-brand {
    color: #ffffff;
    font-weight: 700;
    letter-spacing: 1px;
}

.card-chip {
    font-size: 25px;
    margin: 25px 0 18px;
}

.card-number {
    font-size: 17px;
    letter-spacing: 3px;
}

.card-footer {
    color: #8e9199;
    font-size: 9px;
    margin-top: 23px;
}

hr {
    border-color: #242831;
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
    total = 0

    for tx in d["transactions"]:
        if tx[2] < 0:
            total += abs(tx[2])

    return total


def category_spending(category):
    total = 0

    for tx in d["transactions"]:
        if tx[1] == category and tx[2] < 0:
            total += abs(tx[2])

    return total


def add_transaction(name, category, amount):
    d["transactions"].insert(
        0,
        [name, category, amount]
    )


def health_score():
    spent = spending()

    budget_score = max(
        0,
        40 - int((spent / max(d["monthly_limit"], 1)) * 40)
    )

    saving_score = int(
        min(
            (d["goal_saved"] / max(d["goal_target"], 1)) * 40,
            40
        )
    )

    consistency = 20

    score = budget_score + saving_score + consistency

    return min(100, max(0, score))


# =========================================================
# ONBOARDING
# =========================================================

if not d["onboarded"]:

    st.markdown(
        '<div style="margin-top:80px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand">VELORA</div>',
        unsafe_allow_html=True
    )

    st.caption("A smarter way to manage your money.")

    st.markdown("## Let's set up your wallet.")

    name = st.text_input(
        "Your name",
        placeholder="Enter your name"
    )

    budget = st.number_input(
        "Monthly spending limit",
        min_value=100,
        value=2000,
        step=100
    )

    goal = st.text_input(
        "First savings goal",
        placeholder="Something you're saving for"
    )

    target = st.number_input(
        "Goal target",
        min_value=100,
        value=5000,
        step=100
    )

    if st.button(
        "Create my Velora",
        use_container_width=True
    ):

        if name.strip() == "":
            st.error("Enter your name.")

        else:

            d["user_name"] = name
            d["monthly_limit"] = budget
            d["goal_name"] = goal if goal else "My Goal"
            d["goal_target"] = target
            d["goal_saved"] = 0
            d["onboarded"] = True

            st.session_state.page = "Home"

            st.rerun()

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">'
    'A smarter way to manage your money.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD AFTERNOON")

    st.markdown(
        f"## Welcome back, {d['user_name']}."
    )

    # Balance

    st.markdown(
        '<div class="hero">'
        '<div class="hero-label">AVAILABLE BALANCE</div>'
        f'<div class="hero-number">₹{d["balance"]:,.0f}</div>'
        '<div class="hero-small">'
        'DEMO WALLET · No real money'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # Actions

    st.markdown(
        '<div class="section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    a, b, c, e = st.columns(4)

    with a:
        if st.button("＋", use_container_width=True):
            go("Add")
        st.caption("Add")

    with b:
        if st.button("↗", use_container_width=True):
            go("Send")
        st.caption("Send")

    with c:
        if st.button("⇄", use_container_width=True):
            go("Request")
        st.caption("Request")

    with e:
        if st.button("◉", use_container_width=True):
            go("Insights")
        st.caption("Insights")


    # Health

    score = health_score()

    if score >= 80:
        health_text = "Excellent"
    elif score >= 60:
        health_text = "Healthy"
    elif score >= 40:
        health_text = "Watch"
    else:
        health_text = "Needs attention"

    st.markdown(
        '<div class="section">MONEY HEALTH</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card score">'
        f'<div class="score-number">{score}</div>'
        '<div class="score-label">VELORA SCORE</div>'
        f'<div style="margin-top:8px;color:#c9cbd0;">'
        f'{health_text}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # Overview

    spent = spending()

    remaining = max(
        0,
        d["monthly_limit"] - spent
    )

    st.markdown(
        '<div class="section">THIS MONTH</div>',
        unsafe_allow_html=True
    )

    m1, m2 = st.columns(2)

    with m1:
        st.metric(
            "Spent",
            f"₹{spent:,.0f}"
        )

    with m2:
        st.metric(
            "Budget left",
            f"₹{remaining:,.0f}"
        )


    # Trend

    st.markdown(
        '<div class="section">SPENDING TREND</div>',
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

    st.line_chart(
        chart,
        height=210
    )


    # Goal

    st.markdown(
        '<div class="section">YOUR GOAL</div>',
        unsafe_allow_html=True
    )

    progress = min(
        d["goal_saved"] /
        max(d["goal_target"], 1),
        1
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write(f"**{d['goal_name']}**")

    st.caption(
        f"₹{d['goal_saved']:,.0f} saved "
        f"of ₹{d['goal_target']:,.0f}"
    )

    st.progress(progress)

    st.caption(
        f"{progress * 100:.0f}% complete"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Smart insight

    if spent > d["monthly_limit"] * 0.8:

        st.warning(
            "VELORA INSIGHT · You're approaching your monthly limit."
        )

    elif d["goal_saved"] >= d["goal_target"] * 0.75:

        st.success(
            "VELORA INSIGHT · Your goal is almost there."
        )

    else:

        st.info(
            "VELORA INSIGHT · Your spending is currently on track."
        )


# =========================================================
# INSIGHTS
# =========================================================

elif st.session_state.page == "Insights":

    st.header("Insights")

    st.caption(
        "Understand your money without the noise."
    )

    spent = spending()

    # Main metric

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.caption("TOTAL SPENDING")

    st.markdown(
        f"### ₹{spent:,.0f}"
    )

    budget_percent = min(
        spent / max(d["monthly_limit"], 1),
        1
    )

    st.progress(budget_percent)

    st.caption(
        f"{budget_percent * 100:.0f}% of your monthly budget used"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Categories

    st.markdown(
        '<div class="section">CATEGORY BREAKDOWN</div>',
        unsafe_allow_html=True
    )

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    for category in categories:

        amount = category_spending(category)

        if amount > 0:

            c1, c2 = st.columns([3, 1])

            with c1:
                st.write(category)

            with c2:
                st.write(f"₹{amount:,.0f}")

            st.progress(
                min(amount / max(spent, 1), 1)
            )


    # Savings

    st.markdown(
        '<div class="section">SAVINGS PROGRESS</div>',
        unsafe_allow_html=True
    )

    savings_percent = min(
        d["goal_saved"] /
        max(d["goal_target"], 1),
        1
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write(
        f"**{d['goal_name']}**"
    )

    st.progress(savings_percent)

    st.caption(
        f"{savings_percent * 100:.0f}% of your goal completed"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # AI-style insights

    st.markdown(
        '<div class="section">VELORA INSIGHTS</div>',
        unsafe_allow_html=True
    )

    if category_spending("Food") > 300:

        st.markdown(
            '<div class="notice">'
            '<div class="notice-title">'
            'Food is your biggest category'
            '</div>'
            '<div class="notice-text">'
            'Consider setting a weekly food budget.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if savings_percent >= 0.7:

        st.markdown(
            '<div class="notice">'
            '<div class="notice-title">'
            'You are close to your goal'
            '</div>'
            '<div class="notice-text">'
            'Keep your current saving pace.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if spent < d["monthly_limit"] * 0.5:

        st.markdown(
            '<div class="notice">'
            '<div class="notice-title">'
            'Strong budget control'
            '</div>'
            '<div class="notice-text">'
            'You have used less than half of your monthly budget.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if st.button(
        "← Back to Home",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# NOTIFICATIONS
# =========================================================

elif st.session_state.page == "Notifications":

    st.header("Notifications")

    st.caption(
        "Important updates from Velora."
    )

    spent = spending()

    if spent >= d["monthly_limit"] * 0.8:

        st.markdown(
            '<div class="notice">'
            '<div class="notice-title">'
            'Budget alert'
            '</div>'
            '<div class="notice-text">'
            'You have used more than 80% of your monthly budget.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if d["goal_saved"] >= d["goal_target"] * 0.75:

        st.markdown(
            '<div class="notice">'
            '<div class="notice-title">'
            'Goal milestone'
            '</div>'
            '<div class="notice-text">'
            'You have crossed 75% of your savings goal.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="notice">'
        '<div class="notice-title">'
        'Velora is ready'
        '</div>'
        '<div class="notice-text">'
        'Your demo wallet is up to date.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# ADD MONEY
# =========================================================

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

        if source.strip() == "":
            st.error("Enter a source.")

        else:

            d["balance"] += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.success(
                f"₹{amount:,.0f} added successfully."
            )

            go("Home")

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

    recipient = st.text_input(
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

        if recipient.strip() == "":
            st.error("Enter recipient.")

        elif amount > d["balance"]:
            st.error("Insufficient demo balance.")

        else:

            d["balance"] -= amount

            add_transaction(
                f"Sent to {recipient}",
                category,
                -amount
            )

            st.success(
                f"₹{amount:,.0f} sent."
            )

            go("Home")

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

        if person.strip() == "":
            st.error("Enter a name.")

        else:
            st.success(
                f"₹{amount:,.0f} request created for {person}."
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

    st.header("Velora Card")

    st.caption(
        "Your virtual demo card."
    )

    status = "FROZEN" if d["card_frozen"] else "ACTIVE"

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-chip">▰</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        f'<div class="card-footer">'
        f'{status} · DEMO CARD'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if d["card_frozen"]:

        st.warning("Your demo card is frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            d["card_frozen"] = False
            st.rerun()

    else:

        st.success("Your demo card is active.")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            d["card_frozen"] = True
            st.rerun()

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# GOALS
# =========================================================

elif st