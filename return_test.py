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

#returns True and extra array entry 
#send command and check immediate response
#within timeout after last msg
def scir(inputStr,timeout): 
    buffer = []
    if int(ser.inWaiting()) != 0:
        #print(ser.read(255).decode())
        buffer.append(True)
        buffer.append(crclear())
        ser.reset_input_buffer()
    else:
        buffer.append(False)
        buffer.append(None) 
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    return cr(timeout, buffer)

#check immediate then within timeout since last timeout
#adds to parametered buffer
def cr(timeout, buffer): #check reply 
    if(timeout == None): timeout = 40
    for j in range(int(timeout/serTO)):
        ser.read_until(b"\r\n")#ignore first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        if not val:
            pass
            #print("None")
        elif val == "OK" or val == "ERROR":
            buffer.append(val)
            #print(val)
            return buffer
        else:
            buffer.append(val)
            #print(val)
            j = 0

#returns current buffer
def crclear(): #check reply
    buffer = []
    for j in range(255):
        ser.read_until(b"\r\n")#ignore first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        if not val:
            return buffer
        else:
            buffer.append(val)
    
def simpleOut(inputStr):
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    sleep(0.5)
    ser.reset_input_buffer()
    
if __name__ == "__main__":
    print(scir("ATD+447447571213;",3))
    sleep(20)
    print(scir("AT+CHUP",5))