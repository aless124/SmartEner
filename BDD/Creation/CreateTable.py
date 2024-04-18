from Lib import *
from VariableCommune import *

def CreateTable():
    connexion = sqlite3.connect(connection)
    curseur = connexion.cursor()

    curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY,
                        nom TEXT NOT NULL,
                        age INTEGER
                        )''')

    connexion.commit()
    connexion.close()