import streamlit as st
from death_prediction import death_prediction
from aneamia_prediction import anaemia_prediction
from high_blood_pressure_prediction import hbp
from Description import Description_function



# Custom CSS styles
custom_css = """
    body {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
        margin: 0;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    h1 {
        color: #3498db;
    }
    h2 {
        color: #2ecc71;
    }
    .section {
        margin-top: 20px;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
    }
    .submit-button {
        background-color: #3498db;
        color: #ffffff;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        cursor: pointer;
    }
    .submit-button:hover {
        background-color: #2980b9;
    }
"""

st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

st.title("Health Prediction App")

# Sidebar with slider for app selection
selected_app = st.sidebar.selectbox("Select an App", ["Description", "Death Prediction", "Anaemia Prediction", "High Blood Pressure Prediction"])

# Mapping function names to avoid repetitive if-else
app_functions = {
    "Description": Description_function,
    "Death Prediction": death_prediction,
    "Anaemia Prediction": anaemia_prediction,
    "High Blood Pressure Prediction": hbp,
}

# Call the appropriate function based on the selected app
if selected_app in app_functions:
    app_functions[selected_app]()
else:
    st.warning("Invalid app selection. Please choose a valid app.")
