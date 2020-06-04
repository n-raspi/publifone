import serial
import time
from time import *
val = 0
ser = serial.Serial('/dev/ttyAMA0',4800)
ser.write("AT\r")
val = ser.read(4)
print(val)
