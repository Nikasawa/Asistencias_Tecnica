# Archivo de prueba para ver las librerias time de Python
import time



# time

#print(time.time()) # Devuelve el tiempo actual en segundos

#print(time.asctime()) # Convierte los segundos en una tupla de datos
#print(time.gmtime()) # Convierte una tupla de datos en segundos

#print(time.strftime('%X')) # Devuelve el tipo de dato (Horario), en el formato que se lo especifica
#print(time.strptime('18:30:12', '%H:%M:%S')) # Pasa un tipo de dato (str) y lo reconoce como el segundo formato (si es que puede)

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

#print(sumarHora(3))
#print(sumarMinutos(33))

#print(time.strptime(str(sumarHora(3)) + ':' + str(sumarMinutos(33)), "%H:%M"))

if '720' > '800':
    print('xd')
else:
    print('dadadd')
