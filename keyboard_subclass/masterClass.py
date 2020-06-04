from keyBoardRead import inputVal
from keyBoardRead import dialIn
from gpiozero import *
from time import sleep

handsetSens = DigitalInputDevice(16, pull_up=False)


newStr = dialIn(handsetSens, 1)

print(newStr)
