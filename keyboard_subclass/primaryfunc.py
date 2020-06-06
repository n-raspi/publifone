from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import dialIn

import threading
import serial
import re

from gpiozero import *
from time import *

ser = serial.Serial('/dev/ttyAMA0',4800)
#ser.write(b"ATD"+phoneNum.encode()+b";\r")

handsetSens = DigitalInputDevice(16, pull_up=False)
phoneNum = ""

def CPTONE(toneVal): #might have to move close to keyboard for immediate tone
    ser.write(b"AT+CPTONE="+toneVal.encode()+b";\r")
    print("tone: " , toneVal)
        
def VERIFY():
    #return True
    #return False
    if len(phoneNum) < 5:
        return True
    else:
        return "call"

def CALL():
    ser.write(b"ATD"+phoneNum.encode()+b";\r")
    print("calling: " , phoneNum)
    handsetSens.wait_for_active()
    ser.write(b"AT+CHUP")


def main(): 
    while(1):
        global phoneNum
        while (handsetSens.value==0):
            dialVals = dialIn()
            if(dialVals[1] == "num"):
                CPTONE(dialVals[0])
                phoneNum = phoneNum + dialVals[0]
                print("phone: ", phoneNum)
                verifOut = VERIFY()
                if(verifOut == False):
                   pass 
                elif(verifOut == True):
                    pass
                elif(verifOut == "call"):
                    CALL()
            elif(dialVals[1] == "spec"):
                pass
            elif(dialVals[1] == "com"):
                pass
            elif(dialVals[1] == None):
                pass
        phoneNum = ""

