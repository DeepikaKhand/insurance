import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open("insurance.pickle", "rb") as file:
    model = pickle.load(file)

st.title('Insurance Cost Prediction System')
st.image('https://user-images.githubusercontent.com/69152112/210777775-2e405abe-0753-41d1-aa2f-0eb4d5f39694.png')

# Taking input from user
st.header("Enter details for insurance cost prediction")
age = st.number_input("Your Age=", 20, 70)
bmi = st.number_input("Your BMI",0,50)
children = st.number_input("No. of children",0,5)
gender = st.radio("Enter gender", ['Female', 'Male'])
Female =1 if gender=='Female' else 0
# Male =1 if gender=='Male' else 0
region=st.selectbox('SELECT YOUR REGION',['SOUTHEAST','SOUTHWEST','NORTHEAST','NORTHWEST'])
Smoke = st.radio("Do you smoke?", ['Yes', 'No'])
Yes=1 if Smoke=='Yes' else 0
# No=1 if Smoke=='No' else 0

SOUTHEAST=1 if region=='SOUTHEAST' else 0

# FOR PREDICTION
if st.button("Predict"):
    # Create input array
    input_data = [[age,bmi,children,Female,SOUTHEAST,Yes]]

    # Predict salary
    predicted_insurance_cost = model.predict(input_data)

    # Show result
    st.success('The data is submitted')
    st.success(f"Predicted insurance cost is : ${predicted_insurance_cost[0]:.2f}")
    st.balloons()
    # st.write(df)


