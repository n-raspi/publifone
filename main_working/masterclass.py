from keyboardread import inputVal
from keyboardread import inputTyp
from keyboardread import inputs
from keyboardread import dialIn

import threading

from gpiozero import *
from time import *

handsetSens = DigitalInputDevice(16, pull_up=False)

while 1:
    #creates a thread of the func then wait for end
    #dialVals = "" 
    #thread = threading.Thread(target=dialIn)
    #thread.start()
    #thread.join()
    
    #also look into events within threading
    
    #simplest method but may have interference as sampling may start before previous is finished
    dialVals = dialIn()
    
    
