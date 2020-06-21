from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import dialIn

import threading
import serial
import re

from fonafuncs import *

from gpiozero import *
from time import *

from swissnumbers import updateLists
from swissnumbers import VERIFY


#ser.write(b"ATD"+phoneNum.encode()+b";\r")

handsetSens = DigitalInputDevice(16, pull_up=False)


def callhandle(phoneNum, handsetSens):
    if(INITCALL(phoneNum) == True):
        print("call true")
        while(handsetSens.value==0):
            #print("checking")
            interVal = cr(1)
            if interVal:
                print(interVal)
        return
    else:
        print("failed")
def main():
    phoneNum = ""
    while(1): #runs indefinitely, currently just call mode
        
        while (handsetSens.value==0):
            dialVals = dialIn(handsetSens, 1) #passes hangup to end sample on hangup
            if(dialVals[1] == "num" or dialVals[1] == "spec"):
                phoneNum = phoneNum + dialVals[0]
                print("phone: ", phoneNum)
                verifOut = VERIFY(phoneNum) 
                 
                if(verifOut == False):
                   phoneNum = phoneNum[:-1] 
                elif(verifOut == True):
                    pass
                elif(verifOut == "call"):
                    callhandle(phoneNum, handsetSens)
                    
            elif(dialVals[1] == "com"):
                if(dialVals[0] == "top1"):
                    phoneNum = phoneNum[:-1]
                if(dialVals[0] == "top2"):
                    phoneNum = ""
                if(dialVals[0] == "top3"): #force call for: short numbers, int numbers
                    callhandle(phoneNum, handsetSens)
            elif(dialVals == "cancel"):
                print("cancelled")
            elif(dialVals[1] == None): #just unindexed button
                pass
        phoneNum = ""

if __name__ == "__main__":
    #updateLists()
    #print(GETBAT())
    print(callhandle("+41791384875", handsetSens))
    #callhandle("+447447571213", handsetSens)
    #main()
