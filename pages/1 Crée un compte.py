import streamlit as st
import sqlite3
from VariableCommune import connection
from Lib import *


st.set_page_config(page_title="Application de Création d'utilisateurs", page_icon=":smiley")

st.title("Page de création d'utilisateur")

with st.form(key='user_form'):
    username = st.text_input("Nom d'utilisateur")
    age = st.number_input("Age", min_value=0, step=1)
    password = st.text_input("Mot de passe", type="password")
    role = "User"
    submit_button = st.form_submit_button("Soumettre")

    if submit_button and username and age and password:
        connexion = sqlite3.connect(connection)
        curseur = connexion.cursor()
        curseur.execute("INSERT INTO utilisateurs (name, age, password, role) VALUES (?, ?, ?, ?)", (username, age, password, role))
        connexion.commit()
        connexion.close()
        st.success("Utilisateur ajouté avec succès!")