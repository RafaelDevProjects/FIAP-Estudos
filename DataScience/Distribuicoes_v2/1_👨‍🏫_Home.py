import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo


if "data" not in st.session_state:
    df = pd.read_excel("Dados_InstagramCliente_AULA_3ESP.xlsx", index_col="Post ID")
    df = df.sort_values(by="Reach", ascending=False)
    st.session_state["data"] = df


# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")
st.sidebar.markdown("Desenvolvido por Rafael de Almeida Sigoli [Meu Linkedin](https://www.linkedin.com/in/rafael-almeida-7660a6290/)")


# Adicionando o logo
st.logo("foto.jpg")


pages = st.sidebar.selectbox("Escolha", [
    "Sobre mim",
    "Experiência",
    "Projetos",
    "Soft skills & Hard skills",
    "Entre em contato",
])

if pages == "Sobre mim":
    # Adicionando colunas sobre mim
    col1, col2 = st.columns([1,0.75])   

    col2.image("octocatRafael.png", width=400)

    col1.title("Sobre mim:")
    col1.write("Desenvolvedor Full-stack criativo | Resolvendo Problemas Complexos com Soluções de Programação full-stack")
    col1.write("🎓Formação em Engenharia de Software na FIAP.")
    col1.write("☕Experiência em desenvolvimento de software, desde a faculdade")
    col1.write("💻Proficiente em C# , Java , C/C++ , Python , frameworks como Spring Boot , React e banco de dados como MySQL PostgreSQL Oracle DB")
    col1.write("🌐Interessado em tecnologia, aprendizado de máquina e desenvolvimento de software sustentável.")

elif pages == "Experiência":
    images = [
        "https://via.placeholder.com/600x300?text=Image+1",
        "https://via.placeholder.com/600x300?text=Image+2",
        "https://via.placeholder.com/600x300?text=Image+3"
    ]

    # Exibir o carrossel
    st_carousel(images)

elif pages == "Projetos":
    st.write("Adicionar")

elif pages == "Soft skills & Hard skills":
    st.write("Adicionar")
    
elif pages == "Entre em contato":
    st.write("Adicionar")


    





# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")



# Adicionando o logo no body







