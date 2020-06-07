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
        
def VERIFY(): #main verifying function
    #return True
    #return False
    if len(phoneNum) < 5: #test check
        return True
    else:
        return "call"

def CALL(): #make phone call
    ser.write(b"ATD"+phoneNum.encode()+b";\r")
    print("calling: " , phoneNum)
    handsetSens.wait_for_active()
    ser.write(b"AT+CHUP")


def main(): 
    while(1): #runs indefinitely, currently just call mode
        global phoneNum
        while (handsetSens.value==0):
            dialVals = dialIn(handsetSens, 1) #passes hangup to end sample on hangup
            if(dialVals[1] == "num" or dialVals[1] == "spec"):
                CPTONE(dialVals[0]) #see function comment
                phoneNum = phoneNum + dialVals[0]
                print("phone: ", phoneNum)
                verifOut = VERIFY() 
                if(verifOut == False):
                   pass 
                elif(verifOut == True):
                    pass
                elif(verifOut == "call"):
                    CALL()
                    
            elif(dialVals[1] == "com"):
                pass
            
            elif(dialVals[1] == None): #ambiguous, could be errounous pressing of unindexed button or hangup
                pass
        phoneNum = ""

