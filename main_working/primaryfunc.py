from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import dialIn

import threading
import serial
import re

from fonafuncs import *

from gpiozero import *
from time import *


#ser.write(b"ATD"+phoneNum.encode()+b";\r")

handsetSens = DigitalInputDevice(16, pull_up=False)
phoneNum = ""




def main(): 
    while(1): #runs indefinitely, currently just call mode
        global phoneNum
        while (handsetSens.value==0):
            dialVals = dialIn(handsetSens, 1) #passes hangup to end sample on hangup
            if(dialVals[1] == "num" or dialVals[1] == "spec"):
                phoneNum = phoneNum + dialVals[0]
                print("phone: ", phoneNum)
                verifOut = VERIFY(phoneNum) 
                if(verifOut == False):
                   pass 
                elif(verifOut == True):
                    pass
                elif(verifOut == "call"):
                    CALL(phoneNum, handsetSens)
            elif(dialVals[1] == "com"):
                if(dialVals[0] == "top1"):
                    phoneNum = phoneNum[:-1]
                if(dialVals[0] == "top2"):
                    phoneNum = ""
                if(dialVals[0] == "top3"):
                    CALL()
            elif(dialVals == "cancel"):
                print("cancelled")
            elif(dialVals[1] == None): #just unindexed button
                pass
        phoneNum = ""

if __name__ == "__main__":
    main()