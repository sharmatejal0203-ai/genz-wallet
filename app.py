import streamlit as st

st.set_page_config(
    page_title="GENZ WALLET",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# DEMO DATA
# =========================

if "balance" not in st.session_state:
    st.session_state.balance = 2840

if "saved" not in st.session_state:
    st.session_state.saved = 740

if "spent" not in st.session_state:
    st.session_state.spent = 1260

if "limit" not in st.session_state:
    st.session_state.limit = 2000

# =========================
# GEN-Z EDITORIAL THEME
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #080808;
    color: #F5F0E8;
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Hide default menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* HEADINGS */

h1, h2, h3 {
    font-family: 'Anton', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* HERO */

.hero {
    border: 1px dotted #777;
    background: #0D0D0D;
    padding: 30px;
    margin-bottom: 22px;
}

.hero-small {
    font-size: 12px;
    letter-spacing: 3px;
    color: #999;
    font-weight: 700;
}

.hero-title {
    font-family: 'Anton', sans-serif;
    font-size: clamp(50px, 8vw, 95px);
    line-height: 0.88;
    margin-top: 15px;
}

.red {
    color: #8E1F30;
}

/* BALANCE */

.balance {
    background: #761A2B;
    padding: 30px;
    min-height: 210px;
    position: relative;
    overflow: hidden;
}

.balance::after {
    content: "PAY";
    position: absolute;
    right: -20px;
    bottom: -35px;
    font-family: 'Anton';
    font-size: 130px;
    color: rgba(255,255,255,0.06);
}

.balance-label {
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.balance-number {
    font-size: 50px;
    font-weight: 800;
    margin-top: 20px;
}

/* CARDS */

.card {
    background: #111111;
    border: 1px dotted #555;
    padding: 22px;
    min-height: 145px;
}

.card-label {
    color: #999;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.card-number {
    font-size: 30px;
    font-weight: 800;
    margin-top: 15px;
}

/* SECTION */

.section-title {
    font-family: 'Anton', sans-serif;
    font-size: 32px;
    text-transform: uppercase;
    margin-top: 35px;
    margin-bottom: 15px;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    min-height: 50px;
    background: #8E1F30;
    color: #FFFFFF;
    border: 1px solid #A52A3C;
    border-radius: 2px;
    font-weight: 800;
    letter-spacing: 1px;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #A52A3C;
    transform: translateY(-2px);
}

/* QUICK ACTION */

.quick {
    background: #111;
    border: 1px dotted #555;
    padding: 18px;
    text-align: center;
    min-height: 95px;
}

/* MONEY MOMENT */

.money-moment {
    margin-top: 25px;
    padding: 22px;
    background: #151515;
    border-left: 5px solid #8E1F30;
}

.money-title {
    font-weight: 800;
    letter-spacing: 2px;
    font-size: 13px;
}

/* TRANSACTION */

.transaction {
    border-bottom: 1px dotted #444;
    padding: 16px 0;
}

.transaction-name {
    font-weight: 700;
}

.transaction-date {
    color: #777;
    font-size: 12px;
}

/* MOBILE */

@media (max-width: 700px) {

    .hero-title {
        font-size: 58px;
    }

    .balance-number {
        font-size: 40px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">
    <div class="hero-small">GEN-Z MONEY SPACE / 01</div>

    <div class="hero-title">
        YOUR MONEY.<br>
        <span class="red">YOUR RULES.</span>
    </div>

    <p style="color:#999;">
        Pay. Track. Save. Understand.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# BALANCE + LIMIT
# =========================

col1, col2 = st.columns([1.5, 1])

with col1:

    st.markdown(f"""
    <div class="balance">

        <div class="balance-label">
            Available Balance
        </div>

        <div class="balance-number">
            ₹{st.session_state.balance:,}
        </div>

        <div style="margin-top:15px;color:#E7C8CD;">
            Demo wallet • No real money
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    remaining = max(
        st.session_state.limit - st.session_state.spent,
        0
    )

    st.markdown(f"""
    <div class="card">

        <div class="card-label">
            Monthly Limit
        </div>

        <div class="card-number">
            ₹{st.session_state.spent:,}
        </div>

        <div style="color:#777;margin-top:5px;">
            of ₹{st.session_state.limit:,}
        </div>

        <div style="
            margin-top:20px;
            height:6px;
            background:#333;
        ">

            <div style="
                width:{min(st.session_state.spent / st.session_state.limit * 100,100)}%;
                height:6px;
                background:#8E1F30;
            "></div>

        </div>

        <div style="
            color:#999;
            font-size:12px;
            margin-top:10px;
        ">
            ₹{remaining:,} remaining
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================
# QUICK ACTIONS
# =========================

st.markdown(
    '<div class="section-title">Quick Move</div>',
    unsafe_allow_html=True
)

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.markdown(
        '<div class="quick">⚡<br><b>PAY</b></div>',
        unsafe_allow_html=True
    )

with q2:
    st.markdown(
        '<div class="quick">📊<br><b>TRACK</b></div>',
        unsafe_allow_html=True
    )

with q3:
    st.markdown(
        '<div class="quick">🫙<br><b>SAVE</b></div>',
        unsafe_allow_html=True
    )

with q4:
    st.markdown(
        '<div class="quick">💡<br><b>BILLS</b></div>',
        unsafe_allow_html=True
    )


# =========================
# MONEY SNAPSHOT
# =========================

st.markdown(
    '<div class="section-title">Money Snapshot</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Spent This Month</div>
        <div class="card-number">
            ₹{st.session_state.spent:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Saving Jar</div>
        <div class="card-number">
            ₹{st.session_state.saved:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="card-label">Money Health</div>
        <div class="card-number">
            82 / 100
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# PAY SECTION
# =========================

st.markdown(
    '<div class="section-title">Fast Pay</div>',
    unsafe_allow_html=True
)

pay1, pay2 = st.columns([1, 1])

with pay1:

    recipient = st.text_input(
        "UPI ID / Recipient",
        placeholder="friend@demo"
    )

with pay2:

    amount = st.number_input(
        "Amount ₹",
        min_value=1,
        value=50
    )


if st.button("⚡ CONFIRM PAYMENT"):

    if amount <= st.session_state.balance:

        st.session_state.balance -= amount
        st.session_state.spent += amount

        st.success(
            f"✓ Demo payment of ₹{amount} successful"
        )

        st.markdown("""
        <div class="money-moment">

            <div class="money-title">
                💡 MONEY MOMENT
            </div>

            <p>
                Your payment was automatically added
                to your expense tracker.
            </p>

            <p style="color:#999;">
                Small spends become big spends when repeated.
                Knowing where your money goes is the first step.
            </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.error("Not enough demo balance.")


# =========================
# SAVING JAR
# =========================

st.markdown(
    '<div class="section-title">Saving Jar</div>',
    unsafe_allow_html=True
)

s1, s2 = st.columns([1, 1])

with s1:

    st.markdown(f"""
    <div class="card">

        <div class="card-label">
            Saved So Far
        </div>

        <div class="card-number">
            ₹{st.session_state.saved:,}
        </div>

        <p style="color:#777;">
            Save ₹1 or ₹1,000. Your choice.
        </p>

    </div>
    """, unsafe_allow_html=True)


with s2:

    save_amount = st.number_input(
        "Add to Jar ₹",
        min_value=1,
        value=10
    )

    if st.button("🫙 SAVE MONEY"):

        if save_amount <= st.session_state.balance:

            st.session_state.balance -= save_amount
            st.session_state.saved += save_amount

            st.success(
                f"₹{save_amount} added to your Saving Jar!"
            )

        else:

            st.error("Not enough demo balance.")


# =========================
# MONEY MOMENT
# =========================

st.markdown("""
<div class="money-moment">

    <div class="money-title">
        ⚡ TODAY'S MONEY MOMENT
    </div>

    <p>
        Saving doesn't have to mean saving everything.
        Even ₹10 is a start.
    </p>

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
font-size:11px;
letter-spacing:2px;
">

GENZ WALLET • HACKATHON PROTOTYPE<br>
SIMULATED TRANSACTIONS ONLY

</div>
""", unsafe_allow_html=True)