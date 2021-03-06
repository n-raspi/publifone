import serial

from gpiozero import *
from time import *

import fonaserial
from fonaserial import *

ser = serial.Serial('/dev/ttyAMA0',4800)



def CALL(phoneNum,inter): #make phone call (too simple)
    ser.write(b"ATD"+phoneNum.encode()+b";\r\n")
    print("calling: " , phoneNum)
    inter.wait_for_active()
    ser.write(b"AT+CHUP\r\n")
    print("hungup")
    
def INITCALL(phoneNum): #make phone call
    callInter = scir(f"ATD{phoneNum};",1)
    if callInter[0]:
        HANDLE(callInter[1])
    print(callInter)
    if callInter[2][1] == "OK":
        return True
    else: return False

def HANGUP():
    hangInter = scir("AT+CHUP",2)
    print(hangInter)
    if hangInter[0]:
        HANDLE(hangInter[1])
    if hangInter[2][1] == "OK" or hangInter[2][2] == "OK":
        return True
    else:
        return False
    
def GETBAT():
    batInter = scir("AT+CBC",1)
    if batInter[0]:
        HANDLE(batInter[1])
    #print(batInter)
    batteryInfo = STATUSPARSE(batInter[2][1])
    batteryDict = {"Percentage":int(batteryInfo[2]),"Voltage":float(batteryInfo[3][:-1])}
    return batteryDict
        
def STATUSPARSE(parseSTR):
    #print(parseSTR)
    status = [parseSTR.split(":")[0]]
    infoList = parseSTR.split(":")[1].split(",")
    for i in range(len(infoList)):
        status.append(infoList[i])
    return status

def HANDLE(handleList):
    pass
if __name__ == "__main__":
    pass
     #INITCALL("+41791384875")
#     sleep(2)
#     ser.write(b"AT+CHUP\r\n")