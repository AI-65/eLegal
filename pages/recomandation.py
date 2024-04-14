import streamlit as st


st.title("eLegal Hackathon")

st.sidebar.image("static/Logo_t.png", use_column_width=True)
st.sidebar.Header("eLegal Hackathon - FIYOMA")
st.sidebar.subheader("Find Your Massaction!")
st.subheader("Dein nächster Schritt!")
st.text("Wir haben eine Empfehlung für dich, die dir bei deinem Anliegen helfen könnte.")
st.markdown("### Schritt 1: Überprüfe die Empfehlung")
st.markdown("### Schritt 2: Passe die Empfehlung auf deine Bedrürfnisse weiter an.")
st.markdown("### Schritt 3: Setze die Empfehlung um.")

st.text_area("Empfehlung", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit")

