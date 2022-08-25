from pathlib import Path
from decouple import config

BASE_DIR = Path().resolve()

#------------------------------------------------------------------------------------------------------------
#----------URLs-----------------------------------------------------------------------------------------------
URL_MUSEOS = config('URL_MUSEOS')
URL_SALAS_DE_CINE = config('URL_SALAS_DE_CINE')
URL_BIBLIOTECAS_POPULARES = config('URL_BIBLIOTECAS_POPULARES')

#------------------------------------------------------------------------------------------------------------
#----------PATH WHERE THE CSV FILES WILL BE STORED----------------------------------------------------------
PATH_ARCHIVOS = f"{BASE_DIR}/Sources/"

#-------------------------------------------------------------------------------------------------------------
#------------CONNECTION TO POSTGRESQL-------------------------------------------------------------------------

DATABASE_INFO = {"host":config('DB_HOST',default='localhost'),
                 "port":config('DB_PORT',default='5432'),
                 "user":config('DB_USER',default='postgres'),
                 "password":config('DB_PASSWORD',default='postgresql'),
                 "dbname":config('DB_NAME',default='BaseDeDatosAlkemyProject')}

DATABASE_LOCATION = f"postgresql://{DATABASE_INFO['user']}:{DATABASE_INFO['password']}@{DATABASE_INFO['host']}:{DATABASE_INFO['port']}/{DATABASE_INFO['dbname']}"

#-------------------------------------------------------------------------------------------------------------
#------------PATH TO SQL FILES-------------------------------------------------------------------------

SQL_PATH = f"{BASE_DIR}/sql/crear_tablas.sql"
