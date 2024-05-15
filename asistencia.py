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
    # Preceptores
    # Alumnos

# Mostrar horarios actuales y proxima clase en base al horario actual (Libreria time)

"""
Metodologia de trabajo:
    Nombre de variables: lowerCamelCase
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

    # El cursor va a devolver una tupla con varios valores
    # En la primera posicion de la primera tupla que devuelve, tenemos un objeto que contiene el horario y la fecha
    horario = cursor.fetchall()[0][0]

    # De todos los datos del horario nos quedamos con la hora y los minutos
    return [horario.hour, horario.minute]

# Horarios en los que se retiran normalmente los alumnos
HORARIOS_SALIDA = [[11, 50], [17, 50], [22, 30]]

# Los dias estan en ingles porque asi los devuelve la libreria time
# (Si, googlie los nombres en ingles porque no me los acordaba)
dias = {
    "Monday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50], [1, 20], [2, 30], [3, 40], [4, 50], [5, 50]],
    "Tuesday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Wednesday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50] [13, 20], [14, 30], [15, 40], [16, 50], [17, 50]],
    "Thursday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]],
    "Friday": [[7, 20], [8, 30], [9, 40], [10, 50], [11, 50]]
}

# Funciones para sumar horas y minutos tratando de evitar errores

def sumarMinutos(min1, min2):

    otraHora = 0 # Variable para acumular las horas que se generan por el exceso de minutos
    minutosTotal = min1 + min2 # Minutos totales ingresados
    UNA_HORA = 60 # Una hora tiene 60 minutos en total (Esta en mayusculas porque es una constante)

    while minutosTotal >= UNA_HORA:

        if minutosTotal >= UNA_HORA:
            otraHora += 1
            minutosTotal -= UNA_HORA

    return [otraHora, minutosTotal]

# Para comparar los dos horarios se tienen que ingresar dos horarios en arrays como formato [HORA, MINUTOS]
# Se pregunta si el primer horario es mayor que el segundo
# Si son iguales, se devuelve False
def compararHoras(primerHorario, segundoHorario):

    for index in range(2):

        if primerHorario[index] > segundoHorario[index]:
            return True
    
        if segundoHorario[index] > primerHorario[index]:
            return False
        
    return False
    
        

# Hay que hacer una clase para cada entidad? Alta paja xddd

# Esto es una clase para el grupo de alumnos entero, ya que seria mas comodo tener a todos
# los objetos creados por la clase alumnos acomodados en un mismo lugar
class salon():
    def __init__():
        pass

# Clase alumnos, metodos para medir las faltas, ver el horario al que entra, sale y a la hora
# a la que se supone que tiene que entrar y salir.
class alumno():
    
    def __init__(self, falta, faltasJustificadas, dia, jornada):

        # Faltas y Asistencias, atributos de la BD
        self.falta = falta
        self.faltasJustificadas = faltasJustificadas
        self.faltaTotal = self.falta  + self.faltasJustificadas
        self.asistencias = 28 - self.falta


        ###### TODO LO DE LOS HORARIOS DEBERIA ESTAR EN OTRA FUNCION PARA DECLARARLOS ######
        ###### YA QUE NO ES NECESARIO CARGARLOS SI SOLO ESTAN VIENDO AL ALUMNO EN LA TABLA ######

        # Horarios del alumno
        self.dia = dia
        self.jornada = jornada

        # De los horarios, tomamos la hora a la que entra y a la que sale, respetando los turnos
        # Hora a la que tiene que salir y entrar (en teoria)
        self.horarioEntrada = [self.jornada[0]]
        self.horarioSalida = []

        # Analiza la jornada de los alumnos para determinar en que turno deben estar
        # La documentacion esta en una hoja.
        for hora1 in HORARIOS_SALIDA: 

            for hora2 in self.jornada:
                
                if compararHoras(hora2, hora1):

                    self.horarioEntrada.append(hora2)
                    self.horarioSalida.append(horario)

                    break

                horario = hora2

        # Se añade el ultimo valor de la jornada, es uno que no revisan los for
        self.horarioSalida.append(self.jornada[-1])

        # Variable que muestra si llego o no a la escuela. 
        # Si toca la huella por primera vez quiere decir que entro, 
        # si lo hace por segunda vez quiere decir que se fue
        self.entro = False
        self.retiro = False

        # Hora a la que entra y sale el alumno (Pone el dedo en la huela)
        self.horaLlegada = "No entro" # Despues se cambia por la hora, una lista con la hora y los minutos: [hora, minuto]
        self.horaSalida = "No salio" # Despues se cambia por la hora

        # cantidad de falta que acumula en el dia por llegada tarde, retiros, etc.
        self.falta = 0

    def getTurnos():
        pass

    # Pone el dedo en la huella al entrar
    def getHorarioLlegada(self):

        # Esta funcion solo puede actuar cuando el alumno entre por primera vez
        # (Tendriamos que ver que pasa cuando alguien se hace el gracioso y toca varias veces)
        # Intervalo de tiempo para poner el dedo?

        if self.entro == True:
            return

        # Toma el horario al que entro
        self.horaLlegada = getHora_minuto()

        # Si puso la huella despues del horario de salida se le cuenta como falta completa
        if self.horaLlegada[0] == self.horarioSalida[0] and self.horaLlegada[1] < self.horarioSalida[1] or self.horaLlegada[0] < self.horarioSalida[0]:

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

        self.retiro = True # Bueno ahora si se fue

    # Funcion que calcula la cantidad de faltas que acumula a lo largo del dia
    def medirFalta(self):

        # Valores de las faltas acomodados en las variables
        # (Para que quede mas ordenadito xd)
        Sin_falta = 0
        cuarto_falta = 0.25
        media_falta = 0.5
        Completa_falta = 1

        # Me parecen muchos if, pero despues vemos si los podemos acomodar mejor
        # Los return son para que la funcion termine y no se cargue el resto del codigo al pedo

        # El alumno nunca llego
        if self.entro == False:
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
            
            # ¿LLego justo en la hora? ¿Llego bien con los minutos?
            if self.horaLlegada[0] == self.horarioEntrada[0] and self.horaLlegada[1] <= self.horarioEntrada[1]:
                self.falta = Sin_falta
                return

            # LLego despues de la hora, pero capaz lo salvan los minutos (?
            if self.horaLlegada[0] <= self.horarioEntrada[0] + 1:

                # Se paso por los minutos de llegada, eso ya es un cuarto de falta, pero si se paso por mucho seria otro cuarto de falta mas
                self.falta += cuarto_falta

                # Funcion para sumarle 15 minutos al horario que tiene para llegar tarde
                margenDe15Minutos = sumarMinutos(self.horarioEntrada[1], 15) 

                # Preguntar si el alumno llego dentro de ese margen de 15 minutos
                # Si se paso por mucho se le suma otro cuarto de falta, completando la media falta, si no, se queda con el cuarto que ya tenia
                if self.horaLlegada[1] > margenDe15Minutos[1]:
                    self.falta += media_falta

                return                

            else:

                self.falta += media_falta
                return
                

    # Funcion que aplica todas las faltas acumuladas
    # Si no acumulo ninguna falta simplemente suma 0
    def aplicarFalta(self):
        # Por ahora solo se suma a una variable, pero cuando este la base de datos,
        # Seria una funcion que la modifique sumando la falta que acumulo al valor del atributo que corresponda
        self.faltaTotal + self.falta

class materias:
    pass

class profesor:
    pass


juanito = alumno(
                2, # faltas
                1, # faltas justificadas
                time.strftime("%A"), # Dia actual
                dias.get(time.strftime("%A")), # Horario total
)


horaActual = getHora_minuto()
#print('Hora actual: {}:{}'.format(horaActual[0], horaActual[1])) 