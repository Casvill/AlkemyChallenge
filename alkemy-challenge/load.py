import psycopg2
from sqlalchemy import create_engine, exc
# import sqlalchemy
from constants import DATABASE_INFO
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import logging
from datetime import date

logging.basicConfig(filename='./Sources/logs.log',level='DEBUG')


def crear_db(DATABASE_LOCATION:str) -> None:
    """
    Crea la base de datos en caso de que no exista.

    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy Ejemplo:('postgresql://user:password@host/dbname')

    Return:
    None
    """
    try:

        if not database_exists(DATABASE_LOCATION):
            create_database(DATABASE_LOCATION)

    except(Exception) as error:
        logging.error(f"load.py -> crear_db(): Error: {error}")
        print(f"Error: load.py -> crear_db(): Error: {error}")


def __get_engine(DATABASE_LOCATION:str): #-> sqlalchemy.engine:
    """
    Crea y retorna un motor de SQLAlchemy.
    
    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy Ejemplo:('postgresql://user:password@host/dbname')

    Return:
    sqlalchemy.engine: Un motor de SQLAlchemy
    """

    engine = create_engine(DATABASE_LOCATION)
        
    return engine

def __ejecutar_query(query:str) -> None:
    return None


def cargar_sql(SQL_PATH:str) -> None:
    """
    Ejecuta el archivo .sql pasado por parámetro.

    Parameters:
    SQL_PATH: Ubicación del archivo .sql

    Return:
    None
    """

    try:
        with psycopg2.connect(host=DATABASE_INFO['host'],
                                user=DATABASE_INFO['user'],
                                password=DATABASE_INFO['password'],
                                database=DATABASE_INFO['dbname']) as conn:

            conn.autocommit = True

            with conn.cursor() as cursor:
                try:
                    with open(SQL_PATH, 'r') as myfile:                    
                        data = myfile.read()
                        cursor.execute(data)

                except (Exception) as error:
                    logging.error(f"load.py: cargar_sql: 'with open(SQL_PATH)' Error: {error}")
                    print(f"Error: load.py: cargar_sql: 'with open(SQL_PATH)' Error: {error}")

    except (Exception) as error:
        logging.error(f"load.py -> cargar_sql(): 'with psycopg2.connect' Error: {error}")
        print(f"load.py -> cargar_sql(): 'with psycopg2.connect' Error: {error}")


def load(DATABASE_LOCATION:str,df:pd.DataFrame,table_name:str) -> None:
    """
    Carga un pd.DataFrame a una base de datos con un nombre específico.

    Parameters:
    DATABASE_LOCATION: Una URL del motor SQLAlchemy Ejemplo:('postgresql://user:password@host/dbname')
    df: El pd.DataFrame que será cargado a la base de datos.
    table_name: El nombre de la tabla donde será cargado el pd.DataFrame.

    Return:
    None
    """
    df['fecha_de_carga'] = date.today().strftime("%d-%m-%Y")

    try:

        df.to_sql(table_name,__get_engine(DATABASE_LOCATION),if_exists='replace',index=False)

    except exc.SQLAlchemyError as error:
        logging.error(f"load.py -> load(): Error: {error}")
        print(f"Error: load.py -> load(): Error: {error}")

# crear_db(DATABASE_LOCATION)
# cargar_sql(SQL_PATH)
