from constants import *
import extract as e
import transform as t
from load import crear_db, cargar_sql, load
import pandas as pd
import logging 



def main():

    names= []

    csv_file= e.importar_csv(URL_BIBLIOTECAS_POPULARES,',')
    csv_name= e.crear_ruta_y_nombre_para_archivo_csv(URL_BIBLIOTECAS_POPULARES)
    e.exportar_csv(csv_file,PATH_ARCHIVOS,csv_name)
    print(PATH_ARCHIVOS+csv_name)
    df_bibliotecas= pd.DataFrame(t.transformar_datos(PATH_ARCHIVOS+csv_name))
    file_name= csv_name.split('/')[-1]
    names.append(file_name)

    csv_file= e.importar_csv(URL_SALAS_DE_CINE,',')
    csv_name= e.crear_ruta_y_nombre_para_archivo_csv(URL_SALAS_DE_CINE)
    e.exportar_csv(csv_file,PATH_ARCHIVOS,csv_name)
    df_cine= pd.DataFrame(t.transformar_datos(PATH_ARCHIVOS+csv_name))
    file_name= csv_name.split('/')[-1]
    names.append(file_name)

    df_salas_de_cine = t.transformar_datos_cine(PATH_ARCHIVOS+csv_name)


    csv_file= e.importar_csv(URL_MUSEOS,',')
    csv_name= e.crear_ruta_y_nombre_para_archivo_csv(URL_MUSEOS)
    e.exportar_csv(csv_file,PATH_ARCHIVOS,csv_name)
    df_museos= pd.DataFrame(t.transformar_datos(PATH_ARCHIVOS+csv_name))
    file_name= csv_name.split('/')[-1]
    names.append(file_name)


    dataframes= [df_bibliotecas,df_cine,df_museos]
    df_general= pd.concat(dataframes,keys=['b','c','m'])
    lista_df= t.transformar_datos_df(df_general,names)
#----------------------------------------------------------------------------------------------

    crear_db(DATABASE_LOCATION)
    cargar_sql(SQL_PATH)

    load(DATABASE_LOCATION,df_general,'tabla_general')
    load(DATABASE_LOCATION,lista_df[0],'cant_categoria')
    load(DATABASE_LOCATION,lista_df[1],'cant_fuente')
    load(DATABASE_LOCATION,lista_df[2],'cant_provincia_categoria')

    load(DATABASE_LOCATION,df_salas_de_cine,'salas_de_cine')

#----------------------------------------------------------------------------------------------

    logging.info('Proceso finalizado')
    print('Proceso finalizado')

if __name__ == '__main__':
    main()
