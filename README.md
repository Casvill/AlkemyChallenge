# AlkemyChallenge

Resolución del reto propuesto por [Alkemy](https://www.alkemy.org) para ingresar a su curso de aceleración de Python Data-Analyst.<br>

## Índice:
* [Enunciado del reto](https://github.com/Casvill/AlkemyChallenge/blob/main/Challenge%20Data%20Analytics%20con%20Python.pdf)  
* [Herramientas utilizadas](#Herramientas-utilizadas)  
* [Librerías utilizadas](#Librerías-utilizadas)
* [Uso](#Uso)
* [Modificando variables de entorno](#Modificando-variables-de-entorno)<br><br>

## Herramientas utilizadas:    
- Docker 20.10.17  
- Docker Compose  
- Python 3.10  
- Postgres 14.3  
<br>[Índice](#Índice)<br><br> 
  
## Librerías utilizadas:   
- pandas==1.4.1
- requests==2.27.1
- numpy==1.22.3
- psycopg2-binary==2.9.3
- SQLAlchemy==1.4.37
- SQLAlchemy-Utils==0.38.2
- python-decouple==3.6  
<br>[Índice](#Índice)<br><br> 

## Uso:  
1-  Haciendo uso de una consola, dirígete a la ubicación donde se encuentra el archivo `docker-compose.yml`  
2-  Ejecuta el siguiente comando `docker compose up`  
3-  En un navegador web, abre el siguiente enlace [localhost:5050](http://127.0.0.1:5050)  
4-  Ingresa la contraseña (por defecto es `admin`)  
5-  La primera vez, tendrás que crear un nuevo servidor, haciendo click en "Add New Server", ponle el nombre que quieras, luego dirígete a la pestaña "Connection" 
y en el campo "Host name/address" escribe `postgres`, en el campos Password escribe `postgresql`. Haz click en el botón "Save".  
5-  Ya puedes ver la base de datos creada, que por defecto trae el nombre `BaseDeDatosAlkemyProject`  
6-  En la carpeta del proyecto se creará una nueva carpeta llamada "sources", ahí se almacenarán el log de ejecución del programa y 3 carpetas con los archivos 
.csv jalados de la web [datos.gob.ar/](https://datos.gob.ar/)  
<br>[Índice](#Índice)<br><br> 

## Modificando variables de entorno  
Para modificar las variables de entorno que trae el proyecto por defecto, dirígete a l carpeta "alkemy-challenge" y modifica las variables del archivo `.env`
como más te convenga.  
<br>[Índice](#Índice)<br><br> 
