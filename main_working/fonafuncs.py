import serial

from gpiozero import *
from time import *

ser = serial.Serial('/dev/ttyAMA0',4800)

toneEq = {
    "0":"10",
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "#":"15",
    "*":"16"
    }

def CPTONE(toneVal): #might have to move close to keyboard for immediate tone
    
    ser.write(b"AT+CPTONE="+toneEq[toneVal].encode()+b"\r\n")
    print("tone: " , toneVal)
        


def CALL(phoneNum,inter): #make phone call
    ser.write(b"ATD"+phoneNum.encode()+b";\r\n")
    print("calling: " , phoneNum)
    inter.wait_for_active()
    ser.write(b"AT+CHUP\r\n")
    print("hungup")
