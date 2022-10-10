'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''

# Importando as bibliotecas
import pandas as pd
import streamlit as st # para a interface do nosso App
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

# Título
st.write("# Prevendo Diabetes")

# Dataset
df = pd.read_csv("/home/eddygiusepe/16_examples_with_API_Flask/ML_Web_with_Streamlit/Web_with_Python_and_Streamlit/diabetes.csv")

# Cabeçalho
st.subheader("Informações dos dados")

# Nome do usuário
user_input = st.sidebar.text_input("Digite seu nome")
# Escrevendo o nome do usuário
st.write("Paciente:", user_input)


# Dados de entrada
x = df.drop(['Outcome'], axis=1)
y = df['Outcome']


# Separar Dados em Trin e Test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# Dados dos usuários com a função
# Nesta etapa, vamos criar uma função para coletar os dados que irão ser inseridos pelos usuários. 
# Como parâmetro, vamos definir um valor mínimo, um valor máximo e um valor default.

def get_user_date():
    pregnancies = st.sidebar.slider("Gravidez",0, 15, 1)
    glicose = st.sidebar.slider("Glicose", 0, 200, 110)
    blood_pressure = st.sidebar.slider("Pressão Sanguínea", 0, 122, 72)
    skin_thickness = st.sidebar.slider("Espessura da pele", 0, 99, 20)
    insulin = st.sidebar.slider("Insulina", 0, 900, 30)
    bni= st.sidebar.slider("Índice de massa corporal", 0.0, 70.0, 15.0)
    dpf = st.sidebar.slider("Histórico familiar de diabetes", 0.0, 3.0, 0.0)
    age = st.sidebar.slider ("Idade", 15, 100, 21)

    # Criação de um dicionário para receber informações
    user_data = {
        'Gravidez': pregnancies,
        'Glicose': glicose,
        'Pressão Sanguínea': blood_pressure,
        'Espessura da pele': skin_thickness,
        'Insulina': insulin,
        'Índice de massa corporal': bni,
        'Histórico familiar de diabetes': dpf,
        'Idade': age
                }

    features = pd.DataFrame(user_data, index=[0])


    return features

# Vamos chamar a função criada e gerar um gráfico para exibir as informações.
# O critério utilizado aqui foi a “entropia”, pois é usada para estimar a aleatoriedade da variável a prever (classe).
user_input_variables = get_user_date()

# Gráfico
graf = st.bar_chart(user_input_variables)

dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dtc.fit(x_train, y_train)

# Acurácia do modelo
st.subheader('Acurácia do nosso modelo')
st.write(accuracy_score(y_test, dtc.predict(x_test))*100)


# Se o resultado for igual a “0” ele não possui Diabetes, caso seja igual a “1” ele possui Diabetes.
#previsão do resultado
prediction = dtc.predict(user_input_variables)

st.subheader('Previsão: ')
st.write(prediction)


