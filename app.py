import streamlit as st

st.set_page_config(
    page_title="GENZ WALLET",
    page_icon="💳",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #09090b;
}

.block-container {
    max-width: 500px;
    padding: 25px 18px 80px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.title {
    font-size: 28px;
    font-weight: 800;
    color: white;
    margin-bottom: 4px;
}

.subtitle {
    color: #888;
    font-size: 13px;
    margin-bottom: 25px;
}

.balance {
    background: #7f1834;
    padding: 25px;
    border-radius: 22px;
    margin-bottom: 20px;
}

.balance-label {
    color: #ddd;
    font-size: 12px;
    letter-spacing: 2px;
}

.amount {
    color: white;
    font-size: 40px;
    font-weight: 800;
    margin-top: 8px;
}

.demo {
    color: #ddd;
    font-size: 12px;
}

.card {
    background: #151519;
    border: 1px solid #25252b;
    padding: 20px;
    border-radius: 20px;
    margin-top: 15px;
}

.label {
    color: #888;
    font-size: 11px;
    letter-spacing: 2px;
}

.big {
    color: white;
    font-size: 25px;
    font-weight: 700;
    margin-top: 6px;
}

.small {
    color: #888;
    font-size: 12px;
}

.bar {
    background: #29292e;
    height: 8px;
    border-radius: 20px;
    margin-top: 15px;
}

.fill {
    background: #c52b50;
    height: 8px;
    width: 63%;
    border-radius: 20px;
}

.section {
    color: white;
    font-size: 15px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 12px;
}

.tx {
    background: #151519;
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 8px;
}

.tx-name {
    color: white;
    font-weight: 600;
}

.tx-date {
    color: #777;
    font-size: 11px;
}

.tx-money {
    color: white;
    font-weight: 700;
    float: right;
}
</style>
""", unsafe_allow_html=True)


# HEADER

st.markdown(
    '<div class="title">GENZ WALLET</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your money. Your rules.</div>',
    unsafe_allow_html=True
)


# BALANCE

st.markdown("""
<div class="balance">
    <div class="balance-label">AVAILABLE BALANCE</div>
    <div class="amount">₹2,840</div>
    <div class="demo">Demo wallet</div>
</div>
""", unsafe_allow_html=True)


# QUICK ACTIONS

st.markdown(
    '<div class="section">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("＋ Add")

with col2:
    st.button("↗ Send")

with col3:
    st.button("📊 Track")


# MONTHLY LIMIT

st.markdown(
    '<div class="section">MONTHLY LIMIT</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

    <div class="label">SPENT THIS MONTH</div>

    <div class="big">₹1,260</div>

    <div class="small">₹740 remaining of ₹2,000</div>

    <div class="bar">
        <div class="fill"></div>
    </div>

</div>
""", unsafe_allow_html=True)


# RECENT ACTIVITY

st.markdown(
    '<div class="section">RECENT ACTIVITY</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="tx">
    <span class="tx-money">-₹180</span>
    <div class="tx-name">🍔 Food</div>
    <div class="tx-date">Today</div>
</div>

<div class="tx">
    <span class="tx-money">-₹299</span>
    <div class="tx-name">🎮 Gaming</div>
    <div class="tx-date">Yesterday</div>
</div>

<div class="tx">
    <span class="tx-money">-₹450</span>
    <div class="tx-name">📚 Study</div>
    <div class="tx-date">Aug 10</div>
</div>

<div class="tx">
    <span class="tx-money" style="color:#6ee7a0;">+₹1,000</span>
    <div class="tx-name">💸 Pocket Money</div>
    <div class="tx-date">Aug 08</div>
</div>
""", unsafe_allow_html=True)


# SAVINGS

st.markdown(
    '<div class="section">SAVINGS GOAL</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

    <div class="tx-name">🎧 New Headphones</div>

    <div class="small">
        ₹3,400 saved of ₹5,000
    </div>

    <div class="bar">
        <div class="fill" style="width:68%;"></div>
    </div>

</div>
""", unsafe_allow_html=True)