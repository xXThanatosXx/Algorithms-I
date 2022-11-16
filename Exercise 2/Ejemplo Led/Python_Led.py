#pip install pyserial
import time

import serial

ser = serial.Serial('COM3','9600',timeout=1)
time.sleep(2)

def LED1():
    ser.write(b'P')
    print('P')

def LED2():
    ser.write(b'N')
    print('N')

def operacion(opc):
    
    if opc == 1:
        LED1()
    elif opc == 2:
        LED2()
    else:
        print('texto')

def Menu():
    while True:
        try:
            print("Cual led desea encender?")
            opc = int(input("Led Uno presione (1) o led Dos presione (2): "))
            return opc
            
        except ValueError:
            print("debes ingresar un numero: ")

while True:
    try:
         print("Conexion serial")
         respuesta = input("Desea encender un led? (Y/N): ")
         r=respuesta.lower()
         if r == "y":
             opc= Menu()
             operacion(opc)
         else:
            ser.write(b'D')
            ser.close()
            break    
    except:
        print('termino')


