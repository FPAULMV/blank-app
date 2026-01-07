import pandas
from pandas import DataFrame
from datetime import datetime, timedelta
import streamlit as st

# Valida que las columnas de un dataframe sean las especificadas. 

def validar_columnas(df: DataFrame):
    # Lista de columnas requeridas
    columnas_requeridas = [
        "NumeroPermisoCREProveedor", "Diaareportar", "ProductoId", "SubProductoId", 
        "TipoMov", "CostoFlete", "VolumenVendido", "PrecioVenta", "VolumenComprado", 
        "PrecioCompra", "PrecioDescuentoIncluido", "PermisoTransportista", 
        "NumeroPermisoCRECliente", "TipoDescuentoId", "Entidad", "Municipio", 
        "RazonSocial", "RFC", "SectorEconomico", "TipoCliente"
    ]

    # Lista de las columnas faltantes
    columnas_faltantes = [col for col in columnas_requeridas if col not in df.columns]


    if columnas_faltantes:
        msg = f"Faltan las siguientes columnas en el documento '.csv' \n{columnas_faltantes} \
            valide los nombres de las columnas. \n Estas son todas las columnas requeridas: {columnas_requeridas}" 
    
        st.error(msg)


    pass