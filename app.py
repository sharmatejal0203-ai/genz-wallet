import streamlit as st
import pandas as pd
import math

=========================================================

VELORA V7

INTELLIGENT MONEY MANAGEMENT

DEMO ONLY - NO REAL MONEY / UPI / BANK CONNECTION

=========================================================

st.set_page_config(
page_title="VELORA",
page_icon="V",
layout="centered",
initial_sidebar_state="collapsed"
)

=========================================================

PREMIUM CSS

=========================================================

st.markdown("""

<style>  
  
.stApp {  
    background:  
        radial-gradient(circle at 50% -10%, #292D46 0%, #0B0C11 38%, #08090D 100%);  
    color: #F5F5F7;  
}  
  
.block-container {  
    max-width: 620px;  
    padding: 24px 16px 90px;  
}  
  
#MainMenu, footer, header {  
    visibility: hidden;  
}  
  
h1, h2, h3, h4, p, label {  
    color: #F5F5F7 !important;  
}  
  
.stButton > button {  
    background: #151821 !important;  
    color: white !important;  
    border: 1px solid #303542 !important;  
    border-radius: 14px !important;  
    min-height: 44px !important;  
    font-weight: 700 !important;  
    transition: .2s ease;  
}  
  
.stButton > button:hover {  
    border-color: #9B7BFF !important;  
    background: #1D202B !important;  
    transform: translateY(-1px);  
}  
  
.stTextInput input,  
.stNumberInput input {  
    background: #11141A !important;  
    color: white !important;  
}  
  
.stSelectbox div[data-baseweb="select"] {  
    background: #11141A !important;  
}  
  
[data-testid="stMetric"] {  
    background: #12151C;  
    border: 1px solid #292E38;  
    border-radius: 18px;  
    padding: 15px;  
}  
  
[data-testid="stMetricValue"] {  
    color: white !important;  
    font-weight: 850 !important;  
}  
  
[data-testid="stMetricLabel"] {  
    color: #858B98 !important;  
}  
  
.stProgress > div > div > div > div {  
    background: #9B7BFF;  
}  
  
.brand {  
    font-size: 30px;  
    font-weight: 950;  
    letter-spacing: 5px;  
}  
  
.tagline {  
    color: #858B98;  
    font-size: 10px;  
    letter-spacing: 2px;  
}  
  
.hero {  
    background: linear-gradient(145deg,#1B1F2A,#101217);  
    border: 1px solid #303542;  
    border-radius: 26px;  
    padding: 24px;  
    margin: 18px 0;  
    box-shadow: 0 18px 50px rgba(0,0,0,.18);  
}  
  
.balance-label {  
    color: #858B98;  
    font-size: 10px;  
    letter-spacing: 2px;  
    font-weight: 700;  
}  
  
.balance {  
    font-size: 44px;  
    font-weight: 900;  
    margin: 4px 0;  
}  
  
.muted {  
    color: #858B98 !important;  
    font-size: 11px;  
}  
  
.section {  
    color: white;  
    font-size: 18px;  
    font-weight: 850;  
    margin-top: 26px;  
    margin-bottom: 10px;  
}  
  
.insight {  
    background: linear-gradient(145deg,#1A1624,#101116);  
    border: 1px solid #493960;  
    border-radius: 22px;  
    padding: 20px;  
    margin: 15px 0;  
}  
  
.insight-label {  
    color: #A98CFF;  
    font-size: 10px;  
    font-weight: 850;  
    letter-spacing: 2px;  
}  
  
.insight-title {  
    color: white;  
    font-size: 18px;  
    font-weight: 850;  
    margin-top: 7px;  
}  
  
.insight-text {  
    color: #999DA9;  
    font-size: 12px;  
    line-height: 1.55;  
    margin-top: 5px;  
}  
  
.ai-card {  
    background:  
        radial-gradient(circle at 100% 0%, #463A68 0%, transparent 40%),  
        linear-gradient(145deg,#1E1930,#101116);  
    border: 1px solid #66528B;  
    border-radius: 24px;  
    padding: 21px;  
    margin: 15px 0;  
    box-shadow: 0 15px 45px rgba(77,55,120,.12);  
}  
  
.ai-badge {  
    color: #B69CFF;  
    font-size: 9px;  
    letter-spacing: 2px;  
    font-weight: 900;  
}  
  
.ai-title {  
    font-size: 19px;  
    font-weight: 900;  
    margin-top: 7px;  
}  
  
.ai-text {  
    color: #A9A4B5;  
    font-size: 12px;  
    line-height: 1.6;  
    margin-top: 7px;  
}  
  
.prediction {  
    background: linear-gradient(145deg,#151A25,#101217);  
    border: 1px solid #343D50;  
    border-radius: 23px;  
    padding: 20px;  
    margin: 15px 0;  
}  
  
.prediction-title {  
    font-size: 16px;  
    font-weight: 850;  
}  
  
.prediction-number {  
    font-size: 30px;  
    font-weight: 950;  
    margin-top: 4px;  
}  
  
.prediction-small {  
    color: #858B98;  
    font-size: 10px;  
}  
  
.budget {  
    background: linear-gradient(145deg,#151922,#101217);  
    border: 1px solid #303542;  
    border-radius: 22px;  
    padding: 19px;  
    margin: 14px 0;  
}  
  
.budget-title {  
    font-size: 15px;  
    font-weight: 850;  
}  
  
.budget-value {  
    font-size: 25px;  
    font-weight: 900;  
    margin: 5px 0;  
}  
  
.budget-small {  
    color: #858B98;  
    font-size: 10px;  
}  
  
.transaction {  
    background: #11141A;  
    border: 1px solid #252A34;  
    border-radius: 16px;  
    padding: 14px;  
    margin: 8px 0;  
}  
  
.tx-title {  
    font-weight: 750;  
    font-size: 13px;  
}  
  
.tx-cat {  
    color: #777D89;  
    font-size: 10px;  
}  
  
.tx-income {  
    color: #6EE7A0;  
    font-weight: 800;  
}  
  
.tx-expense {  
    color: #FF7D91;  
    font-weight: 800;  
}  
  
.goal {  
    background: #11141A;  
    border: 1px solid #292E38;  
    border-radius: 20px;  
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
  
.virtual-card {  
    background:  
        radial-gradient(circle at 80% 10%,#5A4E82 0%,transparent 35%),  
        linear-gradient(135deg,#292D3C,#101218);  
    border: 1px solid #505566;  
    border-radius: 27px;  
    padding: 25px;  
    min-height: 170px;  
    margin: 18px 0;  
    box-shadow: 0 15px 45px rgba(0,0,0,.35);  
}  
  
.card-brand {  
    font-weight: 900;  
    letter-spacing: 4px;  
}  
  
.card-number {  
    font-size: 19px;  
    letter-spacing: 3px;  
    margin-top: 32px;  
}  
  
.card-small {  
    color: #858B98;  
    font-size: 9px;  
    letter-spacing: 1px;  
    margin-top: 16px;  
}  
  
.score {  
    background:  
        radial-gradient(circle at 50% 0%,#44335D 0%,transparent 48%),  
        linear-gradient(145deg,#211A31,#111219);  
    border: 1px solid #57436F;  
    border-radius: 25px;  
    padding: 25px;  
    text-align: center;  
    margin: 15px 0;  
}  
  
.score-number {  
    font-size: 48px;  
    font-weight: 950;  
}  
  
.score-label {  
    color: #9A9DA8;  
    font-size: 10px;  
    letter-spacing: 2px;  
}  
  
.score-sub {  
    color: #B49BEF;  
    font-size: 11px;  
    margin-top: 6px;  
}  
  
.score-row {  
    background: #11141A;  
    border: 1px solid #282D38;  
    border-radius: 14px;  
    padding: 12px;  
    margin: 7px 0;  
}  
  
.score-name {  
    font-size: 11px;  
    color: #858B98;  
}  
  
.score-value {  
    font-size: 15px;  
    font-weight: 850;  
}  
  
.notice {  
    background: #151821;  
    border: 1px solid #303542;  
    border-radius: 15px;  
    padding: 13px;  
    margin: 8px 0;  
    color: #C3C6CF;  
    font-size: 12px;  
}  
  
.profile-box {  
    background: linear-gradient(145deg,#1B1F2A,#101217);  
    border: 1px solid #303542;  
    border-radius: 24px;  
    padding: 24px;  
    text-align: center;  
    margin: 18px 0;  
}  
  
.avatar {  
    font-size: 46px;  
}  
  
.profile-name {  
    font-size: 24px;  
    font-weight: 900;  
}  
  
.small-label {  
    color: #858B98;  
    font-size: 9px;  
    letter-spacing: 2px;  
    margin-top: 5px;  
}  
  
</style>  """, unsafe_allow_html=True)

=========================================================

SESSION STATE

=========================================================

defaults = {
"balance": 5000.0,
"monthly_limit": 2000.0,
"name": "Tejal",
"page": "Home",
"jar": 850.0,
"card_frozen": False,
"notifications": [],
"coach_mode": "Smart",
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

=========================================================

CORE FUNCTIONS

=========================================================

def go(page):
st.session_state.page = page
st.rerun()

def add_transaction(name, category, amount):
st.session_state.transactions.insert(
0,
[name, category, float(amount)]
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

def category_totals():
data = {}

for item in st.session_state.transactions:  
    if item[2] < 0:  
        category = item[1]  

        data[category] = (  
            data.get(category, 0)  
            + abs(item[2])  
        )  

return data

def biggest_category():
data = category_totals()

if not data:  
    return "None", 0  

category = max(data, key=data.get)  

return category, data[category]

=========================================================

SMART PREDICTION ENGINE

=========================================================

def average_daily_spend():
expenses = [
abs(x[2])
for x in st.session_state.transactions
if x[2] < 0
]

if not expenses:  
    return 0  

return sum(expenses) / max(len(expenses), 1)

def predicted_monthly_spending():
"""
Demo prediction model.

Uses current spending + transaction frequency  
to estimate future spending.  
"""  

spent = spending_total()  

expense_count = len([  
    x for x in st.session_state.transactions  
    if x[2] < 0  
])  

if expense_count == 0:  
    return 0  

avg_transaction = spent / expense_count  

# Demo assumption:  
# approximately 30 transactions/month  
prediction = avg_transaction * 30  

return prediction

def predicted_7_day_spending():
daily = average_daily_spend()

return daily * 7

def spending_velocity():
expenses = [
abs(x[2])
for x in st.session_state.transactions
if x[2] < 0
]

if len(expenses) < 2:  
    return "Stable"  

recent = expenses[:2]  
older = expenses[2:]  

if not older:  
    return "Stable"  

recent_avg = sum(recent) / len(recent)  
older_avg = sum(older) / len(older)  

if recent_avg > older_avg * 1.25:  
    return "Rising"  

if recent_avg < older_avg * 0.75:  
    return "Improving"  

return "Stable"

def prediction_message():

predicted = predicted_monthly_spending()  
limit = max(  
    float(st.session_state.monthly_limit),  
    1  
)  

velocity = spending_velocity()  

if predicted > limit * 1.20:  
    return (  
        "High spending risk",  
        "At your current transaction pattern, "  
        "VELORA predicts you may significantly exceed "  
        "your monthly budget."  
    )  

if predicted > limit:  
    return (  
        "Budget pressure detected",  
        "Your current spending pattern may push "  
        "you above your monthly limit."  
    )  

if velocity == "Improving":  
    return (  
        "Positive trend",  
        "Your recent spending pattern is moving downward."  
    )  

if velocity == "Rising":  
    return (  
        "Spending is accelerating",  
        "Your recent transactions are higher than earlier spending."  
    )  

return (  
    "Stable spending pattern",  
    "Your current spending pace appears relatively stable."  
)

=========================================================

ADVANCED VELORA SCORE

=========================================================

def score_breakdown():

spent = spending_total()  
income = income_total()  
limit = max(  
    float(st.session_state.monthly_limit),  
    1  
)  

# Budget discipline  
ratio = spent / limit  

if ratio <= 0.50:  
    budget_score = 35  
elif ratio <= 0.70:  
    budget_score = 30  
elif ratio <= 0.85:  
    budget_score = 24  
elif ratio <= 1:  
    budget_score = 17  
else:  
    budget_score = 8  

# Saving behaviour  
if st.session_state.jar >= 2000:  
    saving_score = 25  
elif st.session_state.jar >= 1000:  
    saving_score = 21  
elif st.session_state.jar >= 500:  
    saving_score = 15  
else:  
    saving_score = 8  

# Balance safety  
if income > 0:  
    balance_ratio = st.session_state.balance / income  

    if balance_ratio >= 1:  
        balance_score = 20  
    elif balance_ratio >= 0.50:  
        balance_score = 16  
    elif balance_ratio >= 0.25:  
        balance_score = 12  
    else:  
        balance_score = 7  
else:  
    balance_score = 10  

# Spending trend  
velocity = spending_velocity()  

if velocity == "Improving":  
    trend_score = 20  
elif velocity == "Stable":  
    trend_score = 16  
else:  
    trend_score = 9  

total = min(  
    budget_score  
    + saving_score  
    + balance_score  
    + trend_score,  
    100  
)  

return {  
    "Budget Discipline": budget_score,  
    "Saving Habit": saving_score,  
    "Balance Safety": balance_score,  
    "Spending Trend": trend_score,  
    "Total": total  
}

def financial_score():
return score_breakdown()["Total"]

def score_label(score):

if score >= 90:  
    return "Excellent financial behaviour"  

if score >= 80:  
    return "Strong financial behaviour"  

if score >= 70:  
    return "Good, but can improve"  

if score >= 60:  
    return "Needs attention"  

return "High financial risk"

=========================================================

BUDGET STATUS

=========================================================

def budget_status():

spent = spending_total()  

limit = max(  
    float(st.session_state.monthly_limit),  
    1  
)  

ratio = spent / limit  

remaining = max(  
    limit - spent,  
    0  
)  

if ratio < 0.60:  
    return (  
        "BUDGET HEALTHY",  
        "Your spending is under control.",  
        remaining  
    )  

if ratio < 0.85:  
    return (  
        "WATCH YOUR SPENDING",  
        "You're getting closer to your monthly limit.",  
        remaining  
    )  

if ratio <= 1:  
    return (  
        "BUDGET AT RISK",  
        "Only a small part of your budget remains.",  
        remaining  
    )  

return (  
    "LIMIT EXCEEDED",  
    "You've crossed your monthly spending limit.",  
    remaining  
)

=========================================================

SMART AI FINANCIAL COACH

=========================================================

def ai_coach():

spent = spending_total()  

limit = max(  
    float(st.session_state.monthly_limit),  
    1  
)  

ratio = spent / limit  

biggest, value = biggest_category()  

predicted = predicted_monthly_spending()  

if ratio > 1:  

    return (  
        "🚨 Budget Intervention",  
        "You've already crossed your monthly limit. "  
        "VELORA recommends pausing non-essential purchases "  
        "until your budget resets."  
    )  

if predicted > limit:  

    return (  
        "⚠️ Future Budget Risk",  
        "Your current spending pace predicts approximately "  
        "Rs. {:,.0f} in monthly spending. "  
        "Try reducing your {} spending.".format(  
            predicted,  
            biggest  
        )  
    )  

if st.session_state.jar >= 1000:  

    return (  
        "✨ You're Building Momentum",  
        "Your Savings Jar has Rs. {:,.0f}. "  
        "Keep protecting this money from impulse spending."  
        .format(  
            st.session_state.jar  
        )  
    )  

if biggest != "None":  

    return (  
        "💡 One Smart Move",  
        "{} is your largest spending category at "  
        "Rs. {:,.0f}. Cutting even 10% here could free "  
        "up around Rs. {:,.0f}.".format(  
            biggest,  
            value,  
            value * 0.10  
        )  
    )  

return (  
    "🤖 VELORA is learning",  
    "Add a few transactions and VELORA will identify "  
    "your spending patterns."  
)

=========================================================

RESET

=========================================================

def reset_demo():

st.session_state.balance = 5000.0  
st.session_state.monthly_limit = 2000.0  
st.session_state.name = "Tejal"  
st.session_state.page = "Home"  
st.session_state.jar = 850.0  
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

=========================================================

HEADER

=========================================================

st.markdown(
'<div class="brand">VELORA</div>'
'<div class="tagline">INTELLIGENT MONEY MANAGEMENT</div>',
unsafe_allow_html=True
)

st.write("")

=========================================================

NAVIGATION

=========================================================

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

=========================================================

HOME

=========================================================

if st.session_state.page == "Home":

st.caption("GOOD EVENING")  

st.subheader(  
    st.session_state.name + " 👋"  
)  

st.markdown(  
    '<div class="hero">'  
    '<div class="balance-label">AVAILABLE BALANCE</div>'  
    '<div class="balance">Rs. {:,.0f}</div>'  
    '<div class="muted">Demo wallet · No real money connected</div>'  
    '</div>'.format(  
        st.session_state.balance  
    ),  
    unsafe_allow_html=True  
)  

a, b, c = st.columns(3)  

with a:  
    if st.button("＋ ADD", use_container_width=True):  
        go("Add")  

with b:  
    if st.button("↗ SEND", use_container_width=True):  
        go("Pay")  

with c:  
    if st.button("🎯 GOALS", use_container_width=True):  
        go("Goals")  

# -----------------------------------------------------  
# SMART BUDGET  
# -----------------------------------------------------  

spent = spending_total()  
limit = float(st.session_state.monthly_limit)  

status, status_text, remaining = budget_status()  

percentage = min(  
    spent / max(limit, 1),  
    1  
)  

st.markdown(  
    '<div class="budget">'  
    '<div class="budget-title">Smart Budget Protection</div>'  
    '<div class="budget-value">Rs. {:,.0f} spent of Rs. {:,.0f}</div>'  
    '<div class="budget-small">{:.0f}% used</div>'  
    '</div>'.format(  
        spent,  
        limit,  
        percentage * 100  
    ),  
    unsafe_allow_html=True  
)  

st.progress(percentage)  

if percentage < 0.60:  
    st.success(  
        "{} · {}".format(  
            status,  
            status_text  
        )  
    )  
elif percentage < 0.85:  
    st.warning(  
        "{} · {}".format(  
            status,  
            status_text  
        )  
    )  
else:  
    st.error(  
        "{} · {}".format(  
            status,  
            status_text  
        )  
    )  

    st.caption(
        "Rs. {:,.0f} remains available in your monthly budget."
        .format(remaining)
    )

    # -----------------------------------------------------
    # FINANCIAL SNAPSHOT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Financial Snapshot</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Spent",
            "Rs. {:,.0f}".format(spent)
        )

    with c2:
        st.metric(
            "Budget Left",
            "Rs. {:,.0f}".format(remaining)
        )

    c3, c4 = st.columns(2)

    with c3:
        st.metric(
            "Savings Jar",
            "Rs. {:,.0f}".format(
                st.session_state.jar
            )
        )

    with c4:
        st.metric(
            "VELORA Score",
            "{}/100".format(
                financial_score()
            )
        )

    # -----------------------------------------------------
    # AI FINANCIAL COACH
    # -----------------------------------------------------

    coach_title, coach_text = ai_coach()

    st.markdown(
        '<div class="ai-card">'
        '<div class="ai-badge">VELORA AI · FINANCIAL COACH</div>'
        '<div class="ai-title">{}</div>'
        '<div class="ai-text">{}</div>'
        '</div>'.format(
            coach_title,
            coach_text
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # ML SPENDING PREDICTION
    # -----------------------------------------------------

    predicted = predicted_monthly_spending()
    velocity = spending_velocity()

    st.markdown(
        '<div class="prediction">'
        '<div class="prediction-title">'
        '🔮 Spending Forecast'
        '</div>'
        '<div class="prediction-number">'
        'Rs. {:,.0f}'
        '</div>'
        '<div class="prediction-small">'
        'Estimated monthly spending · Trend: {}'
        '</div>'
        '</div>'.format(
            predicted,
            velocity
        ),
        unsafe_allow_html=True
    )

    # Prediction warning
    if predicted > limit:

        st.error(
            "⚠️ VELORA predicts that your current "
            "spending pattern may exceed your monthly budget."
        )

    elif predicted > limit * 0.80:

        st.warning(
            "⚡ You're approaching your predicted "
            "monthly spending limit."
        )

    else:

        st.success(
            "✓ Your predicted spending is currently "
            "within a safer range."
        )

    # -----------------------------------------------------
    # BIGGEST CATEGORY
    # -----------------------------------------------------

    biggest, value = biggest_category()

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">VELORA INTELLIGENCE</div>'
        '<div class="insight-title">'
        '{} is your biggest category'
        '</div>'
        '<div class="insight-text">'
        'Rs. {:,.0f} spent in this category.'
        '</div>'
        '</div>'.format(
            biggest,
            value
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SPENDING TREND
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Spending Trend</div>',
        unsafe_allow_html=True
    )

    expenses = [
        abs(x[2])
        for x in st.session_state.transactions
        if x[2] < 0
    ]

    if expenses:

        chart = pd.DataFrame(
            {
                "Spending": expenses[::-1]
            }
        )

        st.line_chart(chart)

    else:

        st.info("Add expenses to generate a spending trend.")

    # -----------------------------------------------------
    # SAVINGS JAR
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Savings Jar</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="goal">'
        '<div class="goal-title">Future Fund</div>'
        '<div class="goal-money">'
        'Rs. {:,.0f}'
        '</div>'
        '<div class="muted">'
        'Money intentionally set aside'
        '</div>'
        '</div>'.format(
            st.session_state.jar
        ),
        unsafe_allow_html=True
    )

    if st.button(
        "Manage Savings Jar",
        use_container_width=True
    ):
        go("Jar")

    # -----------------------------------------------------
    # RECENT ACTIVITY
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Recent Activity</div>',
        unsafe_allow_html=True
    )

    for name, category, amount in \
            st.session_state.transactions[:3]:

        css_class = (
            "tx-income"
            if amount > 0
            else "tx-expense"
        )

        sign = "+" if amount > 0 else "-"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-title">{}</div>'
            '<div class="tx-cat">{}</div>'
            '<div class="{}">{} Rs. {:,.0f}</div>'
            '</div>'.format(
                name,
                category,
                css_class,
                sign,
                abs(amount)
            ),
            unsafe_allow_html=True
        )


# =========================================================
# ADD MONEY
# =========================================================

elif st.session_state.page == "Add":

    st.subheader("Add Money")

    st.caption("Demo transaction only.")

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
        "Add to Wallet",
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
            "Rs. {:,.0f} added successfully.".format(
                amount
            )
        )

        st.session_state.page = "Home"
        st.rerun()

    if st.button(
        "← Back",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.subheader("Send Money")

    st.caption(
        "Simulated payment · No real UPI."
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="Friend or contact",
        key="recipient"
    )

    amount = st.number_input(
        "Amount",
        min_value=1.0,
        value=100.0,
        step=50.0,
        key="pay_amount"
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Education",
            "Shopping",
            "Entertainment",
            "Travel",
            "Bills",
            "Other"
        ],
        key="pay_category"
    )

    if st.button(
        "Send Payment",
        use_container_width=True
    ):

        if not recipient.strip():

            st.error("Enter recipient.")

        elif amount > st.session_state.balance:

            st.error("Insufficient demo balance.")

        elif st.session_state.card_frozen:

            st.error("Card is frozen.")

        else:

            st.session_state.balance -= amount

            add_transaction(
                "Sent to " + recipient.strip(),
                category,
                -amount
            )

            st.session_state.notifications.insert(
                0,
                "Rs. {:,.0f} sent to {}.".format(
                    amount,
                    recipient.strip()
                )
            )

            st.success(
                "Payment simulated successfully."
            )

            st.rerun()

    st.markdown(
        '<div class="section">VELORA Card</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="virtual-card">'
        '<div class="card-brand">VELORA</div>'
        '<div class="card-number">'
        '•••• •••• •••• 2840'
        '</div>'
        '<div class="card-small">'
        'DEMO VIRTUAL CARD · 09/30'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.card_frozen:

        st.warning(
            "🔒 VELORA Card is currently frozen."
        )

    else:

        st.success(
            "🟢 VELORA Card is active."
        )

    if st.button(
        "UNFREEZE CARD"
        if st.session_state.card_frozen
        else "FREEZE CARD",
        use_container_width=True
    ):

        st.session_state.card_frozen = (
            not st.session_state.card_frozen
        )

        if st.session_state.card_frozen:

            st.session_state.notifications.insert(
                0,
                "VELORA Card frozen."
            )

        else:

            st.session_state.notifications.insert(
                0,
                "VELORA Card unfrozen."
            )

        st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.subheader("Activity")

    st.caption("Complete demo transaction history")

    if not st.session_state.transactions:

        st.info("No transactions yet.")

    for name, category, amount in \
            st.session_state.transactions:

        css_class = (
            "tx-income"
            if amount > 0
            else "tx-expense"
        )

        sign = "+" if amount > 0 else "-"

        st.markdown(
            '<div class="transaction">'
            '<div class="tx-title">{}</div>'
            '<div class="tx-cat">{}</div>'
            '<div class="{}">{} Rs. {:,.0f}</div>'
            '</div>'.format(
                name,
                category,
                css_class,
                sign,
                abs(amount)
            ),
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.metric(
        "Total Income",
        "Rs. {:,.0f}".format(
            income_total()
        )
    )

    st.metric(
        "Total Spending",
        "Rs. {:,.0f}".format(
            spending_total()
        )
    )


# =========================================================
# INSIGHT
# =========================================================

elif st.session_state.page == "Insight":

    st.subheader("VELORA Intelligence")

    spent = spending_total()
    income = income_total()
    score = financial_score()

    biggest, value = biggest_category()

    # -----------------------------------------------------
    # MAIN SCORE
    # -----------------------------------------------------

    st.markdown(
        '<div class="score">'
        '<div class="score-number">{}/100</div>'
        '<div class="score-label">'
        'VELORA FINANCIAL SCORE'
        '</div>'
        '<div class="score-sub">{}</div>'
        '</div>'.format(
            score,
            score_label(score)
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SCORE BREAKDOWN
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Score Breakdown</div>',
        unsafe_allow_html=True
    )

    breakdown = score_breakdown()

    for name, value_score in breakdown.items():

        if name == "Total":
            continue

        st.markdown(
            '<div class="score-row">'
            '<div class="score-name">{}</div>'
            '<div class="score-value">{}/100</div>'
            '</div>'.format(
                name,
                value_score
            ),
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # AI COACH
    # -----------------------------------------------------

    coach_title, coach_text = ai_coach()

    st.markdown(
        '<div class="ai-card">'
        '<div class="ai-badge">'
        'VELORA AI · FINANCIAL COACH'
        '</div>'
        '<div class="ai-title">{}</div>'
        '<div class="ai-text">{}</div>'
        '</div>'.format(
            coach_title,
            coach_text
        ),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SPENDING FORECAST
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Spending Forecast</div>',
        unsafe_allow_html=True
    )

    predicted = predicted_monthly_spending()
    seven_day = predicted_7_day_spending()
    velocity = spending_velocity()

    p1, p2 = st.columns(2)

    with p1:
        st.metric(
            "Next 7 Days",
            "Rs. {:,.0f}".format(
                seven_day
            )
        )

    with p2:
        st.metric(
            "Monthly Forecast",
            "Rs. {:,.0f}".format(
                predicted
            )
        )

    st.markdown(
        '<div class="prediction">'
        '<div class="prediction-title">'
        '🔮 VELORA Spending Prediction'
        '</div>'
        '<div class="prediction-number">'
        'Rs. {:,.0f}'
        '</div>'
        '<div class="prediction-small">'
        'Projected monthly spending · Trend: {}'
        '</div>'
        '</div>'.format(
            predicted,
            velocity
        ),
        unsafe_allow_html=True
    )

    if predicted > st.session_state.monthly_limit:

        st.error(
            "⚠️ Forecast exceeds your current monthly budget."
        )

    elif predicted > st.session_state.monthly_limit * 0.80:

        st.warning(
            "⚡ Forecast is approaching your monthly budget."
        )

    else:

        st.success(
            "✓ Forecast is currently within your budget."
        )

    # -----------------------------------------------------
    # MONEY OVERVIEW
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Money Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Income",
            "Rs. {:,.0f}".format(
                income
            )
        )

    with c2:
        st.metric(
            "Spent",
            "Rs. {:,.0f}".format(
                spent
            )
        )

    # -----------------------------------------------------
    # CATEGORY BREAKDOWN
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Category Breakdown</div>',
        unsafe_allow_html=True
    )

    totals = category_totals()

    if totals:

        category_df = pd.DataFrame(
            {
                "Category": list(totals.keys()),
                "Amount": list(totals.values())
            }
        )

        category_df = category_df.set_index(
            "Category"
        )

        st.bar_chart(category_df)

    else:

        st.info(
            "No spending data available."
        )

    # -----------------------------------------------------
    # SMART RECOMMENDATIONS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Smart Recommendations</div>',
        unsafe_allow_html=True
    )

    if biggest != "None":

        st.markdown(
            '<div class="notice">'
            '💡 Your highest spending area is '
            '<b>{}</b>. Review this category before '
            'your next purchase.'
            '</div>'.format(
                biggest
            ),
            unsafe_allow_html=True
        )

    if velocity == "Rising":

        st.markdown(
            '<div class="notice">'
            '📈 Your spending velocity is rising. '
            'Try a 24-hour pause before non-essential purchases.'
            '</div>',
            unsafe_allow_html=True
        )

    elif velocity == "Improving":

        st.markdown(
            '<div class="notice">'
            '📉 Your recent spending is improving. '
            'Keep the same pattern.'
            '</div>',
            unsafe_allow_html=True
        )

    if st.session_state.jar < 1000:

        st.markdown(
            '<div class="notice">'
            '🎯 Try building your Savings Jar above Rs. 1,000.'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="notice">'
            '✨ Great! Your Savings Jar shows a consistent '
            'saving habit.'
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.subheader("Profile")

    st.markdown(
        '<div class="profile-box">'
        '<div class="avatar">👤</div>'
        '<div class="profile-name">{}</div>'
        '<div class="small-label">VELORA MEMBER</div>'
        '</div>'.format(
            st.session_state.name
        ),
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">Account Settings</div>',
        unsafe_allow_html=True
    )

    new_name = st.text_input(
        "Your Name",
        value=st.session_state.name,
        key="profile_name"
    )

    if st.button(
        "Save Profile",
        use_container_width=True
    ):

        if new_name.strip():

            st.session_state.name = (
                new_name.strip()
            )

            st.session_state.notifications.insert(
                0,
                "Profile updated successfully."
            )

            st.success(
                "Profile saved."
            )

            st.rerun()

    st.markdown(
        '<div class="section">Monthly Budget</div>',
        unsafe_allow_html=True
    )

    new_limit = st.number_input(
        "Monthly spending limit",
        min_value=100.0,
        value=float(
            st.session_state.monthly_limit
        ),
        step=100.0,
        key="profile_budget"
    )

    if st.button(
        "Update Budget",
        use_container_width=True
    ):

        st.session_state.monthly_limit = (
            float(new_limit)
        )

        st.success(
            "Monthly budget updated."
        )

        st.rerun()

    st.markdown(
        '<div class="section">AI Coach Mode</div>',
        unsafe_allow_html=True
    )

    coach_mode = st.selectbox(
        "Coaching style",
        [
            "Smart",
            "Strict",
            "Encouraging"
        ],
        index=[
            "Smart",
            "Strict",
            "Encouraging"
        ].index(
            st.session_state.coach_mode
        )
    )

    if coach_mode != st.session_state.coach_mode:

        st.session_state.coach_mode = coach_mode

        st.rerun()

    st.markdown(
        '<div class="section">Notifications</div>',
        unsafe_allow_html=True
    )

    if st.session_state.notifications:

        for notification in \
                st.session_state.notifications[:5]:

            st.markdown(
                '<div class="notice">'
                '🔔 {}'
                '</div>'.format(
                    notification
                ),
                unsafe_allow_html=True
            )

    else:

        st.caption(
            "No new notifications."
        )

    st.markdown(
        '<div class="section">Demo Controls</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "VELORA is a prototype. No real money, "
    

        "UPI or bank connection is used."
    )

    st.divider()

    if st.button(
        "🔄 Reset Demo",
        use_container_width=True
    ):
        reset_demo()
        st.rerun()


# =========================================================
# ADD MONEY / TRANSACTION
# =========================================================

elif st.session_state.page == "Add":

    st.markdown(
        '<div class="section">Add Transaction</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Record income or spending in your VELORA demo wallet."
    )

    transaction_type = st.selectbox(
        "Transaction type",
        ["Expense", "Income"]
    )

    name = st.text_input(
        "Transaction name",
        placeholder="e.g. Netflix, Pocket Money, Food"
    )

    category_options = [
        "Food",
        "Shopping",
        "Education",
        "Transportation",
        "Entertainment",
        "Bills",
        "Health",
        "Other"
    ]

    category = st.selectbox(
        "Category",
        category_options
    )

    amount = st.number_input(
        "Amount (Rs.)",
        min_value=1.0,
        step=50.0
    )

    if st.button(
        "＋ Add Transaction",
        use_container_width=True
    ):

        if not name.strip():

            st.warning(
                "Please enter a transaction name."
            )

        else:

            if transaction_type == "Expense":

                add_transaction(
                    name.strip(),
                    category,
                    -amount
                )

                st.session_state.balance -= amount

                st.success(
                    "Expense added successfully."
                )

            else:

                add_transaction(
                    name.strip(),
                    "Income",
                    amount
                )

                st.session_state.balance += amount

                st.success(
                    "Income added successfully."
                )

            st.rerun()

    st.write("")

    if st.button(
        "← Back Home",
        use_container_width=True
    ):
        go("Home")


# =========================================================
# PAY
# =========================================================

elif st.session_state.page == "Pay":

    st.markdown(
        '<div class="section">Send Money</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="notice">'
        '⚠️ Demo only — this does NOT send real money.'
        '</div>',
        unsafe_allow_html=True
    )

    receiver = st.text_input(
        "Send to",
        placeholder="Friend / Contact"
    )

    amount = st.number_input(
        "Amount (Rs.)",
        min_value=1.0,
        step=50.0
    )

    category = st.selectbox(
        "Purpose",
        [
            "Food",
            "Shopping",
            "Transportation",
            "Entertainment",
            "Other"
        ]
    )

    if st.button(
        "↗ Send Demo Payment",
        use_container_width=True
    ):

        if not receiver.strip():

            st.warning(
                "Enter a recipient name."
            )

        elif amount > st.session_state.balance:

            st.error(
                "Insufficient demo balance."
            )

        else:

            add_transaction(
                "To " + receiver.strip(),
                category,
                -amount
            )

            st.session_state.balance -= amount

            st.session_state.notifications.insert(
                0,
                "Rs. {:,.0f} demo payment recorded to {}."
                .format(
                    amount,
                    receiver.strip()
                )
            )

            st.success(
                "Demo payment recorded."
            )

            st.rerun()


# =========================================================
# ACTIVITY
# =========================================================

elif st.session_state.page == "Activity":

    st.markdown(
        '<div class="section">Recent Activity</div>',
        unsafe_allow_html=True
    )

    transactions = (
        st.session_state.transactions
    )

    if not transactions:

        st.caption(
            "No transactions yet."
        )

    else:

        for tx in transactions:

            name, category, amount = tx

            if amount >= 0:

                amount_text = (
                    "+ Rs. {:,.0f}"
                    .format(amount)
                )

                amount_class = "tx-income"

            else:

                amount_text = (
                    "- Rs. {:,.0f}"
                    .format(abs(amount))
                )

                amount_class = "tx-expense"

            st.markdown(
                '<div class="transaction">'
                '<div class="tx-title">{}</div>'
                '<div class="tx-cat">{}</div>'
                '<div class="{}">{}</div>'
                '</div>'.format(
                    name,
                    category,
                    amount_class,
                    amount_text
                ),
                unsafe_allow_html=True
            )


# =========================================================
# INSIGHT
# =========================================================

elif st.session_state.page == "Insight":

    st.markdown(
        '<div class="section">VELORA Intelligence</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # AI COACH
    # -----------------------------------------------------

    coach_title, coach_text = ai_coach()

    st.markdown(
        '<div class="ai-card">'
        '<div class="ai-badge">VELORA AI COACH
        '<div class="ai-title">{}</div>'
        '<div class="ai-text">{}</div>'
        '</div>'.format(
            coach_title,
            coach_text
        ),
        unsafe_allow_html=True
    )

    # =====================================================
    # AI SPENDING PREDICTOR
    # =====================================================

    predicted = predicted_monthly_spending()
    next_7_days = predicted_7_day_spending()
    velocity = spending_velocity()

    st.markdown(
        '<div class="prediction">'
        '<div class="prediction-title">'
        '🔮 AI Spending Forecast'
        '</div>'
        '<div class="prediction-number">'
        'Rs. {:,.0f}'
        '</div>'
        '<div class="prediction-small">'
        'Predicted monthly spending'
        '</div>'
        '<br>'
        '<div class="prediction-small">'
        '7-day forecast: Rs. {:,.0f}'
        ' · Trend: {}'
        '</div>'
        '</div>'.format(
            predicted,
            next_7_days,
            velocity
        ),
        unsafe_allow_html=True
    )

    # =====================================================
    # PREDICTION INSIGHT
    # =====================================================

    prediction_title, prediction_text = (
        prediction_message()
    )

    st.markdown(
        '<div class="insight">'
        '<div class="insight-label">'
        'PREDICTIVE INSIGHT'
        '</div>'
        '<div class="insight-title">'
        '{}'
        '</div>'
        '<div class="insight-text">'
        '{}'
        '</div>'
        '</div>'.format(
            prediction_title,
            prediction_text
        ),
        unsafe_allow_html=True
    )

    # =====================================================
    # SPENDING BREAKDOWN
    # =====================================================

    st.markdown(
        '<div class="section">'
        'Spending Breakdown'
        '</div>',
        unsafe_allow_html=True
    )

    categories = category_totals()

    if categories:

        chart_df = pd.DataFrame(
            list(categories.items()),
            columns=["Category", "Amount"]
        )

        chart_df = chart_df.sort_values(
            "Amount",
            ascending=False
        )

        st.bar_chart(
            chart_df.set_index("Category")
        )

        biggest, biggest_value = (
            biggest_category()
        )

        st.info(
            "Your highest spending category is "
            "{} at Rs. {:,.0f}."
            .format(
                biggest,
                biggest_value
            )
        )

    else:

        st.caption(
            "Add more transactions to unlock "
            "spending analysis."
        )

    # =====================================================
    # VELORA FINANCIAL SCORE
    # =====================================================

    st.markdown(
        '<div class="section">'
        'Financial Health'
        '</div>',
        unsafe_allow_html=True
    )

    score = financial_score()

    st.markdown(
        '<div class="score">'
        '<div class="score-number">{}</div>'
        '<div class="score-label">'
        'VELORA FINANCIAL SCORE'
        '</div>'
        '<div class="score-sub">'
        '{}'
        '</div>'
        '</div>'.format(
            score,
            score_label(score)
        ),
        unsafe_allow_html=True
    )

    breakdown = score_breakdown()

    for key in [
        "Budget Discipline",
        "Saving Habit",
        "Balance Safety",
        "Spending Trend"
    ]:

        st.markdown(
            '<div class="score-row">'
            '<div class="score-name">'
            '{}'
            '</div>'
            '<div class="score-value">'
            '{}'
            '</div>'
            '</div>'.format(
                key,
                breakdown[key]
            ),
            unsafe_allow_html=True
        )