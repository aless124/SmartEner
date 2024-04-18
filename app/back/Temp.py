from VariableCommune import connection
from Lib import *


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
def add_user(name, age):
    conn = get_db_connection()
    conn.execute('INSERT INTO utilisateurs (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    
def run_app():
    # Titre de l'application
    st.title('Application de gestion des utilisateurs')

    # Formulaire pour ajouter un utilisateur
    with st.form("user_form"):
        name = st.text_input("Nom")
        age = st.number_input("Age", min_value=0, step=1)
        submitted = st.form_submit_button("Ajouter")
        if submitted and name and age:
            add_user(name, age)
            st.success("Utilisateur ajouté avec succès!")

    # Affichage des utilisateurs
    st.header("Liste des utilisateurs")
    users = get_users()
    for user in users:
        st.text(f"ID: {user['id']}, Nom: {user['name']}, Age: {user['age']}")
