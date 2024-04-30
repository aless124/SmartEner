import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import sqlite3
from VariableCommune import connection
from Lib import *


# Fonction pour se connecter à la base de données
def get_db_connection():
    conn = sqlite3.connect(connection)
    conn.row_factory = sqlite3.Row
    return conn

