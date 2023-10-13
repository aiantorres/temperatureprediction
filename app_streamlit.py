import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Configuración de la página de Streamlit

st.set_page_config(page_title="Aplicación de predicción ",
                   page_icon="",
                   layout="centered",
                   initial_sidebar_state="auto")

st.title("Aplicación de predicción de Temperatura")
st.markdown("""Está aplicación predice la temperatura en grados celsius según los parámetros que se introducen""")
st.markdown("""--------""")

logo="./img/temperatura.png"
st.sidebar.image(logo, width=150, use_column_width="auto")
st.sidebar.header('   Datos ingresados por el usuario',divider='rainbow')

def input_parameter():
    
    
                
                   