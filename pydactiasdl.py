import serial

def read_from_serial(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Connected to {port} at {baudrate} baud.")
        
        while True:
        
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")
    
    except serial.SerialException as e:
        print(f"Error: {e}")
    
    finally:
        ser.close()

if __name__ == "__main__":
    # Reemplaza 'COM3' con el puerto correcto
    read_from_serial('COM6')

