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
            print("intnl 0")
            for i in range(len(natdestcodes)):
                if (phoneNum[4:6] == natdestcodes[i]) and (len(natdestcodes[i]) == 2) or (phoneNum[4:7] == natdestcodes[i] and len(natdestcodes[i]) == 3):
                    print("swiss NDC")
                    if(len(phoneNum) == 13):
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
    elif phoneNum[:1] == "0":
        print("zero")
        for i in range(len(natdestcodes)):
            if (phoneNum[1:3] == natdestcodes[i]) and (len(natdestcodes[i]) == 2) or (phoneNum[1:4] == natdestcodes[i] and len(natdestcodes[i]) == 3):
                print("swiss NDC")
                if(len(phoneNum) == 10):
                    return "call"
                        
                return True
            else:
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
    print(VERIFY("0041791384985"))
