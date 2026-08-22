import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #090A0F;
}

.block-container {
    max-width: 560px;
    padding: 30px 18px;
}

h1, h2, h3, p {
    color: white !important;
}

.stButton > button {
    width: 100%;
    background: #151820;
    color: white;
    border: 1px solid #303542;
    border-radius: 14px;
    min-height: 45px;
}
</style>
""", unsafe_allow_html=True)

st.title("VELORA")
st.caption("Intelligent money management")

st.divider()

st.subheader("Welcome back, Tejal 👋")

st.metric(
    "Available Balance",
    "₹5,000"
)

st.write("### Quick actions")

a, b, c = st.columns(3)

with a:
    st.button("＋ ADD")

with b:
    st.button("↗ SEND")

with c:
    st.button("⇄ REQUEST")

st.divider()

st.subheader("Financial snapshot")

x, y = st.columns(2)

with x:
    st.metric("Spent", "₹1,280")

with y:
    st.metric("Budget left", "₹720")

st.subheader("VELORA Score")

st.metric(
    "Financial health",
    "84 / 100"
)

st.progress(0.84)

st.info(
    "VELORA is running in Demo Mode. "
    "No real money or bank connection."
)

st.divider()

st.caption(
    "VELORA · Intelligent money management · Demo Mode"
)