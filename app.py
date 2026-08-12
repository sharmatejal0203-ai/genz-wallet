import streamlit as st
from datetime import datetime

# =========================
# PAGE
# =========================
st.set_page_config(
    page_title="GENZ WALLET",
    page_icon="⚡",
    layout="wide"
)

# =========================
# STATE
# =========================
defaults = {
    "balance": 2840,
    "saved": 740,
    "spent": 1260,
    "limit": 2000,
    "page": "Home",
    "transactions": [
        {"category": "Food", "amount": 120, "date": "Today"},
        {"category": "Transport", "amount": 80, "date": "Today"},
        {"category": "Shopping", "amount": 300, "date": "Yesterday"},
        {"category": "Education", "amount": 500, "date": "Aug 8"},
    ],
    "payment_done": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================
# CSS — BLACK + BURGUNDY
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #080808;
    color: #F5F0E8;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1,h2,h3 {
    font-family: 'Anton', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.hero {
    background: #0D0D0D;
    border: 1px dotted #666;
    padding: 28px;
    margin-bottom: 22px;
}

.hero-small {
    font-size: 11px;
    color: #888;
    letter-spacing: 3px;
}

.hero-title {
    font-family: 'Anton', sans-serif;
    font-size: clamp(48px, 8vw, 88px);
    line-height: .88;
    margin-top: 15px;
}

.red {
    color: #8E1F30;
}

.balance {
    background: #761A2B;
    padding: 30px;
    min-height: 190px;
}

.balance-label {
    font-size: 11px;
    letter-spacing: 3px;
}

.balance-number {
    font-size: 48px;
    font-weight: 800;
    margin-top: 15px;
}

.card {
    background: #111;
    border: 1px dotted #555;
    padding: 22px;
    min-height: 140px;
}

.label {
    color: #888;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.big {
    font-size: 30px;
    font-weight: 800;
    margin-top: 12px;
}

.money {
    background: #151515;
    border-left: 5px solid #8E1F30;
    padding: 20px;
    margin-top: 20px;
}

.tx {
    background: #111;
    border-bottom: 1px dotted #555;
    padding: 16px;
}

.txamount {
    float: right;
    font-weight: 800;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    background: #8E1F30;
    color: white;
    border: 1px solid #A52A3C;
    border-radius: 2px;
    font-weight: 800;
}

.stButton > button:hover {
    background: #A52A3C;
}

.section {
    font-family: 'Anton';
    font-size: 30px;
    margin: 32px 0 15px 0;
}

.qr {
    background: #F5F0E8;
    color: #080808;
    padding: 35px;
    text-align: center;
    font-size: 60px;
    font-weight: 900;
}

.success {
    background: #151515;
    border: 1px solid #8E1F30;
    padding: 30px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("# GENZ ⚡")

pages = [
    "Home",
    "Pay",
    "Track",
    "Saving Jar",
    "Monthly Limit",
    "History",
]

st.session_state.page = st.sidebar.radio(
    "MENU",
    pages,
    index=pages.index(st.session_state.page)
)

st.sidebar.markdown("---")
st.sidebar.caption("HACKATHON DEMO")
st.sidebar.caption("SIMULATED MONEY ONLY")

# =========================
# HOME
# =========================
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">GEN-Z MONEY SPACE / 01</div>

        <div class="hero-title">
            YOUR MONEY.<br>
            <span class="red">YOUR RULES.</span>
        </div>

        <p style="color:#888;">
            Pay • Track • Save • Understand
        </p>
    </div>
    """, unsafe_allow_html=True)

    a, b = st.columns([1.4, 1])

    with a:
        st.markdown(f"""
        <div class="balance">
            <div class="balance-label">AVAILABLE BALANCE</div>
            <div class="balance-number">
                ₹{st.session_state.balance:,}
            </div>
            <div style="color:#E5C5CB;">
                Demo wallet
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        remaining = max(
            st.session_state.limit - st.session_state.spent, 0
        )

        st.markdown(f"""
        <div class="card">
            <div class="label">MONTHLY LIMIT</div>
            <div class="big">
                ₹{st.session_state.spent:,}
            </div>
            <div style="color:#777;">
                of ₹{st.session_state.limit:,}
            </div>
            <br>
            <div style="color:#999;">
                ₹{remaining:,} remaining
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section">Money Snapshot</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="label">SPENT</div>
            <div class="big">₹{st.session_state.spent:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="label">SAVED</div>
            <div class="big">₹{st.session_state.saved:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="label">MONEY HEALTH</div>
            <div class="big">82 / 100</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="money">
        <b>💡 MONEY MOMENT</b>
        <p>
        Knowing where your money goes is the first step
        to making better money decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# PAY
# =========================
elif st.session_state.page == "Pay":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">FAST PAYMENT / DEMO</div>
        <div class="hero-title">
            SCAN.<br>
            <span class="red">PAY.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "DEMO ONLY — No real UPI or bank transaction is performed."
    )

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
        <div class="qr">
            ▦<br>
            <span style="font-size:18px;">SCAN QR</span>
        </div>
        """, unsafe_allow_html=True)

    with right:

        recipient = st.text_input(
            "UPI ID / Recipient",
            placeholder="someone@demo"
        )

        amount = st.number_input(
            "Amount ₹",
            min_value=1,
            value=50
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Shopping",
                "Groceries",
                "Transport",
                "Education",
                "Electricity",
                "Water",
                "Recharge",
                "Other"
            ]
        )

        if st.button("🔐 PAY WITH BIOMETRIC"):

            if amount > st.session_state.balance:

                st.error("Insufficient demo balance.")

            else:

                st.session_state.balance -= amount
                st.session_state.spent += amount

                st.session_state.transactions.insert(
                    0,
                    {
                        "category": category,
                        "amount": amount,
                        "date": datetime.now().strftime("%d %b %Y")
                    }
                )

                st.session_state.payment_done = True

                st.success("✓ PAYMENT SUCCESSFUL")

    if st.session_state.payment_done:

        st.markdown("""
        <div class="success">

            <div style="font-size:45px;">✓</div>

            <h2>PAYMENT DONE</h2>

            <p>
            Your payment was automatically added
            to your expense tracker.
            </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="money">

            <b>💡 MONEY MOMENT</b>

            <p>
            Every payment tells a story about where
            your money is going. Keep tracking it.
            </p>

        </div>
        """, unsafe_allow_html=True)

        if st.button("MAKE ANOTHER PAYMENT"):
            st.session_state.payment_done = False
            st.rerun()


# =========================
# TRACK
# =========================
elif st.session_state.page == "Track":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">EXPENSE TRACKER / 02</div>
        <div class="hero-title">
            WHERE DID<br>
            <span class="red">IT GO?</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "TOTAL SPENT THIS MONTH",
        f"₹{st.session_state.spent:,}"
    )

    st.markdown(
        '<div class="section">Categories</div>',
        unsafe_allow_html=True
    )

    categories = {
        "Food": 320,
        "Transport": 250,
        "Shopping": 300,
        "Education": 190,
        "Bills": 120,
        "Other": 80
    }

    for name, value in categories.items():

        st.write(f"**{name}** — ₹{value}")

        percentage = min(
            value / max(st.session_state.spent, 1),
            1.0
        )

        st.progress(percentage)

    st.markdown(
        '<div class="section">Recent Spending</div>',
        unsafe_allow_html=True
    )

    for tx in st.session_state.transactions[:6]:

        st.markdown(f"""
        <div class="tx">

            <span class="tx">
                <b>{tx["category"]}</b>
                <br>
                <small style="color:#777;">
                    {tx["date"]}
                </small>
            </span>

            <span class="txamount">
                ₹{tx["amount"]}
            </span>

        </div>
        """, unsafe_allow_html=True)


# =========================
# SAVING JAR
# =========================
elif st.session_state.page == "Saving Jar":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">VOLUNTARY SAVING</div>
        <div class="hero-title">
            SAVE IT.<br>
            <span class="red">YOUR WAY.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "SAVING JAR",
        f"₹{st.session_state.saved:,}"
    )

    st.write(
        "No forced saving. ₹1 or ₹1,000 — you decide."
    )

    amount = st.number_input(
        "Amount to save ₹",
        min_value=1,
        value=10
    )

    if st.button("🫙 ADD TO SAVING JAR"):

        if amount <= st.session_state.balance:

            st.session_state.balance -= amount
            st.session_state.saved += amount

            st.success(
                f"₹{amount} added to your Saving Jar."
            )

            st.rerun()

        else:
            st.error("Not enough demo balance.")

    st.markdown("---")

    withdraw = st.number_input(
        "Withdraw ₹",
        min_value=1,
        value=10
    )

    if st.button("↩ WITHDRAW"):

        if withdraw <= st.session_state.saved:

            st.session_state.saved -= withdraw
            st.session_state.balance += withdraw

            st.success(
                f"₹{withdraw} withdrawn from your jar."
            )

            st.rerun()

        else:
            st.error("Not enough money in the jar.")


# =========================
# MONTHLY LIMIT
# =========================
elif st.session_state.page == "Monthly Limit":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
            KNOW YOUR<br>
            <span class="red">LIMIT.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    new_limit = st.number_input(
        "Monthly Limit ₹",
        min_value=100,
        value=st.session_state.limit
    )

    if st.button("SAVE MONTHLY LIMIT"):

        st.session_state.limit = new_limit

        st.success("Monthly limit updated.")

        st.rerun()

    remaining = st.session_state.limit - st.session_state.spent

    st.metric(
        "REMAINING",
        f"₹{max(remaining, 0):,}"
    )

    progress = min(
        st.session_state.spent /
        max(st.session_state.limit, 1),
        1.0
    )

    st.progress(progress)

    if remaining <= 0:
        st.error("⚠️ MONTHLY LIMIT REACHED")

    elif remaining < st.session_state.limit * 0.2:
        st.warning("You're close to your monthly limit.")


# =========================
# HISTORY
# =========================
elif st.session_state.page == "History":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">
            YOUR<br>
            <span class="red">HISTORY.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Transactions remain visible in this demo."
    )

    for tx in st.session_state.transactions:

        st.markdown(f"""
        <div class="tx">

            <b>{tx["category"]}</b>

            <span class="txamount">
                ₹{tx["amount"]}
            </span>

            <br>

            <small style="color:#777;">
                {tx["date"]}
            </small>

        </div>
        """, unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown("""
<div style="
text-align:center;
color:#555;
font-size:10px;
letter-spacing:2px;
">
GENZ WALLET • HACKATHON PROTOTYPE<br>
SIMULATED TRANSACTIONS ONLY
</div>
""", unsafe_allow_html=True)