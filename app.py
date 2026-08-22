import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# VELORA 3.0
# Premium intelligent money-management demo
# No real payments / no bank connection
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -15%, #20243A 0%, #0B0C11 38%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 580px;
    padding: 22px 17px 90px;
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

.stSelectbox div[data-baseweb="select"] {
    background: #11141A !important;
    color: #FFFFFF !important;
}

hr {
    border-color: #252A34 !important;
}

.brand {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 4px;
}

.tagline {
    color: #858B98;
    font-size: 11px;
    letter-spacing: .7px;
}

.card {
    background: linear-gradient(145deg, #1A1E28, #101217);
    border: 1px solid #303542;
    border-radius: 24px;
    padding: 22px;
    margin: 14px 0;
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
    margin-top: 6px;
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
    margin-bottom: 9px;
}

.insight {
    background: linear-gradient(145deg, #191522, #101116);
    border: 1px solid #44365D;
    border-radius: 21px;
    padding: 20px;
    margin: 13px 0;
}

.insight-label {
    color: #A98CFF;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
}

.insight-title {
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

.tx-title {
    color: #F4F5F7;
    font-weight: 700;
    font-size: 13px;
}

.tx-cat {
    color: #777D89;
    font-size: 10px;
}

.virtual-card {
    background:
        linear-gradient(135deg, #242735, #101218);
    border: 1px solid #4A4F5D;
    border-radius: 25px;
    padding: 25px;
    height: 165px;
    margin: 15px 0;
}

.card-brand {
    font-weight: 900;
    letter-spacing: 3px;
}

.card-number {
    font-size: 18px;
    letter-spacing: 3px;
    margin-top: 28px;
}

.card-small {
    color: #858B98;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 15px;
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
}

.pill {
    display: inline-block;
    background: #1B1926;
    color: #A98CFF;
    border: 1px solid #403557;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 10px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "name": "Tejal",
    "page": "Home",
    "card_frozen": False,
    "notifications": [],
    "goals": [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ],
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


# =========================================================
# FUNCTIONS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_transaction(name, category, amount):
    st.session_state.transactions.insert(
        0,
        [name, category, amount]
    )


def spending_total():
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    )


def income_total():
    return sum(
        x[2]
        for x in st.session_state.transactions
        if x[2] > 0
    )


def category_total(category):
    return sum(
        abs(x[2])
        for x in st.session_state.transactions
        if x[1] == category and x[2] < 0
    )


def score():
    spent = spending_total()
    limit = max(st.session_state.monthly_limit, 1)
    ratio = spent / limit

    if ratio < 0.50:
        return 94
    elif ratio < 0.70:
        return 88
    elif ratio < 0.85:
        return 80
    elif ratio < 1.00:
        return 70
    else:
        return 58


def biggest_category():
    categories = {}

    for x in st.session_state.transactions:
        if x[2] < 0:
            categories[x[1]] = (
                categories.get(x[1], 0)
                + abs(x[2])
            )

    if not categories:
        return "None", 0

    name = max(
        categories,
        key=categories.get
    )

    return name, categories[name]


def reset_demo():
    st.session_state.balance = 5000.0
    st.session_state.monthly_limit = 2000.0
    st.session_state.card_frozen = False
    st.session_state.notifications = []

    st.session_state.goals = [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ]

    st.session_state.transactions = [
        ["Pocket Money", "Income", 2000.0],
        ["Food", "Food", -250.0],
        ["Study", "Education", -500.0],
        ["Shopping", "Shopping", -350.0],
        ["Gaming", "Entertainment", -180.0]
    ]


# =========================================================
# BRAND
# =========================================================

st.markdown(
    '<div class="brand">VELORA</div>'
    '<div class="tagline">Intelligent money management</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAV
# =========================================================

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
    st.subheader(
        st.session_state.name + " 👋"
    )

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

    # ACTIONS

    a, b, c = st.columns(3)

    with a:
        if st.button("＋ ADD", use_container_width=True):
            st.session_state.show_add = True

    with b:
        if st.button("↗ SEND", use_container_width=True):
            go("Pay")

    with c:
        if st.button("⇄ REQUEST", use_container_width=True):
            st.session_state.show_request = True

    # ADD

    if st.session_state.get("show_add", False):

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
            use_container_width=True
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

            st.session_state.show_add = False
            st.rerun()

    # REQUEST

    if st.session_state.get("show_request", False):

        st.markdown("### Request money")

        person = st.text_input(
            "From",
            placeholder="Friend's name",
            key="req_person"
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=200.0,
            step=50.0,
            key="req_amount"
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

                st.session_state.show_request = False
                st.success("Request created.")

    # SNAPSHOT

    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = spending_total()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    ratio = spent / max(
        st.session_state.monthly_limit,
        1
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
                sum(g["saved"] for g in st.session_state.goals)
            )
        )

    with s4:
        st.metric(
            "VELORA Score",
            "{}/100".format(score())
        )

    if ratio < 0.60:
        st.success(
            "You're on track. Your spending is comfortably below your limit."
        )
    elif ratio < 0.85:
        st.warning(
            "Watch your pace. You're approaching your monthly limit."
        )
    else:
        st.error(
            "Budget risk. Your spending is getting high."
        )

    # INSIGHT CARD

    biggest, biggest_value = biggest_category()

    if biggest != "None":

        st.markdown(
            '<div class="insight">'
            '<div class="insight-label">VELORA INTELLIGENCE</div>'
            '<div class="insight-title">'
            '{} is your biggest category'
            '</div>'
            '<div class="insight-text">'
            '₹{:,.0f} has been spent here. '
            'VELORA is tracking your habits to help '
            'you make better decisions.'
            '</div>'
            '</div>'.format(
                biggest,
                biggest_value
            ),
            unsafe_allow_html=True
        )

    # TREND

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

    # CATEGORIES

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

        value = category_total(category)

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

    # GOALS

    st.markdown(
        '<div class="section">Your goals</div>',
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
            '</div>'.format(
                goal["name"],
                goal["saved"],
                goal["target"]
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

        elif st.session_state.card_frozen:

            st.error("Your demo card is frozen.")

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
            use_container_width=True
        ):

            st.session_state.card_frozen = False
            st.rerun()

    else:

        st.success("🟢 CARD ACTIVE")

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

        if search.lower() not in (
            name + " " + category
        ).lower():
            continue

        found = True

        sign = "+" if amount >= 0 else "−"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-title">{}</div>'
            '<div class="tx-cat">{}</div>'
            '<div style="text-align:right;">'
            '{}₹{:,.0f}'
            '</div>'
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

    spent = spending_total()

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
            "{}/100".format(score())
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
            "{} is your largest spending category "
            "at ₹{:,.0f}.".format(
                biggest,
                biggest_value
            )
        )

    st.markdown(
        '<div class="section">Goal intelligence</div>',
        unsafe_allow_html=True
    )

        for goal in st.session_state.goals:

        progress = min(
            goal["saved"] / max(goal["target"], 1),
            1
        )

        st.markdown(
            '<div class="goal">'
            '<div class="goal-title">{}</div>'
            '<div class="goal-money">₹{:,.0f} / ₹{:,.0f}</div>'
            '<div class="muted">{:.0f}% complete</div>'
            '</div>'.format(
                goal["name"],
                goal["saved"],
                goal["target"],
                progress * 100
            ),
            unsafe_allow_html=True
        )

        st.progress(progress)

        remaining_goal = max(
            goal["target"] - goal["saved"],
            0
        )

        if remaining_goal > 0:
            st.caption(
                "₹{:,.0f} remaining to reach this goal.".format(
                    remaining_goal
                )
            )
        else:
            st.success(
                "🎉 Goal completed!"
            )

    # =====================================================
    # NOTIFICATIONS
    # =====================================================

    st.markdown(
        '<div class="section">Notifications</div>',
        unsafe_allow_html=True
    )

    if st.session_state.notifications:

        for notification in st.session_state.notifications[:5]:
            st.info(notification)

    else:
        st.caption("No new notifications.")

    # =====================================================
    # QUICK RESET
    # =====================================================

    st.divider()

    if st.button(
        "Reset demo data",
        use_container_width=True
    ):
        reset_demo()
        st.success("Demo data reset.")
        st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "VELORA · Intelligent money management · Demo Mode"
)