import streamlit as st

st.set_page_config(
    page_title="GENZ WALLET",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- THEME ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #09090b;
    color: #f5f5f5;
}

.block-container {
    max-width: 520px;
    padding: 25px 18px 90px 18px;
}

/* Hide Streamlit branding */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Top bar */
.topbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:25px;
}

.logo {
    font-size:20px;
    font-weight:800;
    letter-spacing:1px;
}

.avatar {
    width:40px;
    height:40px;
    border-radius:50%;
    background:#7f1d35;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:700;
}

/* Greeting */
.small {
    color:#8f8f95;
    font-size:13px;
    margin-bottom:5px;
}

.greeting {
    font-size:28px;
    font-weight:800;
    margin-bottom:22px;
}

/* Balance card */
.balance-card {
    background:linear-gradient(135deg,#9b1c3d,#671329);
    border-radius:24px;
    padding:25px;
    margin-bottom:18px;
    box-shadow:0 12px 35px rgba(128,20,52,.25);
}

.balance-label {
    font-size:12px;
    letter-spacing:2px;
    opacity:.75;
}

.balance {
    font-size:40px;
    font-weight:800;
    margin:8px 0 3px;
}

.balance-sub {
    font-size:12px;
    opacity:.7;
}

/* Quick actions */
.section-title {
    font-size:15px;
    font-weight:700;
    margin:25px 0 12px;
}

.action {
    background:#151519;
    border:1px solid #24242a;
    border-radius:18px;
    padding:17px 10px;
    text-align:center;
}

.action-icon {
    font-size:22px;
    margin-bottom:6px;
}

.action-text {
    font-size:12px;
    color:#cfcfd3;
}

/* Limit */
.limit-card {
    background:#141417;
    border:1px solid #24242a;
    border-radius:22px;
    padding:20px;
}

.limit-row {
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.limit-title {
    color:#99999f;
    font-size:12px;
    letter-spacing:1.5px;
}

.limit-value {
    font-size:25px;
    font-weight:800;
    margin-top:5px;
}

.remaining {
    color:#8f8f95;
    font-size:12px;
}

.progress {
    height:8px;
    background:#29292e;
    border-radius:20px;
    margin-top:17px;
    overflow:hidden;
}

.progress-fill {
    width:63%;
    height:100%;
    background:#c02b50;
    border-radius:20px;
}

/* Transactions */
.transaction {
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:15px 0;
    border-bottom:1px solid #202025;
}

.tx-left {
    display:flex;
    align-items:center;
    gap:12px;
}

.tx-icon {
    width:42px;
    height:42px;
    border-radius:14px;
    background:#1b1b20;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:19px;
}

.tx-name {
    font-weight:600;
    font-size:14px;
}

.tx-date {
    color:#77777e;
    font-size:11px;
    margin-top:3px;
}

.tx-amount {
    font-weight:700;
    font-size:14px;
}

.minus {
    color:#f0f0f0;
}

.plus {
    color:#72d49a;
}

/* Savings */
.goal {
    background:#151519;
    border:1px solid #24242a;
    border-radius:22px;
    padding:20px;
}

.goal-top {
    display:flex;
    justify-content:space-between;
}

.goal-name {
    font-weight:700;
}

.goal-percent {
    color:#c02b50;
    font-weight:700;
}

.goal-amount {
    color:#888890;
    font-size:12px;
    margin-top:6px;
}

/* Buttons */
div.stButton > button {
    width:100%;
    border-radius:16px;
    border:1px solid #2a2a30;
    background:#17171b;
    color:white;
    height:48px;
    font-weight:600;
}

div.stButton > button:hover {
    border-color:#9b1c3d;
    color:white;
}

/* Bottom nav */
.bottom-nav {
    position:fixed;
    bottom:0;
    left:50%;
    transform:translateX(-50%);
    width:min(520px,100%);
    background:#101014;
    border-top:1px solid #25252a;
    padding:12px 25px;
    display:flex;
    justify-content:space-around;
    z-index:999;
}

.nav-item {
    color:#77777e;
    text-align:center;
    font-size:11px;
}

.nav-active {
    color:#e04468;
}

.nav-icon {
    font-size:20px;
    display:block;
    margin-bottom:3px;
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("""
<div class="topbar">
    <div class="logo">GENZ WALLET</div>
    <div class="avatar">T</div>
</div>

<div class="small">GOOD AFTERNOON 👋</div>
<div class="greeting">Your money,<br>your rules.</div>
""", unsafe_allow_html=True)


# ---------- BALANCE ----------
st.markdown("""
<div class="balance-card">
    <div class="balance-label">AVAILABLE BALANCE</div>
    <div class="balance">₹2,840</div>
    <div class="balance-sub">Demo wallet • Updated just now</div>
</div>
""", unsafe_allow_html=True)


# ---------- QUICK ACTIONS ----------
st.markdown('<div class="section-title">QUICK ACTIONS</div>',
            unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="action">
        <div class="action-icon">＋</div>
        <div class="action-text">Add Money</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="action">
        <div class="action-icon">↗</div>
        <div class="action-text">Send</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="action">
        <div class="action-icon">📊</div>
        <div class="action-text">Insights</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- MONTHLY LIMIT ----------
st.markdown('<div class="section-title">MONTHLY LIMIT</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="limit-card">
    <div class="limit-row">
        <div>
            <div class="limit-title">SPENT THIS MONTH</div>
            <div class="limit-value">₹1,260</div>
        </div>

        <div class="remaining">
            ₹740 left
        </div>
    </div>

    <div class="progress">
        <div class="progress-fill"></div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- RECENT TRANSACTIONS ----------
st.markdown('<div class="section-title">RECENT ACTIVITY</div>',
            unsafe_allow_html=True)

transactions = [
    ("🍔", "Food", "Today", "-₹180"),
    ("🎮", "Gaming", "Yesterday", "-₹299"),
    ("📚", "Study", "Aug 10", "-₹450"),
    ("💸", "Pocket Money", "Aug 08", "+₹1,000"),
]

for icon, name, date, amount in transactions:

    amount_class = "plus" if amount.startswith("+") else "minus"

    st.markdown(f"""
    <div class="transaction">
        <div class="tx-left">
            <div class="tx-icon">{icon}</div>
            <div>
                <div class="tx-name">{name}</div>
                <div class="tx-date">{date}</div>
            </div>
        </div>

        <div class="tx-amount {amount_class}">
            {amount}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- SAVINGS GOAL ----------
st.markdown('<div class="section-title">SAVINGS GOAL</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="goal">
    <div class="goal-top">
        <div class="goal-name">🎧 New Headphones</div>
        <div class="goal-percent">68%</div>
    </div>

    <div class="goal-amount">
        ₹3,400 saved of ₹5,000
    </div>

    <div class="progress">
        <div class="progress-fill" style="width:68%;"></div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- BUTTON ----------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("＋  Add a transaction"):
    st.success("Transaction feature coming next 🚀")


# ---------- BOTTOM NAV ----------
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item nav-active">
        <span class="nav-icon">⌂</span>
        Home
    </div>

    <div class="nav-item">
        <span class="nav-icon">↕</span>
        Activity
    </div>

    <div class="nav-item">
        <span class="nav-icon">🎯</span>
        Goals
    </div>

    <div class="nav-item">
        <span class="nav-icon">⚙</span>
        Settings
    </div>
</div>
""", unsafe_allow_html=True)