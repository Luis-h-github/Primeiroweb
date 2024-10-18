# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSmbAW7snoqGh4OjB0UGM_TgmlxcwGFi6oOFlsctq0KtDrusNHF-iodk9_yXOJuPBkeBdf6jzvh1H7W/pub?gid=414383360&single=true&output=csv"
db = Ler_GooglePlanilha(url)
Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Criando um APP do zero")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Passo a passo para o desenvolvimento")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Primeiro passo")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

