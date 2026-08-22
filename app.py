import streamlit as st
import pandas as pd

# =========================================================
# VELORA 4.0
# Intelligent Money Management
# Demo only — no real payments or bank connection
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #20243A 0%, #0B0C11 40%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 580px;
    padding: 24px 17px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4, p, label {
    color: #F5F5F7 !important;
}

.stButton > button {
    background: #151821 !important;
    color: #FFFFFF !important;
    border: 1px solid #303542 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    border-color: #9B7BFF !important;
    background: #1B1E28 !important;
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
    color: #858B98 !important;
}

.stProgress > div > div > div > div {
    background: #9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background: #11141A !important;
    color: #FFFFFF !important;
}

.card {
    background: linear-gradient(145deg, #1A1E28, #101217);
    border: 1px solid #303542;
    border-radius: 24px;
    padding: 22px;
    margin: 14px 0;
}

.brand {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 4px;
}

.tagline {
    color: #858B98;
    font-size: 11px;
    letter-spacing: 1px;
}

.balance-label {
    color: #858B98;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}

.balance {
    color: #FFFFFF;
    font-size: 43px;
    font-weight: 900;
    letter-spacing: -2px;
    margin: 5px 0;
}

.muted {
    color: #858B98 !important;
    font-size: 11px;
}

.section {
    color: #F5F5F7;
    font-size: 18px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
}

.insight {
    background: linear-gradient(145deg, #191522, #101116);
    border: 1px solid #44365D;
    border-radius: 21px;
    padding: 20px;
    margin: 14px 0;
}

.insight-label {
    color: #A98CFF;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
}

.insight-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 850;
    margin-top: 7px;
}

.insight-text {
    color: #9A9DA8;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 5px;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 15px;
    padding: 14px;
    margin: 7px 0;
}

.virtual-card {
    background: linear-gradient(135deg, #252938, #101218);
    border: 1px solid #4A4F5D;
    border-radius: 25px;
    padding: 25px;
    margin: 15px 0;
}

.card-brand {
    font-weight: 900;
    letter-spacing: 3px;
}

.card-number {
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 30px;
}

.card-small {
    color: #858B98;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 14px;
}

.goal {
    background: #11141A;
    border: 1px solid #292E38;
    border-radius: 19px;
    padding: 18px;
    margin: 10px 0;
}

.goal-title {
    font-weight: 800;
    font-size: 15px;
}

.goal-money {
    font-size: 21px;
    font-weight: 850;
    margin-top: 5px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DEFAULT DATA
# =========================================================

DEFAULT_TRANSACTIONS = [
    ["Pocket Money", "Income", 2000.0],
    ["Food", "Food", -250.0],
    ["Study", "Education", -500.0],
    ["Shopping", "Shopping", -350.0],
    ["Gaming", "Entertainment", -180.0],
]

DEFAULT_GOALS = [
    {
        "name": "New Headphones",
        "target": 5000.0,
        "saved": 3400.0
    }
]


# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "monthly_limit" not in st.session_state:
    st.session_state.monthly_limit = 2000.0

if "name" not in st.session_state:
    st.session_state.name = "Tejal"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "card_frozen" not in st.session_state:
    st.session_state.card_frozen = False

if "transactions" not in st.session_state:
    st.session_state.transactions = DEFAULT_TRANSACTIONS.copy()

if "goals" not in st.session_state:
    st.session_state.goals = DEFAULT_GOALS.copy()

if "notifications" not in st.session_state:
    st.session_state.notifications = []


# =========================================================
# FUNCTIONS
# =========================================================

def navigate(page):
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def total_spent():
    total = 0

    for item in st.session_state.transactions:
        if item[2] < 0:
            total += abs(item[2])

    return total


def category_spent(category):
    total = 0

    for item in st.session_state.transactions:
        if item[1] == category and item[2] < 0:
            total += abs(item[2])

    return total


def get_score():
    spent = total_spent()
    limit = max(st.session_state.monthly_limit, 1)
    ratio = spent / limit

    if ratio < 0.50:
        return 94
    if ratio < 0.70:
        return 88
    if ratio < 0.85:
        return 80
    if ratio < 1.00:
        return 70

    return 58


def biggest_category():
    values = {}

    for item in st.session_state.transactions:
        if item[2] < 0:
            category = item[1]

            if category not in values:
                values[category] = 0

            values[category] += abs(item[2])

    if not values:
        return "None", 0

    biggest = max(values, key=values.get)

    return biggest, values[biggest]


def reset_demo():
    st.session_state.balance = 5000.0
    st.session_state.monthly_limit = 2000.0
    st.session_state.name = "Tejal"
    st.session_state.card_frozen = False
    st.session_state.transactions = [
        item.copy() for item in DEFAULT_TRANSACTIONS
    ]
    st.session_state.goals = [
        item.copy() for item in DEFAULT_GOALS
    ]
    st.session_state.notifications = []


# =========================================================
# BRAND
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("HOME", use_container_width=True):
        navigate("Home")

with n2:
    if st.button("PAY", use_container_width=True):
        navigate("Pay")

with n3:
    if st.button("ACTIVITY", use_container_width=True):
        navigate("Activity")

with n4:
    if st.button("INSIGHT", use_container_width=True):
        navigate("Insight")

with n5:
    if st.button("PROFILE", use_container_width=True):
        navigate("Profile")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")
    st.subheader(st.session_state.name + " 👋")

    st.markdown(
        '<div class="card">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        '<div class="balance">₹{:,.2f}</div>'
        '<div class="muted">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    # Quick actions
    a, b, c = st.columns(3)

    with a:
        add_button = st.button(
            "＋ ADD",
            use_container_width=True
        )

    with b:
        send_button = st.button(
            "↗ SEND",
            use_container_width=True
        )

    with c:
        request_button = st.button(
            "⇄ REQUEST",
            use_container_width=True
        )

    if send_button:
        navigate("Pay")

    # Add money
    if add_button:

        st.markdown("### Add money")

        add_amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="home_add_amount"
        )

        add_source = st.text_input(
            "Source",
            value="Pocket Money",
            key="home_add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="home_confirm_add"
        ):

            st.session_state.balance += add_amount

            add_transaction(
                add_source.strip() or "Income",
                "Income",
                add_amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to your wallet.".format(
                    add_amount
                )
            )

            st.success("Balance updated.")
            st.rerun()

    # Request money
    if request_button:

        st.markdown("### Request money")

        request_person = st.text_input(
            "From",
            placeholder="Friend's name",
            key="request_person"
        )

        request_amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="request_amount"
        )

        if st.button(
            "Create request",
            use_container_width=True,
            key="create_request"
        ):

            if request_person.strip() == "":
                st.error("Enter a name.")
            else:
                st.session_state.notifications.insert(
                    0,
                    "Request of ₹{:,.0f} created.".format(
                        request_amount
                    )
                )

                st.success("Request created.")

    # Financial snapshot
    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = total_spent()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = spent / max(
        st.session_state.monthly_limit,
        1
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Spent this month",
            "₹{:,.0f}".format(spent)
        )

    with c2:
        st.metric(
            "Budget remaining",
            "₹{:,.0f}".format(remaining)
        )

    c3, c4 = st.columns(2)

    with c3:
        savings = sum(
            goal["saved"]
            for goal in st.session_state.goals
        )

        st.metric(
            "Savings",
            "₹{:,.0f}".format(savings)
        )

    with c4:
        st.metric(
            "VELORA Score",
            "{}/100".format(get_score())
        )

    if ratio < 0.60:
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

    # Intelligence
    biggest, biggest_value = biggest_category()

    if biggest != "None":

        st.markdown(
            '<div class="insight">'
            '<div class="insight-label">'
            'VELORA INTELLIGENCE'
            '</div>'
            '<div class="insight-title">'
            '{} is your biggest category'
            '</div>'
            '<div class="insight-text">'
            '₹{:,.0f} has been spent here. '
            'VELORA is tracking your spending patterns.'
            '</div>'
            '</div>'.format(
                biggest,
                biggest_value
            ),
            unsafe_allow_html=True
        )

    # Chart
    st.markdown(
        '<div class="section">Spending trend</div>',
        unsafe_allow_html=True
    )

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

    # Categories
    st.markdown(
        '<div class="section">Where your money goes</div>',
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

        value = category_spent(category)

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

    # Goals
    st.markdown(
        '<div class="section">Savings goals</div>',
        unsafe_allow_html=True
    )

    for goal in st.session_state.goals:

        progress = min(
            goal["saved"] /
            max(goal["target"], 1),
            1
        )

        st.markdown(
            '<div class="goal">'
            '<div class="goal-title">{}</div>'
            '<div class="goal-money">'
            '₹{:,.0f} / ₹{:,.0f}'
            '</div>'
            '<div class="muted">'
            '{:.0f}% complete'
            '</div>'
            '</div>'.format(
                goal["name"],
                goal["saved"],
                goal["target"],
                progress * 100
            ),
            unsafe_allow_html=True
        )

        st.progress(progress)


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
        step=50.0,
        key="payment_amount"
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
        ],
        key="payment_category"
    )

    if st.button(
        "Send payment",
        use_container_width=True,
        key="send_payment"
    ):

        if recipient.strip() == "":
            st.error("Enter recipient.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        elif st.session_state.card_frozen:
            st.error("Your VELORA card is frozen.")

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
        '<div class="virtual-card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">'
        '••••  ••••  ••••  2840'
        '</div>'
        '<div class="card-small">'
        'DEMO VIRTUAL CARD'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.error("🔒 CARD FROZEN")

        if st.button(
            "Unfreeze card",
            use_container_width=True,
            key="unfreeze"
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("🟢 CARD ACTIVE")

        if st.button(
            "Freeze card",
            use_container_width=True,
            key="freeze"
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

    for item in st.session_state.transactions:

        name = item[0]
        category = item[1]
        amount = item[2]

        searchable = (
            name + " " + category
        ).lower()

        if search.lower() not in searchable:
            continue

        found = True

        if amount >= 0:
            sign = "+"
        else:
            sign = "−"

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
        st.info("No matching transactions.")


# =========================================================
# INSIGHT
# =========================================================

elif st.session_state.page == "Insight":

    st.subheader("VELORA Intelligence")

    spent = total_spent()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    biggest, biggest_value = biggest_category()

    if ratio < 0.60:

        title = "You're spending with control."

        message = (
            "Your spending is comfortably below your "
            "monthly limit. Keep your current habits."
        )

    elif ratio < 0.85:

        title = "Watch your spending pace."

        message = (
            "You're approaching your monthly limit. "
            "Consider delaying non-essential purchases."
        )

    else:

        title = "Your budget needs attention."

        message = (
            "Your current spending is close to or "
            "above your monthly limit."
        )

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">'
        'VELORA INTELLIGENCE'
        '</div>'
        '<div class="insight-title">'
        '{}'
        '</div>'
        '<div class="insight-text">'
        '{}'
        '</div>'
        '</div>'.format(
            title,
            message
        ),
        unsafe_allow_html=True
    )

    i1, i2 = st.columns(2)

    with i1:
        st.metric(
            "VELORA Score",
            "{}/100".format(get_score())
        )

    with i2:
        st.metric(
            "Budget used",
            "{:.0f}%".format(
