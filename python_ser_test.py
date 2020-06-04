import serial
import time
from time import *
from gpiozero import *

import sys
sys.path.append('keyboard_subclass/')
from keyBoardRead1 import inputVal
from keyBoardRead1 import dialIn

handsetSens = DigitalInputDevice(16, pull_up=False)
ser = serial.Serial('/dev/ttyAMA0',4800)

#phoneNum = raw_input()
phoneNum = dialIn(handsetSens,1)
ser.write(b"ATD"+phoneNum.encode()+b";\r")
print("number"+str(phoneNum)+" sent")
ser.close()
