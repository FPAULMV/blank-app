import funciones as f
import streamlit as st
import pandas as pd

#st.title("Conversor CSV a XML")
#archivo_csv = st.file_uploader("Sube tu CSV")
archivo_csv = r"C:\Users\AdminTI\Desktop\CreV.4_1.xlsx"
if archivo_csv:
    df = pd.read_excel(archivo_csv)
    # Tu lógica de conversión aquí

    f.set_dataframe(df)
    
    





    #xml_resultado = convertir(df)
    #st.download_button("Descargar XML", xml_resultado)
