import serial
from serial import *
import time
from time import *
val = 0
ser = serial.Serial('/dev/ttyAMA0',4800)
buffer = ""
def scr(inputStr,time_out):
    buffer = ""
    ser.write(inputStr.encode() + b"\n\r")
    ser.flush()
    
    val = ser.read_until(b"\r",size = None).decode() 
    print(val)

scr("aaaaaaaaaaaaa")