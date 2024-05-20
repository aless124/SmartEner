from Lib import *
from VariableCommune import *

def CreateTable():
    connexion = sqlite3.connect(connection)
    curseur = connexion.cursor()

    curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        name TEXT Primary Key NOT NULL,
                        age INTEGER,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                        )''')
    connexion.commit()
    if not utilisateur_existe(curseur):
        curseur.execute('''INSERT INTO utilisateurs (name, age, password, role) VALUES ('admin', 0, 'admin', 'Admin')''')
        connexion.commit()
    connexion.close()

def utilisateur_existe(curseur):
    curseur.execute("SELECT name FROM utilisateurs WHERE name = 'admin'")
    return curseur.fetchone() is not None