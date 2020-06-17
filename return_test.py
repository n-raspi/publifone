import serial
from serial import *
import time
from time import *
val = 0
serTO = 0.5
ser = serial.Serial('/dev/ttyAMA0',4800, timeout = serTO)
#ser.write(b"ATE0\r")
#ser.flush()
ser.reset_input_buffer()
buffer = ""
def scr(inputStr,timeout):
    buffer = ""
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    if(timeout):
        for j in range(int(timeout/serTO)):
            ser.read_until(b"\r\n")#ignore first \r\n
            val = ser.read_until(b"\r\n")[:-2].decode()
            if not val:
                print("aaaaaaah")
            else:
                print(val)
    elif(timeout == None):
        while(1):
            ser.read_until(b"\r\n")#ignore first \r\n
            val = ser.read_until(b"\r\n")[:-2].decode()
            if not val:
                print("aaaaaaah")
            elif val == "OK":
                print(val)
                break
            else:
                print(val)
                break;
    
def nothing(inputStr):
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    sleep(0.5)
    ser.reset_input_buffer()
scr("AT+CBC",2)