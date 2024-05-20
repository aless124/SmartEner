import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import sqlite3
from VariableCommune import connection
from Lib import *

import streamlit as st
import pandas as pd
import sqlite3
from VariableCommune import connection  

st.set_page_config(page_title="Application de gestion des utilisateurs", page_icon=":smiley:")
st.markdown("# Application de Gestion des Utilisateurs")

def get_db_connection():
    conn = sqlite3.connect(connection)
    conn.row_factory = sqlite3.Row
    return conn

def update_user_data(new_name, new_age, new_password, new_role,name):
    conn = get_db_connection()
    conn.execute('UPDATE utilisateurs SET name=?, age=?, password=?, role=? WHERE name=?', (new_name, new_age, new_password, new_role,name))
    conn.commit()
    conn.close()

def delete_user(name):
    conn = get_db_connection()
    conn.execute('DELETE FROM utilisateurs WHERE name=?', (name,))
    conn.commit()
    conn.close()


def check_role(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM utilisateurs WHERE name = ? AND password = ?', (username, password))  
    result = cursor.fetchone()
    conn.close()
    return result['role'] if result else None
    
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT name, age, role FROM utilisateurs').fetchall()
    conn.close()
    return users

def add_user(name, age, password, role):
    conn = get_db_connection()
    conn.execute('INSERT INTO utilisateurs (name, age, password, role) VALUES (?, ?, ?, ?)', (name, age, password, role))
    conn.commit()
    conn.close()

def admin_page():
    with st.form("user_form2"):
        name = st.text_input("Nom")
        age = st.number_input("Age", min_value=0, step=1)
        password = st.text_input("Mot de passe", type="password")
        role = st.radio("Role", ("Admin", "User", "Guest"))
        submitted = st.form_submit_button("Ajouter")
        if submitted and name and role and password:
            add_user(name, age, password, role)
            st.success("Utilisateur ajouté avec succès!")

    users = get_users()
    df = pd.DataFrame(users, columns=['Name', 'Age', 'Role'])
    if not df.empty:
        st.write(df)
    else:
        st.write("Aucun utilisateur trouvé.")
    with st.form("user_form3"):
        st.write("## Mettre à jour les informations de l'utilisateur")
        user_name = st.selectbox("Nom de l'utilisateur", df['Name'])
        new_name = st.text_input("Nouveau nom", user_name)
        new_age = st.number_input("Nouvel âge", min_value=0, step=1)
        new_password = st.text_input("Nouveau mot de passe", type="password")
        new_role = st.radio("Nouveau rôle", ("Admin", "User", "Guest"))
        update_button = st.form_submit_button("Mettre à jour")
        if update_button:
            update_user_data(new_name, new_age, new_password, new_role,df['Name'])
            st.success("Informations de l'utilisateur mises à jour avec succès!")

    with st.form("user_form4"):
        st.write("## Supprimer un utilisateur")
        user_name = st.selectbox("Nom de l'utilisateur", df['Name'])
        print(user_name)
        delete_button = st.form_submit_button("Supprimer")
        if delete_button:
            delete_user(user_name)
            st.success("Utilisateur supprimé avec succès!")

with st.form(key='user_form'):
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    submit_button = st.form_submit_button("Soumettre")

if submit_button:
    role = check_role(username, password)
    if role:
        st.session_state['role'] = role
    else:
        st.session_state['role'] = None
        st.error("Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer.")

if 'role' in st.session_state:
    if st.session_state['role'] == "Admin":
        admin_page()
    elif st.session_state['role'] == "User":
        st.write("Vous n'avez pas les autorisations pour accéder à cette page.")
    elif st.session_state['role'] == "Guest":
        st.write("Vous devez vous connecter en tant qu'administrateur pour accéder à cette page.")
