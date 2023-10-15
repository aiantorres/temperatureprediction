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

#def input_parameter():
#   evspsbl = st.sidebar.slider()
data=pd.read_excel(r"C:\Users\usuario\OneDrive\Documents\GitHub\temperatureprediction\data\raw\OrlandoStation.xls",index_col=0)  


st.map(data,
    latitude='POINT_Y',
    longitude='POINT_X',
    size='20',
    color='#0044ff')
                   