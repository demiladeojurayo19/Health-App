import streamlit as st

def Description_function():

    # Container with a white background
    with st.container():
        # Include the image with a centered caption
        st.image("fitness.png", use_column_width=True)
        st.markdown("<h1 style='text-align: center; color: #333333;'>Health Insights Predictor</h1>", unsafe_allow_html=True)

        description = """
        Welcome to the Health Insights Predictor, your personal tool for predicting health outcomes based on key features. This app leverages advanced machine learning models to provide tailored predictions for various health scenarios. Whether you're interested in predicting Death_Event from heart_attack, diagnose anaemia, or high blood pressure, our app has you covered.

        **Key Features:**
        - *Model Selection:* Choose from a variety of predictive models, each specialized for different health insights.
        - *Intuitive Interface:* An easy-to-use slider allows you to seamlessly navigate between different health prediction modules.
        - *Personalized Predictions:* Input relevant health metrics through intuitive sliders and receive personalized predictions instantly.
        - *Informative Results:* Understand your health predictions with detailed insights and recommendations.

        **How It Works:**
        1. Select the specific health prediction model you are interested in.
        2. Use the interactive sliders to input relevant health features.
        3. Receive instant predictions based on cutting-edge machine learning algorithms.
        4. Gain valuable insights and recommendations to support your well-being.

        Whether you're a fitness enthusiast, health-conscious individual, or someone on a wellness journey, the Health Insights Predictor empowers you with data-driven insights for a healthier lifestyle.
        """
        st.markdown(description, unsafe_allow_html=True)

# Call the function
Description_function()
