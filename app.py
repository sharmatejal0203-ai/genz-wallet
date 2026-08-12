import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# VELORA
# Premium personal finance prototype
# =========================================================

st.set_page_config(
    page_title="Velora",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "balance" not in st.session_state:
    st.session_state.balance = 2840.0

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {"name": "Pocket Money", "category": "Income", "amount": 1000.0, "icon": "↗", "time": "Today"},
        {"name": "Food", "category": "Food", "amount": -180.0, "icon": "F", "time": "Today"},
        {"name": "Study", "category": "Education", "amount": -450.0, "icon": "E", "time": "Yesterday"},
        {"name": "Gaming", "category": "Entertainment", "amount": -299.0, "icon": "G", "time": "Aug 10"},
    ]

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "toast" not in st.session_state:
    st.session_state.toast = ""


# =========================================================
# DESIGN SYSTEM
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --bg: #070709;
    --surface: #101014;
    --surface2: #15151a;
    --border: #25252c;
    --text: #f5f5f7;
    --muted: #8c8c96;
    --accent: #b82d55;
    --accent2: #7c1837;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 560px;
    padding: 24px 18px 100px;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ---------- TYPOGRAPHY ---------- */

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    color: var(--text) !important;
}

h1 {
    font-size: 30px !important;
    letter-spacing: -1.5px;
}

h2 {
    font-size: 21px !important;
    letter-spacing: -0.5px;
}

p {
    color: var(--muted);
}

/* ---------- TOP BAR ---------- */

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -1px;
}

.tagline {
    color: #777780;
    font-size: 12px;
    margin-top: -4px;
}

/* ---------- BALANCE ---------- */

.balance-shell {
    background:
        radial-gradient(circle at 90% 10%, rgba(255,255,255,.10), transparent 25%),
        linear-gradient(135deg, #241019, #64172f 55%, #9d2549);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 28px;
    padding: 27px;
    margin: 24px 0 18px;
    box-shadow: 0 24px 55px rgba(105, 20, 48, .20);
}

.balance-label {
    color: #d8c7cd;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
}

.balance-number {
    color: white;
    font-family: 'Manrope', sans-serif;
    font-size: 43px;
    font-weight: 800;
    letter-spacing: -2px;
    margin: 5px 0 4px;
}

.balance-sub {
    color: #d8c7cd;
    font-size: 11px;
}

/* ---------- PREMIUM CARD ---------- */

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 19px;
    margin: 10px 0;
}

.card-title {
    font-family: 'Manrope', sans-serif;
    font-size: 14px;
    font-weight: 700;
}

.card-muted {
    color: var(--muted);
    font-size: 11px;
}

/* ---------- QUICK ACTIONS ---------- */

.action-title {
    font-size: 12px;
    font-weight: 600;
    color: #d9d9de;
    text-align: center;
    margin-top: 7px;
}

.action-icon {
    text-align: center;
    background: #15151a;
    border: 1px solid #292930;
    border-radius: 17px;
    padding: 14px 5px;
    font-size: 18px;
}

/* ---------- METRICS ---------- */

[data-testid="stMetric"] {
    background: #101014;
    border: 1px solid #25252c;
    border-radius: 18px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #85858e !important;
}

[data-testid="stMetricValue"] {
    color: #f5f5f7 !important;
    font-family: 'Manrope', sans-serif;
}

/* ---------- BUTTON ---------- */

.stButton > button {
    background: #15151a !important;
    border: 1px solid #2b2b33 !important;
    color: #f5f5f7 !important;
    border-radius: 14px !important;
    min-height: 44px !important;
    font-weight: 600 !important;
    transition: .2s ease;
}

.stButton > button:hover {
    border-color: #a5274b !important;
    background: #1b1115 !important;
}

/* ---------- INPUT ---------- */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #101014 !important;
    color: white !important;
    border-color: #292930 !important;
    border-radius: 13px !important;
}

/* ---------- PROGRESS ---------- */

.stProgress > div > div > div > div {
    background: var(--accent);
}

/* ---------- NAV ---------- */

.nav-label {
    text-align: center;
    color: #707079;
    font-size: 10px;
}

.nav-active {
    color: #d63b64;
}

/* ---------- DIVIDER ---------- */

hr {
    border-color: #24242a;
}

/* ---------- INFO ---------- */

.stAlert {
    border-radius: 17px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def total_spending():
    return abs(sum(
        x["amount"]
        for x in st.session_state.transactions
        if x["amount"] < 0
    ))


def add_transaction(name, category, amount, icon, transaction_type):
    value = abs(float(amount))

    if transaction_type == "credit":
        st.session_state.balance += value
        signed = value
    else:
        st.session_state.balance -= value
        signed = -value

    st.session_state.transactions.insert(
        0,
        {
            "name": name,
            "category": category,
            "amount": signed,
            "icon": icon,
            "time": "Just now"
        }
    )


# =========================================================
# TOP BAR
# =========================================================

top1, top2 = st.columns([4, 1])

with top1:
    st.markdown(
        '<div class="brand">VELORA</div>'
        '<div class="tagline">A smarter way to manage money.</div>',
        unsafe_allow_html=True
    )

with top2:
    st.markdown(
        '<div style="text-align:right;font-size:22px;">◉</div>',
        unsafe_allow_html=True
    )


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div style="margin-top:24px;color:#777780;font-size:12px;">'
        'GOOD AFTERNOON'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-family:Manrope;font-size:25px;font-weight:700;'
        'margin-top:3px;">Welcome back.</div>',
        unsafe_allow_html=True
    )

    # Balance
    st.markdown(
        '<div class="balance-shell">'
        '<div class="balance-label">AVAILABLE BALANCE</div>'
        f'<div class="balance-number">₹{st.session_state.balance:,.0f}</div>'
        '<div class="balance-sub">Demo wallet · No real money</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Actions
    st.markdown(
        '<div class="card-title">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    with a:
        st.markdown('<div class="action-icon">＋</div>', unsafe_allow_html=True)
        if st.button("Add", key="add", use_container_width=True):
            st.session_state.page = "Add"
            st.rerun()

    with b:
        st.markdown('<div class="action-icon">↗</div>', unsafe_allow_html=True)
        if st.button("Send", key="send", use_container_width=True):
            st.session_state.page = "Send"
            st.rerun()

    with c:
        st.markdown('<div class="action-icon">⇄</div>', unsafe_allow_html=True)
        if st.button("Request", key="request", use_container_width=True):
            st.session_state.page = "Request"
            st.rerun()

    with d:
        st.markdown('<div class="action-icon">⌁</div>', unsafe_allow_html=True)
        if st.button("Activity", key="activity", use_container_width=True):
            st.session_state.page = "Activity"
            st.rerun()

    # Overview
    st.markdown(
        '<div style="margin-top:28px;" class="card-title">'
        'THIS MONTH'
        '</div>',
        unsafe_allow_html=True
    )

    spent = total_spending()
    monthly_limit = 2000

    m1, m2 = st.columns(2)

    with m1:
        st.metric("Spent", f"₹{spent:,.0f}")

    with m2:
        remaining = max(0, monthly_limit - spent)
        st.metric("Remaining", f"₹{remaining:,.0f}")

    # Chart
    st.markdown(
        '<div style="margin-top:22px;" class="card-title">'
        'SPENDING ACTIVITY'
        '</div>',
        unsafe_allow_html=True
    )

    weekly = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Spend": [120, 80, 210, 140, 260, 180, 90]
    })

    st.line_chart(
        weekly.set_index("Day"),
        height=220
    )

    # Goal
    st.markdown(
        '<div style="margin-top:22px;" class="card-title">'
        'SAVINGS GOAL'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write("**New headphones**")
    st.caption("₹3,400 of ₹5,000")

    st.progress(0.68)

    st.caption("68% complete")

    st.markdown("</div>", unsafe_allow_html=True)

    # Recent
    st.markdown(
        '<div style="margin-top:22px;" class="card-title">'
        'RECENT ACTIVITY'
        '</div>',
        unsafe_allow_html=True
    )

    for tx in st.session_state.transactions[:4]:

        left, right = st.columns([3.2, 1])

        with left:
            st.write(f"**{tx['icon']}  {tx['name']}**")
            st.caption(f"{tx['category']} · {tx['time']}")

        with right:

            if tx["amount"] >= 0:
                st.markdown(
                    f'<div style="text-align:right;color:#6fd49b;'
                    f'font-weight:700;">+₹{tx["amount"]:,.0f}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div style="text-align:right;color:#f1f1f2;'
                    f'font-weight:700;">−₹{abs(tx["amount"]):,.0f}</div>',
                    unsafe_allow_html=True
                )

        st.divider()

    # Insight
    if spent < 1000:
        st.info("Velora insight · Your spending is comfortably within your monthly limit.")
    elif spent < 1600:
        st.info("Velora insight · You're on track. Keep non-essential spending under control.")
    else:
        st.warning("Velora insight · You're getting close to your monthly spending limit.")


# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state.page == "Add":

    st.header("Add money")
    st.caption("Add a demo transaction to your Velora wallet.")

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        max_value=100000.0,
        value=500.0,
        step=100.0
    )

    source = st.text_input(
        "Source",
        placeholder="e.g. Pocket money"
    )

    if st.button("Add to wallet", use_container_width=True):

        if not source.strip():
            st.error("Please enter a source.")
        else:
            add_transaction(
                source,
                "Income",
                amount,
                "↗",
                "credit"
            )

            st.success(f"₹{amount:,.0f} added.")
            st.session_state.page = "Home"
            st.rerun()

    if st.button("← Back", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()


# =========================================================
# SEND MONEY
# =========================================================

elif st.session_state.page == "Send":

    st.header("Send money")
    st.caption("Create a simulated transfer.")

    person = st.text_input(
        "Recipient",
        placeholder="Name"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        max_value=100000.0,
        value=100.0,
        step=50.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Entertainment",
            "Travel",
            "Shopping",
            "Other"
        ]
    )

    if st.button("Review transfer", use_container_width=True):

        if not person.strip():
            st.error("Enter a recipient.")
        elif amount > st.session_state.balance:
            st.error("Not enough demo balance.")
        else:
            st.session_state.pending_transfer = {
                "person": person,
                "amount": amount,
                "category": category
            }
            st.session_state.page = "Confirm"
            st.rerun()

    if st.button("← Back", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()


# =========================================================
# CONFIRM TRANSFER
# =========================================================

elif st.session_state.page == "Confirm":

    transfer = st.session_state.pending_transfer

    st.header("Confirm transfer")
    st.caption("Review the demo transaction before continuing.")

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.write("Recipient")
    st.subheader(transfer["person"])

    st.write("Amount")
    st.markdown(
        f"### ₹{transfer['amount']:,.0f}"
    )

    st.caption(f"Category · {transfer['category']}")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Confirm & send", use_container_width=True):

        add_transaction(
            f"Sent to {transfer['person']}",
            transfer["category"],
            transfer["amount"],
            "↗",
            "debit"
        )

        st.success("Demo transfer completed.")
        st.session_state.page = "Home"
        st.rerun()

    if st.button("Cancel", use_container_width=True):
        st.session_state.page = "Send"
        st.rerun()


# =========================================================
# REQUEST
# =========================================================

elif st.session_state.page == "Request":

    st.header("Request money")
    st.caption("Create a simulated payment request.")

    person = st.text_input(
        "Request from",
        placeholder="Friend's name"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        max_value=100000.0,
        value=200.0,
        step=50.0
    )

    reason = st.text_input(
        "Reason",
        placeholder="e.g. Movie tickets"
    )

    if st.button("Create request", use_container_width=True):

        if not person.strip():
            st.error("Enter a person's name.")
        else:
            st.success(
                f"₹{amount:,.0f} request created for {person}."
            )

    if st.button("← Back", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.header("Activity")
    st.caption("Everything happening in your demo wallet.")

    for tx in st.session_state.transactions:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        left, right = st.columns([3, 1])

        with left:
            st.write(f"**{tx['icon']}  {tx['name']}**")
            st.caption(
                f"{tx['category']} · {tx['time']}"
            )

        with right:

            if tx["amount"] >= 0:
                st.markdown(
                    f'<div style="text-align:right;color:#6fd49b;'
                    f'font-weight:700;">+₹{tx["amount"]:,.0f}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div style="text-align:right;font-weight:700;">'
                    f'−₹{abs(tx["amount"]):,.0f}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("← Back to home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()


# =========================================================
# BOTTOM NAVIGATION
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.divider()

n1, n2, n3 = st.columns(3)

with n1:
    if st.button("Home", key="nav_home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with n2:
    if st.button("Activity", key="nav_activity", use_container_width=True):
        st.session_state.page = "Activity"
        st.rerun()

with n3:
    if st.button("Profile", key="nav_profile", use_container_width=True):
        st.info("Profile & preferences are part of the next Velora module.").