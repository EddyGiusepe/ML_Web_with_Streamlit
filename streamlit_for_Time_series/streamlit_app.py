'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo --> https://github.com/MaiconGavino/inpi_serie_temporal
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("data.xlsx", decimal='.')

def gera_grafico(graf):
    st.header('Registro de Marca por ano no Estado do '+ graf)

    fig = px.bar(df, x=df['Ano'], y=df[graf],text_auto='.2s')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis_title= 'Anos', yaxis_title = '',xaxis_tickangle=-90)
    fig.update_yaxes(showticklabels=False)
    st.plotly_chart(fig, use_container_width = False)
    

def main(): 
    page = st.sidebar.selectbox('Selecione o Estado', [x for x in df.columns if x in ["Acre","Alagoas","Amazonas","Amapá","Bahia","Ceará",
                                                                                      "Distrito Federal","Espírito Santo","Goiás","Maranhão", "Minas Gerais",
                                                                                      "Mato Grosso do Sul","Mato Grosso","Pará","Paraíba","Pernambuco",
                                                                                      "Piauí","Paraná","Rio de Janeiro","Rio Grande do Norte",
                                                                                      "Rondônia", "Roraima", "Rio Grande do Sul","Santa Catarina","Sergipe",
                                                                                      "São Paulo", "Tocantins"]])
    gera_grafico(page)
if __name__ == '__main__':
    main()