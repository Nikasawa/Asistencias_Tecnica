import serial

PUERTO = 'COM3'
ingreso = serial.Serial(PUERTO)
ingreso.timeout = 2.0

print('Se detecto un periferico en el puerto: ' + PUERTO)

huella = ingreso.read()
print('read: {}'.format(huella))
print('read_until: {}'.format(ingreso.read_until(b'1')))
print('read_all: {}'.format(ingreso.read_all()))
print('readinto: {}'.format(ingreso.readinto([1, 2, 3, 4])))
print('readline(): {}'.format(ingreso.readline()))


print('Se corto el programa')