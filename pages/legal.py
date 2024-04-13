import streamlit as st

def start_chat_interface():
    st.sidebar.image("static/Logo_t.png", use_column_width=True)
    st.header(f"Welcome, {st.session_state.name}!")
