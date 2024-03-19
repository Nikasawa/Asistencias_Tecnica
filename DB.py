# Archivo para probar conectar python con phpmyadmin
# A modo de prueba, pero el archivo podria quedar como una biblioteca de funciones para el archivo principal (asistencia.py)

import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()