'''
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro
'''
import streamlit as st
from streamlit_ace import st_ace


st.title("Editor de código Python com Streamlit")

first, second = st.columns(2)

with first:
    st.markdown("## Input")
    code = st_ace(language = 'python', theme='xcode')

with second:
    st.markdown("## Output")
    #st.markdown("``` python\n"+code+"```")
    st_ace(value = code, language = 'python', theme = 'pastel_on_dark', readonly  = True)
