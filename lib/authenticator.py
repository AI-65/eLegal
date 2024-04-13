import streamlit as st
import streamlit_authenticator as stauth


def authenticator(config):
    authenticator_cred = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    return authenticator_cred

