# 3.1415926535897937

# Conectar con MySQL
# Supervisar hora de ingreso de alumnos. Aplicar faltas o llegadas tarde dependiendo la hora de llegada
# Justificativos. Ej: Medico, accidente y/o ilegalidad/es
# Retiros y/o actualizacion de horarios
# Reconocer al alumno por su huella digital
# Sumar cuando falta (Decir si se excedio en las faltas) Maximo de faltas: 28
# Una clase que abarque el salon entero con profesores, alumnos, y sus horarios y otra clase para los alumnos

# Sistema GUI
    # Probar con pantalla (Tele o compu conexion HDMI)

# Hacer mini DB para ir viendo:
    # Asistencias
    # Inasistencias
    # Huellas digitales

# Dos vistas distintas de la interfaz:
    # Preceptories
    # Alumnos

# Mostrar horarios actuales y proxima clase en base al horario actual (Libreria time)

"""
Metodologia de trabajo:
    Nombre de variables: lowCamelCase
    Dejar un comentario antes de cada funcion a modo de explicacion al resto
    Aunque los comentarios despues pueden quedar desactualizados...
    Podriamos considerar que comentar es una mala practica...
"""

# Cuando se termine el proyecto, hay que evaluar los metodos que usamos de cada libreria
# Ya que aca estamos llamando a la libreria entera, y no tiene sentido si es que solo usamos un par de metodos
# una forma de que este un poquito mejor optimizado el programa
import time
import mysql.connector

# Metodo para conectar con la base de datos
# (Bart, esto no tiene contraseña, pero no se lo digas a nadie)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    database="asistencias"
)

# El "Cursor", hace que podamos replicar las funciones de MySQL dentro del codigo de python, llamandolo con el metodo 'execute()'
cursor = conexion.cursor()

# Funcion para conseguir la hora y los minutos actuales
def getHora_minuto():
    # Pedirle el horario y fecha a MySQL
    cursor.execute('SELECT LOCALTIME()')

    # Navegar en el horario devuelto para tomar solo la informacion que queremos
    for infoDeCursor in cursor.fetchall():
        for ObtenerHoraDeInfo in infoDeCursor:
            horario = ObtenerHoraDeInfo

    # De todos los datos del horario nos quedamos con la hora y los minutos
    return [horario.hour, horario.minute]

# Los dias estan en ingles porque asi los devuelve la libreria time
# (Si, googlie los nombres en ingles porque no me los acordaba)
dias = {
    "Monday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Tuesday ": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Wednesday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Thursday ": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Friday ": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]]
}

# Funciones para sumar horas y minutos tratando de evitar errores

def sumarMinutos(min1, min2):

    otraHora = 0
    minutosTotal = min1 + min2

    while minutosTotal >= 60:
        if minutosTotal >= 60:
            otraHora += 1
            minutosTotal -= 60

    return [otraHora, minutosTotal]

# Hay que hacer una clase para cada entidad? Alta paja xddd

# Esto es una clase para el grupo de alumnos entero, ya que seria mas comodo tener a todos
# los objetos creados por la clase alumnos acomodados en un mismo lugar
class salon():
    def __init__():
        pass

# Clase alumnos, metodos para medir las faltas, ver el horario al que entra, sale y a la hora
# a la que se supone que tiene que entrar y salir.
class alumno():
    
    def __init__(self, faltaTotal, faltasJustificadas, dia, jornada, horarioEntrada, horarioSalida):

        self.faltaTotal = faltaTotal
        self.faltasJustificadas = faltasJustificadas
        self.asistencias = 28 - (faltaTotal - faltasJustificadas)

        self.dia = dia
        self.jornada = jornada

        # Variable que muestra si llego o no a la escuela. 
        # Si toca la huella por primera vez quiere decir que entro, 
        # si lo hace por segunda vez quiere decir que se fue
        self.entro = False
        self.retiro = True

        # Hora a la que tiene que salir y entrar (en teoria)
        self.horarioEntrada = horarioEntrada
        self.horarioSalida = horarioSalida

        self.horaLlegada = "No entro" # Despues se cambia por la hora, una lista con la hora y los minutos: [hora, minuto]
        self.horaSalida = "No salio" # Despues se cambia por la hora

        # cantidad de falta que acumula en el dia por llegada tarde, retiros, etc.
        self.falta = 0

    # Pone el dedo en la huella al entrar
    def getHorarioLlegada(self):

        # Esta funcion solo peude actuar cuando el alumno entre por primera vez
        # (Tendriamos que ver que pasa cuando alguien se hace el gracioso y toca varias veces)
        # Intervalo de tiempo para poner el dedo?
        if self.entro == True:
            return

        self.horaLlegada = getHora_minuto()
        self.entro = True        

    # Pone el dedo en la huella al salir
    def getHorarioSalida(self):
                
        if self.entro == False:
            return # El alumno ni siquiera entro y va a salir? Tremenda paradoja wacho
        
        # Conseguir la hora y los minutos a los que se fue
        self.horaSalida = getHora_minuto()

        # Si se retiro
        if self.horaSalida < self.horarioSalida:
            
            # El 'pass', sirve para que el codigo ignore que no hay nada dentro de la estructura del if.
            # Lo que normalmente daria error en la siguiente linea de codigo
            pass

        self.entro = False # Bueno ahora si se fue

    # Funcion que calcula la cantidad de faltas que acumula a lo largo del dia
    def medirFalta(self):

        # Valores de las faltas acomodados en las variables
        # (Para que quede mas ordenadito xd)
        Sin_falta = 0
        cuarto_falta = 0.25
        media_falta = 0.5
        Completa_falta = 1

        # Me parecen muchos if, pero despues vemos si los podemos acomodar mejor

        # El alumno nunca llego
        if self.entro:
            self.falta = Completa_falta

            # Se corta la funcion, ya que si no llego, no hay mucho mas que ver sobre la falta, y nos evitamos la siguiente rama de decisiones
            return

        # El alumno entro a la escuela
        else:

            # Llego antes de la hora?
            if self.horaLlegada[0] < self.horarioEntrada[0]:

                # LLego incluso antes de la hora, la falta es 0
                self.falta = Sin_falta
                return
            
            # LLego despues de la hora, pero capaz lo salvan los minutos (?
            else:

                # LLegar 15 minutos mas tarde, o incluso pasarse de la hora es media falta
                # Este if es una utopia en que la suma de minutos no suma nunca la hora.
                # Despues acomodo ese caso, de momento me manejo con el famoso 7 y 20 xd
                if self.horaLlegada[0] > self.horarioEntrada[0]:

                    # Funcion para sumarle 15 minutos al horario que tiene para llegar tarde
                    margenDe15Minutos = sumarMinutos(self.horarioEntrada[1], 15) 

                    # Preguntar si el alumno llego dentro de ese margen de 15 minutos
                    if self.horaLlegada[1] > margenDe15Minutos[1]:
                        self.falta += media_falta
                    else:
                        self.falta += cuarto_falta

                # LLego a las 7, pero esta dentro del horario en cuestion de minutos?
                elif self.horaLlegada[1] < self.horarioEntrada[1]:
                    self.falta = Sin_falta
                

    # Funcion que aplica todas las faltas acumuladas
    # Si no acumulo ninguna falta simplemente suma 0
    def aplicarFalta(self):
        # Por ahora solo se suma a una variable, pero cuando este la base de datos,
        # Seria una funcion que la modifique sumando la falta que acumulo al valor del atributo que corresponda
        self.faltaTotal + self.falta


juanito = alumno(
                2, # faltas
                1, # faltas justificadas
                time.strftime("%A"), # Dia actual
                dias.get(time.strftime("%A")), # Horario total
                dias.get(time.strftime("%A"))[0], # Hora de llegada 
                dias.get(time.strftime("%A"))[-1] # Hora de salida
)

juanito.medirFalta()
print(juanito.falta)

horaActual = getHora_minuto()
#print('Hora actual: {}:{}'.format(horaActual[0], horaActual[1]))





