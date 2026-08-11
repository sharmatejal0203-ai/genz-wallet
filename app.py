import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GenZ Wallet",
    page_icon="⚡",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "balance" not in st.session_state:
    st.session_state.balance = 2840

if "saved" not in st.session_state:
    st.session_state.saved = 740

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "limit" not in st.session_state:
    st.session_state.limit = 2000

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        ("Food", "₹120", "Today"),
        ("Transport", "₹80", "Today"),
        ("Shopping", "₹300", "Yesterday"),
        ("Education", "₹500", "Aug 8"),
    ]

# ---------------- GEN-Z CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #090909;
    color: #F5F0E8;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

h1, h2, h3 {
    font-family: 'Anton', sans-serif !important;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.hero {
    border: 1px dotted #777;
    padding: 28px;
    margin-bottom: 20px;
    background: #111;
}

.hero-title {
    font-family: 'Anton';
    font-size: 58px;
    line-height: .95;
    color: #F5F0E8;
}

.hero-title span {
    color: #8F1D2C;
}

.balance-card {
    background: #741827;
    padding: 30px;
    border-radius: 4px;
    min-height: 190px;
}

.balance-label {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.balance {
    font-size: 52px;
    font-weight: 800;
    margin-top: 15px;
}

.card {
    background: #121212;
    border: 1px dotted #666;
    padding: 22px;
    min-height: 130px;
}

.card-title {
    font-size: 13px;
    color: #aaa;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.card-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 12px;
}

.section {
    margin-top: 35px;
    margin-bottom: 15px;
    font-family: 'Anton';
    font-size: 30px;
    text-transform: uppercase;
}

.stButton > button {
    width: 100%;
    border-radius: 3px;
    border: 1px solid #8F1D2C;
    background: #8F1D2C;
    color: white;
    font-weight: 800;
    min-height: 48px;
}

.stButton > button:hover {
    background: #A92335;
    border-color: #A92335;
}

.tip {
    background: #171717;
    border-left: 5px solid #8F1D2C;
    padding: 18px;
    margin-top: 20px;
}

.tx {
    border-bottom: 1px dotted #555;
    padding: 15px 0;
}

.small {
    color: #999;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("# GENZ ⚡")
st.sidebar.caption("Money, but make it simple.")

page = st.sidebar.radio(
    "MENU",
    [
        "Home",
        "Pay",
        "Track",
        "Saving Jar",
        "Monthly Limit",
        "Family",
        "Services",
        "History"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("DEMO PROTOTYPE")
st.sidebar.caption("No real UPI or bank connection")

# ---------------- HOME ----------------
if page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="small">WELCOME BACK 👋</div>
        <div class="hero-title">
            YOUR MONEY.<br>
            <span>YOUR RULES.</span>
        </div>
        <p>Pay • Track • Save • Understand</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown(f"""
        <div class="balance-card">
            <div class="balance-label">Available Balance</div>
            <div class="balance">₹{st.session_state.balance:,}</div>
            <div class="small">Demo wallet balance</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        remaining = max(st.session_state.limit - st.session_state.spent, 0)
        st.markdown(f"""
        <div class="card">
            <div class="card-title">Monthly Limit</div>
            <div class="card-value">₹{st.session_state.spent:,} / ₹{st.session_state.limit:,}</div>
            <div class="small">₹{remaining:,} remaining</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section">Quick Actions</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("⚡ PAY"):
            st.session_state.page = "Pay"

    with c2:
        if st.button("📊 TRACK"):
            st.session_state.page = "Track"

    with c3:
        if st.button("🫙 SAVE"):
            st.session_state.page = "Saving Jar"

    with c4:
        if st.button("📱 BILLS"):
            st.session_state.page = "Services"

    st.markdown('<div class="section">Money Snapshot</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.markdown(f"""
        <div class="card">
        <div class="card-title">Spent This Month</div>
        <div class="card-value">₹{st.session_state.spent:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown(f"""
        <div class="card">
        <div class="card-title">Saving Jar</div>
        <div class="card-value">₹{st.session_state.saved:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <div class="card-title">Money Health</div>
        <div class="card-value">82 / 100</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip">
    💡 <b>MONEY MOMENT</b><br><br>
    Small purchases can become big expenses when repeated.
    Knowing where your money goes is the first step to controlling it.
    </div>
    """, unsafe_allow_html=True)

# ---------------- PAY ----------------
elif page == "Pay":

    st.markdown('<div class="hero-title">SCAN.<br><span>PAY.</span></div>',
                unsafe_allow_html=True)

    st.info("⚠️ DEMO PAYMENT — No real money will be transferred.")

    recipient = st.text_input("Recipient / UPI ID", "friend@demo")
    amount = st.number_input("Amount ₹", min_value=1, value=50)

    category = st.selectbox(
        "Expense Category",
        ["Food", "Shopping", "Groceries", "Transport",
         "Education", "Bills", "Recharge", "Other"]
    )

    if st.button("⚡ CONFIRM WITH BIOMETRIC"):

        if amount > st.session_state.balance:
            st.error("Insufficient demo balance.")
        else:
            st.session_state.balance -= amount
            st.session_state.spent += amount

            st.session_state.transactions.insert(
                0,
                (category, f"₹{amount}", "Just now")
            )

            st.success(f"✓ Payment of ₹{amount} successful!")

            st.markdown("""
            <div class="tip">
            💡 <b>MONEY MOMENT</b><br><br>
            Your payment was added to your expense tracker automatically.
            </div>
            """, unsafe_allow_html=True)

# ---------------- TRACK ----------------
elif page == "Track":

    st.markdown('<div class="hero-title">WHERE DID<br><span>IT GO?</span></div>',
                unsafe_allow_html=True)

    categories = {
        "Food": 320,
        "Transport": 250,
        "Shopping": 300,
        "Education": 190,
        "Bills": 120,
        "Other": 80
    }

    st.metric("Total Spent", f"₹{st.session_state.spent:,}")

    st.markdown("### EXPENSE BREAKDOWN")

    for category, value in categories.items():
        percentage = min(value / max(st.session_state.spent, 1), 1.0)
        st.write(f"**{category}** — ₹{value}")
        st.progress(percentage)

# ---------------- SAVING JAR ----------------
elif page == "Saving Jar":

    st.markdown('<div class="hero-title">SAVE IT.<br><span>YOUR WAY.</span></div>',
                unsafe_allow_html=True)

    st.metric("Saving Jar", f"₹{st.session_state.saved:,}")

    st.write("Choose how much you want to save.")

    amount = st.number_input(
        "Amount ₹",
        min_value=1,
        value=10
    )

    if st.button("🫙 ADD TO JAR"):

        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.session_state.saved += amount
            st.success(f"₹{amount} added to your Saving Jar!")
            st.rerun()
        else:
            st.error("Not enough demo balance.")

    st.markdown("---")

    withdraw = st.number_input(
        "Withdraw from Jar ₹",
        min_value=1,
        value=10
    )

    if st.button("↩ WITHDRAW"):

        if withdraw <= st.session_state.saved:
            st.session_state.saved -= withdraw
            st.session_state.balance += withdraw
            st.success(f"₹{withdraw} withdrawn.")
            st.rerun()
        else:
            st.error("Not enough saved money.")

# ---------------- MONTHLY LIMIT ----------------
elif page == "Monthly Limit":

    st.markdown('<div class="hero-title">KNOW YOUR<br><span>LIMIT.</span></div>',
                unsafe_allow_html=True)

    new_limit = st.number_input(
        "Set Monthly Limit ₹",
        min_value=100,
        value=st.session_state.limit
    )

    if st.button("SAVE LIMIT"):
        st.session_state.limit = new_limit
        st.success("Monthly limit updated.")
        st.rerun()

    remaining = st.session_state.limit - st.session_state.spent

    st.metric("Spent", f"₹{st.session_state.spent:,}")
    st.metric("Remaining", f"₹{max(remaining, 0):,}")

    progress = min(st.session_state.spent / st.session_state.limit, 1.0)
    st.progress(progress)

    if remaining <= 0:
        st.error("⚠️ Monthly limit reached.")

    elif remaining < st.session_state.limit * 0.2:
        st.warning("You're close to your monthly limit.")

# ---------------- FAMILY ----------------
elif page == "Family":

    st.markdown('<div class="hero-title">TRUSTED<br><span>PEOPLE.</span></div>',
                unsafe_allow_html=True)

    st.write("Add a parent or sibling as your trusted family contact.")

    name = st.text_input("Name")
    relation = st.selectbox(
        "Relationship",
        ["Parent", "Sibling"]
    )
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("ADD FAMILY CONTACT"):
        if name and phone:
            st.success(f"✓ {name} added as your trusted {relation}.")
        else:
            st.warning("Please enter at least name and phone.")

# ---------------- SERVICES ----------------
elif page == "Services":

    st.markdown('<div class="hero-title">PAY<br><span>STUFF.</span></div>',
                unsafe_allow_html=True)

    service = st.selectbox(
        "Choose Service",
        ["Mobile Recharge", "Electricity Bill",
         "Water Bill", "Internet Bill", "Education Fees"]
    )

    number = st.text_input("Account / Mobile / Consumer Number")
    amount = st.number_input("Amount ₹", min_value=1, value=100)

    if st.button("PAY NOW"):
        st.success(
            f"✓ Demo payment of ₹{amount} for {service} successful."
        )

# ---------------- HISTORY ----------------
elif page == "History":

    st.markdown('<div class="hero-title">YOUR<br><span>HISTORY.</span></div>',
                unsafe_allow_html=True)

    for category, amount, date in st.session_state.transactions:

        st.markdown(
            f"""
            <div class="tx">
                <b>{category}</b><br>
                <span class="small">{date}</span>
                <span style="float:right;font-weight:800">{amount}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.caption("GENZ WALLET • HACKATHON DEMO • SIMULATED TRANSACTIONS ONLY")