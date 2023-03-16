# Prueba-django
Aplicación desarrollada con el framework DJango que consiste en un microservicio provisto de una API REST para la gestión (CRUD) de dos tablas mediante peticiones HTTP. 

## Pre-requisitos:
* Instalar Python 3.
* Instalar Gestor de bases de datos postgreSQL
* Crear y conectar la BD donde se migrarán los modelos de Empleado y Departamento.

## Pasos para trabajar con el proyecto:

Una vez clonado el proyecto y estando en la carpeta de _microservicios_:

1. Instalar las dependencias necesarias
    * Windows: `pip install -r requirements.txt`
2. Crear un archivo .env dentro de la carpeta _microservicios_ con la siguiente información:

      ```
      POSTGRESQL_HOST = YOUR_POSTGRESQL_HOST
      POSTGRESQL_USER = YOUR_POSTGRESQL_USER
      POSTGRESQL_PASSWORD = YOUR_POSTGRESQL_PASSWORD
      POSTGRESQL_DB = YOUR_POSTGRESQL_DB
      POSTGRESQL_PORT = YOUR_POSTGRESQL_PORT
      
      PORT_CONECTION = 1234
      ```
      __Comentario:__ La variable `PORT_CONECTION` indica el puerto de conexión del servidor de desarrollo. Por defecto este es el 8000, pero para la prueba se requiere el puerto TCP 1234.
      
3. Realizar las migraciones con los comandos:
      * Windows: `python manage.py makemigrations`
      * Windows: `python manage.py migrate`

4. Ejecutar el server de desarrollo:
      * Windows: `python manage.py runserver`
      
5. Por último, leer la [documentación dde como usar la API REST para el CRUD de Empleados y Departamentos](https://github.com/luiseduardo23/Prueba-django/blob/main/Documentaci%C3%B3n%20del%20API%20REST%20para%20microservicios.pdf).
