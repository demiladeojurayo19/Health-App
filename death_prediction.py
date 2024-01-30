import streamlit as st
import pandas as pd
import pickle

# Load the model back from the file
with open('death_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


def death_prediction():
    st.title('Death Event Prediction')

    with st.container():
        age = st.slider('Age', 0, 95, 1)
        anemia = st.radio("Do you have anaemia?", ('Yes', 'No'))
        anemia_value = 1 if anemia == 'Yes' else 0
        creatine = st.slider('Creatine Phosphokinase', 0, 8000, 1)

    with st.container():
        diabetes = st.radio("Do you have diabetes?", ('Yes', 'No'))
        diabetes_value = 1 if diabetes == 'Yes' else 0
        ejection_fraction = st.slider('Ejection fraction', 1, 100, 1)
        high_blood_pressure = st.radio("Do you have high blood pressure?", ('Yes', 'No'))
        high_blood_pressure_value = 1 if high_blood_pressure == 'Yes' else 0

    with st.container():
        platelet_range = st.slider('Select Platelet Count', 25100, 850000, 100)
        serum_creatinine = st.slider('Select Serum Creatine Count', 0, 100, 1)
        serum_sodium = st.slider('Select Serum Sodium Count', 0, 200, 1)
        gender = st.radio("What is your gender", ('Male', 'Female'))
        gender_value = 1 if gender == 'Male' else 0
        smoking = st.radio("Smoking Status", ('Yes', 'No'))
        smoking_value = 1 if smoking == 'Yes' else 0
        time = st.slider('Select time', 0, 300, 1)

    # Submit Button
    submit_button = st.button('Submit', key='submit_button')

    if submit_button:
        # Perform actions or calculations with the form data after submission
        st.success("Form submitted! Perform actions with the data.")

    data_collected = {'age': [age], 'anaemia': [anemia_value], 'creatinine_phosphokinase': [creatine],
                      'diabetes': [diabetes_value], 'ejection_fraction': [ejection_fraction],
                      'high_blood_pressure': [high_blood_pressure_value], 'platelets': [platelet_range],
                      'serum_creatinine': [serum_creatinine], 'serum_sodium': [serum_sodium],
                      'gender': [gender_value], 'smoking': [smoking_value], 'time': [time]}

    df = pd.DataFrame(data_collected)
    st.write(df.head())
    # Make predictions using the loaded model
    prediction = loaded_model.predict(df)[0]

    # Display the prediction
    st.write(f"Predicted class: {prediction}")
    if prediction == 1:
        output = 'It resulted in death'
    else:
        output = 'It did not result in death'

    st.write(f"Interpretation is that  {output}")





if __name__ == "__main__":
    death_prediction()
