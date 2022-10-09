'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo --> https://www.youtube.com/watch?v=xl0N7tHiwlw&t=291s
'''

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explorar ou Predezir", ("Predezir", "Explorar"))

if page == "Predezir":
    show_predict_page()
else:
    show_explore_page()
    