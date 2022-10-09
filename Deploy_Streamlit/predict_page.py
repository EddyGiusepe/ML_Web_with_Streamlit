'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo --> https://www.youtube.com/watch?v=xl0N7tHiwlw&t=291s
'''

import streamlit as st
import pickle  # Para carregar nosso modelo, Dados, etc
import numpy as np

# Criamos uma função e carregamos nosso modelo, Dados, codificadores, etc 
def load_model():
    with open('/home/eddygiusepe/16_examples_with_API_Flask/ML_Web_with_Streamlit/Deploy_Streamlit/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Agora criamos uma função para a página de previsão
def show_predict_page():
    st.title("Previsão de salário de Desenvolvedor de Software")

    st.write("""### Nós precisamos algumas informações para predezir seu Salário""")

    # Do Notebook você pode pegar os nomes dos países
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )
    # Também de lá, Notebook, você pode pegar o Nível de educação
    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Países", countries)
    education = st.selectbox("Nível de Educação", education)
    
    # Anos de experência
    expericence = st.slider("Anos de experiência", 0, 50, 3) # Aqui usamos controle Deslizante ("st.slider")
    # Botão de início
    ok = st.button("Calcular Salário")

    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")