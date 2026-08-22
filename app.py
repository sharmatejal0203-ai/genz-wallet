import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# =========================
# STYLE
# =========================

st.markdown("""
<style>
.stApp {
    background: #090A0F;
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 25px 18px 80px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: #F5F5F7 !important;
}

.stButton > button {
    background: #151820 !important;
    color: #FFFFFF !important;
    border: 1px solid #303542 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
}

[data-testid="stMetric"] {
    background: #12151C;
    border: 1px solid #292E38;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #8D929E !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.card {
    background: linear-gradient(145deg, #191D27, #101218);
    border: 1px solid #303542;
    border-radius: 24px;
    padding: 22px;
    margin: 15px 0;
}

.balance {
    font-size: 42px;
    font-weight: 850;
    margin-top: 5px;
}

.muted {
    color: #858B98 !important;
    font-size: 12px;
}

.purple {
    color: #A98CFF !important;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 15px;
    padding: 14px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)


# =========================
# SESSION STATE
# =========================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,
    "name": "Tejal",
    "page": "Home",
    "card_frozen": False,
    "transactions": [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ],
    "notifications": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================
# FUNCTIONS
# =========================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def total_spending():
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[2] < 0
    )


def category_spending(category):
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[1] == category and item[2] < 0
    )


# =========================
# HEADER
# =========================

st.markdown("# VELORA")
st.markdown(
    '<div class="muted">Intelligent money management</div>',
    unsafe_allow_html=True
)


# =========================
# NAVIGATION
# =========================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("HOME", use_container_width=True):
        go("Home")

with n2:
    if st.button("PAY", use_container_width=True):
        go("Pay")

with n3:
    if st.button("ACTIVITY", use_container_width=True):
        go("Activity")

with n4:
    if st.button("INSIGHT", use_container_width=True):
        go("Insight")

with n5:
    if st.button("PROFILE", use_container_width=True):
        go("Profile")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader(st.session_state.name)

    # BALANCE

    st.markdown(
        '<div class="card">'
        '<div class="muted">AVAILABLE BALANCE</div>'
        '<div class="balance">₹{:,.2f}</div>'
        '<div class="muted">Demo wallet · No real money connected</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    # ACTIONS

    a, b, c = st.columns(3)

    with a:
        add_clicked = st.button(
            "＋ ADD",
            use_container_width=True
        )

    with b:
        send_clicked = st.button(
            "↗ SEND",
            use_container_width=True
        )

    with c:
        request_clicked = st.button(
            "⇄ REQUEST",
            use_container_width=True
        )

    # ADD MONEY

    if add_clicked:

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="add_amount"
        )

        source = st.text_input(
            "Source",
            value="Pocket Money",
            key="add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="confirm_add"
        ):

            st.session_state.balance += amount

            add_transaction(
                source.strip() or "Income",
                "Income",
                amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to wallet.".format(amount)
            )

            st.success("Balance updated.")
            st.rerun()

    # REQUEST

    if request_clicked:

        st.markdown("### Request money")

        person = st.text_input(
            "From",
            placeholder="Friend's name",
            key="request_person"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True
        ):

            if not person.strip():

                st.error("Enter a name.")

            else:

                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} created.".format(amount)
                )

                st.success("Request created.")

    # FINANCIAL SNAPSHOT

    st.markdown("### Financial snapshot")

    spent = total_spending()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = (
        spent /
        max(st.session_state.monthly_limit, 1)
    )

    s1, s2 = st.columns(2)

    with s1:
        st.metric(
            "Spent this month",
            "₹{:,.0f}".format(spent)
        )

    with s2:
        st.metric(
            "Budget remaining",
            "₹{:,.0f}".format(remaining)
        )

    s3, s4 = st.columns(2)

    with s3:
        st.metric(
            "Savings",
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:

        if ratio < 0.8:
            score = 84
        elif ratio < 1:
            score = 72
        else:
            score = 58

        st.metric(
            "VELORA Score",
            "{}/100".format(score)
        )

    # STATUS

    if ratio < 0.6:

        st.success(
            "You're on track. Spending is comfortably below your limit."
        )

    elif ratio < 0.85:

        st.warning(
            "Watch your pace. You're approaching your monthly limit."
        )

    else:

        st.error(
            "Budget risk. Your spending is getting high."
        )

    # SPENDING TREND

    st.markdown("### Spending trend")

    chart = pd.DataFrame(
        {
            "Spending": [
                120,
                180,
                90,
                240,
                160,
                280,
                110
            ]
        },
        index=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]
    )

    st.line_chart(chart)

    # CATEGORIES

    st.markdown("### Where your money goes")

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
                "{} · ₹{:,.0f}".format(
                    category,
                    value
                )
            )

            st.progress(
                min(
                    value / max(spent, 1),
                    1
                )
            )

    # GOAL

    st.markdown("### Savings goal")

    progress = (
        st.session_state.goal_saved /
        max(st.session_state.goal_target, 1)
    )

    st.write(
        "🎯 " + st.session_state.goal_name
    )

    st.caption(
        "₹{:,.0f} of ₹{:,.0f}".format(
            st.session_state.goal_saved,
            st.session_state.goal_target
        )
    )

    st.progress(
        min(progress, 1)
    )


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Payments")

    st.caption(
        "Simulated payment · No real UPI or bank connection"
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Friend or contact"
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
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Other"
        ]
    )

    if st.button(
        "Send payment",
        use_container_width=True
    ):

        if not recipient.strip():

            st.error("Enter recipient.")

        elif amount > st.session_state.balance:

            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= amount

            add_transaction(
                "Sent to " + recipient.strip(),
                category,
                -amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} sent to {}.".format(
                    amount,
                    recipient.strip()
                )
            )

            st.success(
                "Payment simulated successfully."
            )

    st.divider()

    st.subheader("VELORA Card")

    st.markdown(
        '<div class="card">'
        '<b>VELORA</b><br><br>'
        '<span style="font-size:18px;letter-spacing:3px;">'
        '•••• •••• •••• 2840'
        '</span><br><br>'
        '<span class="muted">DEMO VIRTUAL CARD</span>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.error("CARD FROZEN")

        if st.button(
            "Unfreeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("CARD ACTIVE")

        if st.button(
            "Freeze card",
            use_container_width=True
        ):

            st.session_state.card_frozen = True
            st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.subheader("Activity")

    search = st.text_input(
        "Search transactions",
        placeholder="Food, shopping, recipient..."
    )

    found = False

    for name, category, amount in st.session_state.transactions:

        text = (
            name + " " + category
        ).lower()

        if search.lower() not in text:
            continue

        found = True

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            '<b>{}</b><br>'
            '<span class="muted">{}</span>'
            '<span style="float:right;font-weight:700;">'
            '{}₹{:,.0f}'
            '</span>'
            '</div>'.format(
                name,
                category,
                sign,
                abs(amount)
            ),
            unsafe_allow_html=True
        )

    if not found:

        st.info(
            "No matching transactions."
        )


# =========================================================
# INSIGHT
# =========================================================

elif st.session_state.page == "Insight":

    st.subheader("VELORA Intelligence")

    spent = total_spending()

    ratio = (
        spent /
        max(st.session_state.monthly_limit, 1)
    )

    categories = {}

    for category in [
        "Food",
        "Education",
        "Shopping",
        "Entertainment",
        "Travel"
    ]:

        value = category_spending(category)

        if value > 0:
            categories[category] = value

    if categories:

        biggest = max(
            categories,
            key=categories.get
        )

        biggest_value = categories[biggest]

    else:

        biggest = "None"
        biggest_value = 0

    if ratio < 0.6:

        title = "You're spending with control."

        message = (
            "Your spending is comfortably below "
            "your monthly limit."
        )

    elif ratio < 0.85:

        title = "Watch your spending pace."

        message = (
            "You're approaching your monthly limit. "
            "Keep upcoming purchases intentional."
        )

    else:

        title = "Your budget needs attention."

        message = (
            "Your current spending is close to "
            "or above your monthly limit."
        )

    st.markdown(
        '<div class="card">'
        '<div class="purple">VELORA INTELLIGENCE</div>'
        '<h3>{}</h3>'
        '<div class="muted">{}</div>'
        '</div>'.format(
            title,
            message
        ),
        unsafe_allow_html=True
    )

    i1, i2 = st.columns(2)

    with i1:
        st.metric(
            "Largest category",
            biggest
        )

    with i2:
        st.metric(
            "Budget used",
            "{:.0f}%".format(
                ratio * 100
            )
        )

    if biggest != "None":

        st.info(
            "{} is currently your largest spending category."
            .format(biggest)
        )

    left = (
        st.session_state.goal_target -
        st.session_state.goal_saved
    )

    if left > 0:

        st.info(
            "₹{:,.0f} remains to reach your {} goal."
            .format(
                left,
                st.session_state.goal_name
            )
        )

    else:

        st.success(
            "Your savings goal is complete."
        )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.subheader("Profile")

    name = st.text_input(
        "Name",
        value=st.session_state.name
    )

    limit = st.number_input(
        "Monthly spending limit",
        min_value=100.0,
        value=float(
            st.session_state.monthly_limit
        ),
        step=100.0
    )

    if st.button(
        "Save profile",
        use_container_width=True
    ):

        st.session_state.name = (
            name.strip() or "User"
        )

        st.session_state.monthly_limit = limit

        st.success(
            "Profile updated."
        )

        st.rerun()

    st.divider()

    st.subheader("Savings goal")

    goal_name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    goal_target = st.number_input(
        "Target amount",
        min_value=1.0,
        value=float(
            st.session_state.goal_target
        ),
        step=100.0
    )

    goal_saved = st.number_input(
        "Already saved",
        min_value=0.0,
        value=float(
            st.session_state.goal_saved
        ),
        step=100.0
    )

    if st.button(
        "Save goal",
        use_container_width=True
    ):

        st.session_state.goal_name = (
            goal_name.strip() or "My Goal"
        )

        st.session_state.goal_target = goal_target

        st.session_state.goal_saved = min(
            goal_saved,
            goal_target
        )

        st.success(
            "Goal updated."
        )

        st.rerun()

    st.divider()

    st.info(
        "VELORA is a prototype. "
        "No real money, UPI, bank or card connection."
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "VELORA · Intelligent money management · Demo Mode"
)