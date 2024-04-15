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
"""

import time

#Esto devuelve el horario, con hora, minutos y segundos
hora = time.strftime("%X")


"""
Se pueden hacer decisiones con el horario si lo comparamos con otro horario en formato texto
if hora < "20:30":
    print("todavia no son las 20 (" + hora + ")")
else:
    print("Hora pasada de las 20:30 (" + hora + ")")
"""

# Los dias estan en ingles porque asi los devuelve la libreria
dias = {
    "Monday": ["7:20", "8:30", "9:40", "10:50", "11:50"],
    "Wednesday": ["7:20", "8:30", "9:40", "10:50", "11:50"]
}

def sumarHora(var):

    min = time.localtime().tm_min
    hour = time.localtime().tm_hour

    if hour + var >= 60:
        hour = hour + var - 60
        min = 0

    horaSumada = time.strptime(str(hour) + ':' + str(min), '%H:%M').tm_hour

    return horaSumada

def sumarMinutos(var):

    min = time.localtime().tm_min
    hour = time.localtime().tm_hour

    if min + var >= 60:
        hour += 1
        min = min + var - 60

    minutosSumados = time.strptime(str(hour) + ':' + str(min), '%H:%M').tm_min
    return minutosSumados

class salon():
    def __init__():
        pass

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

        self.horaLlegada = "No entro" # Despues se cambia por la hora
        self.horaSalida = "No salio" # Despues se cambia por la hora

        # cantidad de falta que acumula en el dia por llegada tarde, retiros, etc.
        self.falta = 0

    # Pone el dedo en la huella al entrar
    def getHorarioLlegada(self):
        self.horaLlegada = time.localtime()
        self.entro = True

    # Pone el dedo en la huella al salir
    def getHorarioSalida(self):
        self.horaSalida = time.strftime("%X")

    def retiro(self):
        if self.horaSalida < self.horarioSalida:
            self.retiro = True

    # Funcion que calcula la cantidad de faltas que acumula a lo largo del dia
    def medirFalta(self):

        if False: # time.strftime("%X") > self.horarioSalida and self.horaLlegada == 'No entro'
            self.falta = 1

        elif True: #self.entro

            print(self.horaLlegada)
            print(self.horarioEntrada + ':00')

            if self.horaLlegada < self.horarioEntrada + ':00':
                
                print('Llego despues de las 7:20')
                self.falta =+ 0.25

                hora = time.mktime(time.localtime())
                
                if self.horaLlegada >= self.horarioEntrada.tm_hour:

                    print('Llego despues de las 7:20 + 15 minutos')
                    self.falta =+ 0.25

            if self.retiro:
                if self.jornada:
                    pass

    # Funcion que aplica todas las faltas acumuladas
    def aplicarFalta(self):
        self.faltaTotal + self.falta


juanito = alumno(
                2, # faltas
                1, # faltas justificadas
                time.strftime("%A"), # Dia actual
                dias.get(time.strftime("%A")), # Horario total
                dias.get(time.strftime("%A"))[0], # Hora de llegada 
                dias.get(time.strftime("%A"))[-1] # Hora de salida
)
                 

juanito.getHorarioLlegada()
juanito.medirFalta()
