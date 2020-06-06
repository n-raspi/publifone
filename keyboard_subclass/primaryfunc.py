from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import inputs
from keyboardread import dialIn

import threading
import serial
import re

from gpiozero import *
from time import *

ser = serial.Serial('/dev/ttyAMA0',4800)
#ser.write(b"ATD"+phoneNum.encode()+b";\r")

handsetSens = DigitalInputDevice(16, pull_up=False)

def CPTONE(toneVal):
    ser.write(b"AT+CPTONE="+toneVal.encode()+b";\r")
        
def VERIFY:
    

def main(): 
    while(1)
        global phoneNum = ""
        while (handsetSens.value==0):
            dialVals = dialIn()
            if(dialVals[1] == "num"):
                CPSTONE(dialVals[0])
                phoneNum = phoneNum + dialVals[0]
                VERIFY
            elif(dialVals[1] == "spec"):
            elif(dialVals[1] == "com"):
            elif(dialVals[1] == None):

