import streamlit as st
import pandas as pd

# =========================================================
# VELORA — PREMIUM INTELLIGENT MONEY MANAGEMENT
# Demo only — no real money / UPI / bank connection
# =========================================================

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -10%, #252944 0%, #0B0C11 35%, #08090D 100%);
    color: #F5F5F7;
}

.block-container {
    max-width: 600px;
    padding: 20px 16px 90px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1,h2,h3,h4,p,label {
    color:#F5F5F7 !important;
}

.stButton > button {
    background:#151821 !important;
    color:#FFFFFF !important;
    border:1px solid #303542 !important;
    border-radius:14px !important;
    min-height:44px !important;
    font-weight:700 !important;
}

.stButton > button:hover {
    border-color:#9B7BFF !important;
    background:#1D202B !important;
}

[data-testid="stMetric"] {
    background:#12151C;
    border:1px solid #292E38;
    border-radius:18px;
    padding:15px;
}

[data-testid="stMetricValue"] {
    color:#FFFFFF !important;
    font-weight:850 !important;
}

[data-testid="stMetricLabel"] {
    color:#858B98 !important;
}

.stProgress > div > div > div > div {
    background:#9B7BFF;
}

.stTextInput input,
.stNumberInput input {
    background:#11141A !important;
    color:#FFFFFF !important;
}

.stSelectbox div[data-baseweb="select"] {
    background:#11141A !important;
}

hr {
    border-color:#252A34 !important;
}

/* BRAND */

.brand {
    font-size:30px;
    font-weight:950;
    letter-spacing:5px;
}

.tagline {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
}

/* CARDS */

.card {
    background:linear-gradient(145deg,#1B1F2A,#101217);
    border:1px solid #303542;
    border-radius:25px;
    padding:22px;
    margin:14px 0;
}

.balance-label {
    color:#858B98;
    font-size:10px;
    letter-spacing:2px;
    font-weight:700;
}

.balance {
    color:#FFFFFF;
    font-size:44px;
    font-weight:900;
    letter-spacing:-2px;
    margin-top:5px;
}

.muted {
    color:#858B98 !important;
    font-size:11px;
}

.section {
    color:#F5F5F7;
    font-size:18px;
    font-weight:850;
    margin-top:25px;
    margin-bottom:9px;
}

/* INSIGHT */

.insight {
    background:linear-gradient(145deg,#1A1624,#101116);
    border:1px solid #493960;
    border-radius:22px;
    padding:20px;
    margin:14px 0;
}

.insight-label {
    color:#A98CFF;
    font-size:10px;
    font-weight:850;
    letter-spacing:2px;
}

.insight-title {
    color:#FFFFFF;
    font-size:18px;
    font-weight:850;
    margin-top:7px;
}

.insight-text {
    color:#999DA9;
    font-size:12px;
    line-height:1.55;
    margin-top:5px;
}

/* TRANSACTIONS */

.transaction {
    background:#11141A;
    border:1px solid #252A34;
    border-radius:16px;
    padding:14px;
    margin:7px 0;
}

.tx-title {
    color:#F4F5F7;
    font-weight:750;
    font-size:13px;
}

.tx-cat {
    color:#777D89;
    font-size:10px;
}

.tx-income {
    color:#6EE7A0;
    font-weight:800;
}

.tx-expense {
    color:#FF7D91;
    font-weight:800;
}

/* GOALS */

.goal {
    background:#11141A;
    border:1px solid #292E38;
    border-radius:20px;
    padding:18px;
    margin:10px 0;
}

.goal-title {
    font-weight:800;
    font-size:15px;
}

.goal-money {
    font-size:21px;
    font-weight:850;
}

/* CARD */

.virtual-card {
    background:
        radial-gradient(circle at 80% 10%,#5A4E82 0%,transparent 35%),
        linear-gradient(135deg,#292D3C,#101218);
    border:1px solid #505566;
    border-radius:26px;
    padding:25px;
    min-height:165px;
    margin:15px 0;
    box-shadow:0 15px 45px rgba(0,0,0,.35);
}

.card-brand {
    font-weight:900;
    letter-spacing:4px;
}

.card-number {
    font-size:19px;
    letter-spacing:3px;
    margin-top:30px;
}

.card-small {
    color:#858B98;
    font-size:9px;
    letter-spacing:1px;
    margin-top:15px;
}

/* SCORE */

.score {
    background:linear-gradient(145deg,#211A31,#111219);
    border:1px solid #46365B;
    border-radius:22px;
    padding:20px;
    text-align:center;
}

.score-number {
    font-size:42px;
    font-weight:950;
}

.score-label {
    color:#9A9DA8;
    font-size:10px;
    letter-spacing:2px;
}

/* JAR */

.jar {
    background:linear-gradient(145deg,#171923,#101116);
    border:1px solid #303542;
    border-radius:22px;
    padding:20px;
    margin:12px 0;
}

.jar-title {
    font-size:17px;
    font-weight:850;
}

.jar-money {
    font-size:27px;
    font-weight:900;
    margin:5px 0;
}

/* NOTICE */

.notice {
    background:#151821;
    border:1px solid #303542;
    border-radius:15px;
    padding:13px;
    margin:8px 0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {

    "balance": 5000.0,

    "monthly_limit": 2000.0,

    "name": "Tejal",

    "page": "Home",

    "card_frozen": False,

    "show_add": False,

    "show_request": False,

    "show_jar": False,

    "show_goal_form": False,

    "active_goal": None,

    "notifications": [],

    "goals": [
        {
            "name": "New Headphones",
            "target": 5000.0,
            "saved": 3400.0
        }
    ],

    "jar": 850.0,

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


def category_total(category):

    return sum(

        abs(x[2])

        for x in st.session_state.transactions

        if x[1] == category and x[2] < 0

    )


def biggest_category():

    data = {}

    for x in st.session_state.transactions:

        if x[2] < 0:

            data[x[1]] = (
                data.get(x[1], 0)
                + abs(x[2])
            )

    if not data:

        return "None", 0

    category = max(
        data,
        key=data.get
    )

    return category, data[category]


def get_score():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit


    if ratio <= 0.50:

        score = 94

    elif ratio <= 0.70:

        score = 88

    elif ratio <= 0.85:

        score = 80

    elif ratio <= 1:

        score = 70

    else:

        score = 58


    if st.session_state.jar >= 1000:

        score += 3


    return min(score, 100)


# =========================================================
# AI FINANCIAL COACH
# =========================================================

def get_financial_insight():

    spent = spending_total()

    limit = max(
        st.session_state.monthly_limit,
        1
    )

    ratio = spent / limit

    biggest, biggest_value = biggest_category()


    if ratio >= 1:

        return (
            "Budget Alert",

            "You've crossed your monthly spending limit. "
            "Try prioritising essential expenses for the rest of the month."
        )


    if ratio >= 0.80:

        return (
            "Watch Your Spending",

            "You're getting close to your monthly limit. "
            "Your biggest category is {} at ₹{:,.0f}."
            .format(
                biggest,
                biggest_value
            )
        )


    if st.session_state.jar >= 1000:

        return (
            "Great Saving Behaviour",

            "You're building a healthy savings habit. "
            "Your Savings Jar currently holds ₹{:,.0f}."
            .format(
                st.session_state.jar
            )
        )


    if biggest != "None":

        return (
            "Spending Pattern Detected",

            "{} is currently your biggest spending category "
            "at ₹{:,.0f}. Keep an eye on it."
            .format(
                biggest,
                biggest_value
            )
        )


    return (
        "You're Doing Well",

        "VELORA is monitoring your spending and savings behaviour."
    )


# =========================================================
# RESET
# =========================================================

def reset_demo():

    st.session_state.balance = 5000.0

    st.session_state.monthly_limit = 2000.0

    st.session_state.name = "Tejal"

    st.session_state.card_frozen = False

    st.session_state.jar = 850.0

    st.session_state.notifications = []

    st.session_state.show_add = False

    st.session_state.show_request = False

    st.session_state.show_jar = False

    st.session_state.show_goal_form = False

    st.session_state.active_goal = None


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


# =========================================================
# HEADER
# =========================================================

st.markdown(

    '<div class="brand">VELORA</div>'

    '<div class="tagline">'
    'INTELLIGENT MONEY MANAGEMENT'
    '</div>',

    unsafe_allow_html=True
)

st.write("")


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4, n5 = st.columns(5)


with n1:

    if st.button(
        "HOME",
        use_container_width=True
    ):

        go("Home")


with n2:

    if st.button(
        "PAY",
        use_container_width=True
    ):

        go("Pay")


with n3:

    if st.button(
        "ACTIVITY",
        use_container_width=True
    ):

        go("Activity")


with n4:

    if st.button(
        "INSIGHT",
        use_container_width=True
    ):

        go("Insight")


with n5:

    if st.button(
        "PROFILE",
        use_container_width=True
    ):

        go("Profile")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.caption("GOOD EVENING")

    st.subheader(
        st.session_state.name + " 👋"
    )


    # BALANCE

    st.markdown(

        '<div class="card">'

        '<div class="balance-label">'
        'AVAILABLE BALANCE'
        '</div>'

        '<div class="balance">'
        '₹{:,.0f}'
        '</div>'

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

        if st.button(
            "＋ ADD",
            use_container_width=True
        ):

            st.session_state.show_add = True


    with b:

        if st.button(
            "↗ SEND",
            use_container_width=True
        ):

            go("Pay")


    with c:

        if st.button(
            "⇄ REQUEST",
            use_container_width=True
        ):

            st.session_state.show_request = True


    # ADD MONEY

    if st.session_state.show_add:

        st.markdown("### Add money")


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


        x1, x2 = st.columns(2)


        with x1:

            if st.button(

                "Confirm",

                use_container_width=True,

                key="add_confirm"

            ):

                st.session_state.balance += amount


                add_transaction(

                    source.strip()
                    or "Income",

                    "Income",

                    amount

                )


                st.session_state.notifications.insert(

                    0,

                    "₹{:,.0f} added successfully."
                    .format(amount)

                )


                st.session_state.show_add = False

                st.rerun()


        with x2:

            if st.button(

                "Cancel",

                use_container_width=True,

                key="add_cancel"

            ):

                st.session_state.show_add = False

                st.rerun()


    # REQUEST

    if st.session_state.show_request:

        st.markdown("### Request money")


        person = st.text_input(

            "From",

            placeholder="Friend's name",

            key="request_person"

        )


        amount = st.number_input(

            "Amount",

            min_value=1.0,

            value=200.0,

            step=50.0,

            key="request_amount"

        )


        x1, x2 = st.columns(2)


        with x1:

            if st.button(

                "Create request",

                use_container_width=True,

                key="request_confirm"

            ):

                if not person.strip():

                    st.error("Enter a name.")

                else:

                    st.session_state.notifications.insert(

                        0,

                        "Request of ₹{:,.0f} created."
                        .format(amount)

                    )

                    st.session_state.show_request = False

                    st.rerun()


        with x2:

            if st.button(

                "Cancel",

                use_container_width=True,

                key="request_cancel"

            ):

                st.session_state.show_request = False

                st.rerun()


    # FINANCIAL SNAPSHOT

    st.markdown(

        '<div class="section">'
        'Financial snapshot'
        '</div>',

        unsafe_allow_html=True
    )


    spent = spending_total()


    remaining = max(

        st.session_state.monthly_limit
        - spent,

        0

    )


    ratio = (

        spent
        / max(
            st.session_state.monthly_limit,
            1
        )

    )


    c1, c2 = st.columns(2)


    with c1:

        st.metric(

            "Spent this month",

            "₹{:,.0f}".format(spent)

        )


    with c2:

        st.metric(

            "Budget remaining",

            "₹{:,.0f}".format(remaining)

        )


    c3, c4 = st.columns(2)


    with c3:

        st.metric(

            "Savings Jar",

            "₹{:,.0f}".format(
                st.session_state.jar
            )

        )


    with c4:

        st.metric(

            "VELORA Score",

            "{}/100".format(
                get_score()
            )

        )


    # SMART ALERT

    if ratio < 0.60:

        st.success(

            "You're on track. Your spending is comfortably below your limit."

        )

    elif ratio < 0.85:

        st.warning(

            "You're approaching your monthly limit. Keep an eye on discretionary spending."

        )

    else:

        st.error(

            "Budget risk detected. Your spending is close to your monthly limit."

        )


    # INTELLIGENCE

    biggest, biggest_value = biggest_category()


    if biggest != "None":

        st.markdown(

            '<div class="insight">'

            '<div class="insight-label">'
            'VELORA INTELLIGENCE'
            '</div>'

            '<div class="insight-title">'
            '{} is your biggest category'
            '</div>'

            '<div class="insight-text">'
            '₹{:,.0f} has been spent here. '
            'VELORA is monitoring your spending behavior.'
            '</div>'

            '</div>'.format(

                biggest,

                biggest_value

            ),

            unsafe_allow_html=True

        )


    # AI COACH

    insight_title, insight_text = (
        get_financial_insight()
    )


    st.markdown(

        '<div class="insight">'

        '<div class="insight-label">'
        'VELORA AI COACH'
        '</div>'

        '<div class="insight-title">'
        '{}'
        '</div>'

        '<div class="insight-text">'
        '{}'
        '</div>'

        '</div>'.format(

            insight_title,

            insight_text

        ),

        unsafe_allow_html=True

    )


    # SPENDING TREND

    st.markdown(

        '<div class="section">'
        'Spending trend'
        '</div>',

        unsafe_allow_html=True

    )


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


    # SAVINGS JAR

    st.markdown(

        '<div class="section">'
        'Savings Jar'
        '</div>',

        unsafe_allow_html=True

    )


    st.markdown(

        '<div class="jar">'

        '<div class="jar-title">'
        'Future Fund'
        '</div>'

        '<div class="jar-money">'
        '₹{:,.0f}'
        '</div>'

        '<div class="muted">'
        'Money you intentionally set aside'
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

        st.session_state.show_jar = True


    if st.session_state.show_jar:

        jar_action = st.selectbox(

            "Action",

            [

                "Add to Jar",

                "Withdraw from Jar"

            ],

            key="jar_action"

        )


        jar_amount = st.number_input(

            "Amount",

            min_value=1.0,

            value=100.0,

            step=50.0,

            key="jar_amount"

        )


        if st.button(

            "Confirm Jar Action",

            use_container_width=True,

            key="confirm_jar"

        ):


            if jar_action == "Add to Jar":


                if jar_amount > st.session_state.balance:

                    st.error(
                        "Insufficient demo balance."
                    )


                else:

                    st.session_state.balance -= jar_amount

                    st.session_state.jar += jar_amount


                    add_transaction(

                        "Savings Jar",

                        "Savings",

                        -jar_amount

                    )


                    st.session_state.notifications.insert(

       