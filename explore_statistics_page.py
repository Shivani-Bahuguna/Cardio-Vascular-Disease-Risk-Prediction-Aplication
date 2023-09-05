import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

#loading dataset
def load_data():
    df = pd.read_csv('CVD.csv')
    return df

df = load_data()


#function to run on page load
def show_explore_statistics_page():
    st.title("Explore Statistics")
    st.write("""### CVD DATASET from KAGGLE""")
    numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
    categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write("""### 1. Plotting for numerical features""")
    for feature in numeric_features:
        plt.figure(figsize=(10, 4))
        plt.hist(data=df, x=feature)
        plt.title('Distribution of ' + feature)
        plt.xlabel(feature)
        plt.ylabel("Count")
        st.pyplot()

    st.write("""### 2. Plotting for categorical features""")
    for feature in categorical_features:
        plt.figure(figsize=(10, 4))
        sns.countplot(data=df, x=feature)
        plt.title('Count of ' + feature)
        plt.xticks(rotation=90)
        st.pyplot()

    st.write("""### 3.Bivariate Analysis """)
    st.write("""### Analyze the relationship between the disease conditions and some selected variables""")

    selected_variables = ['General_Health', 'Exercise', 'Sex', 'Age_Category', 'Smoking_History']
    disease_conditions = ['Heart_Disease', 'Skin_Cancer', 'Other_Cancer', 'Diabetes', 'Arthritis']

    for disease in disease_conditions:
        for variable in selected_variables:
            plt.figure(figsize=(10, 4))
            sns.countplot(data=df, x=variable, hue=disease)
            plt.title('Relationship between ' + variable + ' and ' + disease)
            plt.xticks(rotation=90)
            st.pyplot()

    st.write("""### 4. Multivariate Analysis""")
    st.write("""### Analyze the relationship between disease conditions, general health, and age category""")
    plt.figure(figsize=(10, 7))
    sns.countplot(data=df, x='General_Health', hue='Age_Category')
    plt.title('Distribution of General Health by Age Category')
    plt.xticks(rotation=90)
    #plt.show()
    st.pyplot()

    for disease in disease_conditions:
        plt.figure(figsize=(10, 7))
        sns.countplot(data=df, x='General_Health', hue=disease)
        plt.title('Distribution of ' + disease + ' by General Health')
        plt.xticks(rotation=90)
        #plt.show()
        st.pyplot()


