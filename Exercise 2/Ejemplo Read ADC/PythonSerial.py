#python -m pip show numpy pandas matplotlib openpyxl pyserial     
#pip install pyserial
# import sys 
# sys.path.append('C:\RoboDK\Python37\Lib\site-packages\cv2')
#C:\Users\Shadow\AppData\Local\Programs\Python\Python39\Scripts
#c!cdc9G6*&Dc!9fCMlyCZ!yV
from Arduino import *

#pip install matplotlib
import matplotlib.pyplot as plt

#pip install pandas
#pip install openpyxl
import pandas as pd

#pip install numpy
import numpy as np

#Tiempo de muestreo 0.1 Segundos
ts = 0.1
#Muestras en segundos a tomar 
tf = 30
t = np.arange(0,tf+ts,ts)
N = len(t)

port = 'COM3' 
baudRate = 9600 
sizeData = 2

y  = np.zeros((sizeData,N))

arduino = serialArduino(port,baudRate,sizeData)

arduino.readSerialStart()

for k in range(N):
     
     start_time = time.time()
    
     for n in range(sizeData):
                  y[n,k] = arduino.rawData[n]


     print(f"Voltaje {y[0,k]}")
     print(f"Temperatura {y[1,k]}")
          
     elapsed_time = time.time() - start_time
     while elapsed_time < ts:
             elapsed_time = time.time()-start_time
     
arduino.close()

plt.figure()
plt.plot(t,y[0,:],'r',label='Voltaje')
plt.legend(loc='best')
plt.grid()
plt.xlabel('Eje x')
plt.ylabel('Eje Y')
#plt.legend(loc='upper right')
plt.figure()
plt.plot(t,y[1,:],label='Temperatura')
plt.legend(loc='best')
plt.grid()
plt.xlabel('Eje x')
plt.ylabel('Eje Y')
plt.show()

#Save data Excel
data = {'Voltaje':y[0,:],
        'Temperatura': y[1,:]}

df = pd.DataFrame(data, columns = ['Voltaje','Temperatura'])
df.to_csv('Data.csv',sep = ";")
