import streamlit as st
from predict_page import show_predict_page
from explore_statistics_page import show_explore_statistics_page

#making a sidebar to give the user options of either viewing stats or making predictions
page = st.sidebar.selectbox("Explore Statistics or Predict", ("Explore Statistics","Predict"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_statistics_page()
