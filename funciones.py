import pandas, re
from pandas import DataFrame
from datetime import datetime, timedelta
import streamlit as st

# Valida que las columnas de un dataframe sean las especificadas. 


__DATAFRAME: DataFrame = None

def set_dataframe(df: DataFrame):
    global __DATAFRAME
    if df is not None:
        __DATAFRAME = df
        main()

def mostrar_error(msg: str = "No se agrego ningun mensaje."):
    print(f"<<modo test>> ERROR: -> {msg}")
    #st.error(msg)
    
def dataframe_empty() -> bool:
    "Comprueba que el dataframe tenga contenido."
    _msg = "Error: El '.csv' adjunto está vacío."
    if __DATAFRAME.empty:
        raise pandas.errors.EmptyDataError(_msg)

def comprobar_contenido():
    """Comprueba el contenido del documento. <<Que no esté vacío.>>"""
    try:
        dataframe_empty()
        return True
    except Exception as e:
        mostrar_error(e)
        return False


def validar_columnas():
    # Lista de columnas requeridas
    columnas_requeridas = [
        "NumeroPermisoCREProveedor", "Diaareportar", "ProductoId", "SubProductoId", 
        "TipoMov", "CostoFlete", "VolumenVendido", "PrecioVenta", "VolumenComprado", 
        "PrecioCompra", "PrecioDescuentoIncluido", "PermisoTransportista", 
        "NumeroPermisoCRECliente", "TipoDescuentoId", "Entidad", "Municipio", 
        "RazonSocial", "RFC", "SectorEconomico", "TipoCliente"
    ]
    # Lista de las columnas faltantes
    columnas_faltantes = [col for col in columnas_requeridas if col not in __DATAFRAME.columns]
    if columnas_faltantes:
        _msg = f"Faltan las siguientes columnas en el documento '.csv'\n\n{columnas_faltantes}\n\n-> Valide los nombres de las columnas."
        raise ValueError(_msg)
    print("Las columnas son validas.")
    return True


def comprobar_NumeroPermisoCREProveedor():
    patron = re.compile(r'^(CNE|PL|H)/([0-9]{1,6})/(TRA|DIS)/(OM|DUC|TM)/([0-9]{4})$')
    campos_invalidos = []
    columna = __DATAFRAME['NumeroPermisoCREProveedor']

    for i, valor in enumerate(columna):
        if pandas.isna(valor):
            continue

        valor_str = str(valor).strip()
        
        if patron.match(valor_str):
            continue
        else:
            campos_invalidos.append({"Fila": {i+2}, "Valor":valor})
    
    if len(campos_invalidos) > 0:
        msg = f"Al validar la columna: 'NumeroPermisoCREProveedor' encontramos los siguientes campos como INVALIDOS segun el '.xsd'.\n{campos_invalidos}."
        raise ValueError(msg)
    else:
        return True
        
    






# Pendiente de desarrollo.
def comprobar_columnas():
    "Comprueba que las columnas tengan la informacion esperada."
    comprobar_NumeroPermisoCREProveedor()
    
    
    input("<<test>> Esperando. ")

# Pendiente de desarrollo.
def formatear_columnas():
    "Da formato a las columnas segun la especificacion."
    pass





def comprobar_informacion():
    try:
        validar_columnas()
        comprobar_columnas()
        return True
    except Exception as e:
        mostrar_error(e)
        return False


def obtener_fechas():
    fechas_unicas = __DATAFRAME['Diaareportar'].unique()
    



    

def main(): 
    "Ejecucion Principal"
    # Se comprueba el contenido del documento. 
    comprobar_contenido()

    # Se valida que incluya los campos requeridos.
    comprobar_informacion()


