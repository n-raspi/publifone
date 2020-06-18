import serial

from gpiozero import *
from time import *

import fonaserial
from fonaserial import *

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

def CPTONE(toneVal): 
    ser.write(b"AT+CPTONE="+toneEq[toneVal].encode()+b"\r\n")
    print("tone: " , toneVal)
        


def CALL(phoneNum,inter): #make phone call
    ser.write(b"ATD"+phoneNum.encode()+b";\r\n")
    print("calling: " , phoneNum)
    inter.wait_for_active()
    ser.write(b"AT+CHUP\r\n")
    print("hungup")
    
def GETBAT():
    batInter = scir("AT+CBC",1)
    if batInter[0]:
        HANDLE(batInter[1])
    batteryInfo = STATUSPARSE(batInter[2])
    batteryDict = {"Percentage":int(batteryInfo[2]),"Voltage":float(batteryInfo[3][:-1])}
    return batteryDict
        
def STATUSPARSE(parseSTR):
    status = [parseSTR.split(":")[0]]
    infoList = parseSTR.split(":")[1].split(",")
    for i in range(len(infoList)):
        status.append(infoList[i])
    return status

def HANDLE(handleList):
    pass
if __name__ == "__main__":
    print(GETBAT())
