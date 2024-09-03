##from gpiozero import DigitalInputDevice
from gpiozero import *
from time import sleep
from fonafuncs import *

 
inputs =  [DigitalInputDevice(4, pull_up=False), # molex: 4
           DigitalInputDevice(17, pull_up=False), # molex: 5
           DigitalInputDevice(27, pull_up=False), # molex: 6
           DigitalInputDevice(22, pull_up=False), # molex: 7
           DigitalInputDevice(23, pull_up=False)] # molex: 8

# why start with active_high?
outputs = [DigitalOutputDevice(5, active_high=True), # molex 10
           DigitalOutputDevice(6, active_high=True), # molex 11
           DigitalOutputDevice(13, active_high=True), # molex 12
           DigitalOutputDevice(19, active_high=True), # molex 13
           DigitalOutputDevice(26, active_high=True)] # molex 14

# inputVal(active input, active output) i.e. row: input; column: ouput
inputVal = [["top1","top2",None , None ,"top3"],
            ["circ","vol","*","#","0"],
            ["bott","cont","7","9","8"],
            ["left","right","4","6","5"],
            ["top","L","1","3","2"]]

# Add corresponding molex pins 
correspondingPins = [["4/10","4/11",None , None ,"4/14"],
            ["5/10","5/11","5/12","5/13","5/14"],
            ["6/10","6/11","6/12","6/13","6/14"],
            ["7/10","7/11","7/12","7/13","7/14"],
            ["8/10","8/11","8/12","8/13","8/14"]]

inputTyp = [["com","com", None, None, "com"],
        ["com","com","spec","spec","num"],
        ["com","com","num","num","num"],
        ["com","com","num","num","num"],
        ["com","com","num","num","num"]]


def dialIn(inter, interVal):
    i,j = 0,0
    while inter.value != interVal: # while the interrupt is not... activated?
        for i in range(len(outputs)): # go through all output devices
            outputs[i].on() # turn i on 
            for j in range (len(inputs)): # go through all input devices
                if inputs[j].value: # if one of them is on
                    outputString =[inputVal [j][i],inputTyp[j][i]] # set uoutputString to the corresponding value
                    print(i," ",j, " " , inputVal[j][i], " ")
                    if inputTyp[j][i] == "spec" or inputTyp[j][i] == "num":
                        #pass
                        CPTONE(inputVal[j][i]) # Call FONA function CPTONE if it is a number
                    inputs[j].wait_for_inactive(timeout=2) # Wait until the input is 0 or until timeout (repeated characters when held limit)
                    outputs[i].off() # turn off the output
                    sleep(0.2) # more debouncing
                    return outputString # then return string (too late, must change with threading)
            outputs[i].off() # turn off the output if no input is high
    
    for k in range(len(outputs)): # when interrupted,turn all the outputs off
        outputs[k].off()
    return "cancel"

if __name__ == "__main__":
    handsetSens = DigitalInputDevice(16, pull_up=False)
    #print(dialIn(handsetSens,1))
    while 1:
        dialIn(handsetSens,1)
        print("go")
