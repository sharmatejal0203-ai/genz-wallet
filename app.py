import streamlit as st
import pandas as pd

# =========================================================
# VELORA 2.1
# Intelligent Money Management
# Demo only — no real payments
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #090A0F;
    color: #F5F5F7;
}

.block-container {
    max-width: 560px;
    padding: 24px 18px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3, h4 {
    color: #F5F5F7 !important;
}

p, label {
    color: #A0A4AE !important;
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
    margin: 14px 0;
}

.balance {
    font-size: 42px;
    font-weight: 850;
    color: white;
}

.muted {
    color: #858B98 !important;
    font-size: 12px;
}

.purple {
    color: #A98CFF !important;
    font-weight: 700;
}

.goal-card {
    background: linear-gradient(145deg, #17151F, #101117);
    border: 1px solid #393149;
    border-radius: 20px;
    padding: 20px;
    margin: 12px 0;
}

.transaction {
    background: #11141A;
    border: 1px solid #252A34;
    border-radius: 15px;
    padding: 14px;
    margin: 8px 0;
}

.section {
    font-size: 18px;
    font-weight: 800;
    margin-top: 24px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "balance": 5000.0,
    "monthly_limit": 2000.0,
    "goal_name": "New Headphones",
    "goal_target": 5000.0,
    "goal_saved": 3400.0,
    "name": "Tejal",
    "page": "Home",
    "card_frozen": False,
    "notifications": [],
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


def total_spending():
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[2] < 0
    )


def total_income():
    return sum(
        item[2]
        for item in st.session_state.transactions
        if item[2] > 0
    )


def category_spending(category):
    return sum(
        abs(item[2])
        for item in st.session_state.transactions
        if item[1] == category and item[2] < 0
    )


def budget_ratio():
    return (
        total_spending()
        / max(st.session_state.monthly_limit, 1)
    )


def goal_ratio():
    return min(
        st.session_state.goal_saved
        / max(st.session_state.goal_target, 1),
        1
    )


def velora_score():
    ratio = budget_ratio()

    if ratio <= 0.50:
        return 95
    elif ratio <= 0.65:
        return 90
    elif ratio <= 0.80:
        return 84
    elif ratio <= 1.00:
        return 72
    else:
        return 58


# =========================================================
# HEADER
# =========================================================

st.markdown("# VELORA")
st.markdown(
    '<div class="muted">Intelligent money management</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("HOME", use_container_width=True):
        go("Home")

with n2:
    if st.button("PAY", use_container_width=True):
        go("Pay")

with n3:
    if st.button("GOALS", use_container_width=True):
        go("Goals")

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
        '<div class="muted">'
        'Demo wallet · No real money connected'
        '</div>'
        '</div>'.format(
            st.session_state.balance
        ),
        unsafe_allow_html=True
    )

    # QUICK ACTIONS
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
        goal_clicked = st.button(
            "🎯 GOAL",
            use_container_width=True
        )

    if send_clicked:
        go("Pay")

    if goal_clicked:
        go("Goals")

    # ADD MONEY
    if add_clicked:

        st.markdown("### Add money")

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            value=500.0,
            step=100.0,
            key="home_add_amount"
        )

        source = st.text_input(
            "Source",
            value="Pocket Money",
            key="home_add_source"
        )

        if st.button(
            "Confirm add",
            use_container_width=True,
            key="home_confirm_add"
        ):

            st.session_state.balance += amount

            add_transaction(
                source.strip() or "Income",
                "Income",
                amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to your wallet.".format(amount)
            )

            st.success("Balance updated.")
            st.rerun()

    # =====================================================
    # FINANCIAL SNAPSHOT
    # =====================================================

    st.markdown(
        '<div class="section">Financial snapshot</div>',
        unsafe_allow_html=True
    )

    spent = total_spending()

    remaining = max(
        st.session_state.monthly_limit - spent,
        0
    )

    score = velora_score()

    s1, s2 = st.columns(2)

    with s1:
        st.metric(
            "Spent",
            "₹{:,.0f}".format(spent)
        )

    with s2:
        st.metric(
            "Budget left",
            "₹{:,.0f}".format(remaining)
        )

    s3, s4 = st.columns(2)

    with s3:
        st.metric(
            "Saved",
            "₹{:,.0f}".format(
                st.session_state.goal_saved
            )
        )

    with s4:
        st.metric(
            "VELORA Score",
            "{}/100".format(score)
        )

    # BUDGET
    st.markdown("### Monthly budget")

    ratio = budget_ratio()

    st.progress(
        min(ratio, 1.0)
    )

    st.caption(
        "₹{:,.0f} spent of ₹{:,.0f}".format(
            spent,
            st.session_state.monthly_limit
        )
    )

    if ratio < 0.6:
        st.success(
            "You're comfortably within your budget."
        )
    elif ratio < 0.85:
        st.warning(
            "You're getting close to your budget."
        )
    else:
        st.error(
            "Your spending is high compared with your budget."
        )

    # =====================================================
    # SAVINGS GOAL PREVIEW
    # =====================================================

    st.markdown("### Current goal")

    progress = goal_ratio()

    st.markdown(
        '<div class="goal-card">'
        '<div class="purple">SAVINGS GOAL</div>'
        '<h3>{}</h3>'
        '<p>₹{:,.0f} saved of ₹{:,.0f}</p>'
        '</div>'.format(
            st.session_state.goal_name,
            st.session_state.goal_saved,
            st.session_state.goal_target
        ),
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.caption(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    if st.button(
        "Open savings goal",
        use_container_width=True
    ):
        go("Goals")

    # =====================================================
    # SPENDING TREND
    # =====================================================

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

    # =====================================================
    # RECENT ACTIVITY
    # =====================================================

    st.markdown("### Recent activity")

    for item in st.session_state.transactions[:4]:

        name = item[0]
        category = item[1]
        amount = item[2]

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
# GOALS
# =========================================================

elif st.session_state.page == "Goals":

    st.subheader("Savings Goals")

    st.caption(
        "Turn spending intentions into actual savings."
    )

    st.markdown(
        '<div class="goal-card">'
        '<div class="purple">ACTIVE GOAL</div>'
        '<h2>{}</h2>'
        '<p>₹{:,.0f} saved / ₹{:,.0f}</p>'
        '</div>'.format(
            st.session_state.goal_name,
            st.session_state.goal_saved,
            st.session_state.goal_target
        ),
        unsafe_allow_html=True
    )

    progress = goal_ratio()

    st.progress(progress)

    st.caption(
        "{:.0f}% complete".format(
            progress * 100
        )
    )

    remaining_goal = max(
        st.session_state.goal_target -
        st.session_state.goal_saved,
        0
    )

    if remaining_goal > 0:

        st.info(
            "₹{:,.0f} more to reach your goal.".format(
                remaining_goal
            )
        )

    else:

        st.success(
            "🎉 Goal completed!"
        )

    st.divider()

    st.markdown("### Add savings")

    contribution = st.number_input(
        "Amount to save",
        min_value=1.0,
        value=100.0,
        step=50.0,
        key="goal_contribution"
    )

    if st.button(
        "Move money to goal",
        use_container_width=True
    ):

        if contribution > st.session_state.balance:

            st.error(
                "Not enough demo balance."
            )

        elif st.session_state.goal_saved >= st.session_state.goal_target:

            st.warning(
                "This goal is already complete."
            )

        else:

            remaining_goal = (
                st.session_state.goal_target
                - st.session_state.goal_saved
            )

            actual_amount = min(
                contribution,
                remaining_goal
            )

            st.session_state.balance -= actual_amount

            st.session_state.goal_saved += actual_amount

            add_transaction(
                "Savings Goal",
                "Savings",
                -actual_amount
            )

            st.session_state.notifications.insert(
                0,
                "₹{:,.0f} added to your savings goal.".format(
                    actual_amount
                )
            )

            st.success(
                "₹{:,.0f} saved successfully.".format(
                    actual_amount
                )
            )

            st.rerun()

    st.divider()

    st.markdown("### Edit goal")

    new_name = st.text_input(
        "Goal name",
        value=st.session_state.goal_name
    )

    new_target = st.number_input(
        "Target",
        min_value=1.0,
        value=float(
            st.session_state.goal_target
        ),
        step=100.0
    )

    if st.button(
        "Update goal",
        use_container_width=True
    ):

        st.session_state.goal_name = (
            new_name.strip() or "My Goal"
        )

        st.session_state.goal_target = new_target

        st.success(
            "Goal updated."
        )

        st.rerun()


# =========================================================
# INSIGHT
# =========================================================

elif st.session_state.page == "Insight":

    st.subheader("VELORA Intelligence")

    spent = total_spending()
    ratio = budget_ratio()
    score = velora_score()

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

    st.markdown(
        '<div class="card">'
        '<div class="purple">VELORA INTELLIGENCE</div>'
        '<h2>Financial Health</h2>'
        '<p class="muted">'
        'Your score is based on your current spending pace.'
        '</p>'
        '</div>',
        unsafe_allow_html=True
    )

    i1, i2 = st.columns(2)

    with i1:
        st.metric(
            "Health Score",
            "{}/100".format(score)
        )

    with i2:
        st.metric(
            "Budget Used",
            "{:.0f}%".format(
                ratio * 100
            )
        )

    if biggest != "None":

        st.markdown("### Biggest category")

        st.metric(
            biggest,
            "₹{:,.0f}".format(
                biggest_value
            )
        )

        st.info(
            "{} is currently your largest spending category."
            .format(biggest)
        )

    st.markdown("### VELORA recommendation")

    if ratio < 0.5:

        st.success(
            "Strong control. You have plenty of room "
            "inside your monthly budget."
        )

    elif ratio < 0.8:

        st.info(
            "You're doing well. Keep upcoming purchases "
            "intentional."
        )

    elif ratio < 1:

        st.warning(
            "You're approaching your monthly limit. "
            "Consider slowing discretionary spending."
        )

    else:

        st.error(
            "Your spending has crossed your planned "
            "monthly limit."
        )

    st.markdown("### Savings insight")

    if goal_ratio() >= 1:

        st.success(
            "Your current savings goal is complete."
        )

    else:

        st.info(
            "You are {:.0f}% toward your {} goal."
            .format(
                goal_ratio() * 100,
                st.session_state.goal_name
            )
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

    st.subheader("Notifications")

    if st.session_state.notifications:

        for notification in st.session_state.notifications[:8]:

            st.write(
                "• " + notification
            )

    else:

        st.capt