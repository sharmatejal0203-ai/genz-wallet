import streamlit as st

st.set_page_config(
    page_title="VELORA",
    page_icon="V",
    layout="centered"
)

st.title("VELORA")
st.caption("Intelligent Money Management")

st.divider()

st.subheader("Welcome, Tejal 👋")

st.metric(
    "Available Balance",
    "₹5,000"
)

st.success("VELORA is running successfully.")

st.info(
    "Demo only — no real money, UPI or bank connection."
)