import uuid
import streamlit as st
from agent import LangChatBot  # Ensure this is the correct import based on your project structure
import dotenv

import datetime

import ui.footer as footer


dotenv.load_dotenv()

def main():
    st.title("eLegal Hackathon")

    if 'session_id' not in st.session_state:
        with st.form("user_input_form"):
            name = st.text_input("Enter your name:")
            email = st.text_input("Enter your email:")
            documents = st.file_uploader("Upload relevant documents", accept_multiple_files=True)
            description = st.text_area("Brief description of your legal issue:")
            submit_button = st.form_submit_button("Start Chat")
            footer.display_footer()

        if submit_button:
            # Ensure all data is collected before proceeding
            if not all([name, email, description]):
                st.error("Please fill in all fields.")
                return

            # Initialize session state variables
            st.session_state.session_id = str(uuid.uuid4())
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.documents = documents
            st.session_state.description = description
            st.session_state.chat_history = []
            st.session_state.initial_user_info = {
                "name": name,
                "email": email,
                "description": description
            }
            # Instantiate the chatbot with initial user info
            st.session_state.chatbot = LangChatBot(st.session_state.initial_user_info)
            start_chat_interface()
            footer.display_footer()


    else:
        start_chat_interface()


def start_chat_interface():
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
    st.session_state.chat_history.append({"sender": "Chatbot", "message": response, "timestamp": datetime.datetime.now()})


    st.session_state.chat_history.append(f"You: {user_input}")
    st.session_state.chat_history.append(f"Chatbot: {response}")
    
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

if __name__ == "__main__":
    main()
