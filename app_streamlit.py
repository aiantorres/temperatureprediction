import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import folium
from streamlit_folium import folium_static
from streamlit_folium import st_folium
from prophet import Prophet
from datetime import datetime, timedelta




# Configuración de la página de Streamlit

st.set_page_config(page_title="Aplicación de predicción ",
                   page_icon="",
                   layout="wide",
                   initial_sidebar_state="auto")

st.title("Predicción de Temperatura usando Prophet")
st.markdown("""Está aplicación predice la temperatura en grados celsius según los días que se quieran predecir""")
st.markdown("""--------""")

logo="./img/temperatura.png"
st.sidebar.image(logo, width=150, use_column_width="auto")
st.sidebar.header(' ',divider='rainbow')


data=pd.read_excel(r"C:\Users\usuario\OneDrive\Documents\GitHub\temperatureprediction\data\raw\Estaciones_control_datos_meteorologicos.xls",index_col=0)  

path= r"C:\Users\usuario\OneDrive\Documents\GitHub\temperatureprediction\models\modelStationJuanCarlosI.pkl"
modelo_entrenado = pickle.load(open(path, 'rb'))

def generar_prediccion(dias):
    future = modelo_entrenado.make_future_dataframe(periods=dias, include_history=False)
    forecast = modelo_entrenado.predict(future)
    return forecast
               
col1, espacio ,col2 = st.columns([2,0.2,2])



with col1:
    dias_para_pronosticar = col1.slider('Número de días para pronosticar desde hoy:', 1, 365)
    forecast = generar_prediccion(dias_para_pronosticar)
    hoy = pd.to_datetime(datetime.today().date())
    if col1.button('Generar Predicción'):
        fechas_futuras = forecast[forecast['ds'] >= hoy]
        fechas_futuras.set_index('ds', inplace=True)
        col1.line_chart(fechas_futuras['yhat'], use_container_width=True)

    
with col2:
    m = folium.Map(location=[40.41, -3.667], zoom_start=11)
  
    dias_popup = min(7, dias_para_pronosticar)

    for idx, row in data.iterrows():
        popup_content = f"Estación: {row['ESTACIÓN']}"
        forecast = generar_prediccion(dias_para_pronosticar)
        
        def determinar_color(valor):
                if valor < 10.00:
                    return 'blue'        # Frío extremo
                elif valor < 15.00:
                    return 'lightblue'   # Frío
                elif valor < 20.00:
                    return 'yellow'      # Templado
                elif valor < 25.00:
                    return 'orange'      # Caliente
                else:
                    return 'red'         # Caliente extremo
        
        forecast_futuro = forecast[forecast['ds'] >= hoy]
        if not forecast_futuro.empty:
            for i in range(dias_popup):
                popup_content += f"<br>{forecast_futuro['ds'].iloc[i].date()}: {forecast_futuro['yhat'].iloc[i]:.2f}°C"
        
            prediccion_dia_actual = forecast_futuro['yhat'].iloc[0]
            
            color_icono = determinar_color(prediccion_dia_actual)
            
            folium.Marker(
                location=[row['LATITUD'], row['LONGITUD']],
                popup=popup_content,
                icon = folium.Icon(icon_color=color_icono)
            ).add_to(m)
        else:
            color_icono = 'gray'
          
      
    folium_static(m)
