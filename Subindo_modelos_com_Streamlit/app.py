'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo --> https://www.linkedin.com/pulse/subindo-modelos-com-streamlit-gabriel-constantin/?originalSubdomain=pt


# Importando as nossas bibliotecas
import matplotlib
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

st.image('Logo-Qualidade-de-Vida.jpg')
st.header('Calule seu risco cardíaco!')
st.markdown('Entre com os seus dados para verificar seu risco:')

col1, col2 = st.columns(2)

x1 = col1.slider('Pressão Arterial Sistólica', 50, 150, 70, 1, help = 'Essa é pressão sistólica mais alta')

x6 = col1.slider('Pressão Arterial Diastólica', 50, 150, 50, 1, help = 'Essa é pressão diastólica mais alta')

x2 = col1.slider('Glicose', 50, 250, 70, 2, help = 'Qual sua glicose em mg/dL?')

x3 = col1.slider('Idade',10, 105, 30, 1, help = 'Qual a sua idade')

x4 = col1.slider('Colesterol Total', 50, 250, 80, 10, help = 'Qual é a medida do seu colesterol?')

x5 = col1.slider('Número de cigarros por dia', 0, 65, 0, 1, help = 'Quantos cigarros por dia?')

x7 = col2.radio('Hipertensão: 1 = Sim / 0 = Não', ['1','0'])

x8 = col2.radio('Diabetes: 1 = Sim / 0 = Não', ['1','0'])

x9 = col2.radio('Toma medicação para pressão: 1 = Sim / 0 = Não', ['1','0'])


st.markdown('---')


dicionario = {'sysBP': [x1],

             'glicose': [x2],

             'age': [x3],

             'totChol': [x4],

             'cigsPerDay': [x5],

             'diaBP': [x6],

             'prevalentHyp': [x7],

             'diabetes': [x8],

             'BPMeds': [x9],

             }

dados = pd.DataFrame(dicionario)
st.write(dados)

st.markdown('---')


with open('./modelo_regress_Log_local.pkl', 'rb') as f:
    modelo = pickle.load(f)


if st.button('EXECUTAR O MODELO'):
    saida = modelo.predict(dados)
    if saida == 0:
        st.markdown('Você não tem previsão de doença, continue se cuidando!')
    else:
       st.markdown('Você tem chance de desenvolver doença cardíaca! Mude sua rotina')
else:
    pass














