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
    connexion.close()