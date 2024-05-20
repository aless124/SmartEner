import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import sqlite3
from VariableCommune import connection
from Lib import *


st.set_page_config(page_title="Application de gestion des utilisateurs", page_icon=":smiley:")
st.markdown("# DataFrame Demo")

def get_db_connection():
    conn = sqlite3.connect(connection)
    conn.row_factory = sqlite3.Row
    return conn

def check_role(username, password,connection=connection):
    connection = sqlite3.connect(connection)
    cursor = connection.cursor()
    print('SELECT role FROM utilisateurs WHERE name = ' + f'"{username}"')
    cursor.execute('SELECT role FROM utilisateurs WHERE name = ' + f'"{username}"') 
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM utilisateurs').fetchall()
    conn.close()
    return users

def add_user(name, age,password,role):
    conn = get_db_connection()
    conn.execute('INSERT INTO utilisateurs (name, age,password,role) VALUES (?, ?, ?, ?)', (name, age,password,role))
    conn.commit()
    conn.close()

st.title("Page de création d'utilisateur")

if 'role' not in st.session_state:
    st.session_state['role'] = None


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
            print(name, age, role)

    users = get_users()
    df = pd.DataFrame(users)
    st.write(df)


with st.form(key='user_form'):
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    submit_button = st.form_submit_button("Soumettre")

if submit_button:
    st.session_state['role'] = check_role(username, password)

if st.session_state['role'] == "Admin":
    admin_page()
elif st.session_state['role'] == "User":
    st.write("Vous n'avez pas les autorisations pour accéder à cette page.")
elif st.session_state['role'] == "Guest":
    st.write("Vous devez vous connecter en tant qu'administrateur pour accéder à cette page.")
elif st.session_state['role'] is None and submit_button:
    st.write("Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer.")