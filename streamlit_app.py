import funciones as f
import streamlit as st
import pandas as pd

st.title("Conversor CSV a XML")
archivo_csv = st.file_uploader("Sube tu CSV")
archivo_xsd = st.file_uploader("Sube el XSD (opcional)")

if archivo_csv:
    df = pd.read_csv(archivo_csv)
    # Tu lógica de conversión aquí

    f.validar_columnas(df)
    print("Las columnas son validas.")
    





    #xml_resultado = convertir(df)
    #st.download_button("Descargar XML", xml_resultado)
