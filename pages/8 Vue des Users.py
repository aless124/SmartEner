import streamlit as st
import sqlite3
from VariableCommune import connection

def check_role(username, connection=connection):
    connection = sqlite3.connect(connection)
    cursor = connection.cursor()
    cursor.execute("SELECT role FROM utilisateurs WHERE name = ?", (username,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def home_page():
    st.title("Bienvenue sur l'application")

def admin_page():
    st.title("Page Admin")
    st.write("Cette page est accessible uniquement aux administrateurs.")

st.title("Page d'authentification")

with st.form(key='user_form'):
    username = st.text_input("Nom d'utilisateur")
    submit_button = st.form_submit_button("Soumettre")

if submit_button:
    role = check_role(username)
    if role == "Admin":
        admin_page()
    elif role == "User":
        st.write("Vous n'avez pas les autorisations pour accéder à cette page.")
    elif role == "Guest":
        st.write("Vous devez vous connecter en tant qu'administrateur pour accéder à cette page.")
    else:
        st.write("Nom d'utilisateur incorrect. Veuillez réessayer.")
