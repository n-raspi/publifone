import serial

from gpiozero import *
from time import *

ser = serial.Serial('/dev/ttyAMA0',4800)


def CPTONE(toneVal): #might have to move close to keyboard for immediate tone
    ser.write(b"AT+CPTONE="+toneVal.encode()+b";\r")
    print("tone: " , toneVal)
        
def VERIFY(phoneNum): #main verifying function
    #return True
    #return False
    if len(phoneNum) < 5: #test check
        return True
    else:
        return "call"

def CALL(phoneNum,inter): #make phone call
    ser.write(b"ATD"+phoneNum.encode()+b";\r")
    print("calling: " , phoneNum)
    inter.wait_for_active()
    ser.write(b"AT+CHUP")
    print("hungup")