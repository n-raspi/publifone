##from gpiozero import DigitalInputDevice
from gpiozero import *
from time import sleep
 
inputs =  [DigitalInputDevice(4, pull_up=False),
           DigitalInputDevice(17, pull_up=False),
           DigitalInputDevice(27, pull_up=False),
           DigitalInputDevice(22, pull_up=False),
           DigitalInputDevice(23, pull_up=False)]

outputs = [DigitalOutputDevice(5, active_high=True),
           DigitalOutputDevice(6, active_high=True),
           DigitalOutputDevice(13, active_high=True),
           DigitalOutputDevice(19, active_high=True),
           DigitalOutputDevice(26, active_high=True)]

inputVal = [["top1","top2",None , None ,"top3"],
            ["circ","vol","*","#","0"],
            ["bott","cont","7","9","8"],
            ["left","right","4","6","5"],
            ["top","L","1","3","2"]]

inputTyp = [["com","com", None, None, "com"],
        ["com","com","spec","spec","num"],
        ["com","com","num","num","num"],
        ["com","com","num","num","num"],
        ["com","com","num","num","num"]]


def dialIn():
    i,j = 0,0
    while 1:
        for i in range(len(outputs)):
            outputs[i].on()
            for j in range (len(inputs)):
                if inputs[j].value:
                    outputString =[inputVal [j][i],inputTyp[j][i]] 
                    print(i," ",j, " " , inputVal[j][i], " ")
                    inputs[j].wait_for_inactive(timeout=2)
                    sleep(0.2)
                    outputs[i].off()
                    return outputString
                    
            outputs[i].off()
