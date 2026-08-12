import streamlit as st

# =========================================================
# VELORA — PREMIUM SMART MONEY PROTOTYPE
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "page": "Home",
    "user_name": "Alex",
    "monthly_limit": 2000.0,

    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,

    "card_frozen": False,

    "transactions": [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180],
    ]
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:#08090c;
    color:#f5f5f7;
}

.block-container {
    max-width:520px;
    padding:24px 18px 100px;
}

#MainMenu,
header,
footer {
    visibility:hidden;
}

/* BRAND */

.brand {
    color:#ffffff;
    font-size:30px;
    font-weight:850;
    letter-spacing:-1.7px;
}

.tagline {
    color:#777b84;
    font-size:12px;
    margin-bottom:22px;
}

/* HERO */

.balance {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(255,255,255,.12),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #2b0c18,
            #671631,
            #a52a50
        );

    border-radius:28px;
    padding:27px;
    margin:18px 0;

    box-shadow:
        0 25px 60px rgba(110,20,55,.25);
}

.balance-label {
    color:#d9c4cc;
    font-size:10px;
    letter-spacing:2px;
}

.balance-value {
    color:#ffffff;
    font-size:43px;
    font-weight:850;
    letter-spacing:-2px;
    margin:5px 0;
}

.balance-small {
    color:#dccbd1;
    font-size:11px;
}

/* SECTION */

.section {
    color:#ffffff;
    font-size:13px;
    font-weight:750;
    margin-top:27px;
    margin-bottom:11px;
}

/* CARDS */

.card {
    background:#13151a;
    border:1px solid #252831;
    border-radius:20px;
    padding:18px;
    margin:11px 0;
}

/* BUTTONS */

.stButton > button {
    background:#15171c !important;
    color:#ffffff !important;
    border:1px solid #292d36 !important;
    border-radius:14px !important;
    min-height:45px !important;
    font-weight:650 !important;
}

.stButton > button:hover {
    border-color:#a72b50 !important;
    color:#ffffff !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background:#13151a;
    border:1px solid #252831;
    border-radius:18px;
    padding:14px;
}

[data-testid="stMetricValue"] {
    color:#ffffff !important;
}

/* INPUTS */

input,
textarea {
    background:#13151a !important;
    color:#ffffff !important;
}

[data-baseweb="select"] > div {
    background:#13151a !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background:#a72b50;
}

/* VIRTUAL CARD */

.virtual-card {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(255,255,255,.12),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #17191f,
            #363943
        );

    border:1px solid #41444e;
    border-radius:25px;
    padding:24px;
    margin:15px 0;

    box-shadow:
        0 18px 40px rgba(0,0,0,.28);
}

.card-top {
    color:#a5a8b0;
    font-size:10px;
    letter-spacing:2px;
}

.card-chip {
    font-size:25px;
    margin:25px 0 17px;
}

.card-number {
    color:#ffffff;
    font-size:17px;
    letter-spacing:3px;
}

.card-bottom {
    color:#9b9ea7;
    font-size:9px;
    margin-top:23px;
}

/* INSIGHT */

.insight {
    background:
        linear-gradient(
            135deg,
            #17131a,
            #21151c
        );

    border:1px solid #30262c;
    border-radius:20px;
    padding:19px;
}

.insight-icon {
    font-size:20px;
}

.insight-title {
    color:#ffffff;
    font-size:14px;
    font-weight:750;
    margin-top:7px;
}

.insight-text {
    color:#898c95;
    font-size:11px;
    line-height:1.5;
    margin-top:6px;
}

/* TRANSACTIONS */

.tx {
    background:#13151a;
    border:1px solid #252831;
    border-radius:18px;
    padding:15px;
    margin:9px 0;
}

.tx-name {
    color:#ffffff;
    font-size:13px;
    font-weight:700;
}

.tx-category {
    color:#777b84;
    font-size:10px;
    margin-top:4px;
}

.tx-positive {
    color:#63d697;
    font-weight:750;
    text-align:right;
}

.tx-negative {
    color:#ffffff;
    font-weight:750;
    text-align:right;
}

/* SCORE */

.score-card {
    background:#13151a;
    border:1px solid #252831;
    border-radius:22px;
    padding:20px;
    text-align:center;
}

.score-number {
    color:#ffffff;
    font-size:42px;
    font-weight:850;
}

.score-label {
    color:#777b84;
    font-size:10px;
    letter-spacing:2px;
}

/* NAV */

.nav-label {
    color:#777b84;
    font-size:9px;
    text-align:center;
}

/* DIVIDER */

hr {
    border-color:#252831;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def spending_total():

    total = 0

    for transaction in st.session_state.transactions:

        if transaction[2] < 0:
            total += abs(transaction[2])

    return total


def category_total(category):

    total = 0

    for transaction in st.session_state.transactions:

        if (
            transaction[1] == category
            and transaction[2] < 0
        ):
            total += abs(transaction[2])

    return total


def add_transaction(name, category, amount):

    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def velora_score():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    goal_ratio = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    spending_part = max(
        0,
        65 - (spent / limit * 65)
    )

    saving_part = min(
        goal_ratio * 35,
        35
    )

    return int(
        max(
            0,
            min(
                100,
                spending_part + saving_part
            )
        )
    )


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
        f"## Welcome back, {st.session_state.user_name}."
    )

    # -----------------------------------------------------
    # BALANCE
    # -----------------------------------------------------

    st.markdown(
        '<div class="balance">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="balance-label">'
        'AVAILABLE BALANCE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="balance-value">'
        f'₹{st.session_state.balance:,.0f}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="balance-small">'
        'VELORA DEMO WALLET · No real money'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # QUICK ACTIONS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    with a:

        if st.button(
            "＋",
            use_container_width=True
        ):
            go("Add")

        st.caption("Add")

    with b:

        if st.button(
            "↗",
            use_container_width=True
        ):
            go("Send")

        st.caption("Send")

    with c:

        if st.button(
            "⇄",
            use_container_width=True
        ):
            go("Request")

        st.caption("Request")

    with d:

        if st.button(
            "⌁",
            use_container_width=True
        ):
            go("Activity")

        st.caption("Activity")


    # -----------------------------------------------------
    # MONEY OVERVIEW
    # -----------------------------------------------------

    spent = spending_total()

    remaining = max(
        0,
        st.session_state.monthly_limit - spent
    )

    st.markdown(
        '<div class="section">MONEY OVERVIEW</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Spent",
            f"₹{spent:,.0f}"
        )

    with c2:

        st.metric(
            "Remaining",
            f"₹{remaining:,.0f}"
        )


    # -----------------------------------------------------
    # VELORA SCORE
    # -----------------------------------------------------

    score = velora_score()

    st.markdown(
        '<div class="section">VELORA SCORE</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1, 2])

    with left:

        st.markdown(
            f"""
            <div class="score-card">
                <div class="score-number">
                    {score}
                </div>

                <div class="score-label">
                    MONEY SCORE
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        if score >= 80:

            score_title = "Excellent habits"
            score_text = (
                "Your spending and savings are "
                "looking well balanced."
            )

        elif score >= 60:

            score_title = "You're doing well"
            score_text = (
                "A little more saving can improve "
                "your financial score."
            )

        else:

            score_title = "Needs attention"
            score_text = (
                "Try keeping your spending closer "
                "to your monthly plan."
            )

        st.markdown(
            f"""
            <div class="card">
                <div style="
                    color:white;
                    font-size:14px;
                    font-weight:750;
                ">
                    {score_title}
                </div>

                <div style="
                    color:#858891;
                    font-size:11px;
                    line-height:1.5;
                    margin-top:7px;
                ">
                    {score_text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # SPENDING TREND
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">SPENDING TREND</div>',
        unsafe_allow_html=True
    )

    weekly = {
        "Mon": 120,
        "Tue": 180,
        "Wed": 90,
        "Thu": 240,
        "Fri": 160,
        "Sat": 280,
        "Sun": 110
    }

    st.bar_chart(
        weekly,
        height=210
    )


    # -----------------------------------------------------
    # WHERE MONEY GOES
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">WHERE YOUR MONEY GOES</div>',
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

        value = category_total(category)

        if value > 0:

            left, right = st.columns([3, 1])

            with left:

                st.write(category)

            with right:

                st.write(
                    f"₹{value:,.0f}"
                )

            percentage = min(
                value / max(spent, 1),
                1
            )

            st.progress(
                percentage
            )


    # -----------------------------------------------------
    # SAVINGS GOAL
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">SAVINGS GOAL</div>',
        unsafe_allow_html=True
    )

    goal_progress = min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write(
        f"**{st.session_state.goal_name}**"
    )

    st.caption(
        f"₹{st.session_state.goal_saved:,.0f} "
        f"saved of "
        f"₹{st.session_state.goal_target:,.0f}"
    )

    st.progress(
        goal_progress
    )

    st.caption(
        f"{goal_progress * 100:.0f}% complete"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # SMART INSIGHT
    # -----------------------------------------------------

    shopping = category_total("Shopping")
    food = category_total("Food")
    education = category_total("Education")

    if shopping >= food and shopping >= education:

        insight_title = "Shopping is your biggest category."

        insight_text = (
            "Keep an eye on non-essential purchases "
            "to protect your savings goal."
        )

    elif food >= education:

        insight_title = "Food is taking the lead."

        insight_text = (
            "Small purchases can add up. "
            "Tracking them can help you stay on plan."
        )

    else:

        insight_title = "Your spending looks balanced."

        insight_text = (
            "You're currently keeping your spending "
            "within your planned categories."
        )

    st.markdown(
        '<div class="section">SMART INSIGHT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="insight">

            <div class="insight-icon">
                ✦
            </div>

            <div class="insight-title">
                {insight_title}
            </div>

            <div class="insight-text">
                {insight_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state.page == "Add":

    st.header("Add money")

    st.caption(
        "Add a simulated transaction to your wallet."
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

            st.error(
                "Enter a source."
            )

        else:

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.success(
                f"₹{amount:,.0f} added."
            )

            go("Home")

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# SEND MONEY
# =========================================================

elif st.session_state.page == "Send":

    st.header("Send money")

    st.caption(
        "Simulate a secure transfer."
    )

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

            st.error(
                "Enter recipient."
            )

        elif amount > st.session_state.balance:

            st.error(
                "Insufficient demo balance."
            )

        elif st.session_state.card_frozen:

            st.error(
                "Card is frozen."
            )

        else:

            st.session_state.balance -= amount

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

    st.caption(
        "Create a simulated payment request."
    )

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

            st.error(
                "Enter a name."
            )

        else:

            st.success(
                f"₹{amount:,.0f} request created."
            )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.header("Activity")

    st.caption(
        "Your complete demo wallet history."
    )

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, study..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        searchable = (
            f"{name} {category}"
        ).lower()

        if search.lower() not in searchable:

            continue

        found = True

        st.markdown(
            '<div class="tx">',
            unsafe_allow_html=True
        )

        left, right = st.columns([3, 1])

        with left:

            st.markdown(
                f'<div class="tx-name">'
                f'{name}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="tx-category">'
                f'{category}'
                f'</div>',
                unsafe_allow_html=True
            )

        with right:

            if amount >= 0:

                st.markdown(
                    f'<div class="tx-positive">'
                    f'+₹{amount:,.0f}'
                    f'</div>',
                    unsafe_allow_html=True
      