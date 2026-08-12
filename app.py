import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="◈",
    layout="centered"
)

# =========================
# PREMIUM THEME
# =========================

st.markdown("""
<style>

.stApp {
    background: #08080b;
    color: #f7f7f8;
}

.block-container {
    max-width: 520px;
    padding: 24px 18px 70px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* Text */

h1 {
    font-size: 30px !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3 {
    font-weight: 700 !important;
}

p {
    color: #9b9ba3;
}

/* Balance */

.balance-box {
    background: linear-gradient(135deg, #68162e, #a32149);
    border-radius: 26px;
    padding: 26px;
    margin: 20px 0;
    box-shadow: 0 18px 40px rgba(125, 20, 55, 0.22);
}

.balance-label {
    color: #d8c3cb;
    font-size: 11px;
    letter-spacing: 2px;
}

.balance-number {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin: 8px 0;
}

.balance-note {
    color: #decbd1;
    font-size: 12px;
}

/* Cards */

.card {
    background: #141419;
    border: 1px solid #24242b;
    border-radius: 22px;
    padding: 20px;
    margin: 12px 0;
}

/* Section */

.section {
    font-size: 14px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 12px;
    color: #eeeeef;
}

/* Buttons */

.stButton > button {
    background: #15151a !important;
    color: white !important;
    border: 1px solid #292930 !important;
    border-radius: 16px !important;
    height: 48px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    border-color: #a32149 !important;
}

/* Metric */

[data-testid="stMetric"] {
    background: #141419;
    border: 1px solid #24242b;
    padding: 15px;
    border-radius: 18px;
}

[data-testid="stMetricLabel"] {
    color: #85858d;
}

[data-testid="stMetricValue"] {
    color: white;
}

/* Progress */

.stProgress > div > div > div > div {
    background: #a32149;
}

/* Divider */

hr {
    border-color: #24242a;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.title("VELORA")
st.caption("Smart money. Simply yours.")

st.write("Good afternoon 👋")


# =========================
# BALANCE CARD
# =========================

st.markdown(
    '<div class="balance-box">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="balance-label">AVAILABLE BALANCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="balance-number">₹2,840</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="balance-note">Your demo wallet is looking healthy.</div>',
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# QUICK ACTIONS
# =========================

st.markdown('<div class="section">QUICK ACTIONS</div>',
            unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.button("＋ Add", use_container_width=True)

with b:
    st.button("↗ Send", use_container_width=True)

with c:
    st.button("◷ History", use_container_width=True)


# =========================
# SPENDING OVERVIEW
# =========================

st.markdown(
    '<div class="section">SPENDING OVERVIEW</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.metric(
        "This month",
        "₹1,260",
        "-12%"
    )

with right:
    st.metric(
        "Daily average",
        "₹63",
        "-₹8"
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# PREMIUM SPENDING CHART
# =========================

st.markdown(
    '<div class="section">WEEKLY SPENDING</div>',
    unsafe_allow_html=True
)

chart_data = {
    "Mon": 120,
    "Tue": 80,
    "Wed": 210,
    "Thu": 140,
    "Fri": 260,
    "Sat": 180,
    "Sun": 90
}

st.line_chart(
    chart_data,
    height=230
)


# =========================
# MONTHLY LIMIT
# =========================

st.markdown(
    '<div class="section">MONTHLY LIMIT</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("Monthly spending")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ₹1,260")

with col2:
    st.caption("₹740 remaining")

st.progress(0.63)

st.caption("63% of your ₹2,000 monthly limit used")

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# RECENT ACTIVITY
# =========================

st.markdown(
    '<div class="section">RECENT ACTIVITY</div>',
    unsafe_allow_html=True
)

transactions = [
    ("🍔", "Food", "Today", "-₹180"),
    ("🎮", "Gaming", "Yesterday", "-₹299"),
    ("📚", "Study", "Aug 10", "-₹450"),
    ("💸", "Pocket Money", "Aug 08", "+₹1,000")
]

for icon, name, date, amount in transactions:

    left, right = st.columns([3, 1])

    with left:
        st.write(f"**{icon} {name}**")
        st.caption(date)

    with right:
        st.write(f"**{amount}**")

    st.divider()


# =========================
# SAVINGS GOAL
# =========================

st.markdown(
    '<div class="section">SAVINGS GOAL</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("🎧 **New Headphones**")

st.caption("₹3,400 saved of ₹5,000")

st.progress(0.68)

st.caption("68% complete • ₹1,600 to go")

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# INSIGHT
# =========================

st.markdown(
    '<div class="section">VELORA INSIGHT</div>',
    unsafe_allow_html=True
)

st.info(
    "✨ You spent less this week than last week. "
    "Keep it up — you're on track with your monthly limit."
)


# =========================
# NAVIGATION
# =========================

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