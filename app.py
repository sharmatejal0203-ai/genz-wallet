import streamlit as st

# =========================================================
# VELORA — SMART MONEY PROTOTYPE
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
    background: #08090c;
}

.block-container {
    max-width: 500px;
    padding: 25px 18px 90px;
}

#MainMenu, header, footer {
    visibility: hidden;
}

/* BRAND */

.brand {
    color: white;
    font-size: 29px;
    font-weight: 800;
    letter-spacing: -1.5px;
}

.tagline {
    color: #777b84;
    font-size: 12px;
    margin-bottom: 24px;
}

/* BALANCE */

.balance {
    background: linear-gradient(135deg, #35101d, #7f1d3c, #a72b50);
    border-radius: 27px;
    padding: 27px;
    margin: 18px 0;
    box-shadow: 0 22px 50px rgba(120,20,55,.22);
}

.balance-label {
    color: #d9c4cc;
    font-size: 10px;
    letter-spacing: 2px;
}

.balance-value {
    color: white;
    font-size: 43px;
    font-weight: 800;
    letter-spacing: -2px;
    margin: 5px 0;
}

.balance-small {
    color: #dccbd1;
    font-size: 11px;
}

/* CARDS */

.card {
    background: #13151a;
    border: 1px solid #252831;
    border-radius: 20px;
    padding: 18px;
    margin: 12px 0;
}

.section {
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin-top: 27px;
    margin-bottom: 11px;
}

/* BUTTONS */

.stButton > button {
    background: #15171c !important;
    color: white !important;
    border: 1px solid #292d36 !important;
    border-radius: 14px !important;
    min-height: 45px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    border-color: #a72b50 !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #13151a;
    border: 1px solid #252831;
    border-radius: 18px;
    padding: 14px;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

/* INPUT */

input {
    background: #13151a !important;
    color: white !important;
}

/* PROGRESS */

.stProgress > div > div > div > div {
    background: #a72b50;
}

/* VIRTUAL CARD */

.virtual-card {
    background: linear-gradient(135deg, #17191f, #30323a);
    border: 1px solid #3a3d47;
    border-radius: 23px;
    padding: 23px;
    margin: 12px 0;
}

.card-top {
    color: #999da6;
    font-size: 11px;
    letter-spacing: 2px;
}

.card-chip {
    font-size: 25px;
    margin: 23px 0 16px;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
}

.card-bottom {
    color: #9b9ea7;
    font-size: 9px;
    margin-top: 22px;
}

/* TRANSACTION */

.transaction {
    padding: 10px 0;
}

/* DIVIDER */

hr {
    border-color: #252831;
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
        if transaction[1] == category and transaction[2] < 0:
            total += abs(transaction[2])

    return total


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">A smarter way to manage your money.</div>',
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

    # Balance
    st.markdown(
        '<div class="balance">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="balance-label">AVAILABLE BALANCE</div>',
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
        'DEMO WALLET · No real money'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Quick actions
    st.markdown(
        '<div class="section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

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

    with d:
        if st.button("⌁", use_container_width=True):
            go("Activity")
        st.caption("Activity")


    # Overview
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


    # Spending graph
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

    st.line_chart(
        weekly,
        height=220
    )


    # Categories
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
                st.write(f"₹{value:,.0f}")

            percentage = min(
                value / max(spent, 1),
                1
            )

            st.progress(percentage)


    # Goal
    st.markdown(
        '<div class="section">SAVINGS GOAL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write(
        f"**{st.session_state.goal_name}**"
    )

    goal_progress = min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )

    st.caption(
        f"₹{st.session_state.goal_saved:,.0f} "
        f"of ₹{st.session_state.goal_target:,.0f}"
    )

    st.progress(goal_progress)

    st.caption(
        f"{goal_progress * 100:.0f}% complete"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # Insight
    if spent > st.session_state.monthly_limit * 0.8:

        st.warning(
            "VELORA INSIGHT · You're approaching your monthly spending limit."
        )

    else:

        st.success(
            "VELORA INSIGHT · Your spending is currently under control."
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

            st.error("Enter a source.")

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

            st.error("Enter recipient.")

        elif amount > st.session_state.balance:

            st.error("Insufficient demo balance.")

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
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.header("Activity")

    st.caption(
        "Your complete demo wallet history."
    )

    search = st.text_input(
        "Search",
        placeholder="Search transactions..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        text = f"{name} {category}".lower()

        if search.lower() not in text:
            continue

        found = True

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        left, right = st.columns([3, 1])

        with left:

            st.write(
                f"**{name}**"
            )

            st.caption(category)

        with right:

            if amount >= 0:

                st.markdown(
                    f'<div style="color:#64d497;'
                    f'text-align:right;font-weight:700;">'
                    f'+₹{amount:,.0f}</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f'<div style="color:white;'
                    f'text-align:right;font-weight:700;">'
                    f'−₹{abs(amount):,.0f}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)


    if not found:
        st.info("No transactions found.")


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

    st.markdown(
        '<div class="virtual-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-top">VELORA · DEMO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-chip">▰</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-bottom">'
        'VELORA MEMBER&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEMO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.card_frozen:

        st.warning("Card is currently frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("Card is active.")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = True
            st.rerun()


    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.header("Goals")

    st.caption(
        "Turn something you want into something you can plan for."
    )

    goal_name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    target = st.number_input(
        "Target amount",
        min_value=1,
        value=int(st.session_state.goal_target),
        step=100
    )

    saved = st.number_input(
        "Already saved",
        min_value=0,
        value=int(st.session_state.goal_saved),
        step=100
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal_name = goal_name
        st.session_state.goal_target = target
        st.session_state.goal_saved = saved

        st.success("Goal updated.")
        st.rerun()


    progress = min(
        saved / max(target, 1),
        1
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write(f"**{goal_name}**")

    st.progress(progress)

    st.caption(
        f"₹{saved:,.0f} / ₹{target:,.0f} · "
        f"{progress * 100:.0f}% complete"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.header("Profile")

    st.caption(
        "Personalize your Velora experience."
    )

    name = st.text_input(
        "Your name",
        value=st.session_state.user_name
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100,
        value=int(st.session_state.monthly_limit),
        step=100
    )

    if st.button(
        "Save profile",
        use_container_width=True
    ):

        st.session_state.user_name = name
        st.session_state.monthly_limit = limit

        st.success("Profile updated.")
        st.rerun()


    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write("**VELORA**")
    st.caption("Personal finance prototype")
    st.caption("Demo mode · No real payments")

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# BOTTOM NAVIGATION
# =========================================================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:

    if st.button(
        "⌂ Home",
        use_container_width=True
    ):
        go("Home")

with n2:

    if st.button(
        "▣ Card",
        use_container_width=True
    ):
        go("Card")

with n3:

    if st.button(
        "◇ Goals",
        use_container_width=True
    ):
        go("Goals")

with n4:

    if st.button(
        "◉ Profile",
        use_container_width=True
    ):
        go("Profile")