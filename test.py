import streamlit as st

st.set_page_config(
    page_title="Test",
    layout="centered"
)

st.sidebar.title("Meny")

valg = st.sidebar.radio(
    "Side",
    ["Dashboard", "Favoritter"]
)

st.title("Test")

st.write(f"Du valgte: {valg}")