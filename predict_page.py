import streamlit as st
import numpy as np
import pickle


#loading the ml model
def load_model():
    with open('saved_steps_of_cvdprediction.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


#encoding the categorical variables
logisticregressor = data["model"]
le_General_Health = data["le_General_Health"]
le_Checkup = data["le_Checkup"]
le_Exercise = data["le_Exercise"]
le_Skin_Cancer = data["le_Skin_Cancer"]
le_Other_Cancer = data["le_Other_Cancer"]
le_Depression = data["le_Depression"]
le_Diabetes = data["le_Diabetes"]
le_Arthritis = data["le_Arthritis"]
le_Sex = data["le_Sex"]
le_Smoking_History = data["le_Smoking_History"]


#function to run on page load
def show_predict_page():
    st.title("HEART DISEASE RISK PREDICTION")
    st.write("""### We need some information for prediction""")

    General_Health = (
        "Poor",
        "Very Good",
        "Good",
        "Fair",
        "Excellent"
    )

    Checkup = (
        "Within the past 2 years",
        "Within the past year",
        "5 or more years ago",
        "Within the past 5 years",
        "Never"
    )

    Exercise = (
        "Yes",
        "No"
    )

    Skin_Cancer = (
        "Yes",
        "No"
    )

    Other_Cancer = (
        "Yes",
        "No"
    )

    Depression = (
        "Yes",
        "No"
    )

    Diabetes = (
        "No",
        "Yes",
        "No, pre-diabetes or borderline diabetes",
        "Yes, but female told only during pregnancy"
    )

    Arthritis = (
        "Yes",
        "No"
    )

    Sex = (
        "Male",
        "Female"
    )

    Smoking_History = (
        "Yes",
        "No"
    )

    General_Health = st.selectbox("General Health", General_Health)
    Checkup = st.selectbox("Checkup",Checkup)
    Exercise = st.selectbox("Exercise",Exercise)
    Skin_Cancer = st.selectbox("Skin_Cancer",Skin_Cancer)
    Other_Cancer = st.selectbox("Other_Cancer",Other_Cancer)
    Depression = st.selectbox("Depression",Depression)
    Diabetes = st.selectbox("Diabetes",Diabetes)
    Arthritis = st.selectbox("Arthritis",Arthritis)
    Sex = st.selectbox("Sex",Sex)
    Smoking_History = st.selectbox("Smoking_History",Smoking_History)

    Age_Category = st.number_input("Enter Your Age")
    Height_cm = st.number_input("Enter you height in cm")
    Weight_kg = st.number_input("Enter your weight in kg")
    BMI = st.number_input("Enter your BMI")
    Alcohol_Consumption = st.number_input("Enter you Alcohol Consumption Level")
    Fruit_Consumption = st.number_input("Enter your Fruit Consumption Level")
    Green_Vegetables_Consumption = st.number_input("Enter your Green Vegetables Consumption Level")
    FriedPotato_Consumption = st.number_input("Enter your Fried Potato Consumption Level")

    ok = st.button("PREDICT DISEASE")
    #if ok is true, which means the button is clicked, prediction result is to be shown
    if ok:
        XINPUT = np.array([[General_Health, Checkup, Exercise, Skin_Cancer, Other_Cancer, Depression, Diabetes, Arthritis,
                            Sex, Age_Category, Height_cm,
                            Weight_kg, BMI, Smoking_History, Alcohol_Consumption,
                            Fruit_Consumption, Green_Vegetables_Consumption, FriedPotato_Consumption]])
        XINPUT[:, 0] = le_General_Health.transform(XINPUT[:, 0])
        XINPUT[:, 1] = le_Checkup.transform(XINPUT[:, 1])
        XINPUT[:, 2] = le_Exercise.transform(XINPUT[:, 2])
        XINPUT[:, 3] = le_Skin_Cancer.transform(XINPUT[:, 3])
        XINPUT[:, 4] = le_Other_Cancer.transform(XINPUT[:, 4])
        XINPUT[:, 5] = le_Depression.transform(XINPUT[:, 5])
        XINPUT[:, 6] = le_Diabetes.transform(XINPUT[:, 6])
        XINPUT[:, 7] = le_Arthritis.transform(XINPUT[:, 7])
        XINPUT[:, 8] = le_Sex.transform(XINPUT[:, 8])
        XINPUT[:, 13] = le_Smoking_History.transform(XINPUT[:, 13])
        XINPUT = XINPUT.astype('float')

        disease = logisticregressor.predict(XINPUT)
        if disease[0] == 'No':
            st.subheader("Congratulations!! You are not at risk. Stay Healthy!!")
        else:
            st.subheader("Yes you might have a risk of heart disease. But don't panic. Consult your doctor. You'll be fine.")











