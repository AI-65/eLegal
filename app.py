import uuid
import streamlit as st
from agent import LangChatBot  # Ensure this is the correct import based on your project structure
import dotenv
from agent import create_elastic_search
import yaml
from yaml.loader import SafeLoader
import ui.footer as footer

st.set_page_config(page_title="eLegal Hackathon", page_icon=None, layout="wide", initial_sidebar_state="auto",
                   menu_items=None)
dotenv.load_dotenv()
st.session_state.vector_search = create_elastic_search()

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


def main():
    st.title("eLegal Hackathon")

    st.sidebar.image("static/Logo_t.png", use_column_width=True)
    st.sidebar.header("eLegal Hackathon - FIYOMA")
    st.sidebar.subheader("Find Your Massaction!")
    if 'session_id' not in st.session_state:
        with st.form("user_input_form"):
            name = st.text_input("Enter your name:")
            email = st.text_input("Enter your email:")
            plz = st.number_input("Enter your postal code:", min_value=10000, max_value=99999, step=1)
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
            st.session_state.plz = plz
            st.session_state.documents = documents
            st.session_state.description = description
            st.session_state.chat_history = []
            st.session_state.initial_user_info = {
                "name": name,
                "email": email,
                "description": description
            }
            footer.display_footer()
            # Instantiate the chatbot with initial user info
            st.session_state.chatbot = LangChatBot(st.session_state.initial_user_info)

            st.switch_page("pages/chat.py")



    else:
        st.switch_page("pages/chat.py")


if __name__ == "__main__":
    main()
