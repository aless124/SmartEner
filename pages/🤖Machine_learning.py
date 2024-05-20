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

# Function to load the saved model
def load_model():
    # Load the model from disk
    filename = 'Modele/joblib_model.sav'
    model = joblib.load(filename)
    return model

# Function to plot predictions
def plot_predictions(year, predictions):
    months = np.arange(1, 13)  # Months from January to December
    plt.figure(figsize=(10, 5))
    plt.plot(months, predictions, marker='o', linestyle='-', color='b')
    plt.title(f'Predicted Nuclear Power Production for {year}')
    plt.xlabel('Month')
    plt.ylabel('Production (TWh)')
    plt.grid(True)
    plt.xticks(months)  # Ensure all months are marked
    plt.ylim(min(predictions) - 0.5, max(predictions) + 0.5)  # Adjust y limits for better visual
    st.pyplot(plt)

st.title("Nuclear Power Production Prediction")

    # Load the model
model = load_model()

    # Sidebar for user input
st.sidebar.title("Input Features for Prediction")
year = st.sidebar.slider('Year', 2000, 2035, 2023)  # Adjust the range as needed
month = st.sidebar.slider('Month', 1, 12, 1)

    # Predicting across all months of the selected year
if st.sidebar.button("Predict for All Months"):
        # Generating inputs for all months in the selected year
    input_features = pd.DataFrame([[year, month] for month in range(1, 13)], columns=['Year', 'Month'])
        
        # Making predictions
    predictions = model.predict(input_features)
        
        # Displaying the plot
    plot_predictions(year, predictions)

    # Load the model
model = load_model()


    # Button to make prediction
if st.sidebar.button("Predict at the specified month"):
        # Preparing the input features as a DataFrame
    input_features = pd.DataFrame([[year, month]], columns=['Year', 'Month'])
        
        # Making prediction
    production_prediction = model.predict(input_features)[0]
        
        # Displaying the prediction
    st.write(f"Predicted Production (TWh): {production_prediction:.2f}")