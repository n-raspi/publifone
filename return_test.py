import serial
from serial import *
import time
from time import *
val = 0
ser = serial.Serial('/dev/ttyAMA0',4800, timeout = 1)
#ser.write(b"ATE0\r")
#ser.flush()
ser.reset_input_buffer()
buffer = ""
def scr(inputStr):
    buffer = ""
    ser.write(inputStr.encode() + b"\r")
    ser.flush() 
    val = ser.read_until(b"\r\n")
    print(val)
    val = ser.read_until(b"\r\n")[:-2].decode()
    if not val:
        print("aaaaaaah")
    else:
        print(val)
def nothing(inputStr):
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    sleep(0.5)
    ser.reset_input_buffer()
scr("AT")