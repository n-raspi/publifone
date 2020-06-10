import csv
from io import open
import re

shortcodes = []
natdestcodes = []

def VERIFY(phoneNum): 
    if phoneNum[:2] == "00":
        if phoneNum[2:4] == "44": #uk number for testing
            return True
        elif phoneNum[2:4] == "41": #swiss number with intl code
            print("intnl local ")
            phoneLen = len(phoneNum) - 4
            if phoneLen == 0:
                return True
            for i in range(len(natdestcodes)):
                if (phoneLen == 1) or (phoneLen == 2): #if 07 or 080 match 7 or 80 to the beginning of every NDC
                    if re.findall(rf"^{phoneNum[4:]}",natdestcodes[i]):
                        if ((phoneLen) == len(natdestcodes[i])): #if match AND same length, full NDC match
                             print("swiss NDC0: ", natdestcodes[i])
                        else:
                            print("start of: ", natdestcodes[i])  #else just beginning match
                        return True
                elif (phoneLen >= 3 and (phoneNum[4:7] == natdestcodes[i] or phoneNum[4:6] == natdestcodes[i])): #should be full match
                    print("swiss NDC1: ", natdestcodes[i])
                    if(phoneLen == 13):
                        return "call"        
                    return True
            return False
        else:
            #handling for intnl number
            return True
            
    elif phoneNum[:1] == "1":
        i=0
        for i in range(len(shortcodes)):
            if phoneNum == shortcodes[i]:
                return True
                #return callable #short code callable but should not call by default
            if re.findall(rf"^{phoneNum}",shortcodes[i]):
                return True
            
            
    elif phoneNum[:1] == "0": #handling local phone number, stable-ish
        print("zero")
        phoneLen = len(phoneNum)
        if (phoneLen == 1):
                return True
        for i in range(len(natdestcodes)):
            if (phoneLen == 2) or (phoneLen == 3): #if 07 or 080 match 7 or 80 to the beginning of every NDC
                if re.findall(rf"^{phoneNum[1:]}",natdestcodes[i]):
                    if ((phoneLen-1) == len(natdestcodes[i])): #if match AND same length, full NDC match
                         print("swiss NDC0: ", natdestcodes[i])
                    else:
                        print("start of: ", natdestcodes[i])  #else just beginning match
                    return True
            elif (phoneLen >= 4 and (phoneNum[1:4] == natdestcodes[i] or phoneNum[1:3] == natdestcodes[i])): #should be full match
                print("swiss NDC1: ", natdestcodes[i])
                if(phoneLen == 10):
                    return "call"        
                return True
        return False
       
       
       
    else:
        print("ver_fail")
        return True
        
        
        
def updateLists():
    global shortcodes
    global natdestcodes
    with open('data/short-codes.csv', mode = 'r', encoding='utf-8-sig') as shortCode:
        reader = csv.DictReader(shortCode)
        i=0
        for row in reader:
            shortcodes.append(row['shortcode'])
            i = i+1

    with open('data/national_destination.csv', mode = 'r', encoding='utf-8-sig') as NDC:
        reader = csv.DictReader(NDC)
        i=0
        for row in reader:
            natdestcodes.append(row['NDC'])
            i = i+1
            
if __name__ == "__main__":
    updateLists()
    print(natdestcodes)
    print(VERIFY("004179")) # test code
