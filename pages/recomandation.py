import streamlit as st


st.title("eLegal Hackathon")

st.sidebar.image("static/Logo_t.png", use_column_width=True)
st.sidebar.header("eLegal Hackathon - FIYOMA")
st.sidebar.subheader("Find Your Massaction!")
st.subheader("Dein nächster Schritt!")
st.text("Wir haben eine Empfehlung für dich, die dir bei deinem Anliegen helfen könnte.")
st.markdown("### Schritt 1: Überprüfe die Empfehlung")
st.markdown("### Schritt 2: Passe die Empfehlung auf deine Bedrürfnisse weiter an.")
st.markdown("### Schritt 3: Setze die Empfehlung um.")

st.text_area("Empfehlung", value="""Team
[Deine Adresse]
[PLZ, Stadt]
Email: team@fiyoma.de

[Name des Vermieters]
[Adresse des Vermieters]
[PLZ, Stadt]

[Datum]

Betreff: Anfrage zur Anpassung der Mietkosten aufgrund der Übernahme der Kabelanschlussgebühren

Sehr geehrte(r) [Name des Vermieters],

ich hoffe, dass dieses Schreiben Sie wohlbehalten erreicht. Ich wende mich heute an Sie, um eine Anpassung meiner Mietkosten zu besprechen, die durch eine kürzlich eingetretene Änderung in den Nebenkosten meiner Wohnung notwendig geworden ist.

Wie Ihnen bekannt ist, beziehe ich die Wohnung in [genaue Adresse der Wohnung] und habe bisher die Kosten für den Kabelanschluss als Teil der Nebenkosten von Ihnen, als meinem Vermieter, erstattet bekommen. Seit dem [Datum der Änderung], wie mir mitgeteilt wurde, bin ich jedoch selbst für die Bezahlung des Kabelanschlusses verantwortlich, was eine zusätzliche finanzielle Belastung für mich darstellt.

Da diese Kosten zuvor Teil der Mietnebenkosten waren, bitte ich um eine entsprechende Reduktion meiner Miete, um diese zusätzlichen Kosten auszugleichen. Ich glaube, dass eine faire Anpassung der Miete beiden Parteien gerecht werden würde und die Fortsetzung unseres guten Mietverhältnisses unterstützen würde.

Ich wäre Ihnen dankbar, wenn wir uns zu diesem Thema austauschen könnten, vielleicht könnten wir einen Termin für ein persönliches Gespräch vereinbaren oder die Angelegenheit telefonisch besprechen. Bitte lassen Sie mich wissen, wie Sie dazu stehen und wann es Ihnen passen würde.

Vielen Dank im Voraus für Ihre Aufmerksamkeit und Kooperation. Ich freue mich auf Ihre baldige Antwort.

Mit freundlichen Grüßen,

[Dein Name]""", height=800)

