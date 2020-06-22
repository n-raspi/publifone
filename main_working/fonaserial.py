import serial
from serial import *
import time
from time import *
val = 0
serTO = 0.5 #this solved the cutoff of command return
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
        buffer.append(True)
        buffer.append(crclear())
        ser.reset_input_buffer()
    else:
        buffer.append(False)
        buffer.append(None) 
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    buffer.append(cr(timeout))
    return buffer

        
#check immediate then within timeout since last timeout
#adds to parametered buffer
def cr(timeout): #check reply
    buffer = []
    if(timeout == None): timeout = 10
    j = 0
    while j < int(timeout/serTO):
        #ser.read_until(b"\r\n")#ignore echo AND first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        if not val: #count up on timeout if there's no reply or if it is just \r\n
            j += 1
            continue
        print(val)
        if(val[-1:] == "\r"): #remove \r which appears at the end of commands
            val = val[:-1]
#         if val == "OK" or val == "ERROR": #better to handle in handle functions
#             buffer.append(val)
#             j = 0
#             continue
#         else:
        buffer.append(val)
        j = 0
    return buffer

#returns and clears current buffer
def crclear(): #check reply
    buffer = []
    for j in range(255):
        ser.read_until(b"\r\n")#ignore first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        if not val:
            return buffer
        else:
            buffer.append(val)
#simply return up to 255 bytes       
def crsimple():
    val = ser.read(255)
    return val

#simply ser.write a string, wait a little bit then reset input buffer
def simpleOut(inputStr):
    ser.write(inputStr.encode() + b"\r")
    ser.flush()
    sleep(0.5)
    ser.reset_input_buffer()
    
if __name__ == "__main__":
    pass
#     scir("ATD+447447571213;",3)
#     sleep(2)
#     scir("AT+CHUP",5)