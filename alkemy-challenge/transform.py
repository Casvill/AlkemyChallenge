import pandas as pd
import numpy as np
import logging


def transformar_datos(path:str) -> pd.DataFrame:
    """
    Transforma datos a partir de un archivo csv.
    Hace las transformaciones dependiendo de la fuente de los datos.

    Parameters:
    path: Path absoluto del archivo csv.

    Returns:
    pd.DataFrame: pd.DataFrame del archivo transformado.
    """

    df = pd.read_csv(path,encoding='UTF-8')
    nombre_archivo = path.split('/')[-1][:-4]
    nombre_archivo = nombre_archivo.split('-')[0]

    if nombre_archivo == 'biblioteca_popular':
        df.drop(['Observacion','Subcategoria','Departamento','Piso','Cod_tel','Información adicional',
                 'Latitud','Longitud','TipoLatitudLongitud','Fuente','Tipo_gestion','año_inicio','Año_actualizacion']
                 ,axis=1,inplace=True)
        
        df.rename(columns={'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia',
                              'IdDepartamento':'id_departamento','Categoría':'categoría',
                              'Provincia':'provincia','Localidad':'localidad','Nombre':'nombre',
                              'Domicilio':'domicilio','CP':'código postal','Teléfono':'número de teléfono',
                              'Mail':'mail','Web':'web'},inplace=True)
        


    elif nombre_archivo == 'cine':
        df.drop(['Observaciones','Departamento','Piso','cod_area','Información adicional',
                 'Latitud','Longitud','TipoLatitudLongitud','Fuente','tipo_gestion','año_actualizacion',
                 'Butacas','Pantallas','espacio_INCAA'],
                  axis=1,inplace=True)
        

        df.rename(columns={'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia',
                            'IdDepartamento':'id_departamento','Categoría':'categoría',
                            'Provincia':'provincia','Localidad':'localidad','Nombre':'nombre',
                            'Dirección':'domicilio','CP':'código postal','Cod_tel':'código de teléfono',
                            'Teléfono':'número de teléfono','Mail':'mail','Web':'web'
                            },inplace=True)

    
    elif nombre_archivo == 'galerias':
        df.drop(['piso','cod_area','latitud','longitud','tipo_latitud_longitud','fuente',
                 'tipo_gestion','departamento','año_actualizacion'],axis=1,inplace=True)

        df.rename(columns={'cod_loc':'cod_localidad','categoria':'categoría','cp':'código postal',
                           'telefono':'número de teléfono'},inplace=True)

    
    df.replace('s/d',np.NaN,inplace=True)
    return df

def transformar_datos_cine(path:str) -> pd.DataFrame:
    """
    Transforma archivo csv para crear pd.DataFrame de los datos
    exclusivos de las salas de cine.

    Parameters:
    path: Path absoluto del arvhivo csv.

    Returns:
    pd.DataFrame: pd.DataFrame con las transformaciones pertinentes.
    """

    df = pd.read_csv(path,encoding='latin1',usecols=['Provincia','Pantallas','Butacas','espacio_INCAA'])

    df['espacio_INCAA'].replace(to_replace='SI',value=True,inplace=True)
    df['espacio_INCAA'].replace(to_replace='si',value=True,inplace=True)
    df['espacio_INCAA'].replace(to_replace='0',value=False,inplace=True)
    df['espacio_INCAA'].fillna(False,inplace=True)

    df.rename(columns={'Pantallas':'cantidad de pantallas','Butacas':'cantidad de butacas',
                        'espacio_INCAA':'cantidad de espacios INCAA'},inplace=True)

    df = df.groupby(['Provincia'],as_index=False).sum()
    
    return df

def transformar_datos_df(df:pd.DataFrame,names:list) -> list:
    """
    Usa el pd.DataFrame df_general para crear las tablas:
    Cantidad de registros totales por categoría
    Cantidad de registros totales por fuente
    Cantidad de registros por provincia y categoría
    
    Nota: 
    La lista de nombres debe ir en el orden:
    -Bibliotecas
    -Cines
    -Museos

    Parameters:
    df: pd.DataFrame
    names: Lista de los nombres de los archivos csv para crear el pd.DataFrame
           'Cantidad de resistros totales por fuente'.
    
    Returns:
    list: Lista con los pd.DataFrames generados.
    """

    lista_df = []

    df_categoria = df.groupby('categoría',as_index=False).size()
    df_categoria.rename(columns={'size':'cantidad'},inplace=True)

    lista_df.append(df_categoria)


    bibliotecas=0
    cines=0
    museos=0
    for element,indice in df.index:
        if element == 'b':
            bibliotecas+=1
        elif element == 'c':
            cines+=1
        elif element == 'm':
            museos+=1
    lista = [bibliotecas,cines,museos]
    dicc = {'fuente':names,'cantidad':lista}
    df_fuente = pd.DataFrame(dicc)

    lista_df.append(df_fuente)

    df_provincia_categoria= df.groupby(['provincia','categoría'],as_index=False).size()
    df_provincia_categoria.rename(columns={'size':'cantidad'},inplace=True)

    lista_df.append(df_provincia_categoria)

    return lista_df
