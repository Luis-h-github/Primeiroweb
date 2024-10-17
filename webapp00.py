# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Criando um APP do zero")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Passo a passo para o desenvolvimento")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Primeiro passo")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
