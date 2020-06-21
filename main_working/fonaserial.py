import serial
from serial import *
import time
from time import *
val = 0
serTO = 0.1
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
        #print("inwaiting")
        #print(ser.read(255).decode())
        buffer.append(True)
        #buffer.append(crclear())
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
    #print("new")
    buffer = []
    if(timeout == None): timeout = 10
    j = 0
    while j < int(timeout/serTO):
        #print(ser.inWaiting())
        #print(f"going{j}")
        #ser.read_until(b"\r\n")#ignore echo AND first \r\n
        val = ser.read_until(b"\r\n")[:-2].decode()
        
        if not val:
            #print("pass")
            j += 1
            continue
        if(val[-1:] == "\r"):
            print("asdf")
            val = val[:-1]
            
        if val == "OK" or val == "ERROR":
            #print("it's an ok")
            buffer.append(val)
            #print(val)
            return buffer
        else:
            buffer.append(val)
            #print("reset count!")
            j = 0
            continue
        j +=1
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