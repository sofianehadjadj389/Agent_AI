import sys
import os
sys.path.append(os.path.dirname(__file__))


import streamlit as st
from interface import Interface


# Initialisation de l'interface avec l'agent
agent_interface = Interface()

st.set_page_config(page_title="AI Agent Interface", layout="centered")

st.title("🤖 AI Agent Interface")
st.write("Posez votre question à l'agent ci-dessous :")

user_input = st.text_input("Votre question", "")

if st.button("Envoyer") and user_input.strip():
    response = agent_interface.ask(user_input)
    st.markdown("### Réponse :")
    st.write(response)
