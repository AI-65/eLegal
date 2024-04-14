import streamlit as st
from ui import footer
import datetime


def start_chat_interface():
    st.sidebar.image("static/Logo_t.png", use_column_width=True)
    st.sidebar.Header("eLegal Hackathon - FIYOMA")
    st.sidebar.subheader("Find Your Massaction!")
    st.header(f"Welcome, {st.session_state.name}!")

    # Chat Simulation Section
    st.subheader("Chat with our Legal Bot")

    # Create containers for the chat history and the input area
    chat_container = st.container()
    input_container = st.empty()

    # Continuously update the chat history
    display_chat_history(chat_container)

    # Chat input section
    with input_container.container():
        with st.form("chat_form"):
            user_input = st.text_input("Type your legal question here:", key="user_query")
            send_button = st.form_submit_button("Send")

        if send_button and user_input:
            handle_chat(user_input, chat_container)


def handle_chat(user_input, chat_container):
    # Assume the chatbot instance exists in the session state and use it directly
    chatbot = st.session_state.chatbot

    # Mimic a sending message delay
    with st.spinner("Sending..."):
        response = chatbot.chat(user_input, st.session_state.session_id)

    # Update the chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.session_state.chat_history.append({"sender": "You", "message": user_input, "timestamp": datetime.datetime.now()})
    st.session_state.chat_history.append(
        {"sender": "Chatbot", "message": response, "timestamp": datetime.datetime.now()})

    #st.session_state.chat_history.append( {"You":user_input})
    #st.session_state.chat_history.append( {"Chatbot":response})

    # Redisplay the updated chat history
    display_chat_history(chat_container)
    footer.display_footer()


def display_chat_history(chat_container):
    with chat_container:
        st.write("Conversation:")
        for entry in st.session_state.chat_history:
            if entry["sender"] == "You":
                st.markdown(f"**You ({entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}):** {entry['message']}")
            else:
                st.markdown(f"**Chatbot ({entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}):** {entry['message']}")
