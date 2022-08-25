import requests
import csv
from datetime import date
import os
import logging

logging.basicConfig(filename='./Sources/logs.log',level='DEBUG')


def importar_csv(url:str,delimiter:str) -> csv:
    """
    Importa un archivo csv desde la web a memoria volátil.

    Parameters:
    url: Url de la web donde se aloja el archivo.
    delimiter: Delimitador que usa el archivo.

    Returns:
    Objeto csv.
    """
    try:
        r = requests.get(url)
        r = r.content.decode('utf-8')
        csv_file = csv.reader(r.splitlines(), delimiter=delimiter)

    except(Exception) as error:
        logging.exception(f"extract.py -> importar_csv(): Error: {error}")
        print(f"extract.py -> importar_csv(): Error: {error}")

    return csv_file

def crear_ruta_y_nombre_para_archivo_csv(url:str) -> str:
    """
    Crea el nombre del archivo y la ruta que tendrá
    según la fecha de descarga.

    Parameters:
    url: Url de la web donde se aloja el archivo.

    Returns:
    Cadena de texto del path con nombre del archivo.
    """
    try:
        categoria = url.split('/')[-1][:-4]
    except(Exception) as error:
        logging.exception(f"extract.py -> crear_ruta_y_nombre_para_archivo_csv(): Error: {error}")
        print(f"extract.py -> crear_ruta_y_nombre_para_archivo_csv(): Error: {error}")

    year = date.today().strftime('%Y')
    month_number = date.today().strftime('%m')
    month_name = date.today().strftime('%B')
    day = date.today().strftime('%d')
    csv_name = f'{categoria}/{year}-{month_name}/{categoria}-{day}-{month_number}-{year}.csv'
    
    return csv_name


def exportar_csv(csv_file:csv,path:str,csv_name:str) -> None:
    """
    Guarda archivo de memoria volátil a memoria no-volátil.

    Parameters:
    csv_file: Archivo almacenado en memoria volátil.
    path: Ruta global donde será almacenado el archivo.
    csv_name: Nombre con el que será almacenado el archivo.
    """
    try:
        os.makedirs(os.path.dirname(path+csv_name), exist_ok=True)

        with open(path+csv_name, 'w',newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for elemento in csv_file:
                writer.writerow(elemento)
                
    except(Exception) as error:
        logging.exception(f"extract.py -> exportar_csv(): {error}")
        print(f"extract.py -> exportar_csv(): {error}")
