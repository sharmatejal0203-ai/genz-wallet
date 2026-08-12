import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# ---------------- STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "name" not in st.session_state:
    st.session_state.name = "Alex"

if "limit" not in st.session_state:
    st.session_state.limit = 2000

if "goal" not in st.session_state:
    st.session_state.goal = "New Headphones"

if "target" not in st.session_state:
    st.session_state.target = 5000

if "saved" not in st.session_state:
    st.session_state.saved = 3400

if "frozen" not in st.session_state:
    st.session_state.frozen = False

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000],
        ["Food", "Food", -250],
        ["Study", "Education", -500],
        ["Shopping", "Shopping", -350],
        ["Gaming", "Entertainment", -180],
    ]


# ---------------- STYLE ----------------

st.markdown("""
<style>

.stApp {
    background:#07080b;
}

.block-container {
    max-width:520px;
    padding:25px 18px 80px;
}

#MainMenu {
    visibility:hidden;
}

header {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

.brand {
    color:white;
    font-size:32px;
    font-weight:900;
    letter-spacing:-1px;
}

.sub {
    color:#777b85;
    font-size:12px;
    margin-bottom:25px;
}

.hero {
    background:linear-gradient(135deg,#260b17,#701b39,#a72b52);
    border-radius:28px;
    padding:26px;
    margin:15px 0 22px;
}

.hero small {
    color:#dfc7d0;
    letter-spacing:2px;
}

.money {
    color:white;
    font-size:43px;
    font-weight:900;
    margin:5px 0;
}

.card {
    background:#13151a;
    border:1px solid #272a32;
    border-radius:20px;
    padding:18px;
    margin:10px 0;
}

.white {
    color:white;
    font-weight:800;
}

.grey {
    color:#858992;
    font-size:11px;
}

.vcard {
    background:linear-gradient(135deg,#181a20,#41444e);
    border-radius:26px;
    padding:25px;
    border:1px solid #4b4e59;
}

.number {
    color:white;
    font-size:17px;
    letter-spacing:3px;
    margin-top:35px;
}

.stButton > button {
    background:#15171c !important;
    color:white !important;
    border:1px solid #292d35 !important;
    border-radius:14px !important;
    min-height:45px !important;
}

.stButton > button:hover {
    border-color:#a72b52 !important;
}

[data-testid="stMetric"] {
    background:#13151a;
    border:1px solid #272a32;
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


# ---------------- FUNCTIONS ----------------

def go(page):
    st.session_state.page = page


def spent():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def category_total(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


# ---------------- HEADER ----------------

st.markdown(
    '<div class="brand">VELORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">Smart money, made simple.</div>',
    unsafe_allow_html=True
)


# =====================================================
# HOME
# =====================================================

if st.session_state.page == "Home":

    st.caption("GOOD AFTERNOON")

    st.markdown(
        f"## Welcome back, {st.session_state.name}"
    )

    st.markdown(
        f"""
        <div class="hero">
            <small>AVAILABLE BALANCE</small>
            <div class="money">
                ₹{st.session_state.balance:,.0f}
            </div>
            <div class="grey">
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

    total = spent()
    remaining = max(
        0,
        st.session_state.limit - total
    )

    st.markdown("### Money overview")

    x, y = st.columns(2)

    with x:
        st.metric(
            "Spent",
            f"₹{total:,.0f}"
        )

    with y:
        st.metric(
            "Remaining",
            f"₹{remaining:,.0f}"
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

    st.markdown("### Spending")

    for cat in [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]:

        value = category_total(cat)

        if value > 0:
            st.write(
                f"**{cat}** · ₹{value:,.0f}"
            )

            st.progress(
                min(value / max(total, 1), 1)
            )

    st.markdown("### Savings goal")

    progress = min(
        st.session_state.saved /
        max(st.session_state.target, 1),
        1
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="white">
                🎧 {st.session_state.goal}
            </div>
            <div class="grey">
                ₹{st.session_state.saved:,.0f}
                saved of
                ₹{st.session_state.target:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.info(
        "✦ Velora insight: Keep tracking your spending "
        "to build healthier money habits."
    )


# =====================================================
# ADD MONEY
# =====================================================

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
        "Add to wallet",
        use_container_width=True
    ):

        if source.strip() == "":
            st.error("Enter a source.")

        else:
            st.session_state.balance += amount

            st.session_state.transactions.insert(
                0,
                [source, "Income", amount]
            )

            st.success(
                f"₹{amount:,.0f} added!"
            )

            go("Home")

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# SEND
# =====================================================

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
        "Send money",
        use_container_width=True
    ):

        if person.strip() == "":
            st.error("Enter recipient.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= amount

            st.session_state.transactions.insert(
                0,
                [
                    "Sent to " + person,
                    category,
                    -amount
                ]
            )

            st.success(
                f"₹{amount:,.0f} sent!"
            )

            go("Home")

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# REQUEST
# =====================================================

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

        if person.strip() == "":
            st.error("Enter a name.")
        else:
            st.success(
                f"₹{amount:,.0f} request created."
            )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# ACTIVITY
# =====================================================

elif st.session_state.page == "Activity":

    st.title("Activity")

    search = st.text_input(
        "Search transactions",
        placeholder="Search..."
    )

    for name, category, amount in st.session_state.transactions:

        if search.lower() not in (
            name + category
        ).lower():
            continue

        sign = "+" if amount >= 0 else "-"
        value = abs(amount)

        st.markdown(
            f"""
            <div class="card">
                <div class="white">{name}</div>
                <div class="grey">{category}</div>
                <br>
                <b style="color:white">
                    {sign}₹{value:,.0f}
                </b>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# CARD
# =====================================================

elif st.session_state.page == "Card":

    st.title("Velora Card")

    st.caption("Virtual demo card")

    st.markdown(
        """
        <div class="vcard">

            <div class="grey">
                VELORA · DEMO
            </div>

            <div style="font-size:28px;margin-top:20px;">
                ▰
            </div>

            <div class="number">
                •••• •••• •••• 2840
            </div>

            <div class="grey" style="margin-top:25px;">
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


# =====================================================
# GOALS
# =====================================================

elif st.session_state.page == "Goals":

    st.title("Savings goals")

    name = st.text_input(
        "Goal",
        value=st.session_state.goal
    )

    target = st.number_input(
        "Target amount",
        min_value=1,
        value=int(st.session_state.target),
        step=100
    )

    saved = st.number_input(
        "Already saved",
        min_value=0,
        value=int(st.session_state.saved),
        step=100
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal = name
        st.session_state.target = target
        st.session_state.saved = saved

        st.success("Goal saved!")

    progress = min(
        saved / max(target, 1),
        1
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="white">
                🎯 {name}
            </div>
            <div class="grey">
                ₹{saved:,.0f} / ₹{target:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# PROFILE
# =====================================================

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
        <div class="card">
            <div class="white">VELORA</div>
            <div class="grey">
                Smart money prototype
            </div>
            <br>
            <div class="grey">
                DEMO MODE · NO REAL PAYMENTS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← Back", use_container_width=True):
        go("Home")


# =====================================================
# NAVIGATION
# =====================================================

st.divider()

a, b, c, d = st.columns(4)

with a:
    if st.button("⌂", use_container_width=True):
        go("Home")
    st.caption("Home")

with b:
    if st.button("▣", use_container_width=True):
        go("Card")
    st.caption("Card")

with c:
    if st.button("◇", use_container_width=True):
        go("Goals")
    st.caption("Goals")

with d:
    if st.button("◉", use_container_width=True):
        go("Profile")
    st.caption("Profile")