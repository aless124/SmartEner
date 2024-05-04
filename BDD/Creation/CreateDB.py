from Lib import *
from VariableCommune import *

def CreateDB():
    connexion = sqlite3.connect(connection)
    print("Base de données SQLite créée avec succès.")
