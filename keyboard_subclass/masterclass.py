from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import inputs
from keyboardread import dialIn

import threading

from gpiozero import *
from time import *

handsetSens = DigitalInputDevice(16, pull_up=True)

while 1:
    #dialVals = ""
    #thread = threading.Thread(target=dialIn)
    #thread.start()
    #thread.join()
    dialVals = dialIn()
