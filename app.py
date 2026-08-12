import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="💳",
    layout="centered"
)

# =====================================================
# THEME
# =====================================================

st.markdown("""
<style>
.stApp {
    background-color: #08090D;
}

.block-container {
    max-width: 540px;
    padding: 25px 18px 80px;
}

h1, h2, h3 {
    color: white !important;
}

p, label {
    color: #A5A7B0 !important;
}

[data-testid="stMetric"] {
    background: #14161D;
    border: 1px solid #292C36;
    border-radius: 18px;
    padding: 14px;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: #9295A0 !important;
}

.stButton > button {
    background: #15171E !important;
    color: white !important;
    border: 1px solid #30333D !important;
    border-radius: 14px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #A52B52 !important;
}

.stProgress > div > div > div > div {
    background-color: #A52B52;
}

[data-testid="stExpander"] {
    background: #12141A;
    border: 1px solid #292C36;
    border-radius: 16px;
}

hr {
    border-color: #292C36 !important;
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================

defaults = {
    "balance": 5000.0,
    "spent": 1260.0,
    "monthly_limit": 2000.0,
    "goal_name": "New Headphones",
    "goal_saved": 3400.0,
    "goal_target": 5000.0,
    "card_frozen": False,
    "name": "Tejal",
    "page": "Home",
    "transactions": [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ]
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# FUNCTIONS
# =====================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def total_spending():
    total = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            total += abs(item[2])

    return total


def category_spending(category):
    total = 0

    for item in st.session_state.transactions:
        if item[1] == category and item[2] < 0:
            total += abs(item[2])

    return total


# =====================================================
# HEADER
# =====================================================

st.title("VELORA")
st.caption("Smart money, made simple.")

# =====================================================
# NAVIGATION
# =====================================================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    if st.button("⌂ Home", use_container_width=True):
        go("Home")

with nav2:
    if st.button("▣ Card", use_container_width=True):
        go("Card")

with nav3:
    if st.button("◇ Goals", use_container_width=True):
        go("Goals")

with nav4:
    if st.button("◉ Profile", use_container_width=True):
        go("Profile")


# =====================================================
# HOME
# =====================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader(
        "Welcome back, " +
        st.session_state.name +
        " 👋"
    )

    # Balance
    st.subheader("Available balance")

    st.metric(
        "VELORA WALLET",
        "₹{:,.0f}".format(
            st.session_state.balance
        )
    )

    st.caption("Demo wallet · No real money")

    # Quick actions
    st.subheader("Quick actions")

    a, b, c = st.columns(3)

    with a:
        add = st.button(
            "＋ Add",
            use_container_width=True
        )

    with b:
        send = st.button(
            "↗ Send",
            use_container_width=True
        )

    with c:
        request = st.button(
            "⇄ Request",
            use_container_width=True
        )

    # Add
    if add:

        st.write("### Add money")

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

            if source.strip() == "":
                source = "Added Money"

            st.session_state.balance += amount

            add_transaction(
                source,
                "Income",
                amount
            )

            st.success(
                "₹{:,.0f} added.".format(amount)
            )

    # Send
    if send:

        st.write("### Send money")

        person = st.text_input(
            "Recipient",
            placeholder="Friend's name"
        )

        amount = st.number_input(
            "Amount to send",
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
            "Send",
            use_container_width=True
        ):

            if person.strip() == "":
                st.error("Enter recipient.")

            elif amount > st.session_state.balance:
                st.error("Insufficient demo balance.")

            else:

                st.session_state.balance -= amount
                st.session_state.spent += amount

                add_transaction(
                    "Sent to " + person,
                    category,
                    -amount
                )

                st.success(
                    "₹{:,.0f} sent.".format(amount)
                )

    # Request
    if request:

        st.write("### Request money")

        person = st.text_input(
            "Request from",
            placeholder="Friend's name"
        )

        amount = st.number_input(
            "Request amount",
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

            if person.strip() == "":
                st.error("Enter a name.")
            else:
                st.success(
                    "₹{:,.0f} request created.".format(
                        amount
                    )
                )

    # Overview
    st.divider()

    st.subheader("Money overview")

    spent = total_spending()

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

    # Score
    st.subheader("VELORA Score")

    score = 84

    if spent > st.session_state.monthly_limit:
        score = 65
    elif spent > st.session_state.monthly_limit * 0.8:
        score = 74

    st.metric(
        "Money health",
        "{}/100".format(score),
        "Good habits"
    )

    # Graph
    st.subheader("Spending trend")

    chart = {
        "Mon": 120,
        "Tue": 180,
        "Wed": 90,
        "Thu": 240,
        "Fri": 160,
        "Sat": 280,
        "Sun": 110
    }

    st.line_chart(chart)

    # Categories
    st.subheader("Spending categories")

    categories = [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]

    for category in categories:

        value = category_spending(category)

        if value > 0:

            st.write(
                "{} — ₹{:,.0f}".format(
                    category,
                    value
                )
            )

            percentage = min(
                value / max(spent, 1),
                1
            )

            st.progress(percentage)

    # Goal preview
    st.subheader("Savings goal")

    st.write(
        "🎧 " + st.session_state.goal_name
    )

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.caption(
        "₹{:,.0f} saved of ₹{:,.0f}".format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        )
    )

    st.progress(min(progress, 1.0))

    st.write(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    # Recent activity
    st.subheader("Recent activity")

    search = st.text_input(
        "Search transactions",
        placeholder="Search..."
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

            st.write(
                "🟢 {}   +₹{:,.0f}".format(
                    name,
                    amount
                )
            )

        else:

            st.write(
                "⚪ {}   −₹{:,.0f}".format(
                    name,
                    abs(amount)
                )
            )

        st.caption(category)

    if not found:
        st.info("No transactions found.")

    # Insight
    st.subheader("✦ Velora Insight")

    if spent >= st.session_state.monthly_limit:

        st.warning(
            "You've reached your monthly spending limit."
        )

    elif spent >= st.session_state.monthly_limit * 0.8:

        st.warning(
            "You're getting close to your monthly spending limit."
        )

    else:

        st.success(
            "Your spending is currently within your planned limit."
        )


# =====================================================
# CARD
# =====================================================

elif st.session_state.page == "Card":

    st.subheader("💳 Velora Card")

    st.info(
        "VELORA · DEMO CARD\n\n"
        "••••  ••••  ••••  2840\n\n"
        "VELORA MEMBER"
    )

    if st.session_state.card_frozen:

        st.warning("🔒 Your card is frozen.")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("🟢 Card is active.")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = True
            st.rerun()

    st.caption(
        "Demo card · No real payments"
    )


# =====================================================
# GOALS
# =====================================================

elif st.session_state.page == "Goals":

    st.subheader("🎯 Savings Goals")

    st.write(
        "Turn something you want into a plan."
    )

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

        st.success("Goal saved.")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.write(
        "🎯 " + st.session_state.goal_name
    )

    st.progress(min(progress, 1.0))

    st.write(
        "₹{:,.0f} / ₹{:,.0f} · {:.0f}%".format(
            st.session_state.goal_saved,
            st.session_state.goal_target,
            progress * 100
        )
    )


# =====================================================
# PROFILE
# =====================================================

elif st.session_state.page == "Profile":

    st.subheader("◉ Profile")

    name = st.text_input(
        "Your name",
        value=st.session_state.name
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

        st.session_state.name = name
        st.session_state.monthly_limit = limit

        st.success("Profile updated.")

    st.divider()

    st.write("### VELORA")

    st.caption(
        "Smart money management prototype."
    )

    st.caption(
        "Demo mode · No real payments."
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "VELORA · Smart Money Prototype · Demo Mode"
)