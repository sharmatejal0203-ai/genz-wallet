import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================================================
# STATE
# =========================================================

defaults = {
    "page": "Home",
    "balance": 5000.0,
    "name": "Alex",
    "limit": 2000.0,
    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,
    "frozen": False,
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
}

.block-container {
    max-width:520px;
    padding:25px 18px 90px;
}

#MainMenu, header, footer {
    visibility:hidden;
}

.brand {
    color:white;
    font-size:30px;
    font-weight:900;
    letter-spacing:-1px;
}

.tagline {
    color:#777b84;
    font-size:12px;
    margin-bottom:25px;
}

.hero {
    background:linear-gradient(135deg,#300c1b,#711938,#a52c52);
    border-radius:26px;
    padding:26px;
    margin:15px 0 22px;
}

.hero-label {
    color:#e2cbd3;
    font-size:10px;
    letter-spacing:2px;
}

.hero-money {
    color:white;
    font-size:42px;
    font-weight:900;
    margin:4px 0;
}

.hero-small {
    color:#ddc8d0;
    font-size:11px;
}

.box {
    background:#13151a;
    border:1px solid #252831;
    border-radius:20px;
    padding:18px;
    margin:10px 0;
}

.title {
    color:white;
    font-size:14px;
    font-weight:800;
}

.muted {
    color:#858891;
    font-size:11px;
}

.score {
    color:white;
    font-size:40px;
    font-weight:900;
}

.virtual-card {
    background:linear-gradient(135deg,#17191f,#3a3d47);
    border:1px solid #444752;
    border-radius:25px;
    padding:25px;
    margin:15px 0;
}

.card-number {
    color:white;
    font-size:17px;
    letter-spacing:3px;
    margin-top:30px;
}

.nav-text {
    color:#777b84;
    text-align:center;
    font-size:9px;
}

.stButton > button {
    border-radius:14px !important;
    min-height:44px !important;
    background:#15171c !important;
    color:white !important;
    border:1px solid #292d36 !important;
}

.stButton > button:hover {
    border-color:#a72b50 !important;
}

[data-testid="stMetric"] {
    background:#13151a;
    border:1px solid #252831;
    border-radius:18px;
}

[data-testid="stMetricValue"] {
    color:white !important;
}

input {
    background:#13151a !important;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCTIONS
# =========================================================

def go(page):
    st.session_state.page = page


def total_spent():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def category_spent(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def money_score():
    spent = total_spent()
    limit = max(st.session_state.limit, 1)

    spending_score = max(
        0,
        100 - int((spent / limit) * 60)
    )

    saving_ratio = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    saving_score = min(
        int(saving_ratio * 40),
        40
    )

    return min(
        100,
        spending_score + saving_score
    )


# =========================================================
# BRAND
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
        f"## Welcome back, {st.session_state.name}."
    )

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-label">AVAILABLE BALANCE</div>
            <div class="hero-money">
                ₹{st.session_state.balance:,.0f}
            </div>
            <div class="hero-small">
                DEMO WALLET · NO REAL MONEY
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Quick actions")

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

    spent = total_spent()

    remaining = max(
        0,
        st.session_state.limit - spent
    )

    st.markdown("### Money overview")

    x, y = st.columns(2)

    with x:
        st.metric("Spent", f"₹{spent:,.0f}")

    with y:
        st.metric("Remaining", f"₹{remaining:,.0f}")

    st.markdown("### Velora score")

    x, y = st.columns([1, 2])

    with x:
        st.markdown(
            f"""
            <div class="box">
                <div class="score">{money_score()}</div>
                <div class="muted">MONEY SCORE</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with y:

        if money_score() >= 80:
            msg = "Excellent money habits."
        elif money_score() >= 60:
            msg = "You're doing well."
        else:
            msg = "Try keeping spending lower."

        st.markdown(
            f"""
            <div class="box">
                <div class="title">{msg}</div>
                <div class="muted">
                    Your score combines spending and savings progress.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Weekly spending")

    st.bar_chart({
        "Mon": 120,
        "Tue": 180,
        "Wed": 90,
        "Thu": 240,
        "Fri": 160,
        "Sat": 280,
        "Sun": 110
    })

    st.markdown("### Spending categories")

    for category in [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]:

        amount = category_spent(category)

        if amount > 0:

            st.write(
                f"**{category}** · ₹{amount:,.0f}"
            )

            st.progress(
                min(amount / max(spent, 1), 1)
            )

    st.markdown("### Savings goal")

    progress = min(
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1),
        1
    )

    st.markdown(
        f"""
        <div class="box">
            <div class="title">
                🎧 {st.session_state.goal_name}
            </div>
            <div class="muted">
                ₹{st.session_state.goal_saved:,.0f}
                saved of
                ₹{st.session_state.goal_target:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.markdown("### ✦ Velora insight")

    if category_spent("Shopping") > category_spent("Food"):
        st.info(
            "Shopping is currently your biggest tracked category."
        )
    else:
        st.info(
            "Your spending is currently under your tracked plan."
        )


# =========================================================
# ADD
# =========================================================

elif st.session_state.page == "Add":

    st.title("Add money")

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
        "Add to Velora",
        use_container_width=True
    ):

        if not source.strip():
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

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# SEND
# =========================================================

elif st.session_state.page == "Send":

    st.title("Send money")

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
        "Send",
        use_container_width=True
    ):

        if not person.strip():
            st.error("Enter recipient.")

        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")

        else:
            st.session_state.balance -= amount

            add_transaction(
                "Sent to " + person,
                category,
                -amount
            )

            st.success(
                f"₹{amount:,.0f} sent."
            )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# REQUEST
# =========================================================

elif st.session_state.page == "Request":

    st.title("Request money")

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

        if not person.strip():
            st.error("Enter a name.")
        else:
            st.success(
                f"₹{amount:,.0f} request created."
            )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.title("Activity")

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, study..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        if search.lower() not in (
            name + " " + category
        ).lower():
            continue

        found = True

        sign = "+" if amount >= 0 else "-"
        value = abs(amount)

        st.markdown(
            f"""
            <div class="box">
                <div class="title">{name}</div>
                <div class="muted">{category}</div>
                <br>
                <b style="color:white;">
                    {sign}₹{value:,.0f}
                </b>
            </div>
            """,
            unsafe_allow_html=True
        )

    if not found:
        st.info("No transactions found.")

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# CARD
# =========================================================

elif st.session_state.page == "Card":

    st.title("Velora Card")

    st.caption("Virtual demo card")

    st.markdown(
        """
        <div class="virtual-card">

            <div style="
                color:#aaa;
                font-size:11px;
                letter-spacing:2px;
            ">
                VELORA · DEMO
            </div>

            <div style="
                font-size:25px;
                margin-top:25px;
            ">
                ▰
            </div>

            <div class="card-number">
                •••• •••• •••• 2840
            </div>

            <div style="
                color:#999;
                font-size:9px;
                margin-top:25px;
            ">
                VELORA MEMBER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.frozen:

        st.warning("Card is frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):
            st.session_state.frozen = False

    else:

        st.success("Card is active.")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):
            st.session_state.frozen = True

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.title("Savings goals")

    name = st.text_input(
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

        st.session_state.goal_name = name
        st.session_state.goal_target = target
        st.session_state.goal_saved = saved

        st.success("Goal saved!")

    progress = min(
        saved / max(target, 1),
        1
    )

    st.markdown(
        f"""
        <div class="box">
            <div class="title">🎯 {name}</div>
            <div class="muted">
                ₹{saved:,.0f} / ₹{target:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.write(
        f"{progress * 100:.0f}% complete"
    )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.title("Profile")

    name = st.text_input(
        "Your name",
        value=st.session_state.name
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100,
        value=int(st.session_state.limit),
        step=100
    )

    if st.button(
        "Save profile",
        use_container_width=True
    ):

        st.session_state.name = name
        st.session_state.limit = limit

        st.success("Profile updated!")


    st.markdown(
        """
        <div class="box">
            <div class="title">VELORA</div>
            <div class="muted">
                Smart money prototype
            </div>
            <br>
            <div class="muted">
                Demo mode · No real payments
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =========================================================
# BOTTOM NAVIGATION
# =========================================================

st.divider()

a, b, c, d = st.columns(4)

with a:
    if st.button("⌂", use_container_width=True):
        go("Home")
    st.markdown(
        '<div class="nav-text">HOME</div>',
        unsafe_allow_html=True
    )

with b:
    if st.button("▣", use_container_width=True):
        go("Card")
    st.markdown(
        '<div class="nav-text">CARD</div>',
        unsafe_allow_html=True
    )

with c:
    if st.button("◇", use_container_width=True):
        go("Goals")
    st.markdown(
        '<div class="nav-text">GOALS</div>',
        unsafe_allow_html=True
    )

with d:
    if st.button("◉", use_container_width=True):
        go("Profile")
    st.markdown(
        '<div class="nav-text">PROFILE</div>',
        unsafe_allow_html=True
    )