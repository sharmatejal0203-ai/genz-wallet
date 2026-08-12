import streamlit as st
from datetime import datetime

# =========================================================
# VELORA — PREMIUM DEMO WALLET
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 2500.0

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {
            "icon": "💸",
            "name": "Pocket Money",
            "date": "Today",
            "amount": 1000,
            "type": "credit"
        },
        {
            "icon": "🍔",
            "name": "Food",
            "date": "Yesterday",
            "amount": -180,
            "type": "debit"
        },
        {
            "icon": "📚",
            "name": "Study",
            "date": "Aug 10",
            "amount": -450,
            "type": "debit"
        }
    ]

if "spent" not in st.session_state:
    st.session_state.spent = 630.0

if "monthly_limit" not in st.session_state:
    st.session_state.monthly_limit = 2000.0

if "goal" not in st.session_state:
    st.session_state.goal = 5000.0

if "saved" not in st.session_state:
    st.session_state.saved = 3400.0


# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #08080b;
    color: #f7f7f8;
}

.block-container {
    max-width: 520px;
    padding: 22px 18px 70px;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ---------- GLOBAL ---------- */

h1 {
    font-size: 31px !important;
    font-weight: 800 !important;
    letter-spacing: -1.2px;
}

h2 {
    font-size: 22px !important;
}

h3 {
    font-size: 18px !important;
}

p {
    color: #a0a0a8;
}

/* ---------- BALANCE ---------- */

.balance-card {
    background: linear-gradient(
        135deg,
        #541126 0%,
        #8f1e42 55%,
        #b52b55 100%
    );

    border-radius: 27px;
    padding: 26px;
    margin: 20px 0;

    box-shadow:
        0 20px 45px rgba(120, 20, 55, 0.25);
}

.balance-label {
    color: #decbd2;
    font-size: 11px;
    letter-spacing: 2px;
}

.balance-number {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin: 7px 0;
}

.balance-note {
    color: #e2cfd5;
    font-size: 12px;
}

/* ---------- CARDS ---------- */

.premium-card {
    background: #141419;
    border: 1px solid #27272e;
    border-radius: 22px;
    padding: 20px;
    margin: 12px 0;
}

/* ---------- SECTION ---------- */

.section {
    color: #f0f0f2;
    font-size: 14px;
    font-weight: 700;
    margin-top: 27px;
    margin-bottom: 12px;
}

/* ---------- QUICK ACTION ---------- */

.action-card {
    text-align: center;
    background: #141419;
    border: 1px solid #27272e;
    border-radius: 18px;
    padding: 15px 6px;
}

.action-icon {
    font-size: 22px;
}

.action-name {
    color: #c9c9ce;
    font-size: 11px;
    margin-top: 6px;
}

/* ---------- VIRTUAL CARD ---------- */

.virtual-card {
    background: linear-gradient(
        135deg,
        #17171c,
        #292930
    );

    border: 1px solid #36363e;
    border-radius: 23px;
    padding: 22px;
    margin-top: 12px;
}

.card-brand {
    font-size: 13px;
    letter-spacing: 2px;
    color: #aaaab2;
}

.card-chip {
    font-size: 25px;
    margin: 25px 0 15px;
}

.card-number {
    font-size: 18px;
    letter-spacing: 3px;
    color: #eeeeef;
}

.card-bottom {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    color: #aaaab2;
    font-size: 10px;
}

/* ---------- TRANSACTIONS ---------- */

.transaction-card {
    background: #141419;
    border: 1px solid #24242b;
    border-radius: 17px;
    padding: 13px;
    margin: 8px 0;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    background: #16161b !important;
    color: white !important;
    border: 1px solid #2b2b33 !important;
    border-radius: 15px !important;
    min-height: 46px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    border-color: #a32149 !important;
}

/* ---------- INPUT ---------- */

.stNumberInput input,
.stTextInput input,
.stSelectbox div {
    background: #141419 !important;
    color: white !important;
    border-radius: 13px !important;
}

/* ---------- METRICS ---------- */

[data-testid="stMetric"] {
    background: #141419;
    border: 1px solid #27272e;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: white;
}

/* ---------- PROGRESS ---------- */

.stProgress > div > div > div > div {
    background: #a32149;
}

/* ---------- ALERT ---------- */

.stAlert {
    border-radius: 17px;
}

/* ---------- DIVIDER ---------- */

hr {
    border-color: #25252b;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.title("VELORA")
st.caption("Smart money. Simply yours.")

st.write("Good afternoon 👋")


# =========================================================
# DEMO WALLET SETUP
# =========================================================

with st.expander("⚙️ Demo Wallet Setup"):

    new_balance = st.number_input(
        "Starting balance",
        min_value=0.0,
        max_value=10000000.0,
        value=float(st.session_state.balance),
        step=100.0
    )

    if st.button("Apply Balance", use_container_width=True):
        st.session_state.balance = new_balance
        st.rerun()


# =========================================================
# BALANCE CARD
# =========================================================

st.markdown(
    '<div class="balance-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="balance-label">AVAILABLE BALANCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="balance-number">₹{st.session_state.balance:,.0f}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="balance-note">Demo mode • No real money involved</div>',
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# QUICK ACTIONS
# =========================================================

st.markdown(
    '<div class="section">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

a, b, c, d = st.columns(4)

with a:
    add_money = st.button("＋", use_container_width=True)
    st.caption("Add")

with b:
    send_money = st.button("↗", use_container_width=True)
    st.caption("Send")

with c:
    st.button("⌁", use_container_width=True)
    st.caption("Request")

with d:
    st.button("◷", use_container_width=True)
    st.caption("History")


# =========================================================
# ADD MONEY
# =========================================================

if add_money:

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.subheader("Add money")

    add_amount = st.number_input(
        "Amount",
        min_value=1.0,
        max_value=100000.0,
        value=500.0,
        step=100.0,
        key="add_amount"
    )

    if st.button("Add to Velora", use_container_width=True):

        st.session_state.balance += add_amount

        st.session_state.transactions.insert(
            0,
            {
                "icon": "＋",
                "name": "Money Added",
                "date": "Just now",
                "amount": add_amount,
                "type": "credit"
            }
        )

        st.success(f"₹{add_amount:,.0f} added successfully!")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# SEND MONEY
# =========================================================

if send_money:

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.subheader("Send money")

    receiver = st.text_input(
        "Send to",
        placeholder="Friend's name"
    )

    send_amount = st.number_input(
        "Amount",
        min_value=1.0,
        max_value=100000.0,
        value=100.0,
        step=50.0,
        key="send_amount"
    )

    if st.button("Send securely", use_container_width=True):

        if send_amount > st.session_state.balance:

            st.error("Insufficient demo balance.")

        elif receiver.strip() == "":

            st.warning("Enter a friend's name.")

        else:

            st.session_state.balance -= send_amount
            st.session_state.spent += send_amount

            st.session_state.transactions.insert(
                0,
                {
                    "icon": "↗",
                    "name": f"Sent to {receiver}",
                    "date": "Just now",
                    "amount": -send_amount,
                    "type": "debit"
                }
            )

            st.success("Money sent successfully!")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# VIRTUAL CARD
# =========================================================

st.markdown(
    '<div class="section">VELORA CARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="virtual-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-brand">VELORA • DEMO CARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-chip">▰</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-number">••••  ••••  ••••  2840</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-bottom">'
    '<span>VELORA MEMBER</span>'
    '<span>DEMO</span>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# SPENDING OVERVIEW
# =========================================================

st.markdown(
    '<div class="section">MONEY OVERVIEW</div>',
    unsafe_allow_html=True
)

m1, m2 = st.columns(2)

with m1:
    st.metric(
        "Spent",
        f"₹{st.session_state.spent:,.0f}"
    )

with m2:
    remaining = max(
        0,
        st.session_state.monthly_limit - st.session_state.spent
    )

    st.metric(
        "Remaining",
        f"₹{remaining:,.0f}"
    )


# =========================================================
# SPENDING CHART
# =========================================================

st.markdown(
    '<div class="section">SPENDING TREND</div>',
    unsafe_allow_html=True
)

weekly_spending = {
    "Mon": 120,
    "Tue": 80,
    "Wed": 210,
    "Thu": 140,
    "Fri": 260,
    "Sat": 180,
    "Sun": 90
}

st.line_chart(
    weekly_spending,
    height=230
)


# =========================================================
# MONTHLY LIMIT
# =========================================================

st.markdown(
    '<div class="section">MONTHLY LIMIT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

st.write("Your monthly spending")

st.markdown(
    f"### ₹{st.session_state.spent:,.0f}"
)

st.caption(
    f"of ₹{st.session_state.monthly_limit:,.0f}"
)

percentage = min(
    1,
    st.session_state.spent / st.session_state.monthly_limit
)

st.progress(percentage)

st.caption(
    f"{percentage * 100:.0f}% of your monthly limit used"
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# SAVINGS GOAL
# =========================================================

st.markdown(
    '<div class="section">YOUR GOAL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

st.write("🎧 **New Headphones**")

goal_percent = min(
    1,
    st.session_state.saved / st.session_state.goal
)

st.caption(
    f"₹{st.session_state.saved:,.0f} saved "
    f"of ₹{st.session_state.goal:,.0f}"
)

st.progress(goal_percent)

st.caption(
    f"{goal_percent * 100:.0f}% complete"
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# RECENT ACTIVITY
# =========================================================

st.markdown(
    '<div class="section">RECENT ACTIVITY</div>',
    unsafe_allow_html=True
)

for tx in st.session_state.transactions[:6]:

    left, right = st.columns([3, 1])

    with left:

        st.write(
            f"**{tx['icon']} {tx['name']}**"
        )

        st.caption(tx["date"])

    with right:

        sign = "+" if tx["amount"] > 0 else ""

        st.write(
            f"**{sign}₹{abs(tx['amount']):,.0f}**"
        )

    st.divider()


# =========================================================
# VELORA INSIGHT
# =========================================================

st.markdown(
    '<div class="section">VELORA INSIGHT</div>',
    unsafe_allow_html=True
)

if percentage < 0.5:

    st.success(
        "✨ You're comfortably within your monthly spending limit."
    )

elif percentage < 0.8:

    st.info(
        "💡 You're doing okay. Keep an eye on non-essential spending."
    )

else:

    st.warning(
        "⚡ You're getting close to your monthly limit."
    )


# =========================================================
# FOOTER NAV
# =========================================================

st.divider()

n1, n2, n3, n4 = st.columns(4)

with n1:
    st.caption("⌂")
    st.caption("Home")

with n2:
    st.caption("↕")
    st.caption("Activity")

with n3:
    st.caption("◇")
    st.caption("Goals")

with n4:
    st.caption("⚙")
    st.caption("Profile")