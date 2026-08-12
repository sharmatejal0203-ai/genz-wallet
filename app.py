import streamlit as st

# =========================================================
# VELORA — SMART MONEY APP
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "name" not in st.session_state:
    st.session_state.name = "Alex"

if "limit" not in st.session_state:
    st.session_state.limit = 2000.0

if "goal_name" not in st.session_state:
    st.session_state.goal_name = "New Headphones"

if "goal_target" not in st.session_state:
    st.session_state.goal_target = 5000.0

if "goal_saved" not in st.session_state:
    st.session_state.goal_saved = 3400.0

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180]
    ]


# =========================================================
# CUSTOM STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #08090c;
}

.block-container {
    max-width: 520px;
    padding-top: 25px;
    padding-bottom: 100px;
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

h1, h2, h3 {
    color: white !important;
}

p, label {
    color: #a5a7ad !important;
}

.brand {
    font-size: 31px;
    font-weight: 900;
    color: white;
    letter-spacing: -1px;
}

.tagline {
    color: #777b84;
    font-size: 12px;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(
        135deg,
        #300c1b,
        #711938,
        #a52c52
    );
    padding: 25px;
    border-radius: 26px;
    margin: 15px 0;
}

.hero-label {
    font-size: 10px;
    color: #e3cbd3;
    letter-spacing: 2px;
}

.hero-money {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin-top: 5px;
}

.hero-small {
    color: #e0cbd3;
    font-size: 11px;
}

.box {
    background-color: #13151a;
    border: 1px solid #252831;
    padding: 18px;
    border-radius: 20px;
    margin: 10px 0;
}

.title {
    color: white;
    font-size: 14px;
    font-weight: 800;
}

.muted {
    color: #858891;
    font-size: 11px;
}

.score {
    font-size: 38px;
    color: white;
    font-weight: 900;
}

.card-design {
    background: linear-gradient(
        135deg,
        #16181d,
        #383b45
    );
    padding: 25px;
    border-radius: 25px;
    border: 1px solid #454852;
}

.card-number {
    color: white;
    font-size: 17px;
    letter-spacing: 3px;
    margin-top: 30px;
}

.nav-text {
    text-align: center;
    color: #777b84;
    font-size: 9px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCTIONS
# =========================================================

def home():
    st.session_state.page = "Home"
    st.rerun()


def spent():
    total = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            total += abs(item[2])

    return total


def category_amount(category):
    total = 0

    for item in st.session_state.transactions:
        if item[1] == category and item[2] < 0:
            total += abs(item[2])

    return total


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def score():

    total_spent = spent()

    spending_score = max(
        0,
        100 - int(
            total_spent /
            max(st.session_state.limit, 1)
            * 60
        )
    )

    saving_ratio = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    saving_score = int(
        min(saving_ratio * 40, 40)
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
        f"## Welcome back, {st.session_state.name}."
    )

    # Balance
    st.markdown(
        f"""
        <div class="hero">

            <div class="hero-label">
                AVAILABLE BALANCE
            </div>

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

    # Quick actions
    st.markdown("### Quick actions")

    a, b, c, d = st.columns(4)

    with a:
        if st.button("＋", use_container_width=True):
            st.session_state.page = "Add"
            st.rerun()
        st.caption("Add")

    with b:
        if st.button("↗", use_container_width=True):
            st.session_state.page = "Send"
            st.rerun()
        st.caption("Send")

    with c:
        if st.button("⇄", use_container_width=True):
            st.session_state.page = "Request"
            st.rerun()
        st.caption("Request")

    with d:
        if st.button("⌁", use_container_width=True):
            st.session_state.page = "Activity"
            st.rerun()
        st.caption("Activity")

    # Overview
    total_spent = spent()

    remaining = max(
        0,
        st.session_state.limit - total_spent
    )

    st.markdown("### Money overview")

    x, y = st.columns(2)

    with x:
        st.metric(
            "Spent",
            f"₹{total_spent:,.0f}"
        )

    with y:
        st.metric(
            "Remaining",
            f"₹{remaining:,.0f}"
        )

    # Score
    st.markdown("### Velora score")

    s1, s2 = st.columns([1, 2])

    with s1:
        st.markdown(
            f"""
            <div class="box">
                <div class="score">
                    {score()}
                </div>
                <div class="muted">
                    MONEY SCORE
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:

        if score() >= 80:
            message = "Excellent money habits."
        elif score() >= 60:
            message = "You're doing well."
        else:
            message = "Try spending a little less."

        st.markdown(
            f"""
            <div class="box">
                <div class="title">
                    {message}
                </div>

                <div class="muted">
                    Velora analyses your demo spending
                    and savings progress.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Chart
    st.markdown("### Weekly spending")

    chart_data = {
        "Monday": 120,
        "Tuesday": 180,
        "Wednesday": 90,
        "Thursday": 240,
        "Friday": 160,
        "Saturday": 280,
        "Sunday": 110
    }

    st.bar_chart(chart_data)

    # Categories
    st.markdown("### Spending categories")

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    for cat in categories:

        value = category_amount(cat)

        if value > 0:

            st.write(
                f"**{cat}** — ₹{value:,.0f}"
            )

            st.progress(
                min(
                    value / max(total_spent, 1),
                    1
                )
            )

    # Goal
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

    # Insight
    if category_amount("Shopping") > category_amount("Food"):

        insight = (
            "Shopping is currently your biggest "
            "tracked spending category."
        )

    else:

        insight = (
            "Your spending is currently staying "
            "within your tracked categories."
        )

    st.markdown("### ✦ Velora insight")

    st.info(insight)


# =========================================================
# ADD
# =========================================================

elif st.session_state.page == "Add":

    st.title("Add money")

    st.caption(
        "Add your own demo amount."
    )

    amount = st.number_input(
        "Amount",
        min_value=1,
        value=500,
        step=100
    )

    source = st.text_input(
        "Source",
        placeholder="Pocket money, gift, etc."
    )

    if st.button(
        "Add to Velora",
        use_container_width=True
    ):

        if source.strip() == "":
            st.error("Please enter a source.")

        else:

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.success(
                f"₹{amount:,.0f} added!"
            )

            st.session_state.page = "Home"
            st.rerun()

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# SEND
# =========================================================

elif st.session_state.page == "Send":

    st.title("Send money")

    st.caption(
        "Demo transfer — no real payment."
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

        if person.strip() == "":
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

            st.session_state.page = "Home"
            st.rerun()

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# REQUEST
# =========================================================

elif st.session_state.page == "Request":

    st.title("Request money")

    st.caption(
        "Create a demo payment request."
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
        placeholder="Lunch, trip, movie..."
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
        home()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.title("Activity")

    st.caption(
        "Your demo wallet history."
    )

    search = st.text_input(
        "Search",
        placeholder="Search transactions..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        text = (
            name + " " + category
        ).lower()

        if search.lower() not in text:
            continue

        found = True

        if amount >= 0:
            display_amount = (
                f"+₹{amount:,.0f}"
            )
        else:
            display_amount = (
                f"-₹{abs(amount):,.0f}"
            )

        st.markdown(
            f"""
            <div class="box">

                <div class="title">
                    {name}
                </div>

                <div class="muted">
                    {category}
                </div>

                <br>

                <b style="color:white;">
                    {display_amount}
                </b>

            </div>
            """,
            unsafe_allow_html=True
        )

    if not found:
        st.info("No transactions found.")

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# CARD
# =========================================================

elif st.session_state.page == "Card":

    st.title("Velora Card")

    st.caption(
        "Virtual demo card."
    )

    st.markdown(
        """
        <div class="card-design">

            <div style="
                color:#a5a8b0;
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
                color:#999da6;
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

        st.warning(
            "Your demo card is frozen."
        )

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.frozen = False
            st.rerun()

    else:

        st.success(
            "Your demo card is active."
        )

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.frozen = True
            st.rerun()

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.title("Savings goals")

    st.caption(
        "Plan for something you want."
    )

    name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    target = st.number_input(
        "Target amount",
        min_value=1,
        value=int(
            st.session_state.goal_target
        ),
        step=100
    )

    saved = st.number_input(
        "Already saved",
        min_value=0,
        value=int(
            st.session_state.goal_saved
        ),
        step=100
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal_name = name
        st.session_state.goal_target = target
        st.session_state.goal_saved = saved

        st.success(
            "Goal saved!"
        )

        st.rerun()

    progress = min(
        saved / max(target, 1),
        1
    )

    st.markdown(
        f"""
        <div class="box">

            <div class="title">
                🎯 {name}
            </div>

            <div class="muted">
                ₹{saved:,.0f}
                / ₹{target:,.0f}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.write(
        f"{progress * 100:.0f}% complete"
    )

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.title("Profile")

    st.caption(
        "Personalize your Velora."
    )

    name = st.text_input(
        "Name",
        value=st.session_state.name
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100,
        value=int(
            st.session_state.limit
        ),
        step=100
    )

    if st.button(
        "Save profile",
        use_container_width=True
    ):

        st.session_state.name = name
        st.session_state.limit = limit

        st.success(
            "Profile updated!"
        )

        st.rerun()

    st.markdown(
        """
        <div class="box">

            <div class="title">
                VELORA
            </div>

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

    if st.button(
        "← Back",
        use_container_width=True
    ):
        home()


# =========================================================
# BOTTOM NAVIGATION
# =========================================================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:

    if st.button(
        "⌂",
        use_container_width=True
    ):
        home()

    st.markdown(
        '<div class="nav-text">HOME</div>',
        unsafe_allow_html=True
    )

with n2:

    if st.button(
        "▣",
        use_container_width=True
    ):
        st.session_state.page = "Card"
        st.rerun()

    st.markdown(
        '<div class="nav-text">CARD</div>',
        unsafe_allow_html=True
    )

with n3:

    if st.button(
        "◇",
        use_container_width=True
    ):
        st.session_state.page = "Goals"
        st.rerun()

    st.markdown(
        '<div class="nav-text">GOALS</div>',
        unsafe_allow_html=True
    )

with n4:

    if st.button(
        "◉",
        use_container_width=True
    ):
        st.session_state.page = "Profile"
        st.rerun()

    st.markdown(
        '<div class="nav-text">PROFILE</div>',
        unsafe_allow_html=True
    )