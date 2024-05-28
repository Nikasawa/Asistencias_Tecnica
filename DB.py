# Archivo para probar conectar python con phpmyadmin
# A modo de prueba, pero el archivo podria quedar como una biblioteca de funciones para el archivo principal (asistencia.py)
# Las tablas van a tener: ID, nombre, apellido, asistencias y faltas; No todas las faltas restan asistencias ya que pueden estar justificadas, 
# por lo que cada funcion que verifica las llegadas tarde puede devolver la falta y solo si no esta justificada se le resta a la asistencia 

################ ################ ################ ################ ################ ################ ##########
# El metodo de conexion y la libreria de mysql.connector sirve tanto para phpmyadmin como para MySQL WorkBench #
################ ################ ################ ################ ################ ################ ##########

# Libreria con la que se conecta a la base de datos
import mysql.connector

# Metodo para establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    database="asistencias"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()
# Siempre se va a usar la funcion execute() sobre cursor para interactuar con la db

#print(conexion)

# Se muestran en funciones def para que no se ejecuten cada que se usa el archivo pero que esten ahi como recordatorio

# Crear Tablas
def newTable():

    # Customers: Nombre de la tabla
    # name: Primer valor de la tabla
    # address: Segundo valor de la tabla
    # VARCHAR: Tipo de dato a ingresar (texto)
    # (255): Maxima cantidad de caracteres
    cursor.execute("CREATE TABLE alumnos (ID int AUTOINCREMENT nombre VARCHAR(255), apellido VARCHAR(255), )")

# Funcion para eliminar todo de la base de datos (No usar)
def deleteTable():
    cursor.execute("DELETE FROM prueba WHERE 1")

# Mostrar todas las tablas
def showTable():

    # Toma todas las tablas
    cursor.execute("SHOW TABLES")

    # Las imprime una por una
    for x in cursor:
        print(x)

# Mostrar los elementos cargados en la tabla "alumnos"
def showAlumnos():

    cursor.execute("SELECT ID, fecha FROM prueba")

    # El fetchall() despues de seleccionar los elementos de la tabla devuelve una lista de todos los datos
    for x in cursor.fetchall():
        print("ID: {}".format(x[0]))
        print("Fecha: {}".format(x[1]))

# Inicio probar resta de faltas
def restarAsistencia():

    falta = input("ingrese cantidad de falta")

    cursor.execute('UPDATE alumnos SET Asistencias = {} WHERE Nombre = Raul')


"""
¡IMPORTANTE!
El commit es obligatorio para cargar los cambios en la base de datos
"""

def conseguirHoraActual():

    cursor.execute('SELECT LOCALTIME();')
        
    tiempoSQL = cursor.fetchall()[0][0]

    segundos = tiempoSQL.second
    minutos = tiempoSQL.minute
    horas = tiempoSQL.hour

    cursor.execute("INSERT INTO prueba (fecha) VALUES (%s)", ('{0}-{1}-{2} {3}:{4}:{5}'.format(tiempoSQL.year, 
                                                                                                tiempoSQL.month, 
                                                                                                tiempoSQL.day,
                                                                                                tiempoSQL.hour,
                                                                                                tiempoSQL.minute,
                                                                                                tiempoSQL.second
    )))


# Añadir algo a la tabla
def addToTable():

    # Se toma: La tabla donde se quiere ingresar; los valores que tiene en ella y posteriormente los valores a ingresar; uno por uno
    
    cursor.execute("INSERT INTO prueba (fecha) VALUES (%s)", ('LOCALTIME()',))



def conseguirHoraTabla():

    cursor.execute('SELECT fecha FROM prueba')

    for x in cursor.fetchall():
        print(x)
        for y in x:
            
            print(y)

#addToTable()
conseguirHoraActual()

conexion.commit()