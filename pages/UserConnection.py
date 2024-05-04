import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import sqlite3
from VariableCommune import connection
from Lib import *


st.set_page_config(page_title="Application de gestion des utilisateurs", page_icon=":smiley:")
st.markdown("# DataFrame Demo")
st.title('Application de gestion des utilisateurs')

# Fonction pour se connecter à la base de données
def get_db_connection():
    conn = sqlite3.connect(connection)
    conn.row_factory = sqlite3.Row
    return conn


# Fonction pour récupérer les utilisateurs
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM utilisateurs').fetchall()
    conn.close()
    return users

# Fonction pour ajouter un nouvel utilisateur
def add_user(name, age,password,role):
    conn = get_db_connection()
    conn.execute('INSERT INTO utilisateurs (name, age,password,role) VALUES (?, ?, ?, ?)', (name, age,password,role))
    conn.commit()
    conn.close()

    # Formulaire pour ajouter un utilisateur
    
with st.form("user_form"):
        name = st.text_input("Nom")
        age = st.number_input("Age", min_value=0, step=1)
        password = st.text_input("Mot de passe",type="password")
        role = st.radio(
            "Role",
            ("Admin", "User", "Guest")
        )
        submitted = st.form_submit_button("Ajouter")
        if submitted and name and age and role and password:
            add_user(name, age,password,role)
            st.success("Utilisateur ajouté avec succès!")
    # Affichage des utilisateurs
    
st.header("Liste des utilisateurs")
users = get_users()
for user in users:
        st.text(f"Nom: {user['name']}, Age: {user['age']}, Role: {user['role']}")
