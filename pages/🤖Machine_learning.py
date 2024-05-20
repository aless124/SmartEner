from Lib import *
import streamlit as st
import joblib
from sklearn.model_selection import train_test_split
import streamlit as st
import joblib
import pandas as pd

import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Chargement du modèle
def load_model():
    filename = 'Modele/joblib_model.sav'
    model = joblib.load(filename)
    return model

def plot_predictions(year, predictions):
    months = np.arange(1, 13)  # Les mois de janvier à décembre
    plt.figure(figsize=(10, 5))
    plt.plot(months, predictions, marker='o', linestyle='-', color='b')
    plt.title(f'Predicted Nuclear Power Production for {year}')
    plt.xlabel('Month')
    plt.ylabel('Production (TWh)')
    plt.grid(True)
    plt.xticks(months) 
    plt.ylim(min(predictions) - 0.5, max(predictions) + 0.5) 
    st.pyplot(plt)

st.title("Nuclear Power Production Prediction")

model = load_model()

st.sidebar.title("Input Features for Prediction")
year = st.sidebar.slider('Year', 2000, 2035, 2023)  
month = st.sidebar.slider('Month', 1, 12, 1)


if st.sidebar.button("Predict for All Months"):
    input_features = pd.DataFrame([[year, month] for month in range(1, 13)], columns=['Year', 'Month'])
        
    predictions = model.predict(input_features)
        
    plot_predictions(year, predictions)

model = load_model()


if st.sidebar.button("Predict at the specified month"):
    input_features = pd.DataFrame([[year, month]], columns=['Year', 'Month'])
    production_prediction = model.predict(input_features)[0]
    st.write(f"Predicted Production (TWh): {production_prediction:.2f}")