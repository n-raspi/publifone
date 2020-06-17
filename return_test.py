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
buffer = []
def scir(inputStr,timeout): #send check immediate reply
    if int(ser.inWaiting()) != 0:
        print(ser.read(255).decode())
        ser.reset_input_buffer() 
        
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    return cr(timeout)
    
def cr(timeout): #check reply 
    buffer = []
    if(timeout == None): timeout = 40
    for j in range(int(timeout/serTO)):
        ser.read_until(b"\r\n")#ignore first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        if not val:
            print("None")
        if val == "OK" or val == "ERROR":
            buffer.append(val)
            print(val)
            return buffer
        else:
            buffer.append(val)
            print(val)
            j = 0
    
def nothing(inputStr):
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    sleep(0.5)
    ser.reset_input_buffer()
if __name__ == "__main__":
    print(scir("ATD+447447571213;",10))
    sleep(1)
    print(scir("AT+CLCC",3))
    sleep(1.5)
    print(scir("AT+CHUP",5))